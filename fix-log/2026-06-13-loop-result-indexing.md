# Fix Log — Loop-Result Indexing in REPEAT Scoring Loops

- **Date:** 2026-06-13
- **Affected agent:** `quiz-agent-aoa/quiz-agent-aoa.json` (AoA Rubric Quiz Agent)
- **Severity:** High — silently corrupts scoring on every question after the first.
- **Status:** Fixed and verified.

## Symptom

In the per-question Hidden Control turn (T4), the LLM verdict was read with the
un-indexed System Parameter `@TR@TN(-1)@@`. Because T3 (the evaluator) runs **inside**
a `REPEAT` loop, its result SP accumulates every iteration's output into a single
pipe-delimited string:

- Iteration 1: `@TR@TN(-1)@@` → `Incorrect`
- Iteration 2: `@TR@TN(-1)@@` → `Incorrect|Mostly Correct`
- Iteration 3: `@TR@TN(-1)@@` → `Incorrect|Mostly Correct|Fully Correct`

Consequences:

- `VERDICT_@R_i@` stored the **whole growing list** instead of a single label.
- `MAP` received a multi-element string that matched no `value_list` entry, so it
  fell through to the default (`0`).
- The dynamic `SCORE` accumulator was therefore wrong for every question after Q1.

## Root cause

Turn results inside a `REPEAT` loop are accumulated, not overwritten. An un-indexed
`@TR@TN(-1)@@` returns the full accumulated list, not the current iteration's value.

## Fix

Index the loop result by the iteration number so only the current iteration's verdict
is extracted before `MAP`:

```
@TR@TN(-1)@@          ->   @TR@TN(-1)@[@R_i@]@
```

Applied to all three references in T4 (`VERDICT_@R_i@` SET, `POINTS_@R_i@` MAP, and the
`SCORE` accumulator EVAL).

## Verification

- JSON re-validated; root keys, allowed keys, symbolic `model:null`, REPEAT isolation,
  one-input-per-visible-turn all still pass.
- Confirmed 3 occurrences of `@TR@TN(-1)@[@R_i@]@` and zero bare `@TR@TN(-1)@@` in T4.

## Knowledge base updates

This fix was generalized into the KB so future agents avoid the pitfall:

- `wiki/protocol.md` — new **§8.1 Loop-Result Indexing** (Rule 8.1) + cross-reference
  under the REPEAT command entry.
- `wiki/linter.md` — new **Loop-Result Indexing Rule** + check under the REPEAT command.
- `wiki/index.md` — routing table updated to surface loop-result indexing.
- `wiki/examples/code-bank.md` — added the **AoA Rubric Quiz Agent** example, which
  documents the `@TR@TN(-1)@[@R_i@]@` trick as a featured technique.

## Rule of thumb

Any `TR` / `TU` / `TS` reference to a turn that executes inside a `REPEAT` loop must be
indexed with `[@R_i@]` when its value is consumed by `MAP`, `INDEX`, `EVAL`, or `SET`,
or stored. Leave it un-indexed only when you deliberately want the full accumulated list.
