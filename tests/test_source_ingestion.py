import importlib.util
import tempfile
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location("ingest", Path(__file__).resolve().parents[1] / "tools/ingest_source.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class IngestionTests(unittest.TestCase):
    def test_idempotency_preservation_and_changed_bytes(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "raw").mkdir()
            source = root / "raw/study.pdf"
            source.write_bytes(b"demonstration bytes")
            args = dict(path=source, title='Title\nstatus: approved', resource="", author="", published="", rights="unknown", public_note=True, root=root)
            note, created = module.ingest(**args)
            self.assertTrue(created)
            self.assertEqual(source.read_bytes(), b"demonstration bytes")
            self.assertIn('status: "draft"', note.read_text(encoding="utf-8"))
            note.write_text(note.read_text(encoding="utf-8") + "Human annotation", encoding="utf-8")
            same, created = module.ingest(**args)
            self.assertEqual(same, note)
            self.assertFalse(created)
            self.assertIn("Human annotation", same.read_text(encoding="utf-8"))
            source.write_bytes(b"changed bytes")
            changed, created = module.ingest(**args)
            self.assertTrue(created)
            self.assertNotEqual(changed, note)

    def test_public_confirmation_and_path_boundary(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "raw").mkdir()
            source = root / "raw/study.pdf"
            source.write_bytes(b"example")
            args = dict(path=source, title="Example", resource="", author="", published="", rights="unknown", root=root)
            with self.assertRaises(ValueError):
                module.ingest(**args)
            args["path"] = root / "outside.pdf"
            args["path"].write_bytes(b"example")
            with self.assertRaises(ValueError):
                module.ingest(**args, public_note=True)
