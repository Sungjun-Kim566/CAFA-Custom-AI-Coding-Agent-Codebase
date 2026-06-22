# Cybersecurity Fundamentals Quiz Agent (AoA Framework)

A CAFA quiz agent built with the **AoA (Architecture of Alignment / Assessment)**
framework. It administers a fixed bank of constructed-response cybersecurity
questions, grades each answer against a rigid rubric, maintains a dynamic running
score, and reports a final result.

## Files

- [cybersecurity-quiz-agent-aoa.json](./cybersecurity-quiz-agent-aoa.json) — the CAFA agent configuration (options, params, prompts).

## Target Mechanism

An iterative critique/scoring loop: the agent presents a question, captures the
user's free-text answer via a `TEXTAREA`, evaluates it against a rigid 4-level
rubric, updates a dynamic `SCORE` variable, and routes to the next question or the
final score report.

## Structure — Strict "Sandwich" Architecture

The `REPEAT` loop (Turn 1) wraps a three-turn sandwich, run once per question:

| Turn | Layer | Type | Role |
|------|-------|------|------|
| T1 | Loop controller | Symbolic, hidden | `@REPEAT(@TN(1)@, @TN(3)@, "@TOTAL_QUESTIONS@")@` — alone in its dedicated hidden turn |
| T2 | **Symbolic Input** | Symbolic, visible | Presents `@QUESTIONS[@R_i@]@`, captures answer via `@TEXTAREA("answer_@R_i@", ...)@` |
| T3 | **LLM Evaluation** | LLM, visible | Grades answer vs `@RUBRICS[@R_i@]@`; `output-values` constrains output to one of four verdict labels |
| T4 | **Hidden Control / Routing** | Symbolic, hidden | Indexes verdict, `MAP`s it to points, updates the dynamic `SCORE` via `EVAL` |
| T5 | Final report | Symbolic, visible | Total, percentage, per-question breakdown |

## CAFA Protocol Compliance

- **`model: null` for symbolic turns** (T1, T2, T4, T5); each symbolic `user`
  string begins with a single `/` comment line and the `system` is empty.
- **Standalone hidden logic turns**: the `REPEAT` controller (T1) and the
  scoring/routing logic (T4) are isolated, hidden (`"show": false`) turns.
- **Strict double-quote string formatting**: all JSON strings and all command
  arguments use double quotes; numbers are quoted; no single quotes, no trailing
  commas, no escaped square brackets, no double backslashes.
- **Loop-result indexing**: loop-internal turn results are indexed by the current
  iteration — `@TR@TN(-1)@[@R_i@]@` — before being fed to `MAP`/`EVAL`/`SET`, so
  the accumulating pipe-delimited System Parameter never corrupts the score.
- **No same-turn dependencies**: T4's `SCORE` accumulator re-runs `MAP` inline and
  reads the prior-iteration `SCORE` rather than referencing same-turn variables.
- **Relative turn numbering** (`@TN()@`) throughout — no hardcoded turn references.

## Build Latency

See [BUILD-LOG.md](./BUILD-LOG.md) for the recorded foundry build latency.

## How to Import & Run

1. Copy the entire contents of `cybersecurity-quiz-agent-aoa.json`.
2. Go to https://ai.cafalab.com/
3. Click **Create Agent** → **Build from Scratch** → **Import from Text**.
4. Paste the JSON and click **Import**.

## References

- Choi, J. (2025). AoA Rubric Quiz Agent: Looped Symbolic-Input → LLM-Evaluation → Hidden-Control Sandwich with Loop-Indexed Verdict Scoring. In *Collective AI on the Foundation AI (CAFA): The pathway of digital transformation of intelligence.* CAFA Lab, Inc.
