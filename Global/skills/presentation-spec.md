# Presentation Creation Spec — Universal (Platform-Agnostic)

**How to use this file:**
- **Claude Code:** This file is already integrated into `.claude/skills/deck-builder/SKILL.md`
- **ChatGPT Custom GPT:** Paste this entire file as your Custom GPT system instructions
- **Cursor / Windsurf / any AI coding tool:** Add to context or paste into system prompt
- **Any LLM (Gemini, Mistral, etc.):** Paste as the first message before giving content

**When to invoke:** Any time you want to create a professional HTML slide deck from your content. You provide the content; this spec governs all design, structure, and QA decisions.

---

## What You Get

A single self-contained `.html` file that:
- Works in any browser (open file, no server needed)
- Navigates via keyboard arrows + touch swipe + dot indicators
- Prints to PDF with speaker notes included
- Has WCAG-compliant typography and color contrast
- Shows speaker notes panel when you press `N`

---

## Slide Chrome (Identity Markers — Mandatory)

Every slide carries a persistent 3-zone chrome: subtle header + footer with identity markers. These are your professional signature — always present, never dominant.

```
┌──────────────────────────────────────────────┐
│  COMPANY (9px, brand color)    Project Name  │  ← header chrome
├──────────────────────────────────────────────┤
│                                              │
│            SLIDE CONTENT                    │
│                                              │
├──────────────────────────────────────────────┤
│  Your Name           3/18        July 2026   │  ← footer chrome
└──────────────────────────────────────────────┘
```

