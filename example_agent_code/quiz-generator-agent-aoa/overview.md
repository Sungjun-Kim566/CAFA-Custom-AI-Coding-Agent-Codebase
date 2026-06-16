# AoA Quiz Generator Agent — Overview

A CAFA agent built with the **AoA (Architecture of Alignment / Assessment)**
framework. Unlike a fixed-bank quiz, this is a **generator**: the user configures
the quiz, then the agent dynamically writes each question on the fly, grades the
free-text answer, tracks a running score, and finishes with a transcript and an AI
performance analysis.

- Agent file: [quiz-generator-agent-aoa.json](./quiz-generator-agent-aoa.json)
- Build/evaluation log: [code-log.md](./code-log.md)

## Target Mechanism

1. **Configuration stage** — the user supplies quiz parameters.
2. **Dynamic generation loop** — for each question the agent: tracks the current
   question number (`@R_i@`), generates a tailored, non-repeating question from the
   user's topic/data and difficulty, accepts an answer, grades it, updates the
   score, and routes to the next iteration via `REPEAT`.

## Configuration Inputs (Symbolic Input layer)

| Input | UI control | Stored as |
|-------|-----------|-----------|
| Quiz topic / inference data | `TEXTAREA` (T1) | `TOPIC` |
| Number of questions | `RADIO` `3\|5\|10` (T2) | `NUM_QUESTIONS` |
| Difficulty level | `RADIO` `Easy\|Medium\|Hard` (T3) | `DIFFICULTY` |

A hidden commit turn (T4) maps the captured controls into named Agent Parameters
so the loop count and prompts can reference them.

## Strict "Sandwich" Architecture

```
Symbolic Input (configuration)   →   LLM Generation & Assessment   →   Hidden Control / Routing / Looping
   T1 TEXTAREA topic                    T6  generate question            T5  REPEAT controller (count = NUM_QUESTIONS)
   T2 RADIO   count                     T8  grade answer (verdict)       T9  score: MAP verdict -> points, update SCORE
   T3 RADIO   difficulty                T12 final performance analysis   T10 transcript accumulator (hidden)
   T4 hidden  commit config                                             T11 deterministic score report (symbolic)
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
   in T4, and used as the `REPEAT` count in T5 — separate turns, honoring the
   atomicity/dependency rule. (Pattern from the Socratic Tutor archetype, which
   sets the loop count from a parameter.)

2. **LLM-in-the-loop generation with non-repetition.** T6 references the
   accumulating transcript turn via the forward reference `@TR@TN(4)@@` so each new
   question can avoid earlier ones. On iteration 1 the transcript is empty. (Same
   forward-reference-to-the-log pattern the Socratic Tutor uses for history.)

3. **Loop-result indexing.** Inside `REPEAT`, a turn's result System Parameter
   accumulates *all* iterations into one pipe-delimited string. Every loop-internal
   result consumed by a command (`SET`/`MAP`/`EVAL`) or shown for the current item
   is indexed by the iteration: `@TR@TN(-k)@[@R_i@]@`. The single un-indexed
   loop-internal reference (T6's `@TR@TN(4)@@`) is intentional — the *full* prior
   history is wanted there, and it is injected as prompt text, not fed to a command.

4. **Verdict → points → score.** T8 is constrained by `output-values` to exactly
   four labels, so T9's `MAP("...","Incorrect|Partially Correct|Mostly Correct|Fully Correct","0|1|2|3|0")`
   is reliable (N+1 return list, default last). `SCORE` accumulates by reading its
   prior-iteration value inside the same `SET` — the established accumulator pattern.

5. **Dynamic maximum.** Because the question count is user-chosen, the denominator
   is computed at report time: `@EVAL("@NUM_QUESTIONS@ * 3")@`.

## CAFA Protocol Compliance

- `model: null` on all symbolic configuration/control turns; each symbolic `user`
  starts with a single `/` comment line (or `"/ \n"` for content-only) and an empty
  `system`.
- Control flow isolated: the `REPEAT` controller (T5) is the only command in its
  own hidden turn; scoring (T9) and transcript (T10) routing are standalone hidden
  (`"show": false`) turns.
- Strict double-quote formatting for every JSON string and command argument;
  numbers quoted; no single quotes, trailing commas, escaped brackets, or double
  backslashes.
- Relative turn numbering (`@TN()@`) everywhere — no hardcoded turn references.
- One input control per visible turn (T1/T2/T3/T7 each have exactly one).

## How to Import & Run

1. Copy the contents of `quiz-generator-agent-aoa.json`.
2. Go to https://ai.cafalab.com/ → **Create Agent → Build from Scratch → Import from Text**.
3. Paste and **Import**.

## References

- Choi, J. (2025). ASSISI Framework: On-the-fly Assessment Generation and Analysis. In *Collective AI on the Foundation AI (CAFA).* CAFA Lab, Inc.
- Choi, J. (2025). Socratic Tutor — Essential: Configurable Socratic Dialogue Loop with TN-Based REPEAT. In *Collective AI on the Foundation AI (CAFA).* CAFA Lab, Inc.
- Choi, J. (2025). AoA Rubric Quiz Agent: Looped Symbolic-Input → LLM-Evaluation → Hidden-Control Sandwich. In *Collective AI on the Foundation AI (CAFA).* CAFA Lab, Inc.
