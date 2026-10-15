"""Local helper for the agent-led wiki experiment. No model calls or synthesis."""
import argparse
import hashlib
import json
import re
from pathlib import Path
from ingest_source import ingest


def scan(root):
    result = []
    for path in sorted((root / 'raw').glob('*.md')):
        note, created = ingest(path, path.stem, '', 'Fixture fictícia própria', '',
                               'Material demonstrativo próprio', public_note=True, root=root)
        result.append({'source': path.relative_to(root).as_posix(),
                       'note': note.relative_to(root).as_posix(), 'created': created})
    return result


def check(root):
    errors = []
    notes = list((root / 'sources').glob('source-*.md'))
    for source in sorted((root / 'raw').glob('*.md')):
        digest = hashlib.sha256(source.read_bytes()).hexdigest()
        note = root / 'sources' / ('source-' + digest + '.md')
        if not note.exists():
            errors.append('Unprocessed source: ' + source.name)
    for note in notes:
        text = note.read_text(encoding='utf-8')
        fields = dict(re.findall(r'^([a-z_0-9]+): (.+)$', text, re.M))
        source = (root / json.loads(fields['source_file'])).resolve()
        if not source.is_relative_to(root.resolve()):
            errors.append('Source outside vault: ' + str(note))
        elif not source.is_file() or hashlib.sha256(source.read_bytes()).hexdigest() != json.loads(fields['sha256']):
            errors.append('Changed or missing original: ' + str(note))
    for page in root.rglob('*.md'):
        for target in re.findall(r'(?<!!)\[[^\]]*\]\(([^)]+)\)', page.read_text(encoding='utf-8')):
            if re.match(r'^[a-z]+:', target) or target.startswith('#'):
                continue
            target_path = (page.parent / target.split('#')[0]).resolve()
            if not target_path.is_relative_to(root.resolve()) or not target_path.is_file():
                errors.append('Broken/escaping link: ' + page.name + ' -> ' + target)
    for name in ['index.md', 'log.md', 'AGENTS.md']:
        if not (root / name).is_file():
            errors.append('Missing: ' + name)
    if not list((root / 'wiki').glob('*.md')):
        errors.append('No wiki pages: provenance alone is not a wiki')
    return errors


def search(root, query):
    tokens = set(query.casefold().split())
    hits = []
    paths = [root / 'index.md'] + sorted((root / 'wiki').glob('*.md'))
    for path in paths:
        if not path.is_file():
            continue
        for number, line in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
            if any(token in line.casefold() for token in tokens):
                hits.append(f'{path.relative_to(root).as_posix()}:{number}: {line}')
    return hits


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('operation', choices=['ingest', 'check', 'search'])
    parser.add_argument('--vault', required=True, type=Path)
    parser.add_argument('--query', default='')
    args = parser.parse_args()
    root = args.vault.resolve()
    if not root.is_dir():
        parser.error('Vault must exist')
    if args.operation == 'ingest':
        print(json.dumps(scan(root), ensure_ascii=False, indent=2))
    elif args.operation == 'check':
        errors = check(root)
        print(json.dumps({'structural_check': 'FAIL' if errors else 'PASS', 'errors': errors}, ensure_ascii=False))
        raise SystemExit(bool(errors))
    else:
        if not args.query.strip():
            parser.error('Search requires --query')
        print('\n'.join(search(root, args.query)) or 'No lexical match; consult index before concluding absence.')


if __name__ == '__main__':
    main()
