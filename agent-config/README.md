# agent-config

Restructured CAFA Coding Agent configuration, separated from the original source
notes (which remain untouched in `../1/`, `../README.md`, etc.).

This follows the Wiki-based direction in `../Fix_log/2026-06-10.md`: instruction
strings, framework knowledge, and code/syntax references are kept in distinct layers.

```
agent-config/
├─ CLAUDE.md            # Identity · Workflow · Retrieval instructions (the core config)
├─ prompts/             # instruction strings, one per workflow role
│  ├─ coding-agent.md   #   design + code stages (blueprint, ontology, turns, syntax)
│  ├─ validator.md      #   verify stage (pre-code checklist)
│  └─ reviewer.md       #   review/revise stage + output packaging
└─ wiki/                # framework knowledge (retrieval targets)
   ├─ index.md          #   KB routing table — start retrieval here
   ├─ protocol.md       #   full command/syntax reference  (from 1/2_CAFA_Protocol.md)
   ├─ linter.md         #   linter & rules                 (from 1/01_...Linter and Rules.md)
   └─ examples/
      └─ code-bank.md   #   known-good agent code archetypes (from 1/4_CAFA_Agent_Code_Bank.md)
```

## Source mapping

| New file | Derived from |
|----------|--------------|
| `CLAUDE.md` | `1/00_System_Instruction.md` (persona, workflow, KB index, scope rules) |
| `prompts/coding-agent.md` | `1/00_System_Instruction.md` §3,5–8 (blueprint, ontology, turn, command rules) |
| `prompts/validator.md` | `1/00_System_Instruction.md` §4 + `1/01_...Linter and Rules.md` |
| `prompts/reviewer.md` | `1/00_System_Instruction.md` §9,10,12,13 + references |
| `wiki/index.md` | `1/00_System_Instruction.md` §2.1 (KB index) |
| `wiki/protocol.md` | copy of `1/2_CAFA_Protocol.md` |
| `wiki/linter.md` | copy of `1/01_CAFA Agent Code Linter and Rules.md` |
| `wiki/examples/code-bank.md` | copy of `1/4_CAFA_Agent_Code_Bank.md` |
