# Flame distinctiveness gate

Status: **proposed semantic/human eval**.

Purpose: detect when a technically competent interface or editorial composition looks generic, template-driven or like the default aesthetic of a general-purpose generator.

This gate does not ask whether AI was used.

It asks:

> Does this surface express a specific Cereja product/editorial decision, or could it belong to almost any startup/newsletter after swapping logo and colors?

## 1. Product specificity

Every major surface should reveal what the product is for.

Look for:
- real editorial/research objects;
- real states;
- real actions;
- real provenance;
- real content hierarchy.

Flag:
- generic dashboard shells with placeholder metrics;
- generic three-card feature blocks;
- hero + three cards + CTA as an automatic page recipe;
- components added because a design-system catalogue had them rather than because the product needs them.

## 2. Visual hierarchy with opinion

A page should not distribute visual weight democratically.

Flag:
- every card equally important;
- every section starting with the same eyebrow + heading + paragraph pattern;
- every surface having the same radius/shadow treatment;
- every interaction using the same accent;
- page rhythm that can be described as repeated modules with no editorial interruption.

Flame may be asymmetric when hierarchy stays clear.

## 3. Fluent without Microsoft cosplay

Fluent is a behavior/reference system.

Flag:
- visual cloning of Fluent/Microsoft product surfaces;
- Segoe-like visual assumptions becoming identity by accident;
- Fluent component anatomy used when a simpler native pattern fits;
- Fluent cards/surfaces taking over the editorial language.

Ask:
- what solved behavior are we borrowing?
- what is Flame's visual/content divergence?
- could we replace the cherry color with blue and mistake this for a Microsoft app?

If yes, revise.

## 4. Anti-SaaS defaults

Treat these as warning patterns when they accumulate:

- bento for unrelated information;
- glassmorphism;
- purple/blue AI gradients;
- excessive pills;
- excessive rounded cards;
- icon + title + body repeated across every feature;
- giant centered headline followed by generic product cards;
- decorative charts/metrics with no real analytical job;
- unnecessary shadows on every surface;
- chat bubbles used as shorthand for "AI".

Any one can be valid. The cluster is the problem.

## 5. Component rationale

For each component in a screen:

- what task does it solve?
- why this component and not a simpler one?
- what state does it need?
- what happens on mobile/keyboard?
- what does Cereja add beyond the base primitive?

If the answer is only "it looks good", the component is not mature.

## 6. Image authorship

Flame should not converge on one synthetic-image aesthetic.

A healthy visual system can mix, with rights/provenance:

- photography;
- archival/reference imagery;
- screenshots;
- scans/textures;
- diagrams/data;
- commissioned illustration;
- generative conceptual art.

Flag:
- one AI-collage style across unrelated stories;
- generative imagery used as evidence;
- repeated visual motifs because they are easy to prompt;
- image choices that could belong to any "AI + culture" brand.

Per-issue art direction may vary while brand framing remains recognizable.

## 7. Brand asset integrity

Fixed identity is not generative material.

Hard fail:
- regenerated logo/flame;
- distorted/rotated canonical signature;
- synthetic reconstruction replacing the approved asset;
- unapproved font/identity substitution.

The rejected generative flame from the v0.2 exploration is a useful precedent: generation capability does not grant brand authority.

## 8. Typography

Flag:
- generic giant-serif-plus-neutral-sans used as a complete identity by itself;
- identical display scale on every surface;
- decorative negative tracking that harms accents/readability;
- UI typography inheriting editorial display behavior;
- fallback fonts being treated as final brand typography without a decision.

Typography should carry role, rhythm and content — not merely signal "editorial website".

## 9. Motion

Flag:
- everything enters on scroll;
- identical fade/slide choreography repeated everywhere;
- motion whose only job is to look premium;
- multiple simultaneous attention grabs;
- spring/easing copied from references without product reason.

Prefer:
- one dominant movement;
- state/orientation/reveal/connection/confirmation;
- fast interactive feedback;
- slower editorial choreography;
- meaningful reduced-motion equivalent.

## 10. Content/layout coupling

Generic UI often appears when real content enters late.

Review with actual:
- issue titles;
- source lines;
- long Portuguese strings;
- images of different ratios;
- empty states;
- errors;
- agent/tool states;
- provenance;
- real archive depth.

A layout that only works with ideal placeholder copy is not Flame-ready.

## 11. Channel divergence

Shared DNA does not mean cloned layouts.

- public site → reading/discovery/subscription;
- Instagram/social → visual editorial sequence;
- GitHub → lab/documentation/evidence;
- research/editorial apps → task completion and inspection.

Flag cross-channel repetition that exists only because one composition was easy to reuse.

## 12. AI/product states

Agentic interfaces need explicit states that generic mockups often omit:

- queued;
- researching;
- tool call;
- partial result;
- source missing/stale;
- permission denied;
- check failed;
- human approval required;
- retry budget exhausted;
- completed with uncertainty.

A magic "Generate" button followed by a polished answer is not enough.

## Review result

Use:

- **PASS** — specific product/brand decisions dominate.
- **REVISE — PRODUCT** — UI is generic because product tasks/states are underspecified.
- **REVISE — SYSTEM** — component/tokens/state architecture is weak.
- **REVISE — ART DIRECTION** — imagery/type/composition feels generic or synthetic.
- **REVISE — MOTION** — movement is decorative/template-driven.
- **REVISE — CHANNEL** — same composition is being cloned across surfaces.

## Review record

Surface/version:
Reviewer:
Product task:
Flame sources:
Fluent references:

Specific decisions that should survive:
- 

Generic/template patterns:
- 

Missing real states/content:
- 

Decision:
- 

Suggested intervention:
- 

Human gate:
- canonical Flame change remains Kell-approved.
