# Blueprint (Design) — Syllabus Q&A Chatbot

## Primary goal

A syllabus-bounded Q&A chatbot: a student asks unlimited questions about the course
and gets answers grounded strictly in the instructor's own syllabus (stored as an
editable agent parameter), and can end the chat session at any moment via an explicit
exit choice. Success outcome: accurate, syllabus-only answers with a clean,
student-controlled session end.

## Framework used

- **OMG (Ontology Model-centered Generation)** — the syllabus is embedded as a
  read-only ontology parameter (`OM_SYLLABUS`); the LLM persona is constrained to
  answer only from it.
- **IMPACT (Iterative Multi-turn Process for AI Collaboration Technique)** — a
  `REPEAT` loop alternates an LLM conversation turn with a symbolic history-logging
  turn, preserving dialogue context across iterations.

Both retrieved from the Agent Code Bank entry "Syllabus Q&A Chatbot –
Ontology-Grounded Conversational Agent" (top router match).

## Commands used

| Command | Purpose in this agent |
|---------|----------------------|
| `@REPEAT("@TN(1)@", "@TN(4)@", "@MAX_CHAT@")@` | Control flow — drives the conversational loop (chat → log → exit gate → router). Dedicated hidden turn. |
| `@RADIO("continue_@R_i@", ...)@` | UI — per-iteration exit gate ("Ask another question" / "End chat"). |
| `@MAP(...)@` | Routing — converts the RADIO choice into a jump target; empty default = fall through (continue loop). |
| `@JUMP(...)@` | Control flow — exits the loop to the post-loop end turn when the student chooses "End chat". Dedicated hidden turn. |
| `@TN(n)@` | Relative turn referencing everywhere (linter Rule 4.2 — no hardcoded turn numbers). |
| `@TR@TN(-1)@[@R_i@]@` / `@TU@TN(-1)@[@R_i@]@` | Loop-result indexing — capture only the current iteration's exchange when logging history (linter Loop-Result Indexing Rule). |
| `@TR@TN(1)@@` (un-indexed) | Intentional full-accumulated-history read in the LLM turn's system prompt (conversational memory). |
| `@R_i@` | Current loop iteration — scopes RADIO names and history entries per iteration. |

## Example codes (archetype)

- **Reused:** "Syllabus Q&A Chatbot – Ontology-Grounded Conversational Agent"
  (router score 36) — persona + syllabus ontology + IMPACT loop + RADIO/MAP/JUMP exit.
- **Modified:**
  1. `MAX_CHAT` raised from `10` to `9999` — user requires *no practical limit* on
     chatting; exit is student-controlled, the cap is only a safety bound.
  2. Hardcoded turn numbers (`@TR3@`, `"6|7"`) replaced with `@TN()@` relative
     references per linter Rule 4.2 (linter overrides examples).
  3. RADIO name made iteration-scoped (`continue_@R_i@`) per the loop pattern in the
     "AI-to-AI Monitored Conversation" archetype (`monitor_choice_@R_i@`).
  4. Router MAP uses the 4-arg form with empty default (`""`) so "continue" simply
     falls through — drops the archetype's extra "Okay, let's continue" turn.
  5. `OM_SYLLABUS` desc marks it as the single place to paste the instructor's own
     syllabus; ships with a sample so the agent runs out of the box.

## Ontology model specifications

**Agent Parameters (`AP`) — `options.params`:**

| AP | cond | Content |
|----|------|---------|
| `CHATBOT_PERSONA` | `SELF` | TA persona; syllabus-only answering; polite refusal + redirect to instructor for out-of-scope questions. |
| `OM_SYLLABUS` | `SELF` | The custom syllabus (read-only ontology). **User replaces the sample text with their own syllabus.** |
| `MAX_CHAT` | `SELF` | `9999` — effectively unlimited loop bound. |

**`JP` spec:** none needed (no structured intermediate artifacts).
**Link rules:** none (no paired lists).

## Turn architecture plan

| Turn | Type | show | Role |
|------|------|------|------|
| T1 | Symbolic (hidden) | false | `REPEAT` loop setup over T2–T5. Dedicated control-flow turn. |
| T2 | LLM (visible) | true | Chat turn: persona + syllabus + accumulated history in `system`; `user: ""` pauses for student input; markdown output. |
| T3 | Symbolic (hidden) | false | History logger: appends `Student/TA` exchange for iteration `@R_i@` (indexed `TU`/`TR`). |
| T4 | Symbolic (visible) | true | Exit gate: one `RADIO` input control (`continue_@R_i@`). |
| T5 | Symbolic (hidden) | false | Router: `JUMP` + nested `MAP` — "End chat" → `@TN(1)@` (T6); default `""` → fall through, loop continues. Dedicated control-flow turn. |
| T6 | Symbolic (visible) | true | Post-loop end message (markdown). Reached by exit jump or (theoretical) loop exhaustion. |

## Verification plan

Per `validator.md`:
- Root keys exactly `options`, `prompts`; only allowed keys used; valid JSON, no
  trailing commas/comments.
- Symbolic turns: `system: ""`, `user` first line starts with `/`, `"model": null`,
  max one comment line.
- LLM turn (T2): prompts do not start with `/`; has `model`, `temperature`,
  `max-tokens`.
- Control-flow isolation: `REPEAT` (T1) and `JUMP` (T5) alone in dedicated hidden
  turns.
- Dependency next-turn rule: RADIO value written in T4, read in T5 — OK; no same-turn
  SET/MAP consumption.
- Loop-result indexing: T3 uses `[@R_i@]`; T2's un-indexed history read is
  intentional (full accumulated list).
- One input control per visible symbolic turn (T4).
- Quoting: all command args double-quoted (numbers included); no single quotes, no
  `\\`, no `\[ \]`.
