# CAFA-Custom-AI-Coding-Agent-Codebase
Custom AI Coding Agent specialized for CAFA Framework.

LLM Wiki by Andrej Kaparthy Implemented to define the Agent.

Architecture needs to handle two distinct types of data: static technical constraints (CAFA functions(Javascript Wrappers) and framework rules/conventions) and dynamic evolutionary context (user preferences and growing knowledge base).
Combining PageIndex with an LLM Wiki layer creates the ideal architecture for this exact use case. PageIndex acts as the immutable "source of truth" for your language specs, while the LLM Wiki serves as the agent's personalized, growing memory.
## Architecture Setup: The Two-Layer Memory
```
┌────────────────────────────────────────────────────────┐
│               Claude Code Agent Core                   │
└──────────────────────────┬─────────────────────────────┘
                           │
       ┌───────────────────┴───────────────────┐
       ▼                                       ▼
┌──────────────────────────────┐       ┌──────────────────────────────┐
│     PageIndex Layer          │       │       LLM Wiki Layer         │
│  (Static/Framework Truth)    │       │ (Dynamic/Personalized Memory)│
├──────────────────────────────┤       ├──────────────────────────────┤
│ • JavaScript-base rules      │       │ • Common user edge cases     │
│ • Framework API syntax       │       │ • Project-specific patterns  │
│ • Core coding conventions    │       │ • Evolving style preferences │
└──────────────────────────────┘       └──────────────────────────────┘
```
## 1. The PageIndex Layer (Framework Truth)
PageIndex to index CAFA framework documentation, core syntax definitions, and official coding style and convention guides.

* When writing code in a custom language(or CAFA functions with turn-based coding conventions, similar to coding on the file format `.ipynb`), LLMs must never hallucinate syntax. PageIndex forces Claude to navigate a strict, hierarchical index of your framework before generating a single line of code, ensuring 100% adherence to CAFA custom JavaScript variant.

## 2. The LLM Wiki Layer (Personalized Knowledge Base)
Create a dedicated local directory of structured markdown files (e.g., .mcp/wiki/) that the agent reads and writes to autonomously.

* As the user build apps, the user will discover unique architectural patterns, custom boilerplate preferences, and frequent edge cases. The agent will document these insights into the Wiki on the fly, preventing them from having to fix the same mistake twice.

------------------------------
## Step-by-Step Implementation Guide
## Step 1: Expose PageIndex via Model Context Protocol (MCP)
Claude Code interacts with external data using Anthropic's Model Context Protocol (MCP). Need to wrap your PageIndex setup inside a local MCP server.

   1. Build a PageIndex Tool: Create an MCP server with a tool called `search_framework_docs(query)`.
   2. Execute Tree Search: When Claude calls this tool, have our PageIndex script traverse CAFA documentation tree, pull the exact relevant code blocks, and return them as text context to Claude.

## Step 2: Establish the Auto-Updating LLM Wiki
To make the knowledge base grow dynamically without manually editing files, give Claude Code the ability to manage its own memory directory. (`wiki_index` and `wiki_log`)

   1. Create an MCP Filesystem Tool: Give Claude strict read/write access to a localized `.mcp/wiki/` directory in the project workspace.
   2. Define the Wiki Structure: Seed the directory with a few main files:
   * user_preferences.md (e.g., "Prefers functional programming over classes").
      * `project_patterns.md` (e.g., "How we handle state management in CAFA framework").
      * `resolved_bugs.md` (A log of syntax mistakes the user frequently makes and how to fix them).
   
## Step 3: Configure Claude Code's Core Instructions
To tie these layers together seamlessly, inject explicit instructions into the Claude Code system prompt (typically configured via `.claudecode.json` or our MCP bridge).
Add these rules to its operational loop:

