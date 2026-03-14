---
name: edutrack-studio-chalk
description: Use this skill whenever designing or implementing UI/UX for EduTrack to enforce the Studio Chalk theme, accessibility (WCAG AA for text), and anti-gravity visual rules across components, layouts, and styles.
---

# EduTrack Studio Chalk

## Overview

This skill standardizes EduTrack UI work under the Studio Chalk theme. Apply its palette, typography, spacing, components, and anti-gravity rules to every UI/UX implementation, and ensure WCAG AA text contrast.

## When To Use

Use this skill for any EduTrack UI/UX task, including:
- New pages, components, or layout refactors
- CSS/SCSS/Tailwind/theme tokens
- Visual refreshes, redesigns, or design system updates
- UI QA or accessibility adjustments

If a request is purely backend or unrelated to UI, do not apply.

## Workflow (Always Follow)

1. Load the full guide in `references/theme-guide.md`.
2. Apply tokens (colors, typography, spacing, radius, shadow) before styling.
3. Enforce anti-gravity rules on layout and component hierarchy.
4. Validate WCAG AA contrast for all text and interactive states.
5. When delivering code, include or update theme tokens/variables alongside component styles.

## Output Expectations

- Use the Studio Chalk palette and semantic mappings.
- Use the specified font pairing unless the project already defines fonts; in that case, adapt the rules to the existing typography while preserving visual intent.
- Provide focus states, hover states, and disabled states.
- Avoid default UI patterns; keep it warm, academic, and tactile.
- Prefer Bootstrap for rapid, consistent implementation and override with theme tokens as needed.

## Anti-Gravity Rules (Summary)

- Prefer layered surfaces and cards; avoid flat, full-bleed blocks without depth.
- Use soft shadows and edge highlights to lift key elements.
- Keep visual mass low: light backgrounds, airy spacing, crisp type.
- Create motion or rhythm with staggered sections and varied block sizes.
- Always show a clear hierarchy: headline, subhead, body, metadata.
- Use color accents sparingly (10-15% of UI) to avoid heaviness.
- Anchor the page with a clear primary action; secondary actions are quieter.
- Inputs and tables must feel “desk-grade”: lined, neat, and calm.

For detailed tokens, components, and full anti-gravity rules, read `references/theme-guide.md`.
