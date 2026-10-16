"""Bounded public-source collection. No model/API-key calls and no auto-publication."""
import argparse, hashlib, html, json, re, shutil, sqlite3, sys
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOCAL = ROOT / "local-curation"
ALLOWED = {"api.openalex.org","api.crossref.org","www.ebi.ac.uk","www.scielo.br","scielo.br",
 "www.nasa.gov","science.nasa.gov","www.si.edu","collectionapi.metmuseum.org",
 "revistapesquisa.fapesp.br","api.github.com","raw.githubusercontent.com",
 "ailair.akitaonrails.com"}
LIMIT = 1500000

def stamp():
    return datetime.now(timezone.utc).isoformat()

def canonical(url):
    p = urllib.parse.urlsplit(url)
    args = [(k,v) for k,v in urllib.parse.parse_qsl(p.query) if not k.lower().startswith("utm_")]
    return urllib.parse.urlunsplit((p.scheme.lower(),p.netloc.lower(),p.path,urllib.parse.urlencode(sorted(args)),""))

def safe_url(url):
    p = urllib.parse.urlsplit(url)
    if p.scheme != "https" or p.hostname not in ALLOWED or p.username or p.password or p.port not in (None,443):
        raise ValueError("URL outside approved public sources")
    return url

class Redirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        safe_url(newurl)
        return super().redirect_request(req, fp, code, msg, headers, newurl)

def get(url):
    req = urllib.request.Request(safe_url(url),headers={"User-Agent":"CerejaCurationPilot/0.1 (bounded public research)"})
    with urllib.request.build_opener(Redirect).open(req,timeout=18) as response:
        data = response.read(LIMIT+1)
        if len(data)>LIMIT:
            raise ValueError("Response exceeds text budget")
        return data

def connect():
    if shutil.disk_usage(ROOT).free < 5*1024**3:
        raise RuntimeError("Less than 5 GiB free; pause collection")
    LOCAL.mkdir(exist_ok=True)
    for folder in ["records","notes","reports","reviews","library"]:
        (LOCAL/folder).mkdir(exist_ok=True)
    db = sqlite3.connect(LOCAL/"catalog.sqlite",timeout=20)
    db.execute("CREATE TABLE IF NOT EXISTS records (id TEXT PRIMARY KEY, identity TEXT UNIQUE, payload TEXT, digest TEXT, state TEXT, updated TEXT)")
    db.execute("CREATE TABLE IF NOT EXISTS events (at TEXT, kind TEXT, payload TEXT)")
    return db

def put(db, record):
    identity = "doi:"+record["doi"].lower().replace("https://doi.org/","") if record.get("doi") else canonical(record["url"])
    key = hashlib.sha256(identity.encode()).hexdigest()[:20]
    payload = json.dumps(record,ensure_ascii=False,sort_keys=True)
    digest = hashlib.sha256(payload.encode()).hexdigest()
    existing = db.execute("SELECT digest,payload FROM records WHERE id=?",(key,)).fetchone()
    if existing:
        previous=json.loads(existing[1])
        providers=sorted(set(previous.get("providers",[previous["source"]])+[record["source"]]))
        provider_metadata=previous.get("provider_metadata",{})
        provider_metadata[record["source"]]=record
        if previous["source"]!=record["source"]:
            record={k:v for k,v in previous.items() if k not in ("providers","provider_metadata")}
        record=dict(record,providers=providers,provider_metadata=provider_metadata)
        payload=json.dumps(record,ensure_ascii=False,sort_keys=True)
        digest=hashlib.sha256(payload.encode()).hexdigest()
    else:
        record=dict(record,providers=[record["source"]],provider_metadata={record["source"]:record.copy()})
        payload=json.dumps(record,ensure_ascii=False,sort_keys=True)
        digest=hashlib.sha256(payload.encode()).hexdigest()
    if existing and existing[0]==digest:
        return False
    db.execute("INSERT INTO records VALUES (?,?,?,?,?,?) ON CONFLICT(id) DO UPDATE SET payload=excluded.payload,digest=excluded.digest,state=excluded.state,updated=excluded.updated",
               (key,identity,payload,digest,"candidate",stamp()))
    (LOCAL/"records"/(key+".json")).write_text(payload+"\n",encoding="utf-8")
    return True

def base(src,title,url,**extra):
    return dict(source=src["id"],title=title,url=url,domain=src["domain"],rights=src["rights"],content_scope="metadata_only",**extra)

