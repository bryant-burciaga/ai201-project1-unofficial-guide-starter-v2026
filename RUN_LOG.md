# Evaluation Run Log

## Baseline run

**Command run**

```bash
python run_eval.py --label before
```

**Raw evidence file:** `results/run_2026-09-23_2042_before.md`

**Evaluation function:** `run_eval.py` — use the actual function name from the file/code, if required by your course.

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---:|---:|---:|---:|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 0/5 | 0/5 | 0/5 | MISSED |
| 2. Every answer names a source | 5 of 5 | 0/5 | 0/5 | 0/5 | MISSED |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |

## Criterion evidence

### Criterion 1: Retrieved chunk contains the answer

Source: `results/run_2026-09-23_2042_before.md`  
Produced by: `run_eval.py` / `<actual function name>`

Paste the actual output for criterion 1 from the result file here.

### Criterion 2: Every answer names a source

Source: `results/run_2026-09-23_2042_before.md`  
Produced by: `run_eval.py` / `<actual function name>`

Paste the actual output for criterion 2 from the result file here.

### Criterion 3: Gate stops out-of-corpus questions

Source: `results/run_2026-09-23_2042_before.md`  
Produced by: `run_eval.py` / `<actual function name>`

```text
Out-of-scope questions (the gate should refuse these):
  refused  (best distance 0.803)  What is the capital of Mongolia?
  refused  (best distance 0.891)  How do I change the oil in a diesel engine?
  refused  (best distance 0.873)  Who won the 1994 World Cup?
  refused  (best distance 0.841)  What is the recommended dosage of ibuprofen for a headache?
  refused  (best distance 0.820)  How do I write a for loop in Rust?
  -> gate refused 5 of 5
```