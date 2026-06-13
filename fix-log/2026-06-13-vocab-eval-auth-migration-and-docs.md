# Fix Log — 어휘평가 Auth Migration, Documentation & Annotation

- **Date:** 2026-06-13
- **Context:** CAFA custom AI coding agent — **LLM Wiki idea test** run. The 36-agent
  vocabulary-assessment battery (`User_import/어휘평가`) was used as the working corpus
  to exercise retrieval-grounded edits across a real multi-agent set.
- **Affected corpus:** `User_import/어휘평가` → new `User_import/어휘평가_NewAuth`
  (36 agent JSONs: 초등·중등·고등 × Collocation·Form_Meaning·Derivatives·Context × T1/T2/T3),
  plus `User_import/어휘평가_NewAuth/README.md`.
- **Reference agent (destination format):** `고등/Context/High_Context_T1.json`.
- **Status:** Completed and verified.

---

## Step 1 — Authentication migration (legacy list-match → numeric-range)

**Goal:** standardize every agent's student-authentication onto the scheme used by
`High_Context_T1.json`.

**Before (35 of 36 agents):** single-value string match.
- Param `Identification` = `"S-113"` (placeholder).
- Input label in `S-OOO` format.
- `@JUMP(@MAP("@TEXT(ID)@", "@Identification@", "4|@TN(-1)@", EXACT)@)@`

**After (reference scheme):** numeric range check.
- Dropped `Identification`; added `ID_LOWER` (`26001`), `ID_UPPER` (`26160`),
  `Student_auth_list` (two `@COMPARE/@EVAL` boundary tests → `true|true`); `ID.response` → `26001`.
- Input label in `26OOO` format.
- `@JUMP(@MAP("@EQUAL("@Student_auth_list@", "true|true")@", "true", "4|@TN(-1)@", EXACT)@)@`

**How:** mechanical transform applied to all 36 files; output written to a new parallel
tree `어휘평가_NewAuth/` so originals stayed intact. 35 files transformed; the reference
was copied as-is. Each file had exactly one `@TEXT(ID,…)@` turn and one
`@JUMP/@Identification@` turn — confirmed before editing.

**Verification:** all 36 parse; `Identification` removed; three new params present;
TEXT/JUMP updated; no stale `@Identification@` refs; every question bank, scoring prompt,
and unrelated param byte-identical to its original.

**Note flagged to user:** the range `26001–26160` came from the high-school reference;
originals carried no per-grade range data, so the same range was replicated everywhere.
Per-class ranges only require editing `ID_LOWER`/`ID_UPPER` + the `26000`/`26161` bounds
inside `Student_auth_list`.

## Step 2 — README updated for the new auth

In `어휘평가_NewAuth/README.md`:
- Converted the embedded example agent schema to the new auth (params + TEXT + JUMP),
  mirroring the agent change; embedded JSON re-validated.
- Added a **`# 학생 인증 (Student Authentication)`** section: mechanism, parameter table,
  turn-flow table, changelog note, and per-class adjustment guidance.
- Added a checklist entry recording the migration.

## Step 3 — Tier structure documentation (T1 / T2 / T3)

Analyzed all three tiers across the four categories and added a
**`# Tier별 구조`** section:
- Tier-comparison table — **T1** Form Recognition (MC: `@RADIO` + `@MAP…EXACT`, ~13 turns),
  **T2** Meaning Recall (SA: `@TEXT` + **LLM-judge** returning `1/0` consumed via
  `@TR@TN(-1)@[@R_i@]@`, per-POS ~34 turns), **T3** Form Recall (SA: `@TEXT` + `@MAP…EXACT`,
  ~13 turns). Documented the **Derivatives exception** (T1/T3 use `@TEXT` + `RWORD`).
- **Common parameters** (all tiers) and **tier/category-unique parameters** tables.
- **Turn-architecture** tables (common skeleton, T1/T3 compact flow, T2 6-turn-per-POS
  block) tracing each LLM turn's output and where it is consumed.

## Step 4 — Removed redundant `## Parameters` section

The legacy conceptual table was superseded by Step 3 and partly stale (`BYE`,
`FB_Neg/Pos` never implemented; POS listed as 3 not 4). Removed it, but:
- kept the concrete `GSID` value in the new common-parameters table, and
- preserved its one useful idea as a note (PRM = dependent vars LINK'd to ANS;
  ANS = independent SHUFFLE'd pools, extracted in lockstep via `*_IDX`).

## Step 5 — Per-turn & per-parameter annotation (all 36 agents)

**Goal:** readability and maintainability — describe every parameter and every turn.

- **1,200** empty parameter `desc` fields filled via pattern rules
  (POS-prefix × type-suffix, `P_*` question objects, specials `GSID`/`FLIST`/`LLM_FBK`/
  Collocation headword pools, etc.). Existing non-empty descriptions preserved.
- **601** leading turn-comment lines standardized with role tags
  (`[인증]`, `[셋업]`, `[안내]`, `[루프]`, `[문제]`, `[채점]`(+matching mode),
  `[저장]`, `[집계]`, `[초기화]`, `[리포트]`, `[피드백]`), POS-aware where applicable.
- **115** turns whose `user` is genuine LLM input (not a comment) were intentionally left
  untouched. **3** edge turns (a `@GSTABLE` loader, two comment-only score-adjust turns)
  were patched individually.

**Safety proof:** re-derived the expected pre-annotation state from the originals and
confirmed **only** `desc` fields and first comment lines changed — every operator,
displayed-content line, `org`, `cond`, and prompt field is byte-identical. All 36 parse.

**Incidental observation (pre-existing, not introduced):** in
`중등/Derivatives/Middle_Derivatives_T3.json` (T14) and
`초등/Derivatives/Primary_Derivatives_T3.json` (T12), the "Adjust Final Score / Cumulative"
turns contain a comment but **no operator body** — their final score adjustment may be
unwired. Left as-is; surfaced for review.

## Step 6 — Auth conformance verification

Compared the executable auth logic (TEXT + JUMP operators, ignoring comments) and the four
auth params of every agent against the reference:
- **`어휘평가_NewAuth/`** — all 36 match the reference auth process.
- **`어휘평가/`** (originals) — 35 of 36 still use legacy auth (only the reference itself
  matches), as intended; the original tree is the untouched pre-change backup.

---

## Outcome

- `어휘평가_NewAuth/` is a fully standardized, self-documented copy: uniform numeric-range
  authentication, README covering auth + tier architecture, and inline descriptions on
  every parameter and turn.
- Originals untouched in `어휘평가/`.

## Rule of thumb

When standardizing a behavior across a multi-agent corpus: write to a parallel tree, match
by **operator content** (not comment text, which is cosmetic), change one concern at a time,
and prove the diff is limited to the intended fields by re-deriving the expected state and
comparing byte-for-byte.
