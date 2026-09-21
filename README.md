# The Unofficial Guide

**Bryant Burciaga · Corpus: `city_guides`**

> **This file is your submission.** Fill it in as you go — most sections get
> written during the milestone that produces them, not at the end.
>
> How the starter works, and every command you'll need, is in `RUNNING.md`.
> Leave that file alone.
>
> **Paste everything as text.** No screenshots, no video. A typed table gets
> full credit; a picture of the same table gets none.
>
> Delete these instruction blocks as you replace them. The `<!-- -->` comments
> are notes to you and don't show up when the page renders — you can leave them
> or remove them.

---

# Unit 1

## What This Does

<!-- Three or four sentences. Which corpus you picked, and the kinds of
     questions your system answers. Write it for someone who has never seen
     this repo.

     Milestone 5. -->

 This is a RAG system that uses Google Gemini and a corpus of "unofficial" city guides from prior travelers made to help provide guidance and inform users on their travels thanks to a helpful transportation guide. The corpora this is structured around includes fairly well-detailed, and well organized information. The questions this system answers are around different specific locations and how the weather, food, attractions, distances, and travel modes all play into the planning for a traveler coming into the area. Overall, should give a great 'real', but 'unofficial' guide for making the best out of traveling to these remote and rural areas.     

## Chunking Strategy

**Chunk size:**
450

**Overlap:**
120


<!-- What about YOUR documents made you pick these numbers? Short posts and
     long sectioned guides don't want the same chunking, and "800 seemed
     reasonable" earns nothing. Point at something you noticed when you read
     the documents in Milestone 1.

     If you changed your mind partway through, say so and say why. That's worth
     more than pretending you got it right first time.

     Milestone 3. -->

I chose a chunk size of 450 because that encompasses some of the largest paragraphs and sections of information given in the corpora for City Guides. An overlap of 120 also seem sufficient to provide even lenghtier sentences some overlap into the next paragraph for context. Originally, I had 50 as my overlap, but I changed my mind and made that larger after some consideration to ensure there is a bit more context into the next paragraph, especially where there are some lenghtier sentences. 

## Sample Chunks

<!-- Five chunks, pasted as text. Label each one and name the file it came from
     AND the function that produced it — the grader checks your code against
     what you claim here.

     `python app.py chunks -n 5` prints all three for you. Copy them straight
     across.

     Milestone 3. -->

**Chunk 1** — source: `guide_accessibility.md#0 ` — produced by: `chunker.py::fallback_split`

# Getting around the region with limited mobility

An honest assessment rather than a promotional one. Some of these places are
difficult and it is better to know in advance.

## Straightforward

**Thornby Wells** is the easiest town in the region. It is flat, compact, and
everything is within three minutes of everything else. Parking is free for two
hours anywhere in town and the station is central. The pump room and gardens
are level throughout


**Chunk 2** — source: `guide_corry_vale.md#2 ` — produced by: `chunker.py::fallback_split`

. There is a farm shop at the valley mouth that sells bread, cheese and little else, and it closes at 4pm. Bring supplies; this is not a place with options.

## What to see

The valley itself is the attraction. The footpath network is dense and well marked, and a circuit taking in three of the four villages is about nine miles with 500 metres of ascent. The chapel in the second village is 12th century and always unlocked.

## Where to stay

Perha

**Chunk 3** — source: `guide_givens_mill.md#0 ` — produced by: `chunker.py::fallback_split`

# Givens Mill

Givens Mill is a village of 700 built around a working watermill that still grinds flour commercially. It is the sort of place people visit for an afternoon and then talk about for longer than the visit lasted.

## Getting there

No station and no bus on Sundays; four buses a day from Brightwater on weekdays, taking 30 minutes. Driving is 20 minutes. The village car park holds about forty cars and is full by 11am on summer Saturday


**Chunk 4** — source: `guide_kestrelford.md#3  ` — produced by: `chunker.py::fallback_split`

und but is much reduced from November to February. August is busy with walkers. The single-track approach road is genuinely difficult in snow and the town can be cut off for a day or two most winters.

## Practical notes

Cash is still useful at the market and in smaller places, though cards are
accepted almost everywhere now. Mobile coverage is good in the centre and
patchy on the outskirts. The nearest full hospital is in Brightwater; there is

**Chunk 5** — source: `guide_regional_transport.md#1` — produced by: `chunker.py::fallback_split`

visitors. Services
concentrate on weekday daytimes. Sunday service is minimal to non-existent
outside the Brightwater town routes.

The Kestrelford service is hourly on weekdays, two-hourly on Saturdays, and
does not run on Sundays. The Halden Bay coast service runs four times daily
year-round.

## Driving

Roads are good between the towns and poor on the approaches to both Kestrelfor0d
and Halden Bay. The Kestrelford approach is single-track with

## Sample Answer

<!-- One complete question and answer, pasted as text, with the source line
     visible. Milestone 4. -->

**Question:**
What does the Brightwater guide say about traveling during the Winter time?"

**Answer:**

Based on the provided documents, the transportation guide does not mention traveling during the winter time. However, *guide_seasons.md* notes that several riverside businesses in Brightwater close entirely from January to March.

According to `guide_walking.md`, in winter you should add four minutes to any Brightwater walking estimate because the path past the pond ices over, and boots with real tread matter more than any other equipment. Additionally, `guide_seasons.md` notes that several riverside businesses in Brightwater close entirely from January to March during the winter.

Sources retrieved: guide_regional_transport.md, guide_seasons.md, guide_walking.md

