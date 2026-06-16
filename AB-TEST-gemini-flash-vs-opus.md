# A/B Test — AoA Quiz Agent: Gemini 3.5 Flash (Antigravity CLI) vs. Opus 4.8 (Claude Code)

Same task ("Create a Quiz Agent using the AoA framework — strict sandwich,
CAFA protocol rules, new directory, record latency"), two agents, judged against
the CAFA knowledge base (`wiki/linter.md`, `wiki/protocol.md`, AoA archetype).

- **A — Gemini 3.5 Flash (Medium)** via Antigravity CLI → `custom-quiz-agent-aoa/`
- **B — Opus 4.8** via Claude Code → `cybersecurity-quiz-agent-aoa/`

---

## 1. Headline result

**The two agent outputs are functionally identical in quality.** Both correctly
retrieved and adapted the canonical AoA archetype; both are byte-identical on the
content-independent logic turns; both pass the full automated linter with zero
failures. The meaningful difference is **not** the artifact — it is the **build
process: stability and latency**, where A degraded badly and B did not.

| Dimension | A — Gemini Flash | B — Opus | Winner |
|-----------|------------------|----------|--------|
| Linter result | ALL PASS (0 fails) | ALL PASS (0 fails) | tie |
| Sandwich architecture correct | yes | yes | tie |
| Loop-result indexing `@TR@TN(-1)@[@R_i@]@` | yes | yes | tie |
| MAP N+1 rule / scale consistency | yes | yes | tie |
| Symbolic `model:null`, isolated control turns | yes | yes | tie |
| Topic | Web Dev / Programming Basics | Cybersecurity | n/a (both valid) |
| Deliverable completeness | JSON only (+ raw CLI log) | JSON + README + BUILD-LOG | **B** |
| Artifact file naming | generic `quiz-agent.json` | descriptive | **B** |
| **Build latency** | **~15m 19s** to artifact | **69s** | **B (~13×)** |
| Build stability | unstable (see §4) | clean | **B** |

---

## 2. Output-quality comparison (the artifact)

Logic turns that are independent of quiz content were compared byte-for-byte:

| Turn | Role | A vs B |
|------|------|--------|
| T1 | `REPEAT` controller | **IDENTICAL** |
| T3 system | strict grader prompt | **IDENTICAL** |
| T4 | hidden control / scoring (`SET`+`MAP`+`EVAL`) | **IDENTICAL** |

Both files are 5 turns, same Symbolic-Input → LLM-Evaluation → Hidden-Control
sandwich, same `gpt-4.1-nano` / `temp 0.1` / `max-tokens 100` /
`output-values` config, same `TOTAL_QUESTIONS=3 / MAX_SCORE=9`, same MAP
`value_list(4) → return_list(5)` with the default last (N+1 rule satisfied),
`QUESTIONS (SELF)` + `RUBRICS (LINK(QUESTIONS))`.

**Conclusion:** on the deliverable itself there is no quality gap. Flash was fully
capable of producing a protocol-faithful AoA agent — both agents essentially
reproduced the same KB archetype. This is a clone-quality tie.

Where B edges ahead is **packaging**, not logic: B shipped a README and a
BUILD-LOG (with the requested latency), and used a descriptive filename; A shipped
only the JSON plus the raw CLI server log.

---

## 3. Latency comparison

| | A — Gemini Flash | B — Opus |
|--|------------------|----------|
| Session start | 16:06:59 | 17:24:25 |
| Artifact written | 16:22:18 (`quiz-agent.json`) | 17:25:34 |
| **Effective build latency** | **~919 s (~15m 19s)** | **69 s** |

A's ~15 min is wall-clock from session start to the JSON being written; it
includes long-context retrieval/streaming overhead and tool-confirmation round
trips (first approved `RunCommand` at 16:22:24). B's 69 s is start-of-generation
to verified+linted output. **B is roughly 13× faster to a deliverable of equal
quality.**

---

## 4. Stability — what the Gemini CLI log actually shows

The user's hypothesis was "the context was too long, so it constantly caused
socket timeouts and network instability." The `custom-quiz-agent-aoa/build_log.txt`
(Antigravity language-server log, 273 lines) tells a more specific — and somewhat
different — story. The instability is real, but **context length is not the
primary cause**:

1. **Auth not established (53 events).** From startup:
   `You are not logged into Antigravity` → repeated
   `Failed to get OAuth token` / `failed to set auth token`. The CLI never had a
   valid token source, so every cache refresh (`availableModels`, `userInfo`,
   `loadCodeAssist`) and experiment poll failed in a tight loop.

2. **Client-side socket/port exhaustion (3 events), not payload timeouts.** The
   actual network errors are:
   `read tcp 172.30.1.95:5xxxx->216.239.x.x:443: read: can't assign requested
   address`. `EADDRNOTAVAIL ("can't assign requested address")` is **local
   ephemeral-port / source-address exhaustion** — the client ran out of outbound
   sockets because background pollers (`ListExperiments`, `play.googleapis.com/log`,
   `quotaRefreshLoop`) kept opening short-lived connections that weren't being
   reused. That is **connection churn**, not "the request body was too big to send."

3. **Hard stop = quota, not timeout.** The session ended on
   `RESOURCE_EXHAUSTED (code 429): Individual quota reached … Resets in 96h25m27s`.
   The 429 — not a socket timeout — is what actually halted further work.

**Faithful finding:** payload size likely *amplified* the pain (more streaming, more
retries, more poll traffic), but the log evidence points at **(a) broken auth,
(b) ephemeral-port exhaustion from connection churn, and (c) a 429 quota cap** —
all transport/account issues, independent of the (small) quiz-agent task itself.
This is why A's *output* is still perfect despite a turbulent session.

---

## 5. Recommended fixes for the Gemini/Antigravity path

These target the real causes above (the earlier "chunk the data / use concurrency"
idea would not help port exhaustion or a 429, and could make churn worse):

1. **Fix auth first.** Log in so a valid OAuth token source exists
   (`antigravity` login). The 53 token failures and most cache/poll errors vanish
   once authenticated — this alone likely removes most of the "instability."
2. **Address quota.** The session hit a per-individual 429 with a 96h reset.
   Enable overages / use a higher-quota account, or pace requests; no transport
   tuning fixes a quota cap.
3. **Reduce connection churn (the EADDRNOTAVAIL cause).** Reuse a single
   keep-alive HTTP/2 connection instead of opening many short-lived ones; back off
   the background pollers. On macOS, ephemeral-port exhaustion is also mitigated by
   widening the local port range / lowering `MSL` (`TIME_WAIT` reuse), but the
   primary fix is connection reuse + backoff.
4. **Trim context to cut amplification.** Start fresh sessions per task and avoid
   re-sending the entire KB each turn (retrieve only the needed wiki entry). This
   reduces streaming volume and poll pressure even though it is not the root cause.

---

## 6. Verdict

- **Artifact quality:** tie — both are KB-faithful, lint-clean AoA agents.
- **Engineering deliverable (docs, latency record, naming):** B (Opus).
- **Build latency & stability:** B (Opus), ~13× faster and clean vs. an auth-broken,
  port-exhausted, quota-capped Gemini session.

For this task, model capability was not the differentiator — **the Antigravity CLI
transport/account environment was**. A correctly-authenticated, quota-healthy Flash
run would be expected to produce an equivalent agent much faster than its ~15 min
here.
