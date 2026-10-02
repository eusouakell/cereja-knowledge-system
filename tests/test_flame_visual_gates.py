import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VISUAL = ROOT / "brand" / "flame" / "visual-delivery"
sys.path.insert(0, str(VISUAL))

from check_html import validate_surface
from sensor_html import inspect_html


PASSING = """<!doctype html>
<html lang="pt-BR">
<head>
  <title>Flame specimen</title>
  <style>
    :root { --color-action-primary: #BE1035; }
    a:focus-visible, button:focus-visible { outline: 3px solid currentColor; }
    @keyframes enter { from { opacity: 0; } to { opacity: 1; } }
    .hero { animation: enter 160ms ease-out both; }
    @media (prefers-reduced-motion: reduce) {
      .hero { animation: none; }
    }
  </style>
</head>
<body>
  <header><nav><a href="#content">Pular para conteúdo</a></nav></header>
  <main id="content">
    <h1 class="hero">Cereja</h1>
    <img src="cover.jpg" alt="Ilustração editorial abstrata">
    <button type="button" aria-label="Assinar"></button>
  </main>
</body>
</html>
"""


class FlameVisualGateTests(unittest.TestCase):
    def test_passing_surface_clears_deterministic_gates(self):
        self.assertEqual(validate_surface(inspect_html(PASSING)), [])

    def test_missing_alt_fails(self):
        broken = PASSING.replace('alt="Ilustração editorial abstrata"', "")
        errors = validate_surface(inspect_html(broken))
        self.assertTrue(any("missing alt" in error for error in errors))

    def test_motion_without_reduced_motion_fails(self):
        broken = PASSING.replace(
            '@media (prefers-reduced-motion: reduce) {\n      .hero { animation: none; }\n    }',
            "",
        )
        errors = validate_surface(inspect_html(broken))
        self.assertTrue(any("prefers-reduced-motion" in error for error in errors))

    def test_visual_sensor_keeps_heading_jump_as_observation(self):
        observed = PASSING.replace("</h1>", "</h1><h3>Referências</h3>")
        report = inspect_html(observed)
        self.assertEqual(report["heading_jumps"], [{"from": 1, "to": 3}])
        self.assertEqual(validate_surface(report), [])


if __name__ == "__main__":
    unittest.main()
