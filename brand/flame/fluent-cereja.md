# Fluent 2 × Cereja — Flame v0.2 proposal

Status: **visual prototype for review**, not a production migration or a finished design system.

Kell selected Microsoft Fluent 2 as the main UI reference on 2026-10-03. The existing Flame editorial principles remain authoritative. Fluent informs controls, surfaces, depth and state organization; Cereja provides art direction, color, voice and channel composition.

## Two fronts, shared foundations

| Layer | Flame Web | Flame Editorial / Social |
|---|---|---|
| Atoms | semantic colors, type roles, spacing, shape, border, focus, motion | same roles; composition sizes differ |
| Molecules | action group, issue metadata, tag, source link | source line, issue signature, content/evidence unit |
| Organisms | IssueHero, IssueCollection, SubscribeBlock, ResearchDesk | Cover, SignalSequence, EvidenceStack, ExitQuestion, ResearchDesk |
| Templates | responsive editorial opening and archive | 4:5 carousel, 9:16 story; video contract below |
| Pages / outputs | content-bound website | human-reviewed native compositions |

Content tokens describe editorial meaning. Design tokens describe visual roles. LLM tokens measure model context. Keep these separate.

## Reference boundary

Official references:
- [Microsoft Fluent 2](https://fluent2.microsoft.design/)
- [Design kits and variable organization](https://fluent2.microsoft.design/get-started/design)
- [Implementation libraries](https://fluent2.microsoft.design/get-started/develop)
- [Fluent UI license](https://github.com/microsoft/fluentui/blob/master/LICENSE)

The prototype uses original HTML/CSS, **not Fluent UI components**. No Microsoft fonts, kit files or UI source code are embedded. Four Microsoft Fluent UI System Icons are included under their own MIT license, with notice and source revision recorded in [brand-media-rules.md](brand-media-rules.md). It studies public design patterns and credits Microsoft. Fluent UI code is MIT, with an additional fonts/icons assets notice; do not infer that every Figma kit or Microsoft asset has that license. Check the specific asset's terms before future incorporation. No license change to Cereja materials is proposed.

## Editorial decisions

- Preserve cherry #EA1945, action cherry #BE1035, lime #D7E25B, ink #3A3A3A and white.
- New **proposed** neutrals: soft surface #F6F5F2, muted text #616161 and border #D8D6D1. They are preview values, not approved canonical brand colors.
- Controls use 6px corners; web surfaces may use 12px. This is a scoped proposal extending the previous 8px surface scale. Editorial canvases remain square; tags remain pills. Do not round every social composition.
- Elevation is restrained and semantic: quiet resting surface, stronger actionable hover. Keep graphic borders and editorial rhythm.
- Preserve current Georgia/Arial fallbacks. Canonical brand font kit is still pending verification; no Segoe UI or new font download.
- Make text-bearing cherry actions use #BE1035. Signature pink remains a graphic accent.
- Prototype copy on social frames is demonstrative, not Kell's approved opinion or newsletter excerpts.

## Multimodal contract

For a carousel, every page has an ordinal, one semantic job and a source/provenance slot when making a claim. Export accompanying caption/alt text with the sequence, not only raster images.

For stories and short video, define title, visual, evidence/source, spoken script, timed captions, transcript and exit action. Keep essential text away from platform overlays; validate safe areas in the target platform before export. Do not freeze arbitrary pixel margins as universal platform truth.

Motion uses Flame's named durations and reduced-motion rules. Meaning, sequence, evidence and action remain understandable without motion or sound. The current story is a static frame; no video generator or animation library has been implemented.

## Review prototype

Open [prototype/index.html](prototype/index.html) locally, or serve this directory:

```sh
python -m http.server 8766 --directory prototype
```

Review the separate DS catalogue at index.html and the newsletter calling-card preview at [prototype/site.html](prototype/site.html). The catalogue contains identity, imagery, icons, actions and five visual-magazine compositions. Shared CSS tokens are in [prototype/tokens.css](prototype/tokens.css). Brand assets come from the previously published Cereja site. The icon frames the exact original flame without lettering. A conceptual AI illustration and four licensed Microsoft icons add the visual media layer. See [brand/media rules and credits](brand-media-rules.md). No confidential company materials are included.

The prototype is a visual slice, not a reusable production component library. Next steps after visual review: resolve canonical fonts; consolidate approved tokens and component states; build exportable social templates; apply approved web components to the versioned site via a separate PR; validate browser accessibility and performance; then deploy to HostGator.

## Validation limits

Basic browser checks cover desktop/mobile layout, image loading, horizontal overflow and disclosure behavior. Contrast calculation and semantic HTML checks do not establish complete WCAG conformance. Keyboard, zoom, screen-reader and final channel export reviews remain required before production. No paid model call, benchmark or automatic publication is involved.

## Catalogue is not the public site

The newsletter site invites reading and subscription. Flame lives in GitHub with its own HTML catalogue; a GitHub Pages view can be deployed after review. Do not put design tokens, implementation explanations or component documentation in the newsletter journey.

The user's fixed identity rules are in [brand-media-rules.md](brand-media-rules.md). Never rotate the mark. The standalone icon contains only the original flame/leaf with no lettering.
