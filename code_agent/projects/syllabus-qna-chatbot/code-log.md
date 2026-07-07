# Code Log — Syllabus Q&A Chatbot

## 2026-07-06 — Initial build (v1)

**Request:** Simple syllabus Q&A chatbot; instructor pastes their own syllabus into
the agent; no limit on chatting; student can exit the chat session whenever they want.

**What was built:**
- Adapted the "Syllabus Q&A Chatbot – Ontology-Grounded Conversational Agent"
  archetype (OMG + IMPACT), router score 36. Saved routed entries to
  `local-code-bank.md`.
- Changes vs. archetype:
  - `MAX_CHAT` 10 → 9999 (effectively unlimited chat; exit is student-controlled).
  - All hardcoded turn references (`@TR3@`, `"6|7"`) replaced with `@TN()@` relative
    references (linter Rule 4.2 overrides examples).
  - RADIO exit-gate name made iteration-scoped: `continue_@R_i@`.
  - Router uses 4-arg `MAP` with empty default → fall-through on continue; removed
    the archetype's "Okay, let's continue" filler turn (7 turns → 6 turns).
  - `OM_SYLLABUS` desc marks it as the paste-your-own-syllabus slot; ships with the
    archetype's sample syllabus so it runs out of the box.

**Verification status:** PASSED
- JSON parses (`python -c json.load` — valid).
- Root keys `options`/`prompts` only; allowed keys only; no trailing commas/comments.
- Symbolic turns: `system: ""`, `user` starts with `/`, `"model": null`, one comment
  line each. LLM turn (T2) has `model`/`temperature`/`max-tokens`, prompts don't
  start with `/`.
- `REPEAT` (T1) and `JUMP` (T5) isolated in dedicated hidden turns.
- Loop-result indexing: T3 logs `@TU@TN(-1)@[@R_i@]@` / `@TR@TN(-1)@[@R_i@]@`;
  T2's un-indexed `@TR@TN(1)@@` intentionally reads the full accumulated history.
- Dependency next-turn rule respected (RADIO written T4, read T5).
- One input control per visible symbolic turn; all args double-quoted.
