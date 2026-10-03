# Flame catalogue QA — 2026-10-03

Current surfaces: index.html (DS catalogue), site.html (newsletter calling-card preview).

- Desktop inspected at 1440×1000.
- Mobile at 390×844: catalogue and site scroll width 375, no horizontal overflow.
- All catalogue and site images loaded on mobile, including embedded original flame and four Fluent icons.
- All five 4:5 visual-magazine frames have no vertical clipping on mobile.
- Brand logo/flame elements computed transform: none.
- Icon viewBox excludes lettering and dot; original raster is embedded unchanged, not redrawn.
- One h1, main, pt-BR, skip link and labeled navigation on both surfaces.
- Existing contrast: white/action 6.33:1; ink/lime 8.08:1; muted/soft 5.68:1.
- Focus-visible and reduced-motion CSS retained.
- Desktop carousel preview saved locally as revista-v2.jpg.

Pending: full keyboard/screen-reader/zoom review, final exports and caption/alt package, platform safe areas, image delivery optimization and performance. Catalogue remains a review prototype, not a finished DS or complete WCAG certification.
No HostGator deployment or GitHub Pages settings change.
