# Assignment OS — Handoff Log

_Last updated: 2026-08-08 — first measured outcome, Phases 1–3 shipped, all stages now exercised_

Claude has no memory across sessions. Read this + `CLAUDE.md` first — do not re-derive context that's already here.

**Active work is system-building, not an assignment.** See `Documents/ROADMAP.md` for the plan, the settled decisions, and the cited evidence base — **that file exists so you never re-run the research. Read it before investigating anything about the reasoning library or learning loop.**

---

## Assignments and outcomes

| Company | Folder | Status | Outcome |
|---|---|---|---|
| StockFox | `Companies/StockFox/2026-08-07_StockDiscoveryNewInvestor/` | complete | **pending** — submitted 2026-08-08, no reply. Re-run `/debrief` when it lands |
| Ixigo | `Companies/Ixigo/2026-07-05_InternationalBookingExperience/` | complete | **rejected at screening** — no interview, no feedback |

**The system is 0-for-1 on measured outcomes.** Ixigo passed every internal gate (Checker PASS loop 1) and was carried as a success for a month while having failed the first real screen. Nothing in this repo has yet been shown to produce an interview. Hold that when weighing any internal quality signal.

StockFox's `MEMORY.md` records the 7 predicted interviewer questions and the hiring-signal read *before* the result is known, so the eventual `/debrief` compares evidence rather than recollection.

---

## Pending Actions (User Must Do)

1. **Submit more assignments.** The bottleneck is sample size, not system quality. One rejection with no feedback supports no conclusion, and Phase 4 is starved without more outcomes.
2. **Re-run `/debrief StockFox`** when a reply arrives. That run feeds the library and is the controlled comparison against Ixigo (see the hypothesis table in StockFox's `MEMORY.md` — deck length is the only structural variable that differs).
3. Decide whether to trim `CLAUDE.md` (re-injected into every agent, ≈14.7k/run). Left alone deliberately — it's also what keeps agents correct.
4. Enable GitHub Pages on `github.com/vaibhavk93/CSAixigo` (carried over, Ixigo).

---

## What shipped this session

- **Roadmap Phases 1–3** (`4e13b70`, `b2b8218`, `7c38ef9`) — `decision-builder` split out of `case-builder`; hypothesis-first research + Cynefin routing; library retrieval now *recorded* (`## Methods Used`, including honest "changed the answer: no" entries, which is what lets an entry earn demotion).
- **`ai-justification`** (`158599c`) — conditional stage asking whether AI in the *proposed solution* earns its place. Distinct from the `ai_smell` persona, which asks whether the *prose* reads machine-written. Fires only when `draft.json` contains AI/ML terms.
- **Both `/debrief` runs** (`189815e`, `c70e041`) — the learnings log in `hiring-signal-patterns` holds its **first two entries**.
- **Voice enforcement gap found and closed** (`7d505b2`, `f3dd21e`) — see below.

## Findings worth not re-deriving

- **A Checker PASS is not evidence of conversion.** First entry in the learnings log, from Ixigo. The gate measures rubric compliance; that proxy is looser than it looked.
- **The voice rules existed and were never enforced.** The shipped StockFox deck violates `Global/candidate/VOICE.md:35` twice ("Zero-candidate isn't one stall. It's three."; "Not a formatting choice—it's regulatory") and the Checker passed it, because the Tier 1 voice gate only grepped consultant vocabulary and never opened `VOICE.md`. Now fixed — the gate points at that file directly rather than duplicating a list that drifts.
- **Two AI tells survive every word-level check**, both found in the shipped deck: identical grammatical shape across ≥3 sibling items (four tradeoff rows of `Cost/Rejected/Reason`), and selective sourcing (the safe numbers attributed, the dramatic ones bare). Both are now Tier 1 gates and rules in `voice-and-brevity`.
- **Prep before a shortlist is waste.** Ixigo's 11-question `interview_qa.md` was built for a discussion that never happened. That is why `interview-prep` is opt-in and post-shortlist.
- **A reviewer auditing citations must be given the research files.** The `ai_smell` run's *highest-severity* finding — that citations traced to nothing — was an artifact of the read list it was handed. All of them traced. Check a reviewer's inputs before acting on its strongest claim.

---

## Known Issues / Gotchas

- **Phase 4 is now mechanically unblocked but starved.** `/debrief` has run; one real outcome exists. A rejection with zero feedback gives almost nothing to promote into the library, so `/retro` would be proposing candidates from near-noise. Wait for StockFox.
- **`decision-builder` and `ai-justification` are exercised but not battle-tested.** Both ran once, against StockFox. `decision-builder` was a *replay* into a sandbox — see `Documents/evidence/` for the result and its three confounds. Neither has run in a live assignment.
- **The 8-stage pipeline has never run end to end in one go.** StockFox completed on the 7-stage version.
- **`effort:` on all agents is unverified.** Set on research indicating Claude Code honours the frontmatter field; never confirmed at runtime. If inert, those lines do nothing.
- **The Evidence Contract gate has never executed.** Built and unit-tested; both assignments predate it.
- **Fan-out caps are prose-only.** `research-executor` (×4) and `panel-reviewer` (×5) aren't in `gate_check.py`'s `GATED` tuple. Deliberate: a `PreToolUse` hook has no completion signal, so counting concurrency needs stale-entry expiry, and a false denial mid-run is worse than the retryable session error it prevents.
- **Gates check freshness, not just verdicts.** Chain is `intent.md → research_plan.md → research_<qid>.md → decision.md → draft.json → check_report.json`. `mtime` detects "was written", not "changed meaningfully" — a cosmetic edit forces a re-run. That fired for real during the replay (a 22:08 edit to `research_plan.md` stranded three answers written at 18:26). Use `"gate_override": "<reason>"` and clear it after.
- **Never run a replay inside `Companies/`.** A sandbox with `status: active` hijacks `gate_check.py`'s active-assignment picker for every later run. Delete it, or keep evidence in `Documents/evidence/`.
- **Adding an agent? Re-run the write audit.** Three agents once shipped with read-only `tools:` while their contracts said they write files. Check every `**Writes:**` line has a matching `Write` in frontmatter — and keep that line free of negations ("never edits `draft.json`") or the audit reads them as claims.
- **Two scripts have selftests** — `python3 Global/scripts/gate_check.py --selftest` and `pptx_builder.py --selftest`. Run both after touching either.
- **PPTX/PDF need a shell.** `formatter` has Read/Write only, so it reports rendered properties as `unverified` by contract. The orchestrator renders: `pptx_builder.py` for PPTX, headless Chrome `--print-to-pdf` for PDF.
- **`Global/memory/` never existed** despite being in `CLAUDE.md`'s folder structure. Superseded by `Global/library/`.
