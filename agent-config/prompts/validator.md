# Validator — Pre-Code Verification

Drives the **verify** stage: validate the Blueprint against parser-critical rules
*before* writing any JSON. Authoritative rule source: `../wiki/linter.md`.

---

## Blueprint verification checklist

- The framework choice is explicit and matches the requested workflow.
- Every planned command is listed and sourced from `../wiki/protocol.md`.
- A closest example/pattern is identified from `../wiki/examples/code-bank.md`
  (or you state why none applies).
- AP/JP is fully specified for every planned parameter reference.
- The turn plan respects:
  - Symbolic vs LLM separation
  - control-flow isolation
  - one input control per visible UI turn
  - the dependency next-turn rule

If verification fails: **revise the Blueprint first, then re-verify, then code.**

---

## Parser-critical rules to confirm

**JSON validity**
- Single valid JSON object; no trailing commas; no JSON comments.

**Schema constraints**
- Root keys exactly `options`, `prompts`.
- Only allowed keys under `options` and under each `prompts` entry
  (see `coding-agent.md` §4).

**Symbolic vs LLM integrity**
- Symbolic turns: `"model": null`, `user` first line begins with `/`, `system` empty.
- LLM turns: `system`/`user` do **not** start with `/`; include `model`,
  `temperature`, `max-tokens`.

**Control-flow isolation**
- `REPEAT` / `JUMP` / `END` each alone in their own hidden (`"show": false`) symbolic
  turn.

**Dependency**
- No same-turn use of newly `SET` / `LOAD` / `IMPORT` / `MAP` values.

**UI constraints**
- One input control per visible turn.

**Quoting & escaping**
- All command args double-quoted (numbers too); no single quotes.
- No `\\`, no `\[` / `\]`.

---

For the complete linter checklist (AP `cond` values, SP reference, data-integrity
and concurrency patterns, etc.), retrieve `../wiki/linter.md`.
