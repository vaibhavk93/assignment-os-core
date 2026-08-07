---
description: Analyze and register a media file (screenshot, PDF, recording, Figma export) into the company's media registry.
---

File path from `$ARGUMENTS`.

1. Check `Companies/<Company>/MEDIA_REGISTRY.json` — if this file is already registered, skip re-analysis unless the user asks for a refresh.
2. Otherwise, analyze it (vision for images/Figma, text extraction for PDFs) in the context of the active assignment's `INPUT.md` if one exists.
3. Write `.meta.json` next to the file and append an entry to `MEDIA_REGISTRY.json`:
```json
{ "id": "...", "file": "media/...", "type": "screenshot|pdf|recording|figma", "summary": "one line", "competitor": false, "competitor_name": null, "analysis_confidence": "high|medium|low" }
```
4. Set `analysis_confidence: "low"` rather than guessing if the file is blurry, small, or ambiguous — never fabricate detail. If unreadable, still write a `.meta.json` with `description: "file unreadable"`.
