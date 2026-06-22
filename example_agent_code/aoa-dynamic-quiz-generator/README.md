# AoA Dynamic Quiz Generator (AoA Framework)

A CAFA agent built with the **AoA (Architecture of Alignment / Assessment)**
framework. Unlike a fixed-bank quiz, this is a **generator**: the user configures
the quiz up front, then the agent dynamically writes each question on the fly,
captures and grades the free-text answer, tracks a running score, and finishes
with a deterministic breakdown plus an AI performance analysis.

## Files

- [aoa-dynamic-quiz-generator.json](./aoa-dynamic-quiz-generator.json) — the CAFA agent configuration (options, params, prompts).

## Target Mechanism

1. **Configuration stage** — the user supplies the quiz parameters via UI controls.
2. **Dynamic generation loop** — for each question the agent tracks the current
   question number (`@R_i@`), generates a tailored, non-repeating question from the
   user's topic/data and difficulty, accepts an answer, grades it on a rigid scale,
   updates the score, accumulates the transcript, and routes to the next iteration
   via `REPEAT`.

## Configuration Inputs (Symbolic Input layer)

| Input | UI control | Stored as |
|-------|-----------|-----------|
| Quiz topic / inference data | `TEXTAREA` (T1) | `TOPIC` |
| Number of questions | `RADIO` `3\|5\|10` (T2) | `NUM_QUESTIONS` |
| Difficulty level | `RADIO` `Easy\|Medium\|Hard` (T3) | `DIFFICULTY` |

A hidden commit turn (T4) `SET`s the captured controls into named Agent Parameters
so the loop count and the generation/grading prompts can reference them on the
**next** turn (honoring the atomicity/dependency rule).

## Strict "Sandwich" Architecture

```
Symbolic Input (configuration)   →   LLM Generation & Assessment   →   Hidden Control / Routing / Looping
   T1 TEXTAREA topic                    T6  generate question            T4  commit config (SET)
   T2 RADIO   count                     T8  grade answer (verdict)       T5  REPEAT controller (count = NUM_QUESTIONS)
   T3 RADIO   difficulty                T12 performance analysis         T9  score: MAP verdict → points, update SCORE
   T7 present + TEXTAREA answer                                          T10 transcript accumulator
   T11 deterministic score report
```

### Turn-by-turn

| Turn | Type | show | Role |
|------|------|------|------|
| T1 | Symbolic | true | `TEXTAREA` — capture topic / source material |
| T2 | Symbolic | true | `RADIO` — number of questions |
| T3 | Symbolic | true | `RADIO` — difficulty |
| T4 | Symbolic | false | `SET` `TOPIC` / `NUM_QUESTIONS` / `DIFFICULTY` (commit config) |
| T5 | Symbolic | false | `@REPEAT(@TN(1)@, @TN(5)@, "@NUM_QUESTIONS@")@` — loops T6–T10 |
| T6 | **LLM** | true | Generate question `@R_i@`, tailored to `@TOPIC@`/`@DIFFICULTY@`, avoiding prior questions |
| T7 | Symbolic | true | Present generated question + `TEXTAREA` answer capture |
| T8 | **LLM** | true | Grade answer; `output-values` → one of 4 verdict labels |
| T9 | Symbolic | false | Map verdict → points, update dynamic `SCORE` |
| T10 | Symbolic | false | Accumulate per-question transcript (hidden; `TR` grows) |
| T11 | Symbolic | true | Deterministic final score report + per-question breakdown |
| T12 | **LLM** | true | Holistic performance analysis from the transcript |

## Key Design Decisions (grounded in the CAFA KB)

1. **User-driven loop count.** `NUM_QUESTIONS` is captured via `RADIO`, committed
   in T4, and used as the `REPEAT` count in T5 — separate turns, so the
   atomicity/dependency rule is never violated.

2. **Dynamic question-number tracking.** The loop iteration System Parameter
   `@R_i@` is the "current question number." It threads through generation ("question
   `@R_i@` of `@NUM_QUESTIONS@`"), the answer-capture key (`answer_@R_i@`), the
   per-iteration verdict/points parameters, and the transcript heading.

3. **LLM-in-the-loop generation with non-repetition.** T6 reads the accumulating
   transcript via the forward reference `@TR@TN(4)@@` (which points to T10) so each
   new question can avoid earlier ones. On iteration 1 the transcript is empty.

4. **Loop-result indexing.** Inside `REPEAT`, a turn's result System Parameter
   accumulates *all* iterations into one pipe-delimited string. Every loop-internal
   result consumed by a command (`SET`/`MAP`/`EVAL`) or shown for the current item is
   indexed by the iteration: `@TR@TN(-k)@[@R_i@]@`. The single un-indexed reference
   (T6's `@TR@TN(4)@@`) is intentional — the *full* prior history is wanted there,
   injected as prompt text rather than fed to a command.

5. **Verdict → points → score.** T8 is constrained by `output-values` to exactly
   four labels, so T9's `@MAP("...","Incorrect|Partially Correct|Mostly Correct|Fully Correct","0|1|2|3|0")@`
   is reliable (N+1 return list, last item = default). `SCORE` accumulates by reading
   its prior-iteration value inside the same `SET` — the established accumulator pattern.

6. **Dynamic maximum.** Because the question count is user-chosen, the denominator is
   computed at report time: `@EVAL("@NUM_QUESTIONS@ * @POINTS_PER_Q@")@`.

## CAFA Protocol Compliance

- **`model: null` for symbolic turns** (T1–T5, T7, T9–T11); each symbolic `user`
  begins with a single `/` comment line (or `"/ \n"` for content-only) and the
  `system` is empty.
- **Standalone hidden logic turns**: the `REPEAT` controller (T5), scoring (T9),
  and transcript routing (T10) are each isolated, hidden (`"show": false`) turns.
- **Strict double-quote string formatting**: all JSON strings and command arguments
  use double quotes; numbers are quoted; no single-quote delimiters, no trailing
  commas, no escaped square brackets, no double backslashes.
- **Relative turn numbering** (`@TN()@`) throughout — no hardcoded turn references.
- **One input control per visible turn** (T1/T2/T3/T7 each have exactly one).

## How to Import & Run

1. Copy the entire contents of `aoa-dynamic-quiz-generator.json`.
2. Go to https://ai.cafalab.com/
3. Click **Create Agent** → **Build from Scratch** → **Import from Text**.
4. Paste the JSON and click **Import**.

## References

- Choi, J. (2025). ASSISI Framework: On-the-fly Assessment Generation and Analysis. In *Collective AI on the Foundation AI (CAFA): The pathway of digital transformation of intelligence.* CAFA Lab, Inc.
- Choi, J., Kim, S., & Yoon, K. (2012–present). Collective AI on the Foundation AI (CAFA) Platform. CAFA Lab, Inc. https://ai.cafalab.com