def parse_feed(data, src):
    root = ET.fromstring(data)
    items = root.findall(".//item")
    if not items:
        items = root.findall(".//{http://www.w3.org/2005/Atom}entry")
    result = []
    for item in items[:3]:
        def text(name):
            element = item.find(name)
            if element is None:
                element = item.find("{http://www.w3.org/2005/Atom}"+name)
            return (element.text or "").strip() if element is not None else ""
        link = text("link")
        if not link:
            links=item.findall("{http://www.w3.org/2005/Atom}link")
            link=next((e.get("href","") for e in links if e.get("rel","alternate")=="alternate"),"")
        if link:
            result.append(base(src,html.unescape(text("title")),link,published=text("pubDate") or text("published")))
    return result

def discover(src):
    kind=src["kind"]
    if kind=="reference":
        return [base(src,src["label"],src["url"],processing="reference_only",license_url=src["license_url"])], "reference_only"
    data=get(src["url"])
    if kind=="rss_discover":
        page=data.decode("utf-8","replace")
        links=[]
        for tag in re.findall(r"<link\b[^>]*>",page,re.I):
            if re.search(r"(rss|atom)\+xml",tag,re.I):
                match=re.search(r'href=["\x27]([^"\x27]+)',tag,re.I)
                if match:
                    links.append(urllib.parse.urljoin(src["url"],html.unescape(match[1])))
        if not links:
            links=[urllib.parse.urljoin(src["url"],html.unescape(m)) for m in re.findall(r'href=["\x27]([^"\x27]*(?:feed|rss)[^"\x27]*)',page,re.I)]
        errors=[]
        for url in list(dict.fromkeys(links))[:3]:
            try:
                rows=parse_feed(get(url),src)
                if rows:
                    return rows,"feed:"+url
            except Exception as error:
                errors.append(str(error))
        raise ValueError("No verified feed: "+"; ".join(errors)[:180])
    if kind=="html":
        page=data.decode("utf-8","replace")
        match=re.search(r"<title[^>]*>(.*?)</title>",page,re.I|re.S)
        title=html.unescape(re.sub("<[^>]+>","",match[1])).strip() if match else src["label"]
        if any(x in title.lower() for x in ["just a moment","access denied","captcha","challenge"]):
            raise ValueError("Access challenge; do not bypass")
        return [base(src,title,src["url"])],"metadata_fetched"
    obj=json.loads(data)
    if kind=="openalex":
        return [base(src,x["title"],x.get("doi") or x["id"],doi=x.get("doi") or "",published=x.get("publication_date",""),open_access=x.get("open_access",{}),locations=[{"landing_page_url":p.get("landing_page_url"),"license":p.get("license")} for p in x.get("locations",[])[:3]]) for x in obj["results"][:3]],"metadata_fetched"
    if kind=="crossref":
        return [base(src,(x.get("title") or ["Untitled"])[0],x.get("URL") or "https://doi.org/"+x["DOI"],doi=x["DOI"],published=x.get("published",{}),licenses=x.get("license",[])) for x in obj["message"]["items"][:3]],"metadata_fetched"
    if kind=="europepmc":
        return [base(src,x.get("title",""),"https://europepmc.org/article/"+x["source"]+"/"+x["id"],doi=x.get("doi",""),published=x.get("firstPublicationDate",""),pmcid=x.get("pmcid",""),is_open_access=x.get("isOpenAccess","N")) for x in obj["resultList"]["result"][:3]],"metadata_fetched"
    if kind=="met":
        return [base(src,obj["title"],obj["objectURL"],artist=obj.get("artistDisplayName",""),date=obj.get("objectDate",""),is_public_domain=obj.get("isPublicDomain",False),accession=obj.get("accessionNumber",""))],"metadata_fetched"
    if kind=="github_releases":
        return [base(src,x.get("name") or x["tag_name"],x["html_url"],published=x.get("published_at",""),tag=x["tag_name"],repository="akitaonrails/ai-memory") for x in obj[:3] if not x.get("draft")],"metadata_fetched"
    if kind=="github_readme":
        return [base(src,src["label"],obj["html_url"],blob_sha=obj["sha"],content_url=src["content_url"],license_url=src["license_url"],processing="licensed_reading_eligible")],"metadata_fetched"
    raise ValueError("Unknown connector")

def collect(db, source="all"):
    config=json.loads((ROOT/"config/curation-sources.json").read_text(encoding="utf-8"))
    report={"at":stamp(),"sources":[],"changed":0,"seen":0}
    for src in config["sources"]:
        if source not in ("all",src["id"]):
            continue
        try:
            rows,status=discover(src)
            for row in rows[:config["per_source"]]:
                if report["seen"]>=config["max_candidates"]:
                    break
                report["changed"]+=int(put(db,row));report["seen"]+=1
            report["sources"].append({"id":src["id"],"status":status,"records":len(rows)})
        except Exception as error:
            report["sources"].append({"id":src["id"],"status":"blocked","reason":str(error)[:250],"records":0})
    db.execute("INSERT INTO events VALUES (?,?,?)",(stamp(),"collection",json.dumps(report,ensure_ascii=False)));db.commit()
    (LOCAL/"reports/latest-collection.json").write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding="utf-8")
    return report

