# Flame — Cereja Design System

**Flame** is the design system for Cereja Flamejante.

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

### Beauty must have a non-visual equivalent

The visual experience may be rich, kinetic and surprising. The semantic experience must remain complete, ordered and efficient without vision.

**Beautiful for people who can see it; complete and practical for people using a screen reader.**

No animation, image, layout trick or color treatment may carry essential meaning that disappears from the accessibility tree.

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
- [Foundations and tokens](tokens.md)
- [Motion system](motion.md)
- [Components and editorial patterns](components.md)
- [Accessibility baseline](accessibility.md)
- [Reference board](references.md)
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
