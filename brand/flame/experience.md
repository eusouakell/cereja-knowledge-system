# Flame experience contract

Status: **v0.1 — canonical Flame instantiation**. Approved by Kell on 2026-10-06.

This document instantiates [Experience Design Principles](../experience-design-principles.md) for Cereja Flamejante.

Use it when the surface includes interaction, navigation, task completion or a visual experience that can create cognitive, accessibility or orientation costs.

For color, typography, layout, motion and components, use [DESIGN.md](DESIGN.md) and the linked Flame foundations.

## Flame experience stance

Flame is expressive, editorial and product-aware.

Expression must never make the person pay for the brand with confusion, lost control, inaccessible interaction or unnecessary cognitive load.

Canonical rule:

> **Consistency means predictable behavior and shared vocabulary, not identical composition.**

A second rule follows:

> **Expressiveness must earn attention. Remove what competes with meaning, not what creates authorship.**

## Usability in Flame

The ten usability heuristics in the Núcleo canon apply to interactive Flame surfaces.

Flame-specific interpretation:

- feedback should be visible without becoming visual noise;
- labels use human/task language, not system jargon;
- exits, undo and recovery should be obvious when consequence warrants them;
- recurring interaction jobs behave consistently even when editorial composition varies;
- prevent errors before decorating error states;
- visible context should reduce working-memory burden;
- novice clarity and expert efficiency can coexist;
- minimalism means removing competition with the task, not removing character;
- error messages name the problem and a credible next action;
- help appears near the decision that needs it.

## Information architecture

Before visual styling of a site, product or app surface, define:

- page/screen purpose;
- entry points;
- navigation model;
- primary user flows;
- return/recovery path;
- relationship between primary and secondary destinations.

A screen with no clear job is a design smell. Two screens with the same job should be challenged before both are styled.

For Cereja properties, navigation should make the current distinction understandable when relevant:

- Media;
- Lab;
- Academy;
- Studio / Products;
- personal authority surfaces owned by Kell.

Do not expose internal repository, database or organizational structure as the user's information architecture unless that structure is itself meaningful to the user.

## Interaction states

For applicable components, define the states that matter before implementation:

- default;
- hover when hover exists;
- focus;
- active/pressed;
- disabled when justified;
- loading;
- success;
- error;
- empty;
- reduced-motion behavior where movement exists.

Not every component needs every state. Missing states must be a deliberate scope decision, not an accidental omission.

### Feedback

- no silent data-changing failure;
- no ambiguous success when the user needs confirmation;
- loading feedback appears when waiting could create doubt;
- feedback should not cause avoidable re-orientation or layout instability;
- destructive actions use proportionate confirmation, undo or recovery;
- optimistic interactions need a visible failure path.

## Visual hierarchy and editorial variation

Flame's grid, semantic tokens and components create coherence.

They do **not** mandate one visual composition.

Use variation when it supports:

- editorial pacing;
- distinction between reading and action;
- surprise with meaning;
- a specific object or story;
- channel-native behavior.

Reject variation that makes controls, navigation or state unpredictable.

For editorial and social surfaces, the content object can be visually dominant. For transactional/product surfaces, task clarity and state usually outrank decorative expression.

## Progressive disclosure

Progressive disclosure is both a UX behavior and an agent-context rule.

For people:
- expose what the current decision needs;
- defer secondary complexity behind clear intent;
- never hide a requirement that will unexpectedly block completion later.

For agents:
- read the smallest relevant Flame layer;
- do not load every brand document for every task;
- follow links only when the current artifact says the concern is applicable or a conflict remains unresolved.

## Surface routing

### Editorial/social

Usually load:
- [DESIGN.md](DESIGN.md);
- [accessibility.md](accessibility.md);
- the channel/format contract;
- project-specific direction.

Apply hierarchy, legibility, accessibility, cognitive-load and authorship principles. Do not force transactional heuristics where no interaction exists.

### Website / marketing site

Add:
- this file;
- relevant navigation/IA artifact;
- component contracts;
- responsive and accessibility requirements.

### Interactive product / web app

Add:
- this file in full;
- task/user flows and acceptance criteria;
- all relevant component states;
- interaction/error/recovery requirements;
- verification plan.

### Future native/mobile app

Inherit Núcleo + Flame first. Then add a platform contract for the actual implementation target. Platform guidance specializes Flame; it does not silently replace brand or accessibility decisions.

## Enforcement matrix

| Concern | Authority | Verification |
|---|---|---|
| usability heuristics | Núcleo canon + this Flame interpretation | experience eval + human review |
| IA / primary flows | project/surface artifact under Flame | flow review; E2E when interactive |
| semantic tokens | Flame | deterministic adherence check where available |
| contrast / accessible names / semantics | Flame accessibility | automated check + review |
| keyboard / focus / recovery | Flame + project flow | E2E + human review |
| hierarchy | Flame + task intent | visual/experience eval |
| cognitive load | Flame accessibility | eval + human review |
| motion | Flame motion | deterministic reduced-motion checks where possible + eval |
| distinctiveness / authorship | Flame | distinctiveness eval + Kell gate |
| platform conventions | surface contract | platform-specific review |

A passing token or accessibility check cannot override a failed usability, hierarchy, cognitive-load or authorship review.

## Agent boundary

Agents may:

- apply this contract;
- identify a conflict;
- propose a new pattern or exception;
- generate evidence for checks/evals.

Agents may not:

- change these principles because implementation is inconvenient;
- declare a new Flame interaction pattern canonical;
- use a generic external skill to override Flame;
- treat a technical PASS as proof of product quality.

System-level changes require the governance path in [qa.md](qa.md) and Kell approval.
