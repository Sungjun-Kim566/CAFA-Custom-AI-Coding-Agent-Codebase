# Coding Agent — Design & Code Generation

Purpose: Drives the **design** and **code** stages of the workflow. Produce the Blueprint
first, verify it (`validator.md`, `reviewer.md`), then generate the JSON.

---

## 1. Blueprint-first requirement

Before writing any CAFA agent JSON, produce a Blueprint called **Design**. Create it
first, verify it internally, then use it to generate the code.

### Blueprint (Design) template — required keys

- **Primary goal** — one sentence describing what the agent must accomplish, plus the
  user-facing success outcome.
- **Framework used** — name the selected framework(s) and explain why they fit.
  (Retrieve from the ecosystem/framework entries in `../wiki/index.md`.)
- **Commands used** — list every CAFA command the agent will use; for each, state its
  purpose in this agent (UI, routing, scoring, control flow, storage). (Retrieve from
  `../wiki/protocol.md`.)
- **Example codes** — identify the closest known-good archetype you are adapting; note
  what you reuse vs. modify.
  - Retrieve via the router: extract keywords from the user's request and run
    `python3 tools/code_eg_router.py <keywords>` — it prints the best-matching
    entries from `../wiki/code-bank.md`.
  - On NO MATCH (exit code 2), run `--list` to scan the
    `CAFA Agent Code Bank Master Index` titles directly, or state why no
    archetype applies.
  - Do not read `../wiki/code-bank.md` wholesale; load only routed entries.<br>
  - Keyword Extraction Guidance
    1. The target user is not tech-ish. Always assume the user only has a little technical knowledge to fully explain the intent of the codes or programms that he/she wants to create.
    2. Look for words that has implications of technical intents such as iterations (e.g.`REPEAT`), Frameworks (e.g. `STAR`), or domain-specific coding conventions (e.g. `Basic REPAIR for Listening` at `wiki/code-bank.md`).
- **Ontology model specifications**
  - **Agent Parameters (`AP`) spec** — stable parameters in `options.params` (rubrics, lists, personas,
    routing tables, templates).
  - **JSON Parameters (`JP`) spec** (if needed) — structured intermediate objects that persist across turns.
  - **Link rules** — if lists must stay paired, specify `LINK` relationships.
- **Turn architecture plan** — enumerate every turn in order; classify each as
  Symbolic or LLM; identify hidden control-flow turns and visible UI turns (one input
  control per visible turn).
- **Verification plan** — the exact checks to run before coding (schema/allowed keys,
  triggers, dependency next-turn rule, control-flow isolation). See `validator.md`.

Proceed to coding only after the Blueprint passes verify.

---

## 2. Ontology rules (AP and JP)

- **`AP`** — stable knowledge, reusable rubrics, lists, personas,
  routing keys, templates. Define in `options.params`.
- **`JP`** — only when you need structured intermediate artifacts that
  persist across turns. Keep field names stable and referenced consistently.

Rules:
- Every referenced parameter must be defined before use.
- Any `SET` / `LOAD` / `IMPORT` / `MAP` result is usable only in a **subsequent** turn
  (dependency rule). The engine processes a turn's commands simultaneously.

---

## 3. Turn design (Symbolic vs LLM)

Classify every turn.

**Symbolic turn** — commands, control flow, UI input controls, setup, deterministic
mapping.
- Trigger: the `user` prompt's first line starts with `/` (comment marker) or a
  control-flow command. The `system` prompt should be empty.
- Set `"model": null`.

**LLM turn** — generation, analysis, reasoning, evaluation, persona simulation.
- The `system`/`user` prompt must **not** start with `/`.
- Must include `model`, `temperature`, `max-tokens`.

**Markdown output** — for the final user-visible results turn, set `"markdown": true`
when the output benefits from formatting.

---

## 4. Command syntax, schema & formatting

**Command formatting**
- Full syntax with leading/trailing at-signs: `@COMMAND("arg1", "arg2")@`
- In documentation signatures, show optional args with literal square brackets:
  `@RADIO("name", "prompt", "options"[, "other_prompt"])@`

**Argument quoting**
- All command arguments enclosed in double quotes, including numeric arguments. Single quotes forbidden.

**Character escaping**
- No double backslashes — single backslashes for standard JSON escapes (`\n`, `\"`).
- No escaped square brackets — use normal `[ ]` for parameter access (`@AP[1]@`,
  `@AP[1:3]@`).

**Strict JSON schema & allowed keys**
- Output is a single, valid, parsable JSON object.
- Root keys must be exactly: `options`, `prompts`.
- Allowed keys in `options`: `title`, `name`, `description`, `greeting`, `brief`,
  `params`.
- Allowed keys in each `prompts` entry: `system`, `user`, `show`, `model`,
  `temperature`, `max-tokens`, `markdown`, `output-values`.
- No JSON comments. No trailing commas.

---

## 5. Control flow, UI & dependency

**Dedicated control-flow turns** — `REPEAT`, `JUMP`, `END` must be the only command/text
in that turn's prompt. They must be symbolic, hidden (`"show": false`), and isolated.

**Input controls per visible UI turn** — default to one of `RADIO`, `CHECKBOX`, `TEXT`,
`TEXTAREA`, `SELECT` per visible (`"show": true`) symbolic turn. Multiple controls in
one visible turn are engine-supported (a single Submit gathers all; every
non-`CHECKBOX` control must be filled before submission proceeds). Displaying input
control(s) pauses the agent and provides a submit button.

**Dependency next-turn rule** — values created/changed by `SET`, `LOAD`, `IMPORT`,
`MAP`, etc. cannot be used in the same turn; they become available only in a
subsequent turn.

For full per-command behavior and the complete rule set, retrieve `../wiki/protocol.md`
and `../wiki/linter.md`.

---

## 6. Command referencing in prose

When referencing CAFA commands in explanations or manuals, use only:
- Full syntax with leading/trailing at-signs (e.g., `@SET("x", "1")@`,
  `@REPEAT("2", "5", "3")@`), or
- The command name in uppercase (e.g., `SET`, `REPEAT`).

Never use partial syntax like `@SET()` or `@SET`.

---

## 7. Project workspace persistence

Every build lives in `projects/<agent-slug>/` — create the directory on first
generation and keep it current on every revision:

1. **At design** — save the router output as the project's local code bank:
   `python3 tools/code_eg_router.py <keywords> > projects/<agent-slug>/local-code-bank.md`
   Save the verified Blueprint to `blueprint.md`.
2. **At code** — save the generated JSON to `agent.json` (overwrite on revision);
   append an entry to `code-log.md` (date, change summary, checklist status) on
   every generation or revision.
3. **When debugging an existing agent** — load `agent.json`, `blueprint.md`, and
   `local-code-bank.md` from the workspace first; they already contain the archetype
   this agent was built from. Re-run the router only if the fix requires an archetype
   not in the local code bank, and append any newly routed entries to
   `local-code-bank.md` so the workspace stays self-sufficient.
