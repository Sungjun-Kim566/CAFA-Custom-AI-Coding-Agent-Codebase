# Coding Agent — Design & Code Generation

Drives the **design** and **code** stages of the workflow. Produce the Blueprint
first, verify it (`validator.md`), then generate the JSON.

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
  what you reuse vs. modify. (Retrieve from `../wiki/examples/code-bank.md`.)
- **Ontology model specifications**
  - **AP spec** — stable parameters in `options.params` (rubrics, lists, personas,
    routing tables, templates).
  - **JP spec** (if needed) — structured intermediate objects that persist across turns.
  - **Link rules** — if lists must stay paired, specify `LINK` relationships.
- **Turn architecture plan** — enumerate every turn in order; classify each as
  Symbolic or LLM; identify hidden control-flow turns and visible UI turns (one input
  control per visible turn).
- **Verification plan** — the exact checks to run before coding (schema/allowed keys,
  triggers, dependency next-turn rule, control-flow isolation). See `validator.md`.

Proceed to coding only after the Blueprint passes verify.

---

## 2. Ontology rules (AP and JP)

- **AP (Agent Parameters)** — stable knowledge, reusable rubrics, lists, personas,
  routing keys, templates. Define in `options.params`.
- **JP (JSON Parameters)** — only when you need structured intermediate artifacts that
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
- All command arguments enclosed in double quotes. Single quotes forbidden.
- Numeric arguments must also be quoted strings.

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

**One input control per visible UI turn** — only one of `RADIO`, `CHECKBOX`, `TEXT`,
`TEXTAREA`, `SELECT` per visible (`"show": true`) symbolic turn. Displaying an input
control pauses the agent and provides a submit button.

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