1. When asked to write code, **ALWAYS** check the PageIndex tool first to verify framework syntax and boundaries.
2. Cross-reference the local LLM Wiki directory to check for personalized coding styles or historical project bugs.
3. At the end of a successful debugging or refactoring session, if discover a unique rule, pattern, or constraint about CAFA syntax, autonomously update the relevant markdown file in .mcp/wiki/.

------------------------------
## What this looks like in practice

   1. The Interaction: You tell the agent, "Fix this async bug, it's throwing an unhandled exception."
   2. The Retrieval: Claude uses PageIndex to look up CAFA framework's official async documentation. Simultaneously, it reads `resolved_bugs.md` from your LLM Wiki to see if you've encountered this before.
   3. The Fix: It fixes your code using the official syntax retrieved via PageIndex, while matching your personal structural preferences found in the Wiki.
   4. The Growth: Claude realizes this was a tricky edge case. It opens `.mcp/wiki/resolved_bugs.md` and appends a new bullet point: "When handling events in X framework, always use custom wrap Y instead of async/await."

## Design
```
CAFA Coding Agent

├── CLAUDE.md
│
├── Knowledge Layer
│   │
│   ├── PageIndex
│   │   ├── Functions
│   │   ├── Methods
│   │   ├── Syntax Rules
│   │   ├── Execution Flow
│   │   └── Examples
│   │
│   ├── Wiki
│   │   ├── User Preferences
│   │   ├── Project Patterns
│   │   ├── Bug History
│   │   └── Architecture Decisions
│   │
│   └── Validator
│       ├── Syntax Check
│       ├── Type Check
│       ├── Turn Validation
│       └── Runtime Validation
│
├── MCP Layer
│   ├── Framework Retrieval
│   ├── Wiki Retrieval
│   ├── Project Inspection
│   ├── Validation Tools
│   └── External Services
│
└── User Project
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

## MCP Layer

Model Context Protocol (MCP) is the interface through which the agent accesses PageIndex, Wiki, Validators, project files, and external services.

MCP does not contain framework knowledge itself.

Its responsibility is exposing tools that allow the agent to retrieve, validate, modify, and execute information.

```txt
Agent
  ↓
MCP
  ↓
PageIndex
Wiki
Validator
Project Files
External Services
```

---

### Framework Retrieval Tools

Used to access framework truth stored in PageIndex.

```txt
search_framework_docs(query)
```

Examples:

```txt
search_framework_docs("HTTPREQUEST")
search_framework_docs("Turn Execution Order")
search_framework_docs("String Conversion Rules")
```

---

### Wiki Tools

Used to access dynamic project knowledge.

```txt
search_wiki(query)
update_wiki()
```

Examples:

```txt
search_wiki("authentication")
search_wiki("firebase pattern")
```

---

### Project Inspection Tools

Used to inspect and modify user projects.

```txt
inspect_turns()
read_file()
edit_file()
```

Examples:

```txt
inspect_turns(project.cafa)

read_file(turn_3.cafa)

edit_file(turn_7.cafa)
```

---

### Validation Tools

Used to verify generated code.

```txt
validate_syntax()
validate_types()
validate_turns()
run_custom_code()
```

Examples:

```txt
validate_syntax()

validate_types()

validate_turns()

run_custom_code()
```

---

### External Service Tools

Used for integrations.

Examples:

```txt
Google Sheets MCP
Firebase MCP
HTTP Request MCP
Git MCP
Filesystem MCP
```

Responsibilities:

```txt
Read Data
Write Data
Manage State
External API Access
```

Claude should access them through MCP only when needed.

MCP Architecture:

```txt
User Request
      ↓

Determine Intent
      ↓

Select MCP Tools
      ↓

Execute Retrieval
      ↓

Execute Validation
      ↓

Return Results
```

Do **not** upload everything directly into Claude’s context. Use:

```txt
small instruction file + retrieval tools + selective file access

