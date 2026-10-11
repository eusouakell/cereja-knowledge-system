"""Create a draft provenance note; standard library only, no model calls."""
import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def ingest(path, title, resource, author, published, rights, public_note=False, root=ROOT):
    root = Path(root).resolve()
    path = Path(path).resolve()
    relative = path.relative_to(root)  # reject sources outside the checkout
    if not path.is_file():
        raise ValueError("Source must be a file")
    if relative.parts[0] not in {"raw", "examples"}:
        raise ValueError("Source must be under raw/ or examples/")
    if not public_note:
        raise ValueError("Confirm metadata and filename are safe for a public note")
    if resource and not resource.startswith(("https://", "http://")):
        raise ValueError("Resource must be an HTTP(S) URL")
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    target_dir = root / "sources"
    target_dir.mkdir(exist_ok=True)
    destination = target_dir / f"source-{digest}.md"
    if destination.exists():
        return destination, False
    metadata = {
        "type": "source", "status": "draft", "title": title,
        "source_file": relative.as_posix(), "sha256": digest,
        "resource": resource or "unknown", "author": author or "unknown",
        "published": published or "unknown",
        "ingested": datetime.now(timezone.utc).isoformat(),
        "rights": rights, "extraction_status": "not_attempted",
        "certainty": "unverified", "tags": ["study-curation"],
    }
    # JSON scalar syntax is valid YAML; quoted values prevent metadata injection.
    frontmatter = "\n".join(f"{key}: {json.dumps(value, ensure_ascii=False)}"
                            for key, value in metadata.items())
    body = ("\n\n# Registro de procedência\n\n"
            "Nota criada automaticamente; metadados informados ainda não verificados.\n\n"
            f"Original: [{relative.name}](../{relative.as_posix()}). "
            "O link local pode não estar disponível no repositório público.\n\n"
            "## Revisão humana\n\n"
            "- [ ] Conferir autoria, publicação, URL e direitos.\n"
            "- [ ] Registrar método, população/escopo e limitações quando aplicáveis.\n"
            "- [ ] Vincular afirmações aos trechos ou páginas da fonte.\n\n"
            "## Notas de leitura\n\nAinda não preenchidas.\n\n"
            "## Relações\n\nConectar conceitos e perguntas após leitura e revisão.\n\n"
            "A ingestão não aprova evidência, cria tese ou autoriza publicação.\n")
    with destination.open("x", encoding="utf-8") as output:
        output.write(f"---\n{frontmatter}\n---{body}")
    return destination, True


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path)
    parser.add_argument("--title", required=True)
    parser.add_argument("--resource", default="")
    parser.add_argument("--author", default="")
    parser.add_argument("--published", default="")
    parser.add_argument("--rights", required=True)
    parser.add_argument("--public-note", action="store_true",
                        help="Confirm the metadata and filename may be published")
    args = parser.parse_args()
    try:
        note, created = ingest(**vars(args))
    except (ValueError, OSError) as error:
        parser.exit(1, f"Ingestion failed: {error}\n")
    print(f"{'created' if created else 'existing'}: {note.relative_to(ROOT)}")


if __name__ == "__main__":
    main()

