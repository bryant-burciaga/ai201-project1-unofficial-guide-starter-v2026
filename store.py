"""
Stages 3 and 4 of the pipeline: embedding chunks and retrieving them.

Three things in here are worth knowing about, because they'd quietly break the
rest of the project if they were wrong:

1. The Chroma collection is created with cosine distance, explicitly. Chroma
   defaults to squared L2, and the 0.6 threshold the course uses is calibrated
   against cosine. Getting this wrong makes every distance number meaningless.

2. `search` returns the distance alongside each chunk. Milestone 4 has you
   compare distances, so they have to be visible.

3. The embedding model is the one Chroma bundles, not one loaded through
   `sentence-transformers`. It is the same model — `all-MiniLM-L6-v2`, 384
   dimensions — but it arrives as an ONNX build from Chroma's own CDN, so the
   install needs neither PyTorch nor a reachable Hugging Face. See `_embedder`.
"""

import os
import shutil
from dataclasses import dataclass

# Must be set BEFORE chromadb is imported. Without it, some Chroma versions
# print "Failed to send telemetry event ..." on every single call — which looks
# exactly like a real error, isn't one, and cost a previous cohort a lot of
# confused help-channel messages.
os.environ.setdefault("ANONYMIZED_TELEMETRY", "False")

import chromadb  # noqa: E402

import config
from chunker import Chunk



import re
from rank_bm25 import BM25Okapi

_bm25_cache: dict[str, tuple] = {}  # collection name -> (bm25, ids)


def _tokenize(text: str) -> list[str]:
    return re.findall(r"[a-z0-9]+", text.lower())


def _get_bm25(collection, name: str):
    """
    Build (once per collection) or reuse a BM25 index over every chunk.

    94 chunks makes rebuilding cheap regardless — this cache just avoids
    repeat work across the 15 calls a single run_eval.py pass makes.
    """
    cached = _bm25_cache.get(name)
    if cached is not None:
        return cached

    everything = collection.get(include=["documents"])
    ids = everything["ids"]
    tokenized = [_tokenize(d) for d in everything["documents"]]
    bm25 = BM25Okapi(tokenized)

    cached = (bm25, ids)
    _bm25_cache[name] = cached
    return cached







@dataclass
class Result:
    """One retrieved chunk and how far it was from the question."""

    text: str
    source: str
    label: str
    distance: float   # LOWER IS BETTER. 0.3 is close, 0.9 is unrelated.
    produced_by: str


_model = None

# The model Chroma bundles. Anything else in config.EMBEDDING_MODEL means
# "fetch that one from Hugging Face instead" — see `_embedder`.
BUNDLED_MODEL = "all-MiniLM-L6-v2"


class _OnnxEmbedder:
    """
    Chroma's built-in embedder, wrapped to look like the other two.

    Chroma's embedding functions are called directly and hand back numpy
    arrays. The rest of this file wants `.encode(texts)`, so the adapter lives
    here rather than making every caller care which embedder it got.
    """

    def __init__(self):
        from chromadb.utils.embedding_functions import ONNXMiniLM_L6_V2

        self._ef = ONNXMiniLM_L6_V2()

    def encode(self, texts, show_progress_bar: bool = False):
        return [vector.tolist() for vector in self._ef(list(texts))]


def _sentence_transformer(name: str):
    """
    The escape hatch: any model that isn't the bundled one.

    Unit 2's "try a second embedding model" stretch option comes through here,
    and so does anything you set `EMBEDDING_MODEL` to. This path *does* need
    `sentence-transformers` and a reachable Hugging Face, neither of which the
    default install has — which is the whole point of the default install.
    """
    try:
        from sentence_transformers import SentenceTransformer
    except ImportError as exc:
        raise RuntimeError(
            f"config.EMBEDDING_MODEL is set to {name!r}, which isn't the model "
            f"Chroma bundles ({BUNDLED_MODEL!r}), so it has to be downloaded "
            f"from Hugging Face.\n"
            f"Install the optional dependency first:\n"
            f"    pip install 'sentence-transformers>=3.4,<3.5'\n"
            f"Or set EMBEDDING_MODEL back to {BUNDLED_MODEL!r}."
        ) from exc

    return SentenceTransformer(name)


def _embedder():
    """
    Load the embedding model once and keep it.

    First call is slow — it downloads about 80 MB. That's why setup happens
    before class.
    """
    global _model

    if _model is not None:
        return _model

    # Used only by this repo's own smoke test, which runs where no model can be
    # downloaded at all. Never set this yourself.
    if os.getenv("AI201_FAKE_EMBEDDINGS") == "1":
        from _smoke_embedder import FakeEmbedder

        _model = FakeEmbedder()
    elif config.EMBEDDING_MODEL == BUNDLED_MODEL:
        _model = _OnnxEmbedder()
    else:
        _model = _sentence_transformer(config.EMBEDDING_MODEL)

    return _model


def embed(texts: list[str]) -> list[list[float]]:
    """Turn text into vectors. Runs on your machine, costs no API quota."""
    vectors = _embedder().encode(texts, show_progress_bar=False)
    # sentence-transformers and the smoke stand-in return something with a
    # .tolist(); _OnnxEmbedder has already done that conversion itself.
    return vectors.tolist() if hasattr(vectors, "tolist") else vectors


