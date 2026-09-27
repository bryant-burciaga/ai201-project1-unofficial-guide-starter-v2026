# Run log — before-final

- Produced by: `run_eval.py::main`
- Retrieval: `store.py::search`, chunks from `chunker.py::split_documents`
- Corpus: `city_guides` (index variant `default`)
- top-k: 8 · relevance cutoff: 0.52
- Runs per question: 3, caching off
- When: 2026-09-27 15:47

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
- Time: 2.88s

```
Based on the provided documents, the text does not contain specific information about traveling in Brightwater during the winter. 

*(Source: guide_regional_transport.md, guide_seasons.md, and guide_walking.md)*
```

### What does the Brightwater transportation guide say about traveling during the Winter time? — run 2

- Best distance: 0.4808 (passed the gate)
- Sources retrieved: guide_regional_transport.md, guide_seasons.md, guide_walking.md
- Time: 1.06s

```
Based on the provided documents, there is no specific Brightwater transportation guide mentioned that details traveling during the winter time (the transport document discusses the railway and buses generally, while winter information is found in `guide_seasons.md`). Therefore, I do not have enough information to answer this question.
```

### What does the Brightwater transportation guide say about traveling during the Winter time? — run 3

- Best distance: 0.4808 (passed the gate)
- Sources retrieved: guide_regional_transport.md, guide_seasons.md, guide_walking.md
- Time: 0.87s

```
Based on the provided documents, there is no mention of a Brightwater transportation guide or specific winter travel information for Brightwater's transportation (the documents only note that Brightwater carries on in winter because of the university, and mention winter conditions for Kestrelford's approach road, the coastal path, and Brightwater riverside businesses). Therefore, I do not have enough information to answer your question.
```

### What does the city_guide say is the best place to stay in when visiting Thornby Wells  based on budget? — run 1

- Best distance: 0.3539 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_halden_bay.md, guide_pellew_sands.md, guide_thornby_wells.md, guide_walking.md
- Time: 0.77s

```
The provided documents mention several small guesthouses with prices that are moderate and stable year-round, but they do not specify a single "best" place to stay based on budget (guide_thornby_wells.md).
```

### What does the city_guide say is the best place to stay in when visiting Thornby Wells  based on budget? — run 2

- Best distance: 0.3539 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_halden_bay.md, guide_pellew_sands.md, guide_thornby_wells.md, guide_walking.md
- Time: 0.98s

```
Based on the provided documents, there is no mention of a "city_guide" or specific recommendations for the "best place to stay" based on budget, other than the note that Thornby Wells has "several small guesthouses" with prices that are "moderate and stable year-round" (*guide_thornby_wells.md*). 

I do not have enough information to answer your specific question about the best place to stay based on budget.
```

### What does the city_guide say is the best place to stay in when visiting Thornby Wells  based on budget? — run 3

- Best distance: 0.3539 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_halden_bay.md, guide_pellew_sands.md, guide_thornby_wells.md, guide_walking.md
- Time: 1.34s

```
Based on the provided documents, there is no mention of a "city_guide" or specific recommendations for the "best place to stay" based on budget, other than mentioning that Thornby Wells has "several small guesthouses" with "moderate and stable year-round" prices (guide_thornby_wells.md). 

Sources: guide_thornby_wells.md
```

### When is it best to use a bike, bus, rideshare, or walk according to the city_guide for Elder Ness? — run 1

- Best distance: 0.5103 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_brightwater.md, guide_eating.md, guide_elder_ness.md, guide_halden_bay.md
- Time: 0.88s

```
Based on the provided documents, there is no mention of when it is best to use a bike, bus, or rideshare for Elder Ness. In fact, the documents state there is "No public transport" for Elder Ness (*guide_elder_ness.md*). 

I do not have enough information to answer the rest of your question.
```

### When is it best to use a bike, bus, rideshare, or walk according to the city_guide for Elder Ness? — run 2

- Best distance: 0.5103 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_brightwater.md, guide_eating.md, guide_elder_ness.md, guide_halden_bay.md
- Time: 5.36s

```
Based on the provided documents, there is no mention of when it is best to use a bike, bus, or rideshare in Elder Ness (the documents note there is no public transport). 

Source: `guide_elder_ness.md` and `guide_accessibility.md`.
```

### When is it best to use a bike, bus, rideshare, or walk according to the city_guide for Elder Ness? — run 3

- Best distance: 0.5103 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_brightwater.md, guide_eating.md, guide_elder_ness.md, guide_halden_bay.md
- Time: 0.69s

```
I do not have enough information to answer this question. The provided documents mention transport for other locations like Brightwater and Halden Bay, but they do not state when it is best to use a bike, bus, rideshare, or walk in Elder Ness.
```

### What is best place to stay in town during the winter time according to city_guide for Corry Vale — run 1

- Best distance: 0.4304 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_brightwater.md, guide_corry_vale.md, guide_halden_bay.md, guide_marchwood.md, guide_pellew_sands.md, guide_walking.md
- Time: 0.66s

```
I do not have enough information to answer this question from the provided documents.
```

### What is best place to stay in town during the winter time according to city_guide for Corry Vale — run 2

- Best distance: 0.4304 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_brightwater.md, guide_corry_vale.md, guide_halden_bay.md, guide_marchwood.md, guide_pellew_sands.md, guide_walking.md
- Time: 0.61s

```
I do not have enough information to answer this question. The provided documents do not contain a "city_guide for Corry Vale" that discusses the best place to stay during the winter time.
```

### What is best place to stay in town during the winter time according to city_guide for Corry Vale — run 3

- Best distance: 0.4304 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_brightwater.md, guide_corry_vale.md, guide_halden_bay.md, guide_marchwood.md, guide_pellew_sands.md, guide_walking.md
- Time: 0.79s

```
I do not have enough information to answer this question. The provided documents do not contain a city guide for Corry Vale that discusses the best place to stay during the winter.
```

### What does city_guide best recommendation for food when eating in the area amongst all these locations? — run 1

- Best distance: 0.4964 (passed the gate)
- Sources retrieved: guide_corry_vale.md, guide_eating.md, guide_kestrelford.md, guide_pellew_sands.md
- Time: 0.83s

```
Based on the provided documents, almost everywhere in the region, the general pattern is that the good cooking is found one street back from where the visitors are, where prices are often lower (for example, Corry Lane is about a third less than Brightwater's riverside strip, and Marine Terrace in Pellew Sands is roughly half the seafront price). 

Source: `guide_eating.md` and `guide_pellew_sands.md`
```

### What does city_guide best recommendation for food when eating in the area amongst all these locations? — run 2

- Best distance: 0.4964 (passed the gate)
- Sources retrieved: guide_corry_vale.md, guide_eating.md, guide_kestrelford.md, guide_pellew_sands.md
- Time: 0.73s

```
Based on the provided documents, almost everywhere in the region, the general pattern for good cooking is to look "one street back from wherever the visitors are," as these spots typically serve comparable food for a lower price (guide_eating.md).
```

### What does city_guide best recommendation for food when eating in the area amongst all these locations? — run 3

- Best distance: 0.4964 (passed the gate)
- Sources retrieved: guide_corry_vale.md, guide_eating.md, guide_kestrelford.md, guide_pellew_sands.md
- Time: 0.67s

```
Based on the provided documents, almost everywhere in the region, the general recommendation is that the good cooking is found one street back from wherever the visitors are (from `guide_eating.md`).
```
