# Flame visual delivery

Status: **experimental controls**.

This folder separates three questions that screenshot-to-code systems often collapse:

1. **Does it look close?** → sensor.
2. **Does it preserve deterministic semantic/accessibility invariants?** → check.
3. **Does it solve the right editorial/design problem in a Cereja way?** → human Flame gate.

## Files

- `reference-evaluation.md` — external pattern review and adoption boundary;
- `sensor_html.py` — observations from self-contained HTML;
- `check_html.py` — deterministic semantics/accessibility gates;
- `specimen.html` — minimal CI specimen, not a canonical template.

## Run

```bash
python brand/flame/visual-delivery/sensor_html.py \
  brand/flame/visual-delivery/specimen.html

python brand/flame/visual-delivery/check_html.py \
  brand/flame/visual-delivery/specimen.html

python -m unittest discover -s tests -v
```

## Principle

**Visual fidelity can ask for another iteration. It cannot waive semantics or accessibility.**
