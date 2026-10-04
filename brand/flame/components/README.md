# Flame components

Status: **architecture in progress**.

Flame uses Fluent 2 as a behavior/component reference, not as a visual template.

Start with:

- [Fluent 2 × Flame component coverage audit](../fluent-component-coverage.md)
- [Component contract template](component-contract-template.md)
- [Button / Action control — pilot](button.md)

## Rule

A component enters the canonical system only after its contract covers behavior, states, accessibility, content, responsive behavior, tokens and implementation semantics.

A screenshot or CSS class is not a component definition.

## Composition hierarchy

```text
foundations
  ↓
primitives
  ↓
controls / surfaces / feedback
  ↓
Cereja-specific organisms
  ↓
templates
  ↓
products
```

Flame-specific organisms may wrap stable primitives without inheriting Fluent's visual identity.