def index(db):
    rows=db.execute("SELECT id,payload,state FROM records ORDER BY updated DESC").fetchall()
    lines=["# Curadoria local — índice","", "Rascunhos de pesquisa. Não são teses aprovadas. Originais e notas locais não são enviados ao GitHub.",""]
    for key,payload,state in rows:
        rec=json.loads(payload)
        lines.append("- ["+rec["title"].replace("[","(").replace("]",")")+"](notes/"+key+".md) — "+rec["source"]+" · "+state)
    for page in sorted((LOCAL/"library").glob("*.md")):
        lines.append("- [Leitura: "+page.stem+"](library/"+page.name+") — draft do curador")
    (LOCAL/"index.md").write_text("\n".join(lines)+"\n",encoding="utf-8")

def ingest_metadata(db):
    count=0
    for key,payload,state in db.execute("SELECT id,payload,state FROM records").fetchall():
        rec=json.loads(payload);dest=LOCAL/"notes"/(key+".md")
        if not dest.exists():
            title=rec["title"].replace("\n"," ")
            text="# "+title+"\n\nFonte: "+rec["url"]+"\n\nFamília: "+rec["source"]+"\n\nDireitos registrados: "+rec["rights"]+"\n\nEstado: procedência de metadados; texto integral não lido. Revisão humana pendente.\n\n## Leitura do curador\n\nPendente. Não inferir conclusões a partir do título.\n\n## Relações\n\nPropor após leitura.\n"
            dest.write_text(text,encoding="utf-8");count+=1
        if state=="candidate":
            db.execute("UPDATE records SET state='ingested_metadata' WHERE id=?",(key,))
    db.commit();index(db)
    return {"created_metadata_notes":count,"fulltext_syntheses":0}

def inbox(db):
    raw=ROOT/"raw"; report=[]
    for file in sorted(raw.iterdir()):
        if not file.is_file() or file.name=="README.md" or file.name.endswith(".source.json") or file.name.endswith(".LICENSE.txt"):
            continue
        if file.is_symlink() or getattr(file.stat(),"st_file_attributes",0)&0x400:
            report.append({"file":file.name,"state":"blocked_reparse_point"});continue
        sidecar=file.with_name(file.name+".source.json")
        if not sidecar.exists():
            report.append({"file":file.name,"state":"needs_public_source_metadata"});continue
        meta=json.loads(sidecar.read_text(encoding="utf-8"))
        if meta.get("classification")!="public" or meta.get("processing_allowed") is not True:
            report.append({"file":file.name,"state":"needs_classification_or_rights"});continue
        if file.suffix.lower() not in {".txt",".md",".pdf"} or file.stat().st_size>1048576:
            report.append({"file":file.name,"state":"deferred_size_or_format"});continue
        digest=hashlib.sha256(file.read_bytes()).hexdigest()
        changed=put(db,dict(source="manual-public",title=meta.get("title",file.stem),url=meta["url"],domain=meta.get("domain","research"),rights=meta.get("rights","unknown"),content_scope="local_original",sha256=digest,local_original=file.relative_to(ROOT).as_posix(),processing="eligible_for_agent_review"))
        report.append({"file":file.name,"state":"registered" if changed else "unchanged","sha256":digest})
    db.commit()
    (LOCAL/"reports/latest-inbox.json").write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding="utf-8")
    return report

def health(db):
    missing=[key for key, in db.execute("SELECT id FROM records") if not (LOCAL/"notes"/(key+".md")).exists()]
    total=sum(p.stat().st_size for p in LOCAL.rglob("*") if p.is_file())
    return {"missing_notes":missing,"local_bytes":total,"free_bytes":shutil.disk_usage(ROOT).free,"record_count":db.execute("SELECT count(*) FROM records").fetchone()[0],"semantic_review":"not_performed_by_script"}

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("operation",choices=["collect","ingest-metadata","inbox","health"])
    parser.add_argument("--source",default="all")
    args=parser.parse_args()
    db=connect()
    try:
        result=collect(db,args.source) if args.operation=="collect" else ingest_metadata(db) if args.operation=="ingest-metadata" else inbox(db) if args.operation=="inbox" else health(db)
        print(json.dumps(result,ensure_ascii=False,indent=2))
    finally:
        db.close()

if __name__=="__main__":
    main()
