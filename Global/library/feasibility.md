# Feasibility

Loaded on a trigger match from `INDEX.md`. Answers *can this actually be done, by whom, at what cost* — the question that separates a recommendation from a wish.

---

## Cagan's four risks — *the checklist*
**Trigger:** any product concept, before committing to it.
**Source:** Cagan, *INSPIRED*. `practitioner`

Four independent risks. A concept must clear all four; failing any one is fatal, and they fail for different reasons:

| Risk | Question | Who owns it |
|---|---|---|
| **Value** | Will anyone choose this over what they do today? | Product |
| **Usability** | Can they figure out how to use it? | Design |
| **Feasibility** | Can we build it with the people, data and systems we have? | Engineering |
| **Business viability** | Does it work for legal, finance, sales, support, brand? | The business |

Most PM answers cover value and usability and skip the last two — which is where regulatory ceilings, missing data, and unbuilt APIs actually live.

---

## Long pole
**Trigger:** you need the one thing that sets the timeline.
**Source:** engineering practice. `self-derived` — named here because it's the builder's default move and nothing in the canon states it cleanly.

Find the item on the critical path with the longest lead time, and say it plainly. Everything else is noise until it's resolved. Two questions:

1. **What doesn't exist yet?** The endpoint, the dataset, the licence, the registration, the partnership.
2. **What can't be parallelised?** Sequential dependencies set the floor on delivery no matter how many people you add.

State it as *"v1 is X because Y doesn't exist yet"*. That single sentence does more for credibility than any effort estimate, because it proves you looked at the build rather than the idea.

---

## Core vs context — build / buy / partner
**Trigger:** deciding whether to build a capability at all.
**Source:** Moore, *Dealing with Darwin* (core vs context); Williamson, transaction-cost economics (make-or-buy). `practitioner`

**Core** = what differentiates you and what customers choose you for → build it, own it, invest disproportionately.
**Context** = necessary but non-differentiating → buy, partner, or automate it, and spend as little attention as possible.

The failure mode is inverted: teams build context (because it's tractable and fun) and buy core (because it's hard). Ask directly — *if we do this best in the market, does anyone choose us for it?* If no, don't build it.

---

## Type-1 / type-2 doors
**Trigger:** deciding how much analysis a decision deserves.
**Source:** Bezos, Amazon shareholder letters. `practitioner`

**Type 1** — one-way, effectively irreversible (pricing architecture, data model, a public commitment, a regulatory posture). Analyse hard, decide slowly.
**Type 2** — two-way, cheap to reverse (most UI, copy, ordering, defaults). Decide fast and learn; heavy analysis here is pure cost.

Explicitly rating a decision's reversibility is also how you justify *not* researching something — a defensible answer to "why didn't you go deeper here?"

---

## Working Backwards / PR-FAQ
**Trigger:** testing whether an idea is even articulable as a user benefit.
**Source:** Amazon. `practitioner`

Write the launch announcement and the FAQ *before* building anything. If the press release is unwritable — no clear user, no stated benefit, no reason to care — the idea is not ready, and that is an elimination signal, not a writing problem.
