# Flame traceability mode

Status: proposed operating mode.

Flame is an expressive design system. Most design work should stay lightweight.

For **high-impact or reusable design decisions**, Cereja can switch into a traceability mode inspired by the four-level Digital Design Werkzeuge framework.

Upstream:
https://github.com/blude/digital-design-werkzeuge

## Acknowledgement

Thanks to **Sarah Pratti (@blude)** for creating and openly publishing [Digital Design Werkzeuge](https://github.com/blude/digital-design-werkzeuge), developed in the context of her master's work, and for making the methodology available for others to study and discuss.

Its approach to layered design documentation, explicit abstraction levels and cross-level traceability helped inform Flame's optional traceability mode. Cereja's adaptation applies those ideas to its own design-system, accessibility and agentic-context needs; it is not presented as Sarah's framework or as an extension officially endorsed by her.

If you work with Digital Design, requirements or traceability, take a look at [Sarah's original project](https://github.com/blude/digital-design-werkzeuge) and follow the work at **@blude**.

## Why this matters

The useful idea is not "write four documents".

It is:

> A detailed design decision should be able to trace upward to the reason it exists.

For Flame, an animation, component state, accessibility requirement or layout constraint should be able to answer:

- what user/editorial/business goal asked for this?
- which higher-level requirement does it satisfy or refine?
- what would be affected if it changed?
- is it a true requirement, a design decision, a constraint or a derived implementation detail?

## Proposed Cereja mapping

```text
L0 — DESIGN INITIATIVE
Should we invest in this?
Example: redesign the Cereja site as a motion-rich, accessible editorial experience.

L1 — EXPERIENCE / SOLUTION CONCEPT
What must the experience achieve?
Example: discovery, reading, subscription, identity, accessibility, content reuse.

L2 — DESIGN SYSTEM / EXPERIENCE ARCHITECTURE
How is the experience structured?
Example: Flame foundations, patterns, motion families, accessibility requirements, channel behavior.

L3 — ELEMENT DESIGN
How does one element behave in enough detail to build and test?
Example: IssueHero, navigation, VisualMagazineSpread, animated reference card.
```

This is a Cereja adaptation. The upstream framework was not created specifically for Flame or design systems.

## StrictDoc pilot

The first machine-checkable pilot lives in [traceability-pilot/](traceability-pilot/README.md).

It intentionally covers only a representative L0→L3 slice. StrictDoc validates the SDoc graph; a local sensor reports graph observations; a local deterministic check requires every non-L0 requirement to resolve a path back to the L0 design initiative.

The pilot passed in GitHub Actions with StrictDoc 0.30.1. This validates the **mechanism**, not the design quality of Flame and not a decision to convert all Flame documentation into requirements.

Expansion rule: only add traceability to high-impact or reusable decisions when the graph produces useful review evidence that would otherwise be easy to miss.

## When to use traceability mode

Use for:
- a major redesign;
- a new product/surface;
- a complex interaction reused across contexts;
- a high-risk accessibility interaction;
- a component carrying business/editorial-critical behavior;
- a method we intend to test for future client work.

Do not use for:
- spacing tweaks;
- routine copy changes;
- isolated decorative experiments;
- small variants whose rationale is already obvious and local.

## Accessibility in traceability mode

Accessibility is not a single "screen-reader requirement".

Requirements should be decomposed when materially different constraints exist, for example:

```text
visual
→ contrast / text scale / reflow

non-visual
→ semantic structure / accessible names / alternative media

motor
→ keyboard / targets / no precision-only interaction

vestibular
→ reduced motion / no essential movement dependency

cognitive
→ hierarchy / labels / predictable state / error recovery

auditory
→ captions / transcripts / no audio-only instruction
```

A visually ambitious pattern can therefore remain ambitious while its different accessibility obligations stay explicit and testable.

## Relation to Flame QA

Traceability does not replace visual review, usability testing or accessibility testing.

It adds a question before implementation and review:

> **Can we explain why this design decision exists and what requirement it serves?**

That is particularly useful in agent-generated work, where plausible but unjustified UI decisions can otherwise accumulate quickly.
