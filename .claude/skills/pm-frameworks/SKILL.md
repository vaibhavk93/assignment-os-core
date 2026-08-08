---
name: pm-frameworks
description: How to select a reasoning method and where to load it from — routes into Global/library/. Use when planning research, decomposing a problem, generating or eliminating options, or building the case.
---

# Choosing a Method

This skill is a **router, not a glossary**. The methods live in `Global/library/`; loading a body you don't need is wasted context, so match a trigger first.

**`Global/library/INDEX.md` is the only file to read by default.** One row per move, each with the situation it applies to. Match the trigger, load that row's file, use it. Nothing else.

## The order that matters

Reasoning about a problem has four distinct operations, and doing them out of order is the most common failure:

1. **Route** — classify the problem before picking a method (`decomposition.md` → Cynefin). Complicated problems want analysis; complex ones want an experiment, and a tidy tree there produces a confident wrong answer.
2. **Decompose** — break it apart (`decomposition.md`).
3. **Generate, then eliminate** — options first, cuts second (`behaviour.md` → `elimination.md`).
4. **Rank the survivors** — last, and only on a set that has already been cut.

> **Ranking is not elimination.** RICE, ICE, weighted scoring and impact/effort 2×2s order an option set; they remove nothing, and being compensatory they let a high score paper over a fatal failure. Cut on non-compensatory grounds first — see `elimination.md`.

## MECE is a tool, not the default

An earlier version of this file called MECE *"the default way to decompose any problem statement."* That was wrong, and it is worth knowing why:

- A MECE tree **partitions the existing solution space** — its branches are inherited categories.
- **Test:** if your branches could be swapped for a competitor's org chart, it's MECE, not first principles.
- On a **complex** problem (Cynefin), an issue tree actively misleads by implying a knowable structure that isn't there.

Use MECE where it belongs — exhaustive coverage of a known space — and route to it deliberately rather than reflexively.

## Source tiers — carried on every entry

`peer-reviewed` · `practitioner` (widely used, not empirically validated) · `self-derived`.

**Never present a `practitioner`-tier method as evidence.** RICE and Hooked are useful thinking tools and are not findings; citing them as though they were is a weakness an interviewer will find. The tier travels with the method — check it before a claim leans on it.

## Structure with it, never name it

Do not write "applying a MECE lens", "using a 2×2", "per Cynefin", "the COM-B model shows". The clean breakdown is the evidence; the label adds nothing and reads as framework-first thinking. This is the single clearest consultant tell. Same rule for every method in the library.

## Still-common shorthand

Kept here because they're vocabulary rather than methods, and don't warrant a library load:

**JTBD** — "When [situation], I want to [motivation], so I can [outcome]." Reframes a stated request as a real need.
**AARRR** — Acquisition → Activation → Retention → Revenue → Referral. Growth diagnosis.
**North Star** — one metric capturing delivered value: real user value, correlates with revenue, near-real-time, actionable.
**Outcome vs output** — frame recommendations as outcomes ("+15% D7 retention"), never outputs ("build notifications").
**Hypothesis format** — "We believe [X] causes [users] to [behaviour], resulting in [metric]. We'll know when [outcome]."
**TAM/SAM/SOM** — total → serviceable addressable → serviceable obtainable. Bottom-up beats top-down when you can get unit × price × frequency.
**Pyramid Principle** — answer first → ~3 arguments → evidence. Governs every deliverable; applied form in `deck-builder`.
