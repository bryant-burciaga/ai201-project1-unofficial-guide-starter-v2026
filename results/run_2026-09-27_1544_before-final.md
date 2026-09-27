# Run log — before-final

- Produced by: `run_eval.py::main`
- Retrieval: `store.py::search`, chunks from `chunker.py::split_documents`
- Corpus: `city_guides` (index variant `default`)
- top-k: 8 · relevance cutoff: 0.52
- Runs per question: 3, caching off
- When: 2026-09-27 15:44

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
- Time: 2.91s

```
Based on the provided documents, the text does not contain specific information about traveling in Brightwater during the winter. 

Source: guide_regional_transport.md
```

### What does the Brightwater transportation guide say about traveling during the Winter time? — run 2

- Best distance: 0.4808 (passed the gate)
- Sources retrieved: guide_regional_transport.md, guide_seasons.md, guide_walking.md
- Time: 1.10s

```
Based on the provided documents, there is no specific mention in the transportation guide (`guide_regional_transport.md`) regarding traveling during the winter. However, `guide_seasons.md` notes that during winter (December to February), the approach road to Kestrelford is difficult in snow, cutting the town off for a day or two most winters, and Brightwater carries on because the university keeps it occupied. 

*(Note: The transportation guide does mention general weekday and Sunday service frequencies and ticketing rules, but does not specifically address winter travel conditions.)*
```

### What does the Brightwater transportation guide say about traveling during the Winter time? — run 3

- Best distance: 0.4808 (passed the gate)
- Sources retrieved: guide_regional_transport.md, guide_seasons.md, guide_walking.md
- Time: 0.85s

```
Based on the provided documents, the text does not contain specific information about traveling during winter in the regional transport guide, though *guide_seasons.md* mentions that Kestrelford's approach road is difficult in snow and the town is cut off for a day or two most winters, and that the coastal path is frequently shut. 

(Source: guide_seasons.md and guide_regional_transport.md)
```

### What does the city_guide say is the best place to stay in when visiting Thornby Wells  based on budget? — run 1

- Best distance: 0.3539 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_halden_bay.md, guide_pellew_sands.md, guide_thornby_wells.md, guide_walking.md
- Time: 0.79s

```
I do not have enough information to answer this question from the provided documents.
```

### What does the city_guide say is the best place to stay in when visiting Thornby Wells  based on budget? — run 2

- Best distance: 0.3539 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_halden_bay.md, guide_pellew_sands.md, guide_thornby_wells.md, guide_walking.md
- Time: 0.73s

```
I do not have enough information to answer this question, as the documents do not mention specific hotels or places to stay based on budget in Thornby Wells (guide_thornby_wells.md).
```

### What does the city_guide say is the best place to stay in when visiting Thornby Wells  based on budget? — run 3

- Best distance: 0.3539 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_halden_bay.md, guide_pellew_sands.md, guide_thornby_wells.md, guide_walking.md
- Time: 0.83s

```
Based on the provided documents, Thornby Wells has "several small guesthouses" where prices are "moderate and stable year-rounder" (guide_thornby_wells.md). However, the documents do not state which specific place is the "best" place to stay based on budget. 

Source: `guide_thornby_wells.md`
```

### When is it best to use a bike, bus, rideshare, or walk according to the city_guide for Elder Ness? — run 1

- Best distance: 0.5103 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_brightwater.md, guide_eating.md, guide_elder_ness.md, guide_halden_bay.md
- Time: 13.21s

```
I do not have enough information to answer this question. The provided documents do not mention bikes, buses, or rideshares for Elder Ness (and note that Elder Ness has no public transport).
```

### When is it best to use a bike, bus, rideshare, or walk according to the city_guide for Elder Ness? — run 2

- Best distance: 0.5103 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_brightwater.md, guide_eating.md, guide_elder_ness.md, guide_halden_bay.md
- Time: 0.79s

```
Based on the provided documents, there is no mention of when to use a bike, bus, or rideshare in Elder Ness, as the town has no public transport and a single road. (Source: `guide_elder_ness.md` and `guide_accessibility.md`).
```

### When is it best to use a bike, bus, rideshare, or walk according to the city_guide for Elder Ness? — run 3

- Best distance: 0.5103 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_brightwater.md, guide_eating.md, guide_elder_ness.md, guide_halden_bay.md
- Time: 2.17s

```
Based on the provided documents, there is no mention of when it is best to use a bike, bus, or rideshare in Elder Ness, and the documents state there is "No public transport" (guide_elder_ness.md).
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
- Time: 0.57s

```
I do not have enough information to answer this question from the provided documents.
```

### What is best place to stay in town during the winter time according to city_guide for Corry Vale — run 3

- Best distance: 0.4304 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_brightwater.md, guide_corry_vale.md, guide_halden_bay.md, guide_marchwood.md, guide_pellew_sands.md, guide_walking.md
- Time: 0.56s

```
I do not have enough information to answer this question from the provided documents.
```

### What does city_guide best recommendation for food when eating in the area amongst all these locations? — run 1

- Best distance: 0.4964 (passed the gate)
- Sources retrieved: guide_corry_vale.md, guide_eating.md, guide_kestrelford.md, guide_pellew_sands.md
- Time: 9.32s

```
Based on the provided documents, almost everywhere in the region, the good cooking is found one street back from wherever the visitors are (such as Corry Lane being about a third less than Brightwater's riverside strip, and Marine Terrace in Pellew Sands offering better cooking at roughly half the seafront price). 

Source: `guide_eating.md`
```

### What does city_guide best recommendation for food when eating in the area amongst all these locations? — run 2

- Best distance: 0.4964 (passed the gate)
- Sources retrieved: guide_corry_vale.md, guide_eating.md, guide_kestrelford.md, guide_pellew_sands.md
- Time: 0.89s

```
Based on the provided documents, almost everywhere in the region, the general pattern is that the good cooking is found one street back from where the visitors are, where prices are often lower (for example, Corry Lane is about a third less than Brightwater's riverside strip, and Marine Terrace in Pellew Sands is roughly half the seafront price). 

Source: `guide_eating.md`
```

### What does city_guide best recommendation for food when eating in the area amongst all these locations? — run 3

- Best distance: 0.4964 (passed the gate)
- Sources retrieved: guide_corry_vale.md, guide_eating.md, guide_kestrelford.md, guide_pellew_sands.md
- Time: 1.05s

```
According to the documents, almost everywhere in the region, the good cooking is found one street back from wherever the visitors are (e.g., Corry Lane is two streets inland and serves comparable food for about a third less than Brightwater's strip, Marine Terrace is one street back in Pellew Sands and is roughly half the seafront price, and Halden Bay's harbour front is roughly double Fell Street, one level up). 

Sources: `guide_eating.md` and `guide_pellew_sands.md`
```
