# Validator — Pre-Code Verification

Validate the Blueprint against parser-critical rules
*before* writing any JSON. Authoritative rule source: `../wiki/linter.md`.

---

## Blueprint verification checklist

- The framework choice is explicit and matches the requested workflow.
- Every planned command is listed and sourced from `../wiki/protocol.md`.
- A closest known-good example/pattern is identified from `../wiki/code-bank.md`
  (or you state why none applies).
- `AP`/`JP` is fully specified for every planned parameter reference.
- The turn plan respects:
  - Symbolic vs LLM separation
  - control-flow isolation
  - UI Constraints
  - the dependency next-turn rule

### If verification fails
1. **revise the Blueprint**
2. **re-verify**
3. **code**

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
- **Default**: One input control per visible turn.
- Multiple input controls per visible turn allowed for token efficiency
  (one Submit gathers all; every non-`CHECKBOX` control must be filled before
  submission proceeds).

**Quoting & escaping**
- All command args double-quoted (numbers too); no single quotes.
- No `\\`, no `\[` / `\]`.

---

For the complete linter checklist (`AP` `cond` values, `SP` reference, data-integrity
and concurrency patterns, etc.), retrieve `../wiki/linter.md`.
