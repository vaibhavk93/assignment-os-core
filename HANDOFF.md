# Assignment OS — Handoff Log

_Last updated: 2026-08-08 — Roadmap Phases 1–3 shipped_

Claude has no memory across sessions. Read this + `CLAUDE.md` first — do not re-derive context that's already here.

**Active work is system-building, not an assignment.** See `Documents/ROADMAP.md` for the plan, the settled decisions, and the cited evidence base — **that file exists so you never re-run the research. Read it before investigating anything about the reasoning library or learning loop.**

---

## Active Assignment

| Field | Value |
|---|---|
| Company | StockFox |
| Assignment folder | `Companies/StockFox/2026-08-07_StockDiscoveryNewInvestor/` |
| Assignment type | Case study / presentation hybrid — stock discovery for a first-time investor |
| Pipeline status | **COMPLETE** — Checker PASS loop 0, all Tier 1 gates, Tier 2 0.90–1.0 |
| Outputs delivered | `presentation.html` (12 slides), `.pdf` (12pp, 13.33×7.5in), `.pptx` (11 slides) |
| Outcome | **pending** — run `/debrief` once the real result is known |

Prior: `Companies/Ixigo/2026-07-05_InternationalBookingExperience/` — complete, `outcome` field **absent entirely**.

---

## Pending Actions (User Must Do)

1. **Run `/debrief` on Ixigo and StockFox.** This is the top priority and blocks real progress. `CLAUDE.md` states the optimization target is interview success, measured only by `/debrief` — it has never run, so every quality mechanism in the system is unvalidated. It also blocks Roadmap Phase 4.
2. Decide whether to trim `CLAUDE.md` (1832 tok, re-injected into all 8 agents ≈ 14.7k/run). Left alone deliberately — it's also what keeps agents correct.
3. Enable GitHub Pages on `github.com/vaibhavk93/CSAixigo` (carried over, Ixigo).

---

## Known Issues / Gotchas

- **Roadmap Phases 1–3 are done** (`4e13b70`, `b2b8218`, `7c38ef9`). Phase 4 is blocked on `/debrief`; Phase 5 is deliberately deferred until the library is large. **Every implementable phase is now shipped** — the next real work is running an assignment, not building.
- **The 8-stage pipeline has never run end to end.** `decision-builder` has never executed against a real assignment; StockFox completed on the 7-stage version. The gates around it are verified (live denial proven both ways, selftest asserts the new freshness link in both directions), but the stage's *output quality* is unobserved. The next assignment is its first real test.
- **Three agents shipped write-blind and were fixed mid-run** (`devils-advocate`, `strict-checker`, `executive-reviewer` had read-only `tools:` while their contracts said they write files). An audit now covers all agents; re-run it after adding any agent: check each `**Writes:**` line has a matching `Write` in frontmatter.
- **`effort:` on all 9 agents is unverified.** Set on research indicating Claude Code honours the frontmatter field; never confirmed at runtime. If it's inert, those lines do nothing.
- **The Evidence Contract gate has never executed.** Built and unit-tested, but StockFox was already `complete`. Untested in a real flow.
- **Fan-out caps are prose-only.** `research-executor` (×4) and `panel-reviewer` (×5) aren't in `gate_check.py`'s `GATED` tuple. Deliberately not enforced: a `PreToolUse` hook has no completion signal, so counting concurrency needs stale-entry expiry, and a false denial mid-run is worse than the retryable session error it would prevent.
- **Gates check freshness, not just verdicts.** Re-running a stage strands downstream artifacts; gates compare mtimes along `intent.md → research_plan.md → research_<qid>.md → draft.json → check_report.json`. `mtime` detects "was written", not "changed meaningfully" — a cosmetic edit forces a re-run. Use `"gate_override": "<reason>"` in `state.json` for that, and clear it after.
- **Rewind mid-pipeline:** `/assignment-continue <stage>`. It doesn't delete stale artifacts; the gates refuse to trust them.
- **Two scripts have selftests** — `python3 Global/scripts/gate_check.py --selftest` and `pptx_builder.py --selftest`. Run both after touching either.
- **PPTX/PDF need a shell.** `formatter` has Read/Write only, so it reports rendered properties as `unverified` by contract. The orchestrator renders: `pptx_builder.py` for PPTX, headless Chrome `--print-to-pdf` for PDF.
- **`Global/memory/` never existed** despite being in `CLAUDE.md`'s folder structure. Superseded by `Global/library/`.
