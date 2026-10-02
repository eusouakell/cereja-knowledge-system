# Flame components & editorial patterns

Flame distinguishes **UI primitives** from **editorial organisms**.

The system should not force editorial content into generic product cards.

## Core primitives

### Button

Variants:
- primary action;
- secondary/outline;
- quiet/text;
- on-dark/on-accent.

Requirements:
- clear focus state;
- minimum useful target size;
- loading/disabled states when applicable;
- no motion required to understand status.

### TextLink

Links remain visually identifiable. Do not rely only on color for inline long-form links.

### Navigation

Desktop and mobile patterns may differ structurally. Preserve:
- current location;
- keyboard order;
- clear subscription/action priority;
- skip-to-content support.

### Tag

For taxonomy, state or issue metadata.

Pill form is permitted here because tags are compact semantic units.

### MediaFrame

Supports:
- image;
- illustration;
- screenshot;
- video;
- animation.

Must carry rights/provenance and alt/caption behavior.

## Editorial components

### IssueCard

An IssueCard is not a generic Card.

Anatomy:

```text
issue.number
issue.date
issue.domain
issue.title
issue.summary
issue.artwork?
issue.status?
```

It may change composition across grid positions while preserving semantic anatomy.

### FeatureStory

Large editorial emphasis:
- eyebrow/meta;
- title;
- standfirst;
- optional artwork;
- primary reading action.

### ReferenceCard

Used for book, paper, film, tool, cultural object or external source.

Anatomy:
- type;
- title;
- creator/source;
- why it matters;
- optional visual;
- provenance/link.

### SignalCard

Small observed change or interesting event.

Do not visually imply certainty beyond the source.

### QuoteBlock

Quotes should distinguish:
- direct quotation;
- Kell interpretation;
- source attribution.

### DataCallout

A number or chart fragment needs:
- metric;
- unit;
- timeframe;
- population/scope when relevant;
- source;
- interpretation kept separate.

## Editorial organisms

### IssueHero

Cover-like opening with strong typographic scale and one dominant art-direction move.

### CulturalConnection

Visually connects two or more references that become meaningful together.

### EvidenceStack

Groups claim + evidence + caveat/provenance without making the newsletter look like a research paper.

### VisualMagazineSpread

Instagram-native composition. Uses the same content evidence but can vary:
- cover;
- signal;
- context;
- connection;
- reference;
- interpretation;
- exit question.

### ResearchDesk

Stories/social pattern for provisional research artifacts:
- link;
- image;
- note;
- poll;
- "why I saved this".

## Component rule

Before adding a new component, ask:

1. Is this a genuinely repeated semantic structure?
2. Can an existing component take a new variant?
3. Does the component carry meaning that should survive across channels?
4. What accessibility states does it require?
5. Does it need a content schema in Núcleo?
