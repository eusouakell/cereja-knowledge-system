import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PILOT = ROOT / "brand" / "flame" / "traceability-pilot"
sys.path.insert(0, str(PILOT))

from check import validate_graph
from sensor import parse_requirements, snapshot


class FlameTraceabilityPilotTests(unittest.TestCase):
    def setUp(self):
        text = (PILOT / "flame-pilot.sdoc").read_text(encoding="utf-8")
        self.requirements = parse_requirements(text)

    def test_graph_has_one_l0_root(self):
        report = snapshot(self.requirements)
        self.assertEqual(report["by_level"]["L0"], 1)
        self.assertEqual(report["roots"], ["FLAME-L0-EXPERIENCE"])

    def test_every_non_root_reaches_l0(self):
        self.assertEqual(validate_graph(self.requirements), [])

    def test_pilot_has_all_four_levels(self):
        report = snapshot(self.requirements)
        self.assertEqual(set(report["by_level"]), {"L0", "L1", "L2", "L3"})

    def test_sensor_observes_multiple_parent_requirements(self):
        report = snapshot(self.requirements)
        self.assertIn("FLAME-L2-MOTION", report["multi_parent_requirements"])


if __name__ == "__main__":
    unittest.main()
