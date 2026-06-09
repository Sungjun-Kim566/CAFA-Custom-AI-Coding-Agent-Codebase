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
│   └── wiki/ docs loaded only when needed; RAG Pipeline implemented
│
├── MCP Schema
│   ├── search_wiki(): Retrieves information from wiki for inference
│   ├── inspect_turn(): inspect each turn
│   ├── read_file(): read the uploaded user file
│   ├── edit_file(): edit the uploaded user file
│   ├── run_custom_code(): compilability (sanity check) (@RUN@)
│   ├── Execute: MCP Tool management Class
│       ├── select_exe_tool()
│
└── Project files
    └── read selectively, not all at once
```

### `CLAUDE.md`:

```md
# CAFA Coding Agent Rules

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
User request (prompt)
   ↓
Claude Code
   ↓
CLAUDE.md tells Claude what tools to use
   ↓
MCP search_wiki retrieves only relevant chunks
   ↓
MCP read_file retrieves only target uploaded files
   ↓
Claude edits specific files
   ↓
MCP run_code validates output
```

Do **not** upload everything directly into Claude’s context. Use:

```txt
small instruction file + retrieval tools + selective file access

This is similar to using Claude Desktop
that utilizes pre-configured MCP Tools with additional context
provided with PDF or any other forms of texts and images.
```

### Basic Setup
Frontend
  - Chat Host (CLI)
    - setup differs depending on the user OS (Windows, Mac, Linux; Default: Mac/Linux)
  - file upload (Obsidian; personal vault; offline)
  - code viewer (CLI)
  - turn-cell editor (CAFA; `run_custom_code()` or `@RUN@` on CAFA)

Backend
  - workspace file store (Obsidian)
  - file parser/indexer (Obsidian; `index.md`)
  - embedding/vector index (potentially LanceDB; still deciding)
  - MCP client (Plugin Setup; differs depending on user OS)
  - agent orchestrator (`CLAUDE.md` Agent Configuration)

MCP Server
  - custom language tools (TBD)
  - validation tools (Edge Case Checker)
  - execution tools
      - Google Sheet MCP: read, edit, manage accessibility, etc. automatically by prompts
      - HTTP requests MCP: fetch, send, or update data in CAFA LOG or specific CAFA data address

LLM Wiki
  - language rules (Function documentations; CAFA Coding Conventions)
      - default delimiter: `|`
      - function wrapper special character: `@`
      - function execution order within the same turn
      - when to make arguments string to compile
         - E.g.
         - argument datatype determines or 
         - output datatype determines whether make arguments string or not
  - API wrappers
      - Function/Method Lists from the Protocol Slides
      - Function, arguments, descriptions
         - input/output type
         - Method execution flow
  - examples (Code examples with turn-based approach)
      - examples of each function basic usage
      - several examples of each function to integrate with other functions mostly used with
  - anti-patterns (Case-sensitive, must-be-string arguments, etc.)
      - examples of wrong function/method format
      - wrong Agent Parameter/JSON query (in CAFA) examples and their outputs
      - default CAFA Function/Method output datatype: String
         - other output datatype could cause an error to process next or other turns

## CAFA Agent Code Examples/Explanations

## CAFA Function Documentation

## Vibe Coding vs. CAFA Foundry