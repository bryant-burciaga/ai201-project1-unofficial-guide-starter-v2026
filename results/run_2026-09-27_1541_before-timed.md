# Run log — before-timed

- Produced by: `run_eval.py::main`
- Retrieval: `store.py::search`, chunks from `chunker.py::split_documents`
- Corpus: `city_guides` (index variant `default`)
- top-k: 8 · relevance cutoff: 0.52
- Runs per question: 3, caching off
- When: 2026-09-27 15:41

This table is one row per QUESTION. The run log your README asks for is
one row per CRITERION, so aggregate these into it — criterion 1 is how many
of your questions had the answer in the retrieved chunks, and so on.

| Question | Run 1 | Run 2 | Run 3 |
|---|---|---|---|
| What does the Brightwater transportation guide say about traveling during the Winter time? | fail | fail | fail |
| What does the city_guide say is the best place to stay in when visiting Thornby Wells  based on budget? | fail | fail | fail |
| When is it best to use a bike, bus, rideshare, or walk according to the city_guide for Elder Ness? | fail | fail | fail |
| What is best place to stay in town during the winter time according to city_guide for Corry Vale | fail | fail | fail |
| What does city_guide best recommendation for food when eating in the area amongst all these locations? | fail | fail | fail |

---

## The relevance gate on out-of-corpus questions

Produced by `run_eval.py::check_out_of_scope`, cutoff 0.52. Refused 5 of 5.

Retrieval is deterministic and the gate is a comparison against a
fixed number, so these do not vary between runs — one pass over the
list is the whole measurement.

| Out-of-scope question | Best distance | Gate |
|---|---|---|
| What is the capital of Mongolia? | 0.803 | refused |
| How do I change the oil in a diesel engine? | 0.891 | refused |
| Who won the 1994 World Cup? | 0.873 | refused |
| What is the recommended dosage of ibuprofen for a headache? | 0.841 | refused |
| How do I write a for loop in Rust? | 0.820 | refused |

---

## Real output

This is what the system actually produced. Paste the relevant parts
into your README underneath the table — the rubric asks for real
output as text, not a description of it.

### What does the Brightwater transportation guide say about traveling during the Winter time? — run 1

- Best distance: 0.4808 (passed the gate)
- Sources retrieved: guide_regional_transport.md, guide_seasons.md, guide_walking.md
- Time: 3.02s

```
Based on the provided documents, the transportation guide does not contain specific information about traveling during the winter time (though `guide_seasons.md` mentions winter conditions for other areas like Halden Bay, Kestrelford, and Brightwater's businesses). 

Source: `guide_regional_transport.md` and `guide_seasons.md`.
```

### What does the Brightwater transportation guide say about traveling during the Winter time? — run 2

- Best distance: 0.4808 (passed the gate)
- Sources retrieved: guide_regional_transport.md, guide_seasons.md, guide_walking.md
- Time: 0.68s

```
Based on the provided documents, the text does not contain specific information about traveling in Brightwater during the winter. 

Source: guide_regional_transport.md
```

### What does the Brightwater transportation guide say about traveling during the Winter time? — run 3

- Best distance: 0.4808 (passed the gate)
- Sources retrieved: guide_regional_transport.md, guide_seasons.md, guide_walking.md
- Time: 1.03s

```
Based on the provided documents, the transportation guide does not mention traveling during the winter time. However, *guide_seasons.md* notes that in winter (December to February) Brightwater carries on because the university keeps it occupied, while several riverside businesses there close entirely from January to March. 

Sources: *guide_seasons.md* and *guide_regional_transport.md* (Note: The regional transport guide does not mention winter travel specifically).
```

### What does the city_guide say is the best place to stay in when visiting Thornby Wells  based on budget? — run 1

- Best distance: 0.3539 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_halden_bay.md, guide_pellew_sands.md, guide_thornby_wells.md, guide_walking.md
- Time: 1.35s

```
I do not have enough information to answer this question, as the documents do not mention specific best places to stay based on budget (they only mention that prices at the small guesthouses are moderate and stable year-round). 

Source: `guide_thornby_wells.md`
```

### What does the city_guide say is the best place to stay in when visiting Thornby Wells  based on budget? — run 2

- Best distance: 0.3539 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_halden_bay.md, guide_pellew_sands.md, guide_thornby_wells.md, guide_walking.md
- Time: 0.75s

```
I don't have enough information to answer this question. The provided documents do not mention specific hotels or places to stay based on budget in Thornby Wells, other than noting there are "several small guesthouses" with prices that are "moderate and stable year-round" (guide_thornby_wells.md).
```

### What does the city_guide say is the best place to stay in when visiting Thornby Wells  based on budget? — run 3

- Best distance: 0.3539 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_halden_bay.md, guide_pellew_sands.md, guide_thornby_wells.md, guide_walking.md
- Time: 0.86s

