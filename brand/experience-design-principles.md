# Experience Design Principles

Status: **v0.1 — canonical for the Cereja system**. Approved by Kell on 2026-10-06.

## Purpose

Define durable experience principles that remain valid across websites, interactive products and future applications.

This document is intentionally **brand-neutral in wording**. It belongs to Núcleo because it records the durable principles and source boundaries that Flame and project-specific contracts instantiate.

It is not a component library, channel playbook or agent prompt.

## Authority order

For experience work, use the smallest applicable context in this order:

```text
EXPERIENCE DESIGN PRINCIPLES
        ↓
FLAME EXPERIENCE CONTRACT
        ↓
SURFACE / PLATFORM CONTRACT
        ↓
PROJECT OR TASK ARTIFACT
        ↓
AGENT / SKILL / TOOL
```

Lower layers may specialize higher ones. They may not silently contradict them.

External skills and benchmarks are execution or research aids. They are never the canonical authority.

## Usability heuristics

Use Nielsen's ten heuristics as review lenses, adapted here in Cereja's own wording.

1. **System status is visible.** A person should be able to tell what is happening, what changed and whether an action succeeded.
2. **The interface speaks the user's language.** Organize and label around real tasks and concepts, not implementation structure.
3. **People retain control.** Provide exits, cancellation, undo or recovery when the interaction makes them relevant.
4. **Consistency reduces cognitive load.** The same job should behave and be named consistently. Consistency does not require identical composition.
5. **Prevent avoidable errors.** Prefer constraints, clear choices and validation before failure.
6. **Prefer recognition over recall.** Keep relevant options, context and requirements visible rather than demanding memory of hidden state.
7. **Support both learning and efficiency.** A new user should have a clear path; recurrent users may benefit from shortcuts and efficient defaults.
8. **Every element must earn attention.** Remove competition with meaning and task completion without flattening useful expression or authorship.
9. **Errors support diagnosis and recovery.** Explain what happened in human language and provide a credible next step.
10. **Help is contextual.** When explanation is necessary, place it close to the task and make it actionable.

A heuristic finding is not automatically a defect. The review must state the context, consequence and recommended action.

## Information architecture

Define purpose and movement before styling an interactive surface.

For each page, screen or major state, answer:

- What is this for?
- How did the person get here?
- What is the primary path?
- What can they do next?
- How do they leave, return or recover?
- Where would they reasonably expect to find this?

Prefer:

- task and mental-model organization over internal schema;
- shallow, findable structures;
- one obvious primary route per goal;
- stable navigation and naming;
- progressive disclosure of secondary complexity;
- reading and focus order that remain coherent without visual rearrangement.

Primary flows should be concrete enough to become acceptance criteria or tests when the surface is interactive.

## Interaction and feedback

Interactive surfaces should make consequence and state legible.

- interactive elements must look and behave interactive;
- data-changing actions need appropriate success and failure feedback;
- destructive or irreversible actions need prevention, confirmation, undo or another proportionate safeguard;
- loading feedback should appear when latency becomes perceptible or could create uncertainty;
- optimistic feedback is acceptable only when failure can be visibly reconciled or rolled back;
- empty, error, loading, success and disabled states are part of the experience, not implementation leftovers;
- progressive disclosure should reduce cognitive load without hiding essential requirements or state.

Do not canonize a single latency threshold, animation duration or implementation pattern as universal UX truth.

## Visual hierarchy

Importance should map to prominence.

Use size, weight, contrast, position, alignment and space to make sequence and priority understandable.

Consistency exists to reduce cognitive load. Variation is appropriate when it communicates meaning, editorial rhythm or brand authorship.

A surface can comply with tokens and still fail hierarchy. Mechanical conformance and design judgment are separate checks.

## Accessibility

Accessibility is a baseline condition of the experience, not a later feature.

For production web interfaces, the Cereja system uses **WCAG 2.2 AA** as the minimum conformance target, complemented by usability and cognitive/sensory review.

The applicable contract must consider, as relevant:

- semantic structure;
- keyboard and non-pointer operation;
- visible focus;
- contrast and non-color cues;
- zoom, reflow and text scaling;
- meaningful alternatives for visual/audio media;
- target size and motor accessibility;
- reduced motion and vestibular safety;
- understandable labels and status;
- cognitive load and working-memory demand.

Automated accessibility checks do not prove that an experience is understandable or comfortable.

## Design systems

A design system provides reusable vocabulary and constraints.

- use semantic tokens instead of arbitrary values where a token exists;
- recurring interaction jobs should use stable component behavior;
- a new pattern should exist because the job is genuinely different, not because a screen wanted novelty;
- design consistency must not collapse all editorial or expressive surfaces into one template.

Brand-specific tokens, components and motion belong to Flame, not this document.

## Verification model

Every important rule should declare how it is defended.

| Type | Meaning | Typical verification |
|---|---|---|
| **Principle** | durable decision that guides judgment | eval + human review |
| **Guideline** | contextual recommendation | review, may allow justified exception |
| **Guard** | pre-execution constraint | deterministic rule or explicit gate |
| **Check** | machine-verifiable condition | automated test/check |
| **Eval** | structured semantic judgment | independent reviewer/model + evidence |
| **Human gate** | accountable decision | explicit approval |

Do not convert subjective design quality into a fake deterministic check.

A rule with no verification mechanism remains guidance; that is acceptable when its nature is judgment-based, but the system should say so explicitly.

## Applicability by surface

Not every principle applies with the same weight everywhere.

| Concern | Website | Interactive web app | Mobile/native app | Social/editorial asset |
|---|---:|---:|---:|---:|
| visual hierarchy | high | high | high | high |
| accessibility | high | high | high | high, surface-appropriate |
| information architecture | high | high | high | limited |
| status and feedback | contextual | high | high | not usually applicable |
| user control / recovery | contextual | high | high | not usually applicable |
| error prevention | forms/tasks | high | high | not usually applicable |
| recognition over recall | high | high | high | useful |
| cognitive load | high | high | high | high |
| brand/editorial authorship | high | contextual | contextual | high |

Platform-specific patterns belong in a surface contract. Future mobile work should add Apple HIG, Material Design or other platform guidance only when a real product requires it.

## Progressive disclosure for agentic context

Agents should not receive the entire design system by default.

Load context progressively:

1. task intent and approved artifact;
2. this canon only when experience principles are relevant;
3. Flame contract when the work is for Cereja;
4. only the surface/platform file required by the task;
5. only the component, channel or project contract being changed;
6. execution skill last.

If a narrower artifact already resolves a decision, do not re-open higher-level strategy unless a conflict is detected.

## Sources and provenance

Primary references:

- Nielsen Norman Group, *10 Usability Heuristics for User Interface Design*: https://www.nngroup.com/articles/ten-usability-heuristics/
- W3C, WCAG 2.2: https://www.w3.org/TR/WCAG22/
- W3C, COGA — *Making Content Usable for People with Cognitive and Learning Disabilities*: https://www.w3.org/TR/coga-usable/

Architecture benchmark reviewed:

- Databricks Solutions, Consort `ui-ux-design-principles`: https://github.com/databricks-solutions/consort/tree/main/skills/ui-ux-design-principles

The Consort repository uses a Databricks-specific license. No Consort text, code or internal artifact is incorporated here. Its public structure was reviewed only as an architectural benchmark; the principles and wording in this document are Cereja's own synthesis from the cited public design standards and prior internal decisions.
