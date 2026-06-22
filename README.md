# agent-config — CAFA Agent Foundry

The operational core of the **CAFA Custom AI Coding Agent**. This directory is the
concrete, file-based realization of the **LLM Wiki** direction described in the
repository root (`../README.md`): a small instruction core plus a retrievable knowledge
base, kept in distinct layers so the agent grounds CAFA syntax in truth instead of
hallucinating it.

Its job is to turn a user request into two artifacts:

- a **Blueprint** — the design of a CAFA agent, and
- **CAFA Agent Code** — valid, executable CAFA agent JSON generated from the Blueprint.

Per `fix-log/2026-06-10.md`, the current codebase is the **LLM-Wiki-based** implementation
(instruction strings, framework knowledge, and code/syntax references separated into
layers), with verification handled by dedicated workflow prompts rather than a separate
MCP server. The broader *PageIndex + Wiki + Validator* architecture is documented in
`../README.md`; this directory is where the Wiki + Validator half lives and runs.

---

## Two-layer separation

```
┌──────────────────────────────────────────────────────────┐
│                  AGENTS.md  (Agent Core)                   │
│            Identity · Workflow · Retrieval rules           │
└───────────────┬──────────────────────────┬────────────────┘
                │                          │
                ▼                          ▼
┌──────────────────────────────┐  ┌──────────────────────────────┐
│   Workflow Prompts            │  │   Knowledge Base (wiki/)      │
│   (how to work)               │  │   (what is true)              │
├──────────────────────────────┤  ├──────────────────────────────┤
│ • coding-agent.md  (design)   │  │ • index.md     (routing)      │
│ • validator.md     (verify)   │  │ • protocol.md  (syntax truth) │
│ • reviewer.md      (review)   │  │ • linter.md    (rules/schema) │
│                               │  │ • examples/code-bank.md       │
└──────────────────────────────┘  └──────────────────────────────┘
                │                          │
                └────────────┬─────────────┘
                             ▼
        fix-log/ (growing memory)   ·   User_import/ (user projects)
```

- **Instructions** (CLAUDE.md + `prompts/`) stay small and stable — they describe *how*
  the agent works.
- **Knowledge** (`wiki/`) is the retrieval target — the authoritative *what is correct*.
- **Memory** (`fix-log/`) grows over time — resolved bugs and reusable techniques.

This mirrors the root architecture's core idea: do **not** pour everything into the
prompt; keep a small instruction file plus selective, grounded retrieval.

---

## Directory map

```
agent-config/
├─ AGENTS.md              # Agent Core: Identity · Workflow · Retrieval instructions
│
├─ prompts/               # Workflow instruction strings, one per stage/role
│  ├─ coding-agent.md     #   design + code  (Blueprint, ontology, turns, command rules)
│  ├─ validator.md        #   verify         (pre-code, parser-critical checklist)
│  └─ reviewer.md         #   review/revise  (final JSON gate + output packaging)
│
├─ wiki/                  # Knowledge Base (retrieval targets) — grounding source
│  ├─ index.md            #   KB routing table — retrieval ALWAYS starts here
│  ├─ protocol.md         #   full command/syntax reference (authoritative)
│  ├─ linter.md           #   schema, allowed keys, parser rules (authoritative)
│  └─ examples/
│     └─ code-bank.md     #   known-good agent archetypes to adapt
│
├─ fix-log/               # Growing memory: dated resolved-bug / change logs
│  ├─ 2026-06-10.md
│  ├─ 2026-06-13-loop-result-indexing.md
│  └─ 2026-06-13-vocab-eval-auth-migration-and-docs.md
│
├─ quiz-agent-aoa/        # Worked example: AoA rubric quiz agent (sandwich architecture)
├─ quiz-agent-python-aoa/ # Worked example: Python-concepts quiz agent (+ its README)
│
└─ User_import/           # User projects the agent inspects / edits
   └─ 어휘평가/ · 어휘평가_NewAuth/   # 36-agent vocabulary-assessment battery (case study)
```

---

## 1. The Agent Core (`AGENTS.md`)

Holds only **Identity**, **Workflow**, and **Retrieval instructions** — deliberately
small. Detailed instruction strings live in `prompts/`; framework knowledge lives in
`wiki/`. Every output must be **grounded** (in retrieved KB content), **logically
coherent** (turn-by-turn, dependency-safe), **syntactically valid** (parser-safe JSON +
correct quoting), and **reproducible**.

Operating rules (paraphrased):

1. Never assume syntax — ground it in `wiki/`.
2. Start retrieval at `wiki/index.md`.
3. Read only relevant files.
4. Respect turn-based structure before editing.
5. Preserve project conventions.
6. Validate after every edit.

## 2. The Workflow Prompts (`prompts/`)

Each file drives one stage of the pipeline and points back at the authoritative `wiki/`
sources:

| Prompt | Stage | Responsibility |
|--------|-------|----------------|
| `coding-agent.md` | design · code | Blueprint-first design (goal, framework, commands, ontology, turn plan), then generate the JSON. |
| `validator.md` | verify | Validate the Blueprint against parser-critical rules **before** coding (AP/JP specified, symbolic-vs-LLM separation, control-flow isolation, one input per visible turn, dependency next-turn rule). |
| `reviewer.md` | review · revise | Re-validate the final JSON (root/allowed keys, `model:null` on symbolic turns, `REPEAT`/`JUMP`/`END` isolation, no same-turn dependency), revise until it passes, package output. |

