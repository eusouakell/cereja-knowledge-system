# Flame component contract template

Status: template.

# <Component name>

## Status

- proposal / pilot / canonical / deprecated
- owner
- source/version

## Purpose

What job does this component solve?

## Use when

- 

## Do not use when

- 
- Preferred alternative:

## Fluent reference

- Fluent component/pattern:
- Adopt / Adapt / Wrap / Cereja-specific:
- Behavior retained from Fluent:
- Flame divergence:

## Anatomy

1. 
2. 

## Variants

| Variant | Use |
|---|---|
| | |

## States

- default
- hover
- pressed
- focus-visible
- disabled
- selected/checked if applicable
- loading if applicable
- error/success if applicable

## Content rules

- label:
- helper copy:
- empty/error copy:
- truncation/wrapping:
- localization:
- provenance/AI disclosure if relevant:

## Interaction

Pointer/touch behavior:

Keyboard behavior:

Focus entry/exit:

## Accessibility

- semantic element / ARIA pattern:
- accessible name:
- contrast:
- target size:
- zoom/reflow:
- assistive-tech notes:

Automated checks do not prove conformance.

## Responsive behavior

- narrow:
- standard:
- wide:
- container behavior:

## Motion

- allowed transition:
- duration token:
- reduced-motion equivalent:
- no-motion meaning preserved:

## Tokens

- color:
- type:
- spacing:
- shape:
- elevation:
- motion:

No raw visual value becomes canonical only because it appears in a prototype.

## API / implementation contract

Suggested semantic API:

```text
<Component
  variant=
  state=
  size=
  ...
/>
```

Framework-specific implementation is an adapter to this semantic contract.

## Deterministic checks

- 

## Human evals

- Flame identity
- hierarchy
- product specificity
- cognitive load
- accessibility beyond automated checks

## Anti-patterns

- 

## Examples

Good:

Bad:

## Provenance

- decision:
- evidence:
- external reference:
- human approval:
