# CAFA-Custom-AI-Coding-Agent-Codebase
Custom AI Coding Agent specialized for CAFA Framework.

LLM Wiki by Andrej Kaparthy Implemented to define the Agent.

## Design

Structure:

```txt
Claude Code context
│
├── Tiny always-loaded instruction file
│   └── CLAUDE.md
│
├── Searchable knowledge base
│   └── wiki/ docs loaded only when needed
│
├── MCP tools
│   ├── search_wiki()
│   ├── inspect_turn()
│   ├── read_file()
│   ├── edit_file()
│   └── run_custom_code()
│
└── Project files
    └── read selectively, not all at once
```

`CLAUDE.md`:

```md
# Custom Language Agent Rules

1. Never assume syntax.
2. Search the wiki before writing code.
3. Read only relevant files.
4. Use `inspect_turns` before editing turn-based code.
5. Preserve project conventions.
6. Run validation after edits.
```

Then the larger files stay outside the prompt:

```txt
wiki/
docs/
examples/
uploaded-projects/
```

Claude should access them through MCP/RAG only when needed.

MCP/RAG Architecture:

```txt
User request
   ↓
Claude Code
   ↓
CLAUDE.md tells Claude what tools to use
   ↓
MCP search_wiki retrieves only relevant chunks
   ↓
MCP read_file retrieves only target files
   ↓
Claude edits specific files
   ↓
MCP run_code validates output
```

Do **not** upload everything directly into Claude’s context. Use:

```txt
small instruction file + retrieval tools + selective file access
```

### Basic Setup
Frontend
  - chat (CLI)
    - setup differs depending on the user OS (Windows, Mac, Linux)
  - file upload (Obsidian; personal vault)
  - code viewer (CLI)
  - turn-cell editor (CAFA)

Backend
  - workspace file store (Obsidian)
  - file parser/indexer (Obsidian; `index.md`)
  - embedding/vector index (TBD)
  - MCP client (Plugin Setup)
  - agent orchestrator (`CLAUDE.md` Agent Configuration)

MCP Server
  - custom language tools (TBD)
  - validation tools (Edge Case Checker)
  - execution tools (Google Sheet MCP, Gmail MCP, etc.)
  - documentation/wiki tools (LLM Wiki; follow `CLAUDE.md` config)

LLM Wiki
  - language rules (Function documentations)
  - API wrappers
  - examples (Code examples with turn-based approach)
  - anti-patterns (Case-sensitive, must-be-string arguments, etc.)

## CAFA Agent Code Examples/Explanations

## CAFA Function Documentation

## Vibe Coding vs. CAFA Foundry