**Rules:**
- Chrome text: 9px maximum. Never larger. It is metadata, not content.
- Company name: brand primary color, uppercase, letter-spaced
- Project name: muted color, truncated if > 40 chars
- Footer: your name left · slide number center · date right
- Appendix slides: "APPENDIX A1" replaces project name on right
- Chrome stays visible when printing to PDF (it's the watermark)
- Chrome does NOT appear on the outer dot-nav bar — only inside each slide

---

## Input Format (paste to AI after loading this spec)

```
CREATE PRESENTATION:

Company: [Company Name]
Brand colors: [hex codes if known, or "search for it"]
Topic: [what the presentation is about]
Audience: [who will see this]

SLIDES:
1. [Title of slide 1 — write the argument, not the topic]
   Content: [bullets or description of what goes on this slide]
   Notes: [what you'd say verbally]

2. [Title of slide 2]
   Content: [...]
   Notes: [...]

[continue for all slides]

APPENDIX (optional):
A1. [Appendix slide title]
    Content: [...]
```

---

## Design Rules (AI must follow all)

### 1. Brand Colors — Mandatory First Step

Before writing HTML:
- If user provides hex codes → use them
- If user says "search for it" → search `[Company] brand colors hex`
- Never use generic blue (#007BFF, #1A73E8) as default
- Default fallback (only if search fails): `#E85D04` + `#0D1B2A`

### 2. Token System

All colors and sizes go through CSS variables:

```css
:root {
  --color-primary: [brand color];
  --color-background: [dark bg or #0D1B2A];
  --color-surface: rgba(255,255,255,0.06);
  --color-text-primary: #FFFFFF;
  --color-text-muted: rgba(255,255,255,0.55);
  --color-border: rgba(255,255,255,0.10);
  --space-1: 0.5rem;
  --space-2: 1rem;
  --space-3: 1.5rem;
  --space-4: 2rem;
  --space-6: 3rem;
  --space-8: 4rem;
  --text-title: clamp(1.375rem, 2.8vw + 0.5rem, 2.25rem);
  --text-body: clamp(0.875rem, 1.4vw + 0.25rem, 1.125rem);
  --text-small: clamp(0.625rem, 0.8vw + 0.15rem, 0.75rem);
  --text-stat: clamp(2rem, 5vw + 0.5rem, 4rem);
}
```

**Rule:** Never hardcode hex in element styles. Never use `font-size: 14px`. Always `var(--text-body)`.

### 3. Viewport Fix (iOS Safari)

Every `height: 100vh` must be immediately followed by `height: 100dvh`:

```css
.deck {
  height: 100vh;
  height: 100dvh;   /* iOS Safari fix */
  overflow: hidden;
}
```

### 4. No Scrolling

Slides never scroll. Content that doesn't fit gets cut. Max per slide:
- 1 heading (the argument, not the topic)
- 5 bullets maximum
- 1 visual element (stat, table, chart, timeline, diagram)
- 1 footnote line

### 5. Headings = Arguments, Not Topics

- ❌ "Market Analysis"
- ✅ "India outbound market is $35B at 11.4% CAGR — Ixigo captures <5%"

---

## 12 Slide Types

| # | Type | When to use |
|---|---|---|
| 1 | Title/Cover | First slide always |
| 2 | Executive Summary | 3-card (Problem/Rec/Impact) with stat callout |
| 3 | Section Divider | Between major sections |
| 4 | Insight/Analysis | Data + evidence bullets + stat callout |
| 5 | Recommendation | Action verb heading + framework + impact |
| 6 | Comparison/Tradeoffs | 2-column: chosen vs rejected |
| 7 | Metrics/KPI | Card grid, one card per metric |
| 8 | Timeline/Roadmap | Horizontal phases with deliverables |
| 9 | Process/Flowchart | Mermaid diagram (LR flowchart) |
| 10 | Quote/Principle | Blockquote + why it matters |
| 11 | Two-Column | Current state vs proposed state |
| 12 | Appendix | Dense data, labeled "APPENDIX A1" |

For **Process slides** → use Mermaid (CDN: `cdn.jsdelivr.net/npm/mermaid`):
```html
<pre class="mermaid">flowchart LR
    A[Input] --> B{Decision}
    B -->|yes| C[Action]
    B -->|no| D[Other action]
</pre>
<script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
```

For **Chart slides** → use Chart.js (CDN: `cdn.jsdelivr.net/npm/chart.js`):
- Bar, line, or doughnut only (no pie)
- Colors must use `getComputedStyle(document.documentElement).getPropertyValue('--color-primary')`

---

## Navigation

```javascript
(function() {
  const slides = document.querySelectorAll('.slide');
  const dots = document.querySelectorAll('.dot');
  const counter = document.querySelector('.slide-counter');
  let current = 0;

  function show(n) {
    slides[current].classList.remove('active');
    dots[current]?.classList.remove('active');
    current = Math.max(0, Math.min(n, slides.length - 1));
    slides[current].classList.add('active');
    dots[current]?.classList.add('active');
    if (counter) counter.textContent = `${current + 1} / ${slides.length}`;
  }

  document.addEventListener('keydown', e => {
    if (e.key === 'ArrowRight' || e.key === ' ') { e.preventDefault(); show(current + 1); }
    if (e.key === 'ArrowLeft') { e.preventDefault(); show(current - 1); }
    if (e.key === 'n' || e.key === 'N') toggleNotes();
  });

  dots.forEach((dot, i) => dot.addEventListener('click', () => show(i)));

  let touchStartX = 0;
  document.addEventListener('touchstart', e => { touchStartX = e.touches[0].clientX; }, {passive: true});
  document.addEventListener('touchend', e => {
    const dx = e.changedTouches[0].clientX - touchStartX;
    if (Math.abs(dx) > 50) show(dx < 0 ? current + 1 : current - 1);
  }, {passive: true});

  show(0);
})();

function toggleNotes() {
  document.querySelectorAll('.speaker-notes').forEach(n => n.classList.toggle('visible'));
}
```

---

## Speaker Notes

Every slide includes:
```html
<aside class="speaker-notes" aria-hidden="true">
  Key talking point. Anticipated question. Stat to have ready.
</aside>
```

Hidden by default. Shown when user presses `N`. Visible on print (PDF export).

---

## Infographic Patterns (CSS-only, choose by data type)

Every slide needs ≥1 non-text visual. Pick by what the data is:

| Data type | Pattern |
|---|---|
| Single % or ratio | Stat Ring — CSS conic-gradient donut |
| 3 hero numbers | Data Cluster — large numbers in a row |
| Process steps | Step Chain — boxes with → arrows |
| Single metric vs benchmark | Progress Bar — horizontal fill with marker |
| Priority matrix | 2×2 Matrix — 4 quadrants, highlight chosen |
| Current vs future state | Before/After — two column split |

**Rules:**
- CSS only — no images, no SVG files, no CDN for infographics
- Max 2 infographic elements per slide
- Infographic must touch data from the slide — no decorative filler
- If data doesn't fit a pattern → use a stat callout box (large number + label)

---

## Anti-Patterns (Never Do)

- No accent lines under headings
- No decorative color bars on card edges
- No prev/next buttons (dots + keyboard only)
- No external CDN except Mermaid (diagrams) + Chart.js (data viz)
- No cream/beige backgrounds
- No alternating dark/light slides
- No more than 5 bullets per slide
- No hardcoded hex in element styles
- No `height: 100vh` without `height: 100dvh` on next line

---

## QA Before Delivering

Check all 10 before finishing:

- [ ] Every `height: 100vh` has `height: 100dvh` on next line
- [ ] No slide scrolls at 1280×800
- [ ] All font sizes use `var(--text-*)` tokens
- [ ] Slide headings are arguments (verb + outcome), not topic labels
- [ ] Max 5 bullets per slide
- [ ] No placeholder text or [TODO] markers
- [ ] Brand colors applied (not default blue)
- [ ] Dot count matches slide count
- [ ] Arrow keys work (left/right/N)
- [ ] File opens in browser with no errors

---

## For ChatGPT / Custom GPT Setup

To install this as a Custom GPT:
1. Go to ChatGPT → Explore GPTs → Create a GPT
2. In "Instructions": paste the entire contents of this file
3. Name: "Slide Deck Builder"
4. Starter message: "Create a professional HTML slide deck from my content. I'll follow the Presentation Spec rules — send me your content in the input format above."
5. No special tools needed — the GPT generates the HTML directly as a code block

To use: give the GPT your content in the input format above. It generates a complete `.html` file. Save it, open in browser.

---

## For Cursor / Windsurf / Copilot

Add this file as a context rule:
- **Cursor:** `.cursorrules` → paste this file contents
- **Windsurf:** `.windsurfrules` → paste this file contents  
- **Copilot:** Include in your workspace context when asking for slides

Then just ask: "Create a slide deck about [topic]" — the rules apply automatically.
