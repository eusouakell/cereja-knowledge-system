# StrictDoc × Flame traceability pilot

Status: **experimental / non-canonical**.

This pilot tests whether Flame's optional L0→L3 traceability model can become machine-checkable without turning the whole design system into requirements bureaucracy.

## Scope

The pilot models a deliberately small slice:

- **L0** — expressive + accessible editorial experience;
- **L1** — reading/hierarchy and access across modes;
- **L2** — semantic tokens, purposeful motion, reduced motion and semantic structure;
- **L3** — IssueHero, Navigation and MediaFrame behavior.

The source design requirements remain in the existing Flame documentation. This folder is a traceability experiment, not a second canonical design system.

## Tool boundary

StrictDoc is used as an external validation tool. No StrictDoc source code is copied into Cereja.

Pinned pilot version: `strictdoc==0.30.1`.

StrictDoc is Apache-2.0 licensed. See the upstream project and documentation:

- https://github.com/strictdoc-project/strictdoc
- https://strictdoc.readthedocs.io/

## What is a sensor here?

`sensor.py` observes the validated graph and emits:

- requirement count;
- relation count;
- nodes by L0/L1/L2/L3;
- graph roots;
- requirements with multiple parents;
- relation density.

These values do not decide design quality.

## What is a check here?

`check.py` deterministically requires:

- non-L0 requirements to have at least one Parent;
- every Parent UID to resolve;
- every non-L0 requirement to have a path to an L0 root.

StrictDoc remains the authoritative SDoc syntax/traceability validator. The local check only asserts Cereja-specific graph invariants.

## Run

```bash
pip install strictdoc==0.30.1
strictdoc export brand/flame/traceability-pilot/flame-pilot.sdoc \
  --formats=json \
  --output-dir /tmp/flame-strictdoc
python brand/flame/traceability-pilot/sensor.py \
  brand/flame/traceability-pilot/flame-pilot.sdoc
python brand/flame/traceability-pilot/check.py \
  brand/flame/traceability-pilot/flame-pilot.sdoc
python -m unittest discover -s tests -v
```

## Success criterion

The pilot is useful if it catches a broken design-requirement relation that visual review alone would not make explicit, while remaining lightweight enough that high-impact Flame work can still move quickly.

Do not expand traceability mode to routine design changes until that value is observed.