## 3. The Knowledge Base (`wiki/`)

The retrieval layer — authoritative CAFA truth. **Always start at `index.md`**, then open
the file that answers the question:

| Entry | File | Use when |
|-------|------|----------|
| CAFA Protocol | `protocol.md` | Exact command syntax, quoting, turn triggers, parameter systems (AP/SP/JP), loop-result indexing. |
| Linter & Rules | `linter.md` | Schema / allowed keys, symbolic-vs-LLM requirements, escaping, dependency rules, parser compliance. **Overrides examples.** |
| Agent Code Bank | `examples/code-bank.md` | Finding a working archetype (router, loop, evaluator, scorer, sandwich quiz, adaptive test) to adapt. |

Precedence: `linter.md` and `protocol.md` are authoritative and **override any example**.
Grounding rule: if a CAFA behavior claim cannot be supported by these files, label it an
assumption or omit it.

## 4. Growing Memory (`fix-log/`)

Dated logs of resolved bugs, migrations, and reusable techniques. When a session uncovers
a non-obvious rule or pattern, it is captured here (and, when generalizable, folded back
into `wiki/`). Example: `2026-06-13-loop-result-indexing.md` documents the
`@TR@TN(-1)@[@R_i@]@` loop-result-indexing trick, which was promoted into `protocol.md`
(§8.1), `linter.md`, and `code-bank.md`.

## 5. Worked Examples & User Projects

- `quiz-agent-aoa/`, `quiz-agent-python-aoa/` — reference agents demonstrating the
  **sandwich architecture** (symbolic input → LLM evaluation → hidden control) and
  protocol-safe scoring loops.
- `User_import/` — user projects the agent inspects and edits. The `어휘평가` vocabulary
  battery (below) is the current case study.

---

## Workflow

Driven by `CLAUDE.md`, every request follows the same order. No stage is skipped; if
verify or review fails, revise **Blueprint → ontology → turn architecture → code** and
re-run the stage.

```txt
User Request
     ↓
retrieve   →  wiki/index.md → protocol.md / linter.md / examples/code-bank.md
     ↓
design     →  prompts/coding-agent.md   (produce the Blueprint)
     ↓
verify     →  prompts/validator.md      (check Blueprint before coding)
     ↓
code       →  prompts/coding-agent.md   (write CAFA agent JSON)
     ↓
review     →  prompts/reviewer.md       (re-validate, revise, package)
     ↓
Return Blueprint + CAFA Agent Code
```

This is the same `Search → Generate → Validate → Repair → Revalidate` loop the root
README argues for — retrieval grounded in `wiki/`, correctness enforced by the
validator/reviewer prompts.

---

## Case study — `User_import/어휘평가` (LLM Wiki idea test)

A real 36-agent battery used to exercise the agent across an existing multi-agent set:
**3 bands** (초등·중등·고등) × **4 vocabulary elements** (Collocation, Form_Meaning,
Derivatives, Context) × **3 tiers** (T1 Form Recognition · T2 Meaning Recall · T3 Form
Recall).

- `어휘평가/` — original corpus (untouched backup).
- `어휘평가_NewAuth/` — standardized output: uniform numeric-range student authentication,
  a documentation README (auth + tier architecture), and inline descriptions on every
  parameter and turn.

The work is logged chronologically in
`fix-log/2026-06-13-vocab-eval-auth-migration-and-docs.md` (auth migration → README
updates → tier documentation → full annotation → conformance verification), and the
corpus-specific structure is documented in `User_import/어휘평가_NewAuth/README.md`.

---

## Why layered, not Wiki-only

CAFA is a custom, turn-based DSL with strict syntax, datatypes, execution order, and
dependency rules — closer to a compiler problem than a search problem. A flat Wiki cannot
guarantee correctness on its own, so this directory separates concerns:

| Layer | Responsibility | Prevents |
|-------|----------------|----------|
| `CLAUDE.md` + `prompts/` | How to work (workflow) | Skipped steps, ungrounded generation |
| `wiki/` | Framework truth | Syntax hallucinations, knowledge contamination |
| `prompts/validator.md` + `reviewer.md` | Correctness enforcement | Invalid generated JSON |
| `fix-log/` | Growing memory | Repeating the same mistake twice |

Together they shift the agent from a "search → generate" RAG chatbot toward a
compiler-assisted coding agent for the CAFA Framework.

---

## Source mapping

Where each file in this layer came from when the codebase was restructured (see
`fix-log/2026-06-10.md`):

| File | Derived from |
|------|--------------|
| `AGENTS.md` | `1/00_System_Instruction.md` (persona, workflow, KB index, scope rules) |
| `prompts/coding-agent.md` | `1/00_System_Instruction.md` §3,5–8 (blueprint, ontology, turn, command rules) |
| `prompts/validator.md` | `1/00_System_Instruction.md` §4 + `1/01_…Linter and Rules.md` |
| `prompts/reviewer.md` | `1/00_System_Instruction.md` §9,10,12,13 + references |
| `wiki/index.md` | `1/00_System_Instruction.md` §2.1 (KB index) |
| `wiki/protocol.md` | copy of `1/2_CAFA_Protocol.md` |
| `wiki/linter.md` | copy of `1/01_CAFA Agent Code Linter and Rules.md` |
| `wiki/examples/code-bank.md` | copy of `1/4_CAFA_Agent_Code_Bank.md` |
