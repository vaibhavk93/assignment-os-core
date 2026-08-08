# AI Justification Review

## Verdict
Earns its place

## Justification Matrix
| Capability | What it does | Necessary? | Deterministic alternative | Recommendation | Confidence |
|---|---|---|---|---|---|
| Theme rail sort (S2/S3) | Orders cards in a rail by one disclosed objective metric ("profitable 5yrs, sorted alphabetically") | N/A — designed as rule-based, not AI | Already the design | Keep. Correctly rejected a ranking/scoring model here specifically because SEBI's broadened "opinion on securities" definition (S3, S7) makes any AI-driven ranking a regulatory liability, not just an engineering one | High |
| Confidence-score harm guardrail (S6) | Flags users whose existing confidence score rises with zero Confidence Journal steps completed | Yes, but reuses an already-shipped score field in a deterministic rule (delta + zero-count check) — no new inference | Already deterministic | Keep as specified | High |
| AI Research Copilot (referenced, S5) | Existing query-answering AI surface, explicitly *not* extended into Explore | Correctly scoped — Explore serves users with no query to type, a different job | N/A, already built, out of scope for this deliverable | Keep the boundary as drawn | High |
| Scorecard's AI-generated 200+-metric engine (referenced, S3/S5) | Existing analysis engine behind the terminal action | Out of scope per `intent.md` ("Design of the Scorecard itself" explicitly excluded) | N/A | Correctly left untouched | High |
| Rail personalization post-signal, "cold-start recommender" (Appendix A) | After ≥1 Scorecard open or an explicit interest tap, rails reorder toward that signal | Marginal, and only in a hypothetical v2 — the draft itself defers it | A single rule: boost the rail matching the sector of the last-opened stock or tapped interest. With 4–5 rails total, this is a bounded categorical lookup, not a recommendation problem | Ship the rule; drop "recommender" framing until a v2 with real usage data shows the heuristic underperforms | Medium |

## Issues

### Medium — Appendix A frames future personalization as a "recommender" it doesn't need
- **Quote:** "Rails personalize only after a signal exists... Avoids building a cold-start recommender on zero data."
- **Why it fails:** The sentence correctly avoids the *cold-start* trap, but still names "recommender" as the target architecture for later. With only 4–5 rails and a single categorical signal (last sector viewed/added), the entire personalization problem is "which one of five buckets does this user prefer" — a lookup, not a model. Calling it a recommender invites building ML infrastructure (training data pipeline, model versioning, drift monitoring) for a decision space smaller than a `switch` statement.
- **What a CTO asks out loud:** "Why does reordering five rails need a model at all?"
- **What to do instead:** Ship a simple weighted-rule reorder (boost the rail matching the sector of the user's last Scorecard open or interest tap) as v1 personalization. Revisit only if usage data shows the heuristic materially underperforms — which, at this scale, it's unlikely to.
- **What that costs:** Nothing extra now; the flag is preventive. Cost of *not* fixing it: a future engineer inherits appendix language that quietly greenlights a training pipeline for a five-way choice.

### Low — Card's read-time/complexity tag mechanism is unspecified
- **Quote:** "A read-time or complexity tag ('~3 min', 'Beginner-friendly')"
- **Why it matters:** the draft doesn't say whether this is editorially authored, a static content-type mapping, or algorithmically classified. It's a minor gap, not a flaw — but if the next revision reaches for an LLM classifier to tag five bounded difficulty tiers, that's overkill for a static taxonomy.
- **What to do instead:** State explicitly it's a config-driven tag per content template, not inferred per-card.
- **What that costs:** One clarifying line, zero engineering cost either way.

## What is genuinely justified
The strongest AI decision in this deck is a negative one: S3 and S7 correctly withhold the composite Health Score, valuation calls, and peer ranking from the pre-click card specifically because SEBI's Research Analyst Regulations (amended through Dec 2024) treat "opinion on securities" broadly enough that a ranked or scored surface could constitute a recommendation StockFox isn't licensed to make. That's a case-builder choosing rules (disclosed, objective, single-criterion sort) over a scoring model precisely where a model would be legally dangerous, not just technically avoidable — the sharpest possible answer to "should AI do this." S5's decision not to rebuild AI Research Copilot inside Explore, and to leave the Scorecard's existing AI engine untouched, both show correct scope discipline for an 8-page hybrid case study that explicitly rules AI-architecture depth out of scope (`intent.md` red herrings table). Nothing in this draft asks AI to do CRUD, routing, or anything deterministic dressed up as intelligence.

## Scores (0-10, one clause each)
AI necessity: 9 — no unnecessary AI proposed; existing AI correctly referenced, not rebuilt
Architecture balance: 9 — rules over models everywhere it matters, especially under the SEBI ceiling
Implementation feasibility: 9 — everything shippable is deterministic; the one soft spot is a future appendix note
Operational simplicity: 8 — nothing new to operate; watch the recommender framing before it becomes a ticket
Executive confidence: 9 — a CTO reads this as an AI company correctly choosing not to use AI where it would create legal and UX risk