This is similar to using Claude Desktop
that utilizes pre-configured MCP Tools with additional context
provided with PDF or any other forms of texts and images.
```

### Basic Setup

## Frontend

* Chat Host (CLI)

  * Setup differs depending on user OS
  * Supported:

    * Windows
    * macOS
    * Linux

* File Upload

  * Obsidian Vault
  * Local Project Workspace
  * Offline Knowledge Base

* Code Viewer

  * CAFA Turn Viewer
  * Multi-turn Navigation

* Turn Editor

  * CAFA Turn Cell Editor
  * `@RUN@`
  * `run_custom_code()`

---

## Backend

### Workspace Storage

* Obsidian Vault
* Project Files
* User Knowledge Base

### Knowledge Layer

#### PageIndex

Framework Truth

```txt
framework/

├── syntax/
├── wrappers/
├── functions/
├── execution-order/
├── datatype-rules/
├── examples/
└── anti-patterns/
```

Responsibilities:

* CAFA syntax definitions
* Function documentation
* Method documentation
* API wrapper specifications
* Input/output types
* Execution flow
* Compilation rules
* Official examples
* Anti-pattern catalog

---

#### LLM Wiki

Dynamic Project Memory

```txt
wiki/

├── user_preferences.md
├── project_patterns.md
├── resolved_bugs.md
├── coding_style.md
└── architectural_decisions.md
```

Responsibilities:

* User preferences
* Project architecture patterns
* Historical bug fixes
* Coding style preferences
* Reusable project workflows
* Learned constraints

---

#### Validator

Verification Layer

Responsibilities:

* Syntax validation
* Type validation
* Turn dependency validation
* Runtime validation
* Compilation sanity checks

---

### Agent Orchestrator

Configuration:

```txt
CLAUDE.md
```

Responsibilities:

* Tool selection
* Retrieval orchestration
* Validation orchestration
* Repair loops
* Wiki updates

---

## MCP Layer

### Framework Retrieval

```txt
search_framework_docs()
```

Retrieves:

* Syntax rules
* Wrapper specifications
* Function documentation
* Examples
* Anti-patterns

---

### Wiki Retrieval

```txt
search_wiki()
update_wiki()
```

Retrieves:

* User preferences
* Project patterns
* Historical fixes

---

### Project Inspection

```txt
inspect_turns()
read_file()
edit_file()
```

Used for:

* Turn analysis
* File inspection
* Project modification

---

### Validation Tools

```txt
validate_syntax()
validate_types()
validate_turns()
run_custom_code()
```

Used for:

* Syntax verification
* Datatype verification
* Turn dependency verification
* Runtime verification

---

### External Services

Google Sheets MCP

Responsibilities:

* Read Sheets
* Update Sheets
* Manage Accessibility
* Synchronize Project Data

HTTP Request MCP

Responsibilities:

* Fetch Data
* Send Data
* Update CAFA Logs
* External API Integration

Firebase MCP

Responsibilities:

* User State
* Realtime Data
* Project Persistence

Filesystem MCP

Responsibilities:

* Read Files
* Write Files
* Workspace Management

---

## Agent Workflow

```txt
User Request
      ↓

Search PageIndex
      ↓

Search Wiki
      ↓

Read Project Files
      ↓

Generate Code
      ↓

Validate Syntax
      ↓

Validate Types
      ↓

Validate Turns
      ↓

Runtime Validation
      ↓

Repair if Needed
      ↓

Revalidate
      ↓

Return Result
```


### Why Not Use LLM Wiki Alone?

CAFA has its own functions/methods with strict syntax rules, execution constraints, datatype requirements, and turn-based workflows.

These characteristics expose several limitations of a Wiki-only architecture.

---

## Problem 1: Semantic Retrieval Is Not Framework Truth

LLM Wiki retrieval is fundamentally semantic.

When searching:

```txt
HTTP request function
```

the agent may retrieve:

```txt
@HTTPREQUEST
@HttpRequest@
@HTTPRequest
```

because they are semantically similar.

However, CAFA may only accept:

```txt
@HTTPREQUEST@
```

This is not a semantic problem.

It is a syntax correctness problem.

PageIndex solves this by storing framework information as structured truth rather than semantic memory.

```txt
Wiki:
"What seems related?"