**My relevance cutoff:**

<!-- The number you set in config.py, and how you got there.

     You ran five questions your corpus covers and the five in OUT_OF_SCOPE
     that it clearly doesn't, and wrote down the best distance for each. What
     did those two groups look like? Where was the gap? Put the actual numbers
     here — the table below wants all ten rows.

     Milestone 4. -->

I set the number in config.py to .520 because the closest any query got was .510 from my in-scope corpus list. All out of scope questions were in the .8 range and above so I felt like this kept things tight and provided good answers.

| Question | In corpus? | Best distance |
|---|---|---|
| What does the Brightwater guide say about traveling during the Winter time? |Yes| .480 |
| What does the city_guide say is the best place to stay in when visiting Thornby Wells based on budget? | Yes | .354 |
| When is it best to use a bike, bus, rideshare, or walk according to the city_guide for Elder Ness? | Yes | .510 |
| What is best place to stay in town during the winter time according to city_guide for Corry Vale? | Yes | .444 |
| What does city_guide best recommendation for food when eating in the area amongst all these locations? | Yes | .496 |
|What is the capital of Mongolia?  | No | .803 |
| How do I change the oil in a diesel engine? | No | .891 |
| Who won the 1994 World Cup? | No | .873 |
| What is the recommended dosage of ibuprofen for a headache? | No | .841 |
| How do I write a for loop in Rust? | No | .820 |


## How I Used AI

<!-- Two specific moments. For each: what you asked for, what came back, and
     what you changed about it.

     "I asked Claude to write the chunking function from my notes. It ignored
     the overlap, so I added that myself" is the level of detail we're after.
     "I used AI to help me code" is not.

     Milestone 5. -->

**1.**
I asked perplexity with assistance in helping me to structure a question that didn't seem to be clear enough for the AI to pick up or or be structured correctly to meet the criteria. It was successful in helping to guide me.  

**2.**
I asked perplexity for guidance on how to think about the concept of chunks and overlaps. I had wrong mental model and it helped to clear up the right way to think about those concepts.

<!-- ── Stretch features ─────────────────────────────────────────────────────
     Doing one? Say so here BEFORE you start. A feature this README never
     claims earns nothing.
     ───────────────────────────────────────────────────────────────────────── -->

---

# Unit 2

<!-- These sections get ADDED to what's already above. Don't delete or rewrite
     unit 1 — the point is that someone can see what you said before you knew
     how it went. -->

## Run Log — Before

<!-- Your five criteria, three runs each. `python run_eval.py --label before`
     runs the questions, puts the OUT_OF_SCOPE ones through the gate, and
     writes it all into results/ for you. Targets come from criteria.md; the
     verdict column is your call.

     Criterion 3 is measured in one deterministic pass rather than three, so
     the same number goes in all three run columns. That's correct, not lazy.

     Milestone 1. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 |  |  |  |  |
| 2. Every answer names a source | 5 of 5 |  |  |  |  |
| 3. Gate stops out-of-corpus questions | 4 of 5 |  |  |  |  |
| 4. | | | | | |
| 5. | | | | | |

<!-- Underneath, paste the REAL output for each criterion from one of your
     runs — the actual text your system produced, not a description of it.
     Name the file and function that produced it. -->

## Verdicts

<!-- MET or MISSED for each of the five, against the target you wrote last
     unit — not a new one. Plus a sentence on how you decided. That sentence
     matters most where it was close.

     If your target said 4 of 5 and your runs came out 4, 3, 4, that's a MISS.
     The target has to hold, not show up occasionally.

     Milestone 2. -->

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 |  |  |  |
| 2 |  |  |  |
| 3 |  |  |  |
| 4 |  |  |  |
| 5 |  |  |  |

## Diagnoses

<!-- For each miss: which stage caused it, and how. The stage alone isn't
     enough — you need the mechanism.

     Not a diagnosis: "Question 3 didn't work."
     A diagnosis:     "Question 3 asks about laundry costs. The answer is in
                       one sentence that got split across two chunks, so
                       neither chunk on its own contains it."

     The five stages: loading → chunking → embedding → retrieval → generation.

     Look for a pattern. If three misses all ask about numbers, that's one
     problem, not three.

     Missed nothing? Say so, then say honestly whether your targets were set
     low, and which one you'd tighten and to what.

     Milestone 3. -->

## The Improvement

**What I changed:**

**Why I picked it:**

<!-- Connect it to a specific diagnosis above in one sentence. If you can't,
     you picked a fix because it sounded impressive. -->

### Run Log — After

<!-- Same format, same five criteria, three runs each.
     `python run_eval.py --label after` -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 |  |  |  |  |
| 2. Every answer names a source | 5 of 5 |  |  |  |  |
| 3. Gate stops out-of-corpus questions | 4 of 5 |  |  |  |  |
| 4. | | | | | |
| 5. | | | | | |

**Did it help?**

<!-- Say plainly whether it did, and how you know. If it made things worse,
     say that — a change that backfired, honestly reported, earns full credit
     and is more interesting than one that worked. What matters is that you can
     tell.

     Milestone 4. -->

## What's Still Broken

<!-- For each criterion still missed after your fix: what you'd do about it,
     and why you stopped where you did.

     "I ran out of time" is fine if it's true. Pretending nothing is left is
     not.

     Milestone 5. -->

## What I'd Do Differently

<!-- Knowing what you know now — which of your five criteria would you write
     differently, and why?

     Milestone 5. -->
