# Studio Chalk Theme Guide

## Theme Intent

Studio Chalk is warm, academic, and tactile. It should feel like a modern classroom studio: calm surfaces, readable typography, and handcrafted accents. The UI must be light, breathable, and legible in all lighting conditions.

## Tooling (Implementation Baseline)

- Use Bootstrap for rapid, consistent UI scaffolding.
- Override Bootstrap defaults with the Studio Chalk tokens (colors, typography, spacing, radius, shadows).
- Prefer Bootstrap utility classes for spacing/layout; use custom CSS only for theme overrides and unique components.

## Accessibility Baseline (WCAG AA)

- Normal text contrast: >= 4.5:1
- Large text (18pt+ regular or 14pt+ bold): >= 3:1
- Interactive focus outline must be >= 3:1 against adjacent colors
- Minimum touch target: 44x44
- Do not place text directly on photos unless a solid overlay achieves AA contrast

## Color Palette

### Core
- `Charcoal` #1E1E1B (primary text, headings)
- `Chalk` #F4F1E9 (main background)
- `Terracotta` #D46A4A (primary action, highlights)
- `Sage` #7C9A82 (success, calm accents)
- `Sky` #6FA3D9 (links, informational accents)
- `Gold` #E7B84B (warnings, emphasis)
- `Rose` #C95E76 (errors, critical)

### Neutrals (Derived)
- `Chalk-Deep` #EFE9DD (subtle panels)
- `Ink-Soft` #2A2A25 (secondary text)
- `Line` #D9D2C7 (borders, separators)
- `Paper` #FFFFFF (cards, elevated surfaces)

### Semantic Mapping
- Background: `Chalk`
- Surface: `Paper`
- Surface subtle: `Chalk-Deep`
- Border: `Line`
- Text primary: `Charcoal`
- Text secondary: `Ink-Soft`
- Link: `Sky`
- Primary action: `Terracotta`
- Success: `Sage`
- Warning: `Gold`
- Error: `Rose`

## Typography

- Headings: `Fraunces` (serif), weights 600-700
- Body/UI: `IBM Plex Sans` (sans), weights 400-600
- Code/monospace: `IBM Plex Mono`

If fonts are already defined in the project, keep them and map the hierarchy to match the intent: expressive headings and clean, high-legibility body text.

### Type Scale
- Display: 40/48
- H1: 32/40
- H2: 26/34
- H3: 22/30
- H4: 18/26
- Body: 16/24
- Small: 14/20
- Caption: 12/16

## Spacing + Layout

- Base spacing unit: 4
- Recommended scale: 4, 8, 12, 16, 20, 24, 32, 40, 56, 72
- Content width: 1120 max; 72ch for text blocks
- Section padding: 56-72 on desktop, 32-40 on mobile

## Radius + Shadows

- Radius: 10 for cards, 8 for inputs/buttons, 999 for pills
- Shadows:
  - Low: 0 1px 2px rgba(30, 30, 27, 0.08)
  - Mid: 0 6px 18px rgba(30, 30, 27, 0.12)
  - Lift: 0 10px 24px rgba(30, 30, 27, 0.16)

## Components

### Buttons
- Primary: `Terracotta` bg, `Chalk` text, hover darken 6-8%
- Secondary: `Paper` bg, `Charcoal` text, `Line` border
- Tertiary: text-only, `Sky` or `Charcoal`
- Radius 8, height 40-44, focus outline `Sky`

### Inputs
- Background `Paper`, border `Line`, text `Charcoal`
- Focus border `Sky` with soft glow
- Helper text `Ink-Soft`, error text `Rose`

### Cards
- `Paper` surface, `Line` border, soft shadow
- Use header strip in `Chalk-Deep` for grouped info

### Tables
- Header row `Chalk-Deep`, body `Paper`
- Row hover: `Chalk-Deep`
- Use 1px separators with `Line`

## Anti-Gravity Rules (Full)

1. Use layered surfaces and gentle elevation. Every dense block should sit on a surface.
2. Break long sections into lighter modules with air between them.
3. Avoid full-bleed dark sections; keep them rare and short.
4. Keep color accents under 15% of screen area.
5. Use typography to create vertical rhythm, not just color.
6. Prefer inset highlights (top borders, soft gradients) to heavy dividers.
7. Primary actions are warm and confident; secondary actions are quiet.
8. Avoid over-saturated gradients; use soft, natural transitions.
9. Use small, intentional shapes (tabs, chips, badges) to add rhythm.
10. Every section needs a lead-in and a takeaway (headline + helper line).

## Quick Checklist

- Does every text color meet AA contrast?
- Are there layered surfaces with subtle lift?
- Is the palette applied semantically?
- Are sections airy and balanced on mobile?
- Is the primary action clear and warm?
