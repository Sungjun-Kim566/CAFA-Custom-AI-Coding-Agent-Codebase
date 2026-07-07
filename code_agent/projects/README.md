# Projects — Per-Agent Workspaces

One directory per generated agent: `projects/<agent-slug>/`. The agent creates and
maintains these automatically (see `AGENTS.md` → "Project workspace" and
`prompts/coding-agent.md` §7).

## Layout

| File | Purpose |
|------|---------|
| `blueprint.md` | The verified Blueprint (Design) the code was generated from. |
| `agent.json` | The latest full CAFA agent code (overwritten on each revision). |
| `local-code-bank.md` | The code-bank entries this agent was built from — saved router output plus any KB excerpts consulted during revisions. |
| `code-log.md` | Dated iteration log: what changed, why, verification status. |

## Why

Debugging and revision requests load this workspace (a few thousand tokens) instead
of re-routing `wiki/code-bank.md` — the reference material the agent was built from
is already cached in `local-code-bank.md`, and `code-log.md` carries the revision
history forward across sessions.
