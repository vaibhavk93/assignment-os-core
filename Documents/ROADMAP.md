# Roadmap — Reasoning Library & Learning Loop

_Approved 2026-08-08. Phase 0 complete._

**Read this before re-researching anything.** The evidence base at the bottom cost ~500k tokens to gather and is preserved with citations. Do not re-run it.

---

## The reframe this roadmap rests on

**Learning ≠ telemetry.** Run logs, cost per stage, ROI per question, checker scores — all useful, all belong in the *assignment folder* as an operational record. They are not learning.

**The unit of learning is a transferable reasoning move.** StockFox didn't teach us "Q4 cost 20 searches." It taught us *"when a regulatory ceiling forbids recommendation, engagement must attach to exploration, never to the commit action"* — which applies to any regulated product, forever.

**Index on the finite axis, parameterise with the infinite one.**

| Finite — index on this | Infinite — pass as input |
|---|---|
| Problem archetypes, reasoning moves, constraint types | Which company, which market, which constraints |

Case-Based Reasoning solved this in 1994: the **index vocabulary** is the finite axis, case content the infinite one.

---

## Phase status

| Phase | What | Status |
|---|---|---|
| **0** | Seed `Global/library/` with canon; rebuild `pm-frameworks` as a router | ✅ **done** (`65d96de`) |
| **1** | New stage `decision-builder`; shrink `case-builder` to argue-only | ⬜ next |
| **2** | Scope: day-1 hypothesis + Cynefin routing (planner); elimination gate (checker); attack-the-elimination (panel) | ⬜ |
| **3** | Retrieval — library surfaced at intake / planning / decision | ⬜ |
| **4** | `/retro` proposes candidates; human promotes | ⬜ **blocked on `/debrief`** |
| **5** | Anti-rot — cap, version, demote, expire, footprint-prune | ⬜ defer until library is large |

---

## Why `decision-builder` is a new stage, not scope

Two independent analyses converged on the same seam — that's the justification, not thoroughness.

**1. First-principles re-derivation of the pipeline.** The irreducible operations are Frame → Acquire → **Decide** → Argue → Attack → Judge → Deliver → **Learn**. Current stages cover all but Decide (blended into `case-builder`) and Learn (absent).

**2. Practitioner-persona sweep.** Four of five distinctive moves land in that same gap:

| Persona | Move | Present today |
|---|---|---|
| Founder | Cheapest test that kills it this week | Falsifiers exist; **tests don't** |
| Builder | The long pole / what doesn't exist yet | Missing |
| CEO | "And then what?" — competitive response, precedent, opportunity cost | Missing |
| Consultant | Day-1 hypothesis, then try to break it | Research is a survey, not a test |
| PM | Guardrail metric | ✅ present |

**Why it can't live inside `case-builder`:** the system already established the principle — `panel-reviewer` runs fresh-context *"with no memory of how the draft was built"* because an agent can't neutrally attack what it built. Same logic one step earlier: an agent that knows which recommendation it's about to write cannot neutrally eliminate the alternatives. **Evidence it matters:** StockFox's `tradeoffs.md` `rejected_alternative` entries were written *after* the decision as justification — the options were never real candidates.

`case-builder` **shrinks** to argue-only, so the net cost is below the ~50k/run a new stage implies.

**Phase 2's checker gate is not optional** — without a Tier 1 gate asking *"was elimination real or rationalised?"*, the new stage degenerates into theatre.

---

## Settled decisions — do not re-litigate

- **Seed with canon; never auto-promote self-generated assets.** Human gate required.
- **Two separate fields:** `tier` (peer-reviewed / practitioner / self-derived = provenance) and `status` (seeded / proven / candidate / demoted = our evidence).
- **`INDEX.md` is the only always-loaded file.** Bodies load on trigger match. Grep, no embeddings.
- **Triggers are written as situations, not definitions** — that's what makes an entry retrievable.
- **Ranking ≠ elimination.** RICE/ICE/2×2 order; they remove nothing and are compensatory. Eliminate non-compensatorily first, rank survivors last.
- **Classify archetypes on both axes** (business-decision and PM-competency). Collapsing them loses the competency axis, which is what's actually graded.
- **MECE is not the default decomposition.** Route via Cynefin. Test: *if your branches could be swapped for a competitor's org chart, it's MECE, not first principles.*

---

## Evidence base — cited, do not re-research

**The finding that shaped the design**
- **SoK: Agentic Skills** (arxiv 2602.20867) — self-generated skill libraries average **−1.3 pp** vs skill-free baselines (1 of 5 configs improved); **curated** gain **+16.2 pp**. Self-generation only works with a **deterministic verifier** (Voyager's game env). PM deck quality has none. Coins *"skill debt"*.
- **MemoryAgentBench** (arxiv 2507.05257) — agents resolve conflicting memories at **≤6%**. Never auto-overwrite; version instead.
- **Smyth & Keane 1995** — *utility problem* (retrieval cost eventually exceeds benefit) and *swamping problem* (a bigger base performs worse than a smaller curated one). Fix: classify by competence footprint, delete lowest first, preserve pivotal.

**Architecture sources**
- **Aamodt & Plaza 1994** — CBR cycle Retrieve→Reuse→Revise→**Retain**; Retain is *selective*; indexing needs a fixed index vocabulary.
- **Voyager** (arxiv 2305.16291) — index on the **LLM-generated description, not the artifact** (descriptions grep; code doesn't); gate-before-retain via self-verification; top-k=5.
- **Generative Agents** (arxiv 2304.03442) — importance score as promotion gate; accumulation threshold (reflection fires at summed importance >150); **citations back to source memory IDs** → later demotion evidence; recency decay 0.995.
- **Reflexion** (arxiv 2303.11366) — bounded window of 1–3 reflections; aggressive forgetting is the design.
- **Anthropic** — memory tool recommends expiry + size caps; Agent Skills progressive disclosure (description tier → body tier); context rot confirmed across all models; folder names and timestamps are themselves retrieval signals; agents authoring their own Skills is explicitly *future* work.

**Token economics (verified 2026-06 docs)**
- Opus $5/$25 · Sonnet 5 $3/$15 (intro $2/$10 to 2026-08-31) · Haiku $1/$5 per MTok. **Opus is 5× Haiku, not 10–20×.**
- Anthropic: agents ≈ **4×** chat tokens; multi-agent ≈ **15×**. A 600k–1M run is the documented band, not a defect.
- **Token usage alone explains 80% of performance variance** — cutting tokens cuts capability. Remove waste, don't just spend less.
- Cache: write 1.25× (5m TTL) / 2× (1h), read 0.1×. Minimum cacheable prefix is model-dependent. **Not directly actionable — Claude Code owns `cache_control`, not this repo.**
- Subagents get a fresh context window **plus the full CLAUDE.md re-injected** — CLAUDE.md × 8 agents ≈ 14.7k/run of duplication.

**Taxonomy sources** — already encoded in `Global/library/`; see each entry's inline citation.
