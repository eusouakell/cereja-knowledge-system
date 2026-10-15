import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parents[1] / 'tools'
sys.path.insert(0, str(TOOLS))
import wiki_lab


class WikiLabTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / 'raw').mkdir()
        (self.root / 'wiki').mkdir()
        for name in ['index.md', 'log.md', 'AGENTS.md']:
            (self.root / name).write_text('# Demo\n', encoding='utf-8')
        (self.root / 'wiki/topic.md').write_text('[Source](../raw/source.md)\n', encoding='utf-8')
        (self.root / 'raw/source.md').write_text('# Source\nVersion one\n', encoding='utf-8')

    def test_new_source_idempotency_and_reading_preservation(self):
        self.assertTrue(any('Unprocessed' in e for e in wiki_lab.check(self.root)))
        first = wiki_lab.scan(self.root)
        note = self.root / first[0]['note']
        note.write_text(note.read_text(encoding='utf-8') + '\nReading annotation\n', encoding='utf-8')
        second = wiki_lab.scan(self.root)
        self.assertFalse(second[0]['created'])
        self.assertIn('Reading annotation', note.read_text(encoding='utf-8'))
        self.assertEqual([], wiki_lab.check(self.root))

    def test_changed_original_and_broken_link_fail(self):
        wiki_lab.scan(self.root)
        (self.root / 'raw/source.md').write_text('Changed original', encoding='utf-8')
        (self.root / 'wiki/topic.md').write_text('[Missing](missing.md)', encoding='utf-8')
        errors = wiki_lab.check(self.root)
        self.assertTrue(any('Changed or missing original' in e for e in errors))
        self.assertTrue(any('Broken/escaping link' in e for e in errors))

    def test_provenance_without_wiki_is_incomplete(self):
        wiki_lab.scan(self.root)
        (self.root / 'wiki/topic.md').unlink()
        self.assertTrue(any('provenance alone' in e for e in wiki_lab.check(self.root)))

    def test_search_is_lexical_and_does_not_invent_answer(self):
        self.assertEqual([], wiki_lab.search(self.root, 'price'))
        self.assertTrue(any('topic.md:1:' in h for h in wiki_lab.search(self.root, 'source')))


if __name__ == '__main__':
    unittest.main()
