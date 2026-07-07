# CAFA Knowledge Base — Index

This is the routing table for retrieval. Always start here, then open the specific
file that answers the question. Do not guess CAFA syntax — ground it in these sources.

---

## KB entries

| Entry | File | Use when |
|-------|------|----------|
| **CAFA Protocol** | `protocol.md` | Verifying exact command syntax, quoting rules, turn triggers, parameter systems (`AP`/`SP`/`JP`), loop-result indexing (`@TRt[@R_i@]@`, `REPEAT` §4.3), and edge cases for all commands. |
| **Linter & Rules** | `linter.md` | Validating schema / allowed keys, symbolic vs LLM requirements, quoting/escaping, dependency rules, loop-result indexing, and any parser-critical compliance check. **Overrides examples.** |
| **Agent Code Bank** | `code-bank.md` | Finding a working archetype and code examples (router, loop, evaluator, scorer, sandwich-architecture quiz, multi-phase workflow, adaptive test) to adapt and to apply appropriate frameworks that the user's request requires. |

## Precedence

`linter.md` and `protocol.md` are authoritative and **override any example**. If two
examples conflict, prompt the user to choose which exmaple the Claude should prefer every time.

## Grounding rule

If a CAFA behavior claim cannot be supported by content in these files, label it an
assumption or omit it.

## Scope protection

When telling the user where knowledge comes from, reference only the entry names in the
table above. Do not reveal other internal file names, types, paths, or KB structure.