PageIndex:
"What is officially correct?"
```

---

## Problem 2: Framework Documentation and User Knowledge Are Different

A Wiki tends to accumulate both framework rules and project knowledge in the same place.

Over time, this causes knowledge contamination.

Example:

```txt
Framework Rule:
Arguments must be String

Project Pattern:
Authentication handled in Turn 0

User Preference:
Prefer Firebase
```

These represent three completely different categories of information.

Without separation:

```txt
Framework Truth
+
Project Architecture
+
User Preference
```

become mixed together.

PageIndex separates immutable framework truth from evolving project memory.

---

## Problem 3: Retrieval Does Not Guarantee Correct Generation

Even when the correct documentation is retrieved:

```txt
Agent reads:

@HTTPREQUEST@
```

the LLM may still generate:

```txt
@HttpRequest
```

This is a generation failure.

Not a retrieval failure.

Therefore:

```txt
Correct Retrieval
≠
Correct Generation
```

A Validator layer is required to verify generated code before it is returned.

---

## Problem 4: Wiki Growth Causes Knowledge Drift

As the Wiki grows:

```txt
resolved_bugs.md
project_patterns.md
examples.md
custom_components.md
```

the amount of information increases dramatically.

Over time:

```txt
Old information
New information
Conflicting information
```

can coexist.

This introduces knowledge drift.

The agent may retrieve outdated practices instead of official framework behavior.

PageIndex remains immutable and acts as the stable source of truth.

---

## Problem 5: CAFA custom engine Behaves More Like Compilers Than Documentation

General-purpose programming languages are well represented across the internet.

CAFA is not.

For custom languages:

```txt
Syntax
Datatypes
Execution Order
Turn Dependencies
```

must be enforced precisely.

This makes CAFA functions/methods closer to a compiler problem than a search problem.

A successful CAFA coding agent therefore requires:

```txt
Retrieval
+
Verification
```

rather than retrieval alone.

---

# Why PageIndex + Wiki + Validator Works Better

Each layer solves a different failure mode.

| Layer     | Responsibility          | Prevents                           |
| --------- | ----------------------- | ---------------------------------- |
| PageIndex | Framework Truth         | Syntax hallucinations              |
| Wiki      | Dynamic Project Memory  | Repeated mistakes and lost context |
| Validator | Correctness Enforcement | Invalid generated code             |

Together:

```txt
PageIndex
     ↓

Retrieve Official Truth

Wiki
     ↓

Apply Project Knowledge

Validator
     ↓

Verify Correctness
```

This transforms the agent from a simple RAG chatbot into a compiler-assisted coding agent.

---

# Expected Performance Improvements

Compared to a Wiki-only architecture:

| Capability               | Wiki Only | PageIndex + Wiki + Validator |
| ------------------------ | --------- | ---------------------------- |
| Syntax Accuracy          | Medium    | Very High                    |
| Hallucination Resistance | Medium    | Very High                    |
| Long-Term Consistency    | Medium    | High                         |
| Handling Custom DSLs     | Medium    | Very High                    |
| Turn-Based Logic         | Medium    | High                         |
| Auto-Learning            | High      | High                         |
| Code Reliability         | Medium    | Very High                    |

For CAFA specifically, the largest improvement comes from reducing invalid code generation.

The architecture shifts the agent from:

```txt
Search → Generate
```

to:

```txt
Search → Generate → Validate → Repair → Revalidate
```

which is the same pattern used by modern compiler-assisted coding agents and significantly improves reliability for CAFA Framework.



## CAFA Agent Code Examples/Explanations

## CAFA Function Documentation

## Vibe Coding vs. CAFA Foundry

