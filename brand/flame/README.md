# Flame — Cereja Design System

**Flame** is the design system for Cereja Flamejante.

[![Explore the Flame catalogue](assets/catalogue-banner.svg)](https://cerejaflamejante.com.br/flame/)

[Open the visual catalogue](https://cerejaflamejante.com.br/flame/). Identity, foundations, components, visual language and applications are organized in one reference. Detailed examples live in the editorial book; earlier experiments are grouped under history.

Status: **v0.1 — proposed canonical design language**.

The goal is not to turn Cereja into a generic SaaS component library. Flame treats the brand as a **digital editorial object**: part magazine, part product, part cultural artifact.

## Design intent

Cereja should feel:

- curious without being chaotic;
- expressive without becoming noisy;
- editorial without feeling old-fashioned;
- digital without looking like a generic startup;
- playful without losing rigor;
- cool without trying too hard;
- accessible by default, not retrofitted later.

The system should reflect Kell's mix of communication, product thinking, UX, technology, culture and curiosity.

## Principles

### Editorial first

Hierarchy, rhythm, typography and pacing should feel closer to a strong independent publication than to a SaaS dashboard.

### Curiosity over decoration

Visual surprise should create attention, reveal meaning or reward exploration. Decorative novelty without editorial purpose is noise.

### Controlled contrast

The identity can use sharp scale changes, asymmetry, pink/lime tension, oversized issue numbers, full-bleed moments and abrupt rhythm changes. The underlying grid, type hierarchy and accessibility rules remain disciplined.

### Motion has a job

Motion can orient, reveal, connect, confirm or create personality. It should not constantly compete with reading.

### Human before automation

Agent-generated UI must follow Flame. Flame does not follow whatever aesthetic an agent happens to prefer.

### Accessible is expressive

Accessibility is a design constraint that can increase clarity and character. It is not a reason to flatten the identity.

### Expressive across modes

The visual experience may be rich, kinetic and surprising. Accessibility is broader than a non-visual equivalent or screen-reader support.

Flame should preserve meaning, control and task completion across different ways of perceiving and operating an interface — including visual, non-visual, keyboard, touch, reduced-motion and cognitively lower-load experiences.

### Canonical accessibility principle

> **Expressão visual está no nosso DNA. Acessibilidade também. Queremos movimento, surpresa e personalidade sem sacrificar foco, orientação, compreensão, conforto sensorial ou a capacidade de concluir uma tarefa. Cool is for everyone.**

This is the canonical product principle for Flame. It expresses the design direction; the detailed accessibility requirements live in [accessibility.md](accessibility.md).

No animation, image, layout trick, sound or color treatment may be the only carrier of essential meaning or action.

## System layers

```text
PRINCIPLES
    ↓
FOUNDATIONS
color · type · spacing · grid · shape · motion
    ↓
SEMANTIC TOKENS
roles instead of raw values
    ↓
COMPONENTS
buttons · cards · navigation · tags · media
    ↓
EDITORIAL PATTERNS
issue hero · reference · signal · quote · data story
    ↓
CHANNEL PATTERNS
web · newsletter · Instagram · LinkedIn · stories
    ↓
ACCESSIBILITY + QA
```

## Start here

- [Agent-readable design language](DESIGN.md)
- [Fixed brand rules, media credits and site/catalogue separation](brand-media-rules.md)
- [Foundations and tokens](tokens.md)
- [Motion system](motion.md)
- [Components and editorial patterns](components.md)
- [Accessibility baseline](accessibility.md)
- [Reference board](references.md)
- [Fluent 2 × Cereja proposal and visual prototype](fluent-cereja.md) — scoped v0.2 proposal for review; v0.1 remains canonical until approval
- [QA and governance](qa.md)

## Current known source material

The existing website establishes a working palette and interaction baseline:

- cherry pink: `#EA1945`;
- accessible action cherry: `#BE1035`;
- lime: `#D7E25B`;
- ink: `#3A3A3A`;
- white: `#FFFFFF`.

The current website implementation uses Georgia/Times for display and Arial/Helvetica for body/UI as fallbacks. **These are implementation facts, not yet a declaration that they are the canonical brand fonts.** The original font kit should be promoted here after its canonical source is recovered and reviewed.

Do not silently substitute a trending typeface.
