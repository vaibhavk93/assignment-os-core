# Deck Builder — DEPRECATED (v0)

> **DEPRECATED — DO NOT USE.** Canonical version is at `.claude/skills/deck-builder/SKILL.md` (v1).
> This file kept for reference only. Differences: v0 has no speaker notes, no 100dvh, no clamp enforcement, no Mermaid/Chart.js, 7 slide types (v1 has 12), wrong Ixigo color example (#E8420C should be #EC5B24).

---

# Deck Builder v0 (archived) — HTML Presentation Skill

How to build a professional HTML slide deck for interview assignment deliverables. This skill governs all HTML deck output. It overrides the HTML section of `brand-templates.md`.

---

## Step 0 — Brand Color Search (MANDATORY, always first)

Before writing a single line of HTML, search for the company's brand colors.

**Search query:** `[Company Name] brand colors hex` or `[Company Name] brand guidelines`

**What to extract:**
- Primary brand color (main action color — button, highlight, logo)
- Secondary brand color (if exists)
- Whether brand uses dark or light backgrounds

**Examples:**
- Ixigo: primary red-orange (#E8420C), white, dark background preferred
- Swiggy: primary orange (#FC8019), dark navy (#0B0C10)
- Zepto: primary purple (#7B2FBE), white
- CRED: deep black (#0A0A0A), gold accent (#C9A84C)

**If brand colors cannot be found:** use the default executive palette:
- Primary: `#0D1B2A` (deep navy)
- Accent: `#E85D04` (warm orange)
- Text: `#FFFFFF`

**Never use generic blue as default.** Brand colors are non-negotiable.

---

## Slide Structure Rules

### One message per slide
Slide heading = the argument. Not the topic.
- ❌ "Market Analysis"
- ✅ "India outbound market is $23–35B growing 11.4% YoY — and ixigo captures less than 5%"

### Fixed-height slides — NO scrolling
Every slide must fit in the viewport. If content overflows, shorten it. Never allow a scrollable slide body. The user will NOT scroll down inside a slide — if it doesn't fit, it doesn't exist.

Max content per slide:
- 1 heading (the argument)
- 3–5 bullets OR 1 table (max 4 rows) OR 1 stat callout
- 1 footnote/citation line (optional, bottom)
- No long paragraphs — bullets only in slide body

### No speaker notes in the slide
Speaker notes belong in a separate `OUTPUTS/speaker_notes.md` file, not in the HTML deck. The slide HTML should contain no `<aside>`, `<details>`, or hidden note elements. A clean presentation surface only.

---

## HTML Architecture

Self-contained single file. No CDN dependencies. All CSS inline.

### Slide container model
```html
<div class="deck">
  <div class="slides-container">
    <div class="slide active" data-index="0"> ... </div>
    <div class="slide" data-index="1"> ... </div>
    <!-- appendix slides get data-section="appendix" -->
    <div class="slide" data-index="N" data-section="appendix"> ... </div>
  </div>

  <!-- Dot indicator — replaces prev/next buttons -->
  <div class="dot-nav">
    <span class="dot active" data-target="0"></span>
    <span class="dot" data-target="1"></span>
    <!-- one dot per slide -->
  </div>

  <!-- Minimal controls: slide counter only + optional "Appendix ↓" jump -->
  <div class="slide-counter">1 / N</div>
  <button class="appendix-jump">Appendix ↓</button>
</div>
```

### Navigation
- **Dot indicators** — one dot per slide, bottom center of viewport. Active dot = filled. Click dot = jump to slide.
- **Keyboard:** Left/Right arrow keys navigate slides
- **No prev/next buttons** — dots are sufficient
- **Slide counter** — "Slide X of N" — small, top right corner
- **Appendix jump** — single small button bottom right: "Appendix ↓" (only visible on non-appendix slides)

### Slide layout (CSS)
```css
.deck {
  width: 100vw;
  height: 100vh;
  overflow: hidden; /* hard cap — no scroll ever */
  position: relative;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  background: var(--bg);
  color: var(--text);
}

.slides-container {
  width: 100%;
  height: calc(100vh - 60px); /* reserve 60px for dot nav */
  overflow: hidden;
}

.slide {
  width: 100%;
  height: 100%;
  display: none;
  padding: 48px 64px;
  box-sizing: border-box;
  overflow: hidden; /* no scroll inside slide */
}

.slide.active {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
}

.dot-nav {
  position: fixed;
  bottom: 20px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  gap: 8px;
  z-index: 100;
}

.dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: rgba(255,255,255,0.35);
  cursor: pointer;
  transition: background 0.2s;
}

.dot.active {
  background: var(--accent);
}
```

---

## Color System

Use CSS variables tied to brand colors found in Step 0.

```css
:root {
  --bg: [brand dark bg or #0D1B2A];
  --card-bg: rgba(255,255,255,0.06);
  --accent: [brand primary color];
  --text: #FFFFFF;
  --text-muted: rgba(255,255,255,0.55);
  --border: rgba(255,255,255,0.10);
}
```

**Color rules (from Anthropic pptx skill — adapted):**
- One color dominates (60–70% visual weight) — usually the dark background
- Accent = brand primary color — use for: key numbers, highlighted bullets, active dots, heading underline alternative
- Text-muted = footnotes, citations, labels
- Never equal weight across colors — dominance matters
- Commit to dark background throughout (not alternating dark/light per slide)

---

## Typography

```css
.slide-heading {
  font-size: clamp(22px, 2.8vw, 36px);
  font-weight: 700;
  line-height: 1.2;
  margin-bottom: 24px;
  color: var(--text);
}

.slide-body {
  font-size: clamp(14px, 1.6vw, 18px);
  line-height: 1.6;
  color: var(--text);
}

.slide-body li {
  margin-bottom: 10px;
  list-style: none;
  padding-left: 1.2em;
  position: relative;
}

.slide-body li::before {
  content: "→";
  position: absolute;
  left: 0;
  color: var(--accent);
}

.slide-footnote {
  font-size: 11px;
  color: var(--text-muted);
  margin-top: auto; /* pushes to bottom of slide */
  padding-top: 12px;
  border-top: 1px solid var(--border);
}
```

**Rules:**
- Heading: bold, specific (argument not topic), clamp-sized for responsive
- Body: max 5 bullets per slide — if more, cut
- Footnotes/citations: small, muted, always bottom of slide
- No centered body text — left-align always
- No paragraph prose in slide body — bullets only

---

## Slide Types

### Title / Cover slide
```
Background: brand dark color (full bleed)
Content: company name (small, top) + assignment title (large, center) + date (small, bottom)
No bullets.
```

### Executive Summary slide
```
3-column card layout:
[Problem card] | [Recommendation card] | [Impact card]
Each card: 1 bold headline + 2-3 bullets
Bottom: large stat callout (e.g., "$23–35B market, 11.4% CAGR")
```

### Insight / Analysis slide
```
Heading: the insight as an argument
Body: 3-4 evidence bullets with supporting data
Supporting stat: callout box right side (large number + label)
Footnote: sources
```

### Recommendation slide
```
Heading: the recommendation as an action
Body: what changes, why, expected impact
Supporting: before/after comparison OR priority list
```

### Metrics / Monitoring slide
```
Use a 2-column or 3-column card grid — one card per metric
Each card: metric name + how measured + target
```

### Rollout slide
```
Use a horizontal timeline OR numbered phases
Each phase: title + timeline + key deliverable
```

### Appendix slides
```
"APPENDIX" label top right (small, muted)
Dense formatting acceptable
Same color scheme — not white
```

---

## Visual Elements (required — no text-only slides)

Every slide must have at least one non-text visual element:
- **Stat callout box** — large number, brand accent color background
- **Card grid** — 2-4 cards in a grid (light border, subtle bg)
- **Timeline** — numbered horizontal steps
- **Comparison** — two columns: current state vs proposed state
- **Table** — max 4 rows, alternating row tint

**Never:** plain title + bullet list with no visual element.

---

## Design Anti-Patterns (DO NOT DO)

- No accent lines under headings (AI-generated tell)
- No decorative color bars/stripes on edges of cards
- No scrollable slides — if content overflows, cut it
- No speaker notes in HTML
- No prev/next buttons — dots only
- No external CDN (self-contained only)
- No cream/beige backgrounds — dark or white only
- No mixing dark/light slides (commit to one)
- No more than 5 bullets per slide

---

## QA Before Handing Off

Self-check before passing to Visual QA:
- [ ] All slides fit in viewport (no overflow/scroll)
- [ ] No speaker notes anywhere in HTML
- [ ] Dot indicators match slide count
- [ ] Brand colors applied (not default generic blue)
- [ ] Every slide has a non-text visual element
- [ ] No placeholder text
- [ ] File is self-contained (no CDN links)
- [ ] Slide headings are arguments, not topic labels
