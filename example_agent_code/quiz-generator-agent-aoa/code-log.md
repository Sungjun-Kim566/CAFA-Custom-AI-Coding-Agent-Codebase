# Code Log — AoA Quiz Generator Agent (Performance Evaluation Record)

A structured record of how this agent was produced, suitable for performance
evaluation of the Foundry build (Opus 4.8 via Claude Code).

## 1. Task

Build an **AoA Quiz Generator**: configuration stage (topic, count, difficulty)
→ dynamic per-question LLM generation loop (generate → answer → grade → score →
route) → final report, in a strict Sandwich architecture, fully CAFA-compliant.

## 2. Foundry Workflow (`retrieve → design → verify → code → review`)

| Stage | Action |
|-------|--------|
| retrieve | Read `wiki/index.md`, `wiki/linter.md`; pulled archetypes **ASSISI** (on-the-fly generation from a topic) and **Socratic Tutor** (param-driven `REPEAT` count + LLM-in-loop with forward-referenced accumulating log) from the Agent Code Bank. |
| design | Composed both: ASSISI's topic→generation + Socratic's user-set loop count and history forward-reference, on top of the AoA verdict→points→SCORE scorer. 12-turn plan. |
| verify | Pre-checked parser-critical rules: symbolic `model:null`, control-flow isolation, double-quote args, one input control per visible turn, loop-result indexing. |
| code | Wrote `quiz-generator-agent-aoa.json`. |
| review | Automated loop-aware linter pass against `wiki/linter.md`. |

## 3. Build Latency

| Metric | Value |
|--------|-------|
| Build latency (start of generation → verified, linted agent) | **142 s (2m 22s)** |
| Start | 2026-06-16 22:41:44 KST |
| End | 2026-06-16 22:44:06 KST |

> This is Foundry generation latency. It is separate from the agent's **runtime**
> latency on CAFA, which scales with the user-chosen `NUM_QUESTIONS`: each question
> incurs two LLM calls (generation T6 + grading T8), plus one final analysis call
> (T12). Runtime LLM calls ≈ `2 × NUM_QUESTIONS + 1`.

## 4. Complexity / Structure Metrics

| Metric | Value |
|--------|-------|
| Total turns | 12 |
| LLM turns | 3 (T6 generate, T8 grade, T12 analyze) |
| Symbolic turns | 9 |
| Hidden control turns (`show:false`) | 4 (T4, T5, T9, T10) |
| Input controls | 4 (TEXTAREA, RADIO, RADIO, TEXTAREA) |
| Agent Parameters | 7 |
| Loop body size | 5 turns (T6–T10) |
| JSON size | ~8.4 KB |
| Runtime LLM calls | 2·N + 1 (N = NUM_QUESTIONS) |

## 5. Linter Result (review stage)

Automated checks against `wiki/linter.md`:

- Root keys exactly `options` + `prompts` — **PASS**
- Required metadata (`title/brief/name/description/greeting`) — **PASS**
- Every AP has `org`/`cond`/`desc`; valid `cond` — **PASS**
- Symbolic turns: `model:null`, empty `system`, exactly one `/` comment line, no
  stray `temperature`/`max-tokens`/`output-values` — **PASS**
- LLM turns: non-null `model`, no leading `/` — **PASS**
- ≤ 1 input control per visible turn — **PASS**
- `REPEAT` is the only control-flow command in its own hidden turn — **PASS**
  (Note: an initial linter script falsely flagged this because it counted the
  `@TN()@` *arguments* as commands; corrected check confirms isolation — the form
  matches the canonical AoA archetype `@REPEAT(@TN(1)@, @TN(n)@, "@PARAM@")@`.)
- No escaped square brackets, no double backslashes — **PASS**
- Loop-result indexing — **PASS** (see §6)

**OVERALL: ALL PASS.**

## 6. Loop-Result Indexing Audit (the critical AoA pitfall)

REPEAT body = T6–T10. Every loop-internal turn-result reference was audited:

| Turn | Reference | Indexed? | Verdict |
|------|-----------|----------|---------|
| T6 | `@TR@TN(4)@@` (prior transcript) | no | **Intentional** — full history injected into the generation prompt; not fed to a command |
| T7 | `@TR@TN(-1)@[@R_i@]@` (this question) | yes | OK |
| T8 | `@TR@TN(-2)@[@R_i@]@` (this question) | yes | OK |
| T9 | `@TR@TN(-1)@[@R_i@]@` ×2 (in SET/MAP/EVAL) | yes | OK — all command-fed results indexed |
| T10 | `@TR@TN(-4)@[@R_i@]@`, `@TR@TN(-2)@[@R_i@]@` | yes | OK |

Post-loop references (T11 `@TR@TN(-1)@@`, T12 `@TR@TN(-2)@@`) are intentionally
un-indexed to read the **full** accumulated transcript — correct per the rule.

## 7. Known Assumptions / Risks

- **Free-text injection.** The accumulated transcript (containing LLM and user
  text) is injected into the T6 generation prompt and the T11/T12 outputs. This
  follows the KB-established Socratic history pattern; user text is not sanitized of
  reserved `@`/`|` characters. Acceptable here because the transcript is used only
  as prompt context / display, never as input to list commands. If this agent later
  writes user text to a list-based command or `LOG`, add a sanitization turn
  (linter Rule 9.1).
- **RADIO-bounded count.** `NUM_QUESTIONS` is constrained to `3|5|10` for a clean,
  parseable `REPEAT` count; switching to free-text count would require validation.

## 8. Reproducibility

Re-running the same request against the same KB is expected to reproduce this
architecture (same sandwich, same 12-turn skeleton, same indexing), per the
Foundry "reproducible" quality constraint. Content (personas, options) may vary.