```
I don't have enough information to answer this question. The provided documents mention that there are "several small guesthouses" with prices that are "moderate and stable year-round" (`guide_thornby_wells.md`), but they do not state what the *best* place to stay is based on budget.
```

### When is it best to use a bike, bus, rideshare, or walk according to the city_guide for Elder Ness? — run 1

- Best distance: 0.5103 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_brightwater.md, guide_eating.md, guide_elder_ness.md, guide_halden_bay.md
- Time: 0.80s

```
I do not have enough information to answer this question about when to use a bike, bus, or rideshare in Elder Ness, as the provided documents only mention that there is "No public transport" (`guide_elder_ness.md`).
```

### When is it best to use a bike, bus, rideshare, or walk according to the city_guide for Elder Ness? — run 2

- Best distance: 0.5103 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_brightwater.md, guide_eating.md, guide_elder_ness.md, guide_halden_bay.md
- Time: 0.95s

```
I do not have enough information to answer this question about when to use a bike, bus, rideshare, or walk in Elder Ness based on the provided documents.
```

### When is it best to use a bike, bus, rideshare, or walk according to the city_guide for Elder Ness? — run 3

- Best distance: 0.5103 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_brightwater.md, guide_eating.md, guide_elder_ness.md, guide_halden_bay.md
- Time: 0.82s

```
Based on the provided documents, there is no mention of when to use a bike, bus, rideshare, or walk in Elder Ness (the documents state that Elder Ness has no public transport). 

Therefore, I do not have enough information to answer your question from the documents.
```

### What is best place to stay in town during the winter time according to city_guide for Corry Vale — run 1

- Best distance: 0.4304 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_brightwater.md, guide_corry_vale.md, guide_halden_bay.md, guide_marchwood.md, guide_pellew_sands.md, guide_walking.md
- Time: 0.57s

```
I do not have enough information to answer this question from the provided documents.
```

### What is best place to stay in town during the winter time according to city_guide for Corry Vale — run 2

- Best distance: 0.4304 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_brightwater.md, guide_corry_vale.md, guide_halden_bay.md, guide_marchwood.md, guide_pellew_sands.md, guide_walking.md
- Time: 0.60s

```
I do not have enough information to answer this question from the provided documents.
```

### What is best place to stay in town during the winter time according to city_guide for Corry Vale — run 3

- Best distance: 0.4304 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_brightwater.md, guide_corry_vale.md, guide_halden_bay.md, guide_marchwood.md, guide_pellew_sands.md, guide_walking.md
- Time: 0.55s

```
I do not have enough information to answer this question from the provided documents.
```

### What does city_guide best recommendation for food when eating in the area amongst all these locations? — run 1

- Best distance: 0.4964 (passed the gate)
- Sources retrieved: guide_corry_vale.md, guide_eating.md, guide_kestrelford.md, guide_pellew_sands.md
- Time: 1.06s

```
Based on the provided documents, almost everywhere in the region, the general pattern is that the good cooking is found one street back from where the visitors are, as places closer to the main tourist strips (like riverside strips or seafronts) are more expensive or limited to items like chips and ice cream (*guide_eating.md*). 

Specifically mentioned locations for good food include:
- **Marine Terrace** in Pellew Sands, which is one street back from the seafront, has four or less genuinely good places at roughly half the seafront price (*guide_pellew_sands.md*).
- **Corry Lane** in Brightwater, which is two streets inland and serves comparable food for about a third less than the riverside strip (*guide_eating.md*).
```

### What does city_guide best recommendation for food when eating in the area amongst all these locations? — run 2

- Best distance: 0.4964 (passed the gate)
- Sources retrieved: guide_corry_vale.md, guide_eating.md, guide_kestrelford.md, guide_pellew_sands.md
- Time: 1.08s

```
Based on the provided documents, almost everywhere in the region, the good cooking is found one street back from wherever the visitors are (such as Corry Lane being about a third less than Brightwater's riverside strip, Marine Terrace being roughly half the seafront price in Pellew Sands, and Halden Bay's harbour front being roughly double Fell Street). 

Source: `guide_eating.md`
```

### What does city_guide best recommendation for food when eating in the area amongst all these locations? — run 3

- Best distance: 0.4964 (passed the gate)
- Sources retrieved: guide_corry_vale.md, guide_eating.md, guide_kestrelford.md, guide_pellew_sands.md
- Time: 0.84s

```
Based on the provided documents, the general pattern for good cooking is to look one street back from where the visitors are, as it is typically priced lower or offers better quality than the main tourist strips (guide_eating.md). Additionally, specific notable recommendations include Marine Terrace in Pellew Sands (one street back) where the cooking is genuinely good and roughly half the seafront price (guide_pellew_sands.md). 

Sources: `guide_eating.md` and `guide_pellew_sands.md`.
```