def _client():
    return chromadb.PersistentClient(
        path=str(config.CHROMA_DIR),
        settings=chromadb.config.Settings(anonymized_telemetry=False),
    )


def build_index(
    chunks: list[Chunk],
    corpus: str | None = None,
    variant: str = "default",
) -> int:
    """
    Embed every chunk and store it.

    `variant` lets you keep more than one index of the same corpus at the same
    time. In unit 2, when you compare two chunking strategies, index the second
    one as variant="v2" and you can query both instead of deleting the first
    and starting over.
    """
    name = config.collection_name(corpus, variant)
    client = _client()

    try:
        client.delete_collection(name)
    except Exception:
        pass

    collection = client.create_collection(
        name=name,
        # ⚠️ Do not remove. Chroma defaults to squared L2, and every distance
        # number in this course assumes cosine.
        metadata={"hnsw:space": "cosine"},
    )

    batch = 256
    for start in range(0, len(chunks), batch):
        window = chunks[start : start + batch]
        collection.add(
            ids=[f"{c.source}#{c.index}" for c in window],
            documents=[c.text for c in window],
            embeddings=embed([c.text for c in window]),
            metadatas=[
                {"source": c.source, "index": c.index, "produced_by": c.produced_by}
                for c in window
            ],
        )

    return len(chunks)


def search(
    question: str,
    top_k: int | None = None,
    corpus: str | None = None,
    variant: str = "default",
) -> list[Result]:
    """
    Retrieve the chunks closest to a question using hybrid search:
    semantic (embedding) distance combined with BM25 keyword matching,
    merged by Reciprocal Rank Fusion.

    Semantic-only search rewards shared generic vocabulary ("stay",
    "winter", "bus") over an exact place-name match, so a question naming
    one town plus a common attribute can lose to a different town's chunk
    using similar wording. BM25 scores the literal words in the question —
    including the place name — so it pulls the right town's chunk back up
    even when embedding distance alone doesn't.

    Returns nearest-first by semantic distance, and each Result's
    `distance` is still the real cosine distance — fusion only changes
    WHICH chunks make top_k, not what "distance" means downstream (the
    gate is untouched).
    """
    top_k = top_k or config.TOP_K
    name = config.collection_name(corpus, variant)

    try:
        collection = _client().get_collection(name)
    except Exception as exc:
        raise RuntimeError(
            f"No index called '{name}'. Run `python app.py index` first."
        ) from exc

    total = collection.count()
    if total == 0:
        return []

    # Semantic pass over EVERY chunk, so fusion has a complete ranking to
    # work with, not just the top_k Chroma would have picked alone.
    raw = collection.query(query_embeddings=embed([question]), n_results=total)
    sem_ids = raw["ids"][0]
    distance_by_id = dict(zip(sem_ids, raw["distances"][0]))
    doc_by_id = dict(zip(sem_ids, raw["documents"][0]))
    meta_by_id = dict(zip(sem_ids, raw["metadatas"][0]))
    semantic_rank = {doc_id: rank for rank, doc_id in enumerate(sem_ids)}

    # BM25 pass over the same chunks.
    bm25, bm25_ids = _get_bm25(collection, name)
    bm25_scores = bm25.get_scores(_tokenize(question))
    bm25_order = sorted(range(len(bm25_ids)), key=lambda i: bm25_scores[i], reverse=True)
    bm25_rank = {bm25_ids[i]: rank for rank, i in enumerate(bm25_order)}

    # Reciprocal Rank Fusion — combines two differently-scaled rankings
    # (cosine distance, BM25 score) without needing to normalize either.
    RRF_K = 60
    fused = [
        (
            1.0 / (RRF_K + semantic_rank[doc_id])
            + 1.0 / (RRF_K + bm25_rank.get(doc_id, len(bm25_ids))),
            doc_id,
        )
        for doc_id in sem_ids
    ]
    fused.sort(key=lambda pair: pair[0], reverse=True)
    chosen_ids = [doc_id for _, doc_id in fused[:top_k]]

    results = [
        Result(
            text=doc_by_id[doc_id],
            source=str(meta_by_id[doc_id].get("source", "unknown")),
            label=f"{meta_by_id[doc_id].get('source', 'unknown')}#{meta_by_id[doc_id].get('index', 0)}",
            distance=float(distance_by_id[doc_id]),
            produced_by=str(meta_by_id[doc_id].get("produced_by", "unknown")),
        )
        for doc_id in chosen_ids
    ]

    results.sort(key=lambda r: r.distance)  # keep the nearest-first contract
    return results


def index_exists(corpus: str | None = None, variant: str = "default") -> bool:
    """Is there an index here to search, without searching it?

    `serve.py`'s health check asks this. It deliberately does not embed
    anything: loading the embedding model takes 80 MB and a few seconds, and a
    health check that heavy is a health check nobody can afford to call.
    """
    try:
        collection = _client().get_collection(config.collection_name(corpus, variant))
        return collection.count() > 0
    except Exception:
        return False


def reset():
    """Delete every index. Occasionally the fastest way out of a mess."""
    if config.CHROMA_DIR.exists():
        shutil.rmtree(config.CHROMA_DIR)
