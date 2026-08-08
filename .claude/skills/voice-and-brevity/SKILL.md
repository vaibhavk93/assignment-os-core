---
name: voice-and-brevity
description: Hard numeric limits on sentence and slide length, the extended AI/consultant-tell blocklist, the compression test, and the recall test. Read when writing or scoring any draft.json prose. Pairs with Global/candidate/VOICE.md, which supplies the candidate's register.
---

# Voice and Brevity

Three failures this prevents: prose that is smart but unreadable, output that sounds like a model instead of the candidate, and a deck the interviewer cannot repeat to a colleague after the room empties.

**Register comes from `Global/candidate/VOICE.md`.** Read it before writing. This file is the ruler; that file is the voice.

## Hard limits (countable, no code needed)

| Limit | Value | Applies to |
|---|---|---|
| Sentence length | **≤25 words**, anywhere in `draft.json` content | every sentence |
| Bullet length | **≤16 words**, one line at 1280×800 | slide bullets |
| Slide body | **≤80 words** total, excluding heading, footnote, chrome | every core slide |
| Heading | **≤14 words** — still an argument, not a topic | every slide |
| Paragraph | **≤3 sentences** | prose blocks, appendix |
| Bullets per slide | **≤5** — set by `deck-builder`, not restated here | every slide |
| Speaker notes | **<100 words** — set by `deck-builder` | every slide |

The caps are reconciled: 5 bullets × 16 words = 80, so the bullet limit and the slide limit never fight. Appendix prose gets the sentence and paragraph caps but not the 80-word slide cap.

A sentence over 25 words is a failure even if it is correct. Split it. Two short sentences always beat one dash-spliced sentence — see the dash rule in `case-builder`.

## Blocklist — extension only

The consultant-speak bans and the "never name the framework" rule already live in `.claude/agents/case-builder.md` and `.claude/skills/pm-frameworks/SKILL.md`. Do not restate them. These are the **additional** bans, all AI tells rather than consultant tells:

- **Escalation:** "it's not just X, it's Y", "isn't merely", "at its core", "fundamentally", "the real question is", "the key insight here", "make no mistake", "the reality is".
- **Self-praise on own work:** "robust", "comprehensive", "deep dive", "seamless", "game-changer", "paradigm", "thoughtful".
- **Filler adverbs:** "crucially", "significantly", "notably", "importantly", "very", "really", "incredibly", "extremely".
- **Stacked hedges:** any two of may/might/could/potentially/possibly/somewhat in one sentence.
- **Scenery:** "landscape", "navigate the", "in today's", "double-edged sword", "delve".

One hit is a defect, not a style note. Rewrite the sentence around the thing it was decorating.

## Structural uniformity — the tell that survives every word-level check

Every rule above operates on sentences. This one operates on shape, which is why a deck can pass the whole blocklist and still read as machine-written.

**Three or more sibling items sharing an identical grammatical skeleton is a filled template, because it is one.** Tradeoff rows, recommendation blocks, metric definitions, persona cards — if each one is `[Thing]. Cost: X. Rejected: Y. Reason: Z.` with only the nouns swapped, a reader clocks the mould before they read the content.

A person writing under time pressure does not produce four identical rows. One is two clauses because that was all there was to say. One is a fragment. One carries an aside that did not fit anywhere else. One drops the third clause because it was obvious.

**Rule:** in any set of three or more siblings, at least one must break the pattern — different clause count, different ordering, or a dropped clause where it is implicit. Uniformity is not tidiness here; it is the fingerprint.

Same applies to rhythm: if every slide body is three bullets of near-identical length, vary one. Real emphasis is uneven.

## One citation convention, applied everywhere

Selective sourcing reads as content assembled across different passes, which is exactly what it is. **If any slide carries a source or confidence line, every slide making a comparable factual claim carries one.**

The specific failure to avoid: the safe, checkable numbers get attributed while the dramatic ones sit bare. A reader who notices that the competitor table is sourced but "93% lost money" is not will discount the second number, and reasonably so — it looks like the number nobody wanted to attach a source to.

Pick one treatment (inline footnote, per-slide source line, or a numbered endnote slide), then apply it to every factual claim of the same weight. Not the ones that were easy.

## The compression test

For every line: **if I delete this line, what question becomes unanswerable?**

Name the question out loud. If you cannot, delete the line. If the question is already answered elsewhere in the deck, delete the line. If the question is real and unanswered anywhere else, the line stays — and it should then be the shortest sentence that answers it.

Run this on the whole core section before the appendix split. Most "useful to have" lines die here rather than moving to appendix.

## The recall test

The panel decides after the candidate leaves the room, and it decides on what one interviewer can repeat to another from memory. Design for that. Every deliverable must have exactly three things a person can carry out of the room:

1. **One named concept** — ≤4 words, coined by the candidate, appearing ≥2 times in the core deck. Not a framework name. It is the label for *this* recommendation ("confidence before conviction", "the empty-state problem").
2. **One number** — a single hero figure the argument returns to. Cited. Not four competing numbers; four numbers means zero remembered.
3. **One visual** — describable in one sentence by someone who saw it once ("the 2×2 with the empty top-right quadrant"). If describing it takes two sentences, it is too busy to recall.

Fewer than three, or a concept nobody would repeat, means the deck is forgettable regardless of how correct it is.

## Scored by

`strict-checker` — Tier 2 rows *Readability*, *Candidate voice*, *Memorability*. See `checker-rubrics`.
