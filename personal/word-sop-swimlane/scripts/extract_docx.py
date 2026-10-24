"""Extract DOCX body blocks and embedded images with their evidence context."""

import argparse
import hashlib
import json
import posixpath
from pathlib import Path
import xml.etree.ElementTree as ET
import zipfile

W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
A = '{http://schemas.openxmlformats.org/drawingml/2006/main}'
R = '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}'
V = '{urn:schemas-microsoft-com:vml}'


def extract(source, output):
    """Write ordered paragraph/table evidence and original media into a new folder."""
    if output.exists():
        raise FileExistsError(f'Output directory already exists: {output}')
    with zipfile.ZipFile(source) as archive:
        document = ET.fromstring(archive.read('word/document.xml'))
        rels = ET.fromstring(archive.read('word/_rels/document.xml.rels'))
        relations = {item.get('Id'): item for item in rels}
        media = {}
        for index, name in enumerate(sorted(n for n in archive.namelist() if n.startswith('word/media/') and not n.endswith('/')), 1):
            data = archive.read(name)
            media[name] = {
                'id': f'image-{index:03d}', 'package_path': name,
                'file': f'images/image-{index:03d}{Path(name).suffix}',
                'sha256': hashlib.sha256(data).hexdigest(), 'bytes': len(data),
                'blocks': [],
            }
        blocks = []

        def paragraph(element, context=None):
            text = ''.join(e.text or '' if e.tag == W + 't' else '\n' if e.tag == W + 'br' else '\t' for e in element.iter() if e.tag in (W + 't', W + 'br', W + 'tab'))
            references = []
            for e in element.iter():
                rid = e.get(R + 'embed') or e.get(R + 'link') if e.tag == A + 'blip' else e.get(R + 'id') if e.tag == V + 'imagedata' else None
                if not rid:
                    continue
                rel = relations.get(rid)
                if rel is None:
                    references.append({'relationship': rid, 'missing': True})
                    continue
                target = rel.get('Target', '')
                if rel.get('TargetMode') == 'External':
                    references.append({'relationship': rid, 'external': target})
                    continue
                name = posixpath.normpath(posixpath.join('word', target)) if not target.startswith('/') else target.lstrip('/')
                references.append({'relationship': rid, 'image_id': media[name]['id']} if name in media else {'relationship': rid, 'unsupported_part': name})
            block = {'id': f'block-{len(blocks)+1:04d}', 'text': text, 'images': references}
            if context:
                block['table_cell'] = context
            blocks.append(block)
            for ref in references:
                if 'image_id' in ref:
                    next(item for item in media.values() if item['id'] == ref['image_id'])['blocks'].append(block['id'])

        def walk(container, prefix=''):
            for child in container:
                if child.tag == W + 'p':
                    paragraph(child, prefix or None)
                elif child.tag == W + 'tbl':
                    table = len(blocks) + 1
                    for row_index, row in enumerate(child.findall(W + 'tr'), 1):
                        for cell_index, cell in enumerate(row.findall(W + 'tc'), 1):
                            walk(cell, f'{prefix}/table-{table}/row-{row_index}/cell-{cell_index}')
                elif child.tag in (W + 'sdt', W + 'sdtContent'):
                    walk(child, prefix)

        walk(document.find(W + 'body'))
        output.mkdir(parents=True)
        (output / 'images').mkdir()
        for name, item in media.items():
            (output / item['file']).write_bytes(archive.read(name))
        manifest = {'source': str(source.resolve()), 'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(), 'blocks': blocks, 'images': list(media.values()), 'scope': 'Main document body including tables; headers, footers and chart rendering are not extracted.'}
        (output / 'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding='utf-8')
        lines = ['# DOCX evidence extraction', '']
        for block in blocks:
            lines += [f'## {block["id"]}', block.get('table_cell', ''), block['text']]
            for ref in block['images']:
                if 'image_id' in ref:
                    item = next(item for item in media.values() if item['id'] == ref['image_id'])
                    lines.append(f'![{item["id"]}]({item["file"]})')
                else:
                    lines.append('Image reference: ' + json.dumps(ref, ensure_ascii=False))
            lines.append('')
        (output / 'document.md').write_text('\n'.join(lines), encoding='utf-8')
        return manifest


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', required=True, type=Path)
    parser.add_argument('--out', required=True, type=Path)
    args = parser.parse_args()
    result = extract(args.input, args.out)
    print(f'Extracted {len(result["blocks"])} blocks and {len(result["images"])} media files.')
