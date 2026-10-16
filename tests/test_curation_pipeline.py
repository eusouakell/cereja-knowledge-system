import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

spec=importlib.util.spec_from_file_location("curation",Path(__file__).resolve().parents[1]/"tools/curation_pipeline.py")
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)

class CurationTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
        self.oldroot,self.oldlocal=m.ROOT,m.LOCAL
        self.addCleanup(lambda: (setattr(m,"ROOT",self.oldroot),setattr(m,"LOCAL",self.oldlocal)))
        m.ROOT=Path(self.tmp.name);m.LOCAL=m.ROOT/"local-curation";(m.ROOT/"raw").mkdir()
        self.db=m.connect();self.addCleanup(self.db.close)

    def record(self,source="openalex",url="https://doi.org/10.1234/example"):
        return dict(source=source,title="Example",url=url,doi="10.1234/example",rights="metadata",domain="research",content_scope="metadata_only")

    def test_duplicate_and_two_provider_provenance(self):
        self.assertTrue(m.put(self.db,self.record()))
        self.assertFalse(m.put(self.db,self.record()))
        self.assertTrue(m.put(self.db,self.record("crossref")))
        self.assertFalse(m.put(self.db,self.record("crossref")))
        rows=self.db.execute("SELECT payload FROM records").fetchall()
        self.assertEqual(1,len(rows));self.assertEqual(["crossref","openalex"],json.loads(rows[0][0])["providers"])
        self.assertFalse(m.put(self.db,self.record()))

    def test_metadata_ingestion_preserves_curator_text(self):
        m.put(self.db,self.record());m.ingest_metadata(self.db)
        note=next((m.LOCAL/"notes").glob("*.md"));note.write_text(note.read_text(encoding="utf-8")+"\nCurator annotation\n",encoding="utf-8")
        self.assertEqual(0,m.ingest_metadata(self.db)["created_metadata_notes"])
        self.assertIn("Curator annotation",note.read_text(encoding="utf-8"))
        self.assertEqual([],m.health(self.db)["missing_notes"])

    def test_unclassified_raw_not_read_or_registered(self):
        raw=m.ROOT/"raw/file.md";raw.write_text("Private data",encoding="utf-8")
        result=m.inbox(self.db)
        self.assertEqual("needs_public_source_metadata",result[0]["state"])
        self.assertEqual(0,self.db.execute("SELECT count(*) FROM records").fetchone()[0])

    def test_classified_small_source_is_registered(self):
        raw=m.ROOT/"raw/file.md";raw.write_text("Public fixture",encoding="utf-8")
        raw.with_name("file.md.source.json").write_text(json.dumps(dict(classification="public",processing_allowed=True,title="Example",url="https://example.org/source",rights="Own fixture")),encoding="utf-8")
        self.assertEqual("registered",m.inbox(self.db)[0]["state"])
        self.assertEqual("unchanged",m.inbox(self.db)[0]["state"])

    def test_domain_guard(self):
        for url in ["http://api.openalex.org/works","https://127.0.0.1/","https://api.openalex.org:8443/","https://user:pass@api.openalex.org/"]:
            with self.assertRaises(ValueError):m.safe_url(url)
        self.assertEqual("https://api.openalex.org/works",m.safe_url("https://api.openalex.org/works"))

    def test_url_tracking_normalization(self):
        self.assertEqual("https://example.org/a?q=1",m.canonical("https://example.org/a?utm_source=x&q=1#frag"))

if __name__=="__main__":unittest.main()
