# Bilinc on DolphinBench

Bilinc as the memory of Hermes Agent with GPT 5.6 Luna on [DolphinBench](https://dolphinbench.ai): **443 of 600 tasks passed (73.8%) for $55.61 in total.**

Results page: https://bilinc.space/benchmark

| Memory | Tasks passed | Accuracy | Total cost |
|---|---|---|---|
| **Bilinc** | **443 / 600** | **73.8%** | **$55.61** |
| Mem0 | 424 / 600 | 70.7% | $96.21 |
| Hindsight | 417 / 600 | 69.5% | $84.65 |
| Honcho | 411 / 600 | 68.5% | $142.85 |
| Built-in (no external memory) | 394 / 600 | 65.7% | $61.48 |
| Supermemory | 355 / 600 | 59.2% | $345.64 |

Hermes Agent + GPT 5.6 Luna for every row. Bilinc: our run, completed 25 November 2026. Other rows: as published on the [DolphinBench leaderboard](https://dolphinbench.ai/leaderboard), read 25 November 2026.

## By persona

| Persona | History | Tasks passed |
|---|---|---|
| Morgan | 3,400 messages | 158 / 200 |
| Riley | 5,128 messages | 150 / 200 |
| Alex | 5,011 messages | 135 / 200 |

13,539 messages ingested in total, then 600 tests. Total cost $55.61: ingestion $51.48, tests $4.13.

## How the run was done

- The official harness and dataset, with Bilinc connected through the published Bilinc plugin for Hermes (version 1.1).
- The benchmark's fair-run settings: no bundled skills, no file or terminal tools.
- Rules written down before the run: when to stop, what counts as a deviation, and that aborts happen only for infrastructure faults, never for slow or empty recalls.
- Every persona started from an empty memory and read its whole history in order before any test. Tests ran one at a time, after all ingestion had finished.
- Graded by the benchmark's own grader. During the run only completion counts, error rates and costs were watched; no test, trace or grade was read.
- The grades were sealed before anyone read them: the sha256 below was taken over all 600 grade files first, and the totals were read after.

## Check it yourself

```
python3 verify.py
```

It recounts every grade file in `grades/<persona>/<test>.json` (a task passes only when every check passes) and recomputes the seal:

```
532dd1e635c63b0aaafa53cd43120720f2ae3e1bf73ca469928baf532a85c3a4
```

The full records (every conversation, tool call, grade and cost, with the exact harness, plugin and model settings) are available for review: support@bilinc.space.

## License

The grade files and this report: CC BY 4.0, ReARC Labs.
