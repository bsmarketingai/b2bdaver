#!/usr/bin/env python3
"""Statický export canvasu Daver (.dc.html) do HTML stránek pro web / GitHub Pages.

Použití: python3 export.py <složka s .dc.html> <manifest.json> <výstupní složka>
- Main.dc.html -> index.html, ostatní stránky -> <Název>.html
- šablony se převedou na JSON strom, logika se spustí runtimem dc/dc-runtime.js (Preact)
- /_blob/<id> se nahradí cestou z assets/manifest.json (assets/…)
"""
import json, os, re, sys
from html.parser import HTMLParser

SRC, MANIFEST, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'source', 'track', 'wbr'}
SVG_VOID = {'path', 'circle', 'rect', 'line', 'polyline', 'polygon', 'ellipse', 'use', 'stop'}
ATTR_RE = re.compile(r'''([^\s"'>/=]+)(?:\s*=\s*(?:"([^"]*)"|'([^']*)'|([^\s>]+)))?''')


class TplParser(HTMLParser):
    """Lenient parser bez foster-parentingu (sc-for v <tbody> zůstane na místě), zachovává velikost písmen atributů."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = ['#root', [], []]
        self.stack = [self.root]

    def _attrs(self):
        raw = self.get_starttag_text()
        m = re.match(r'<\s*[^\s>/]+', raw)
        body = raw[m.end():].rstrip('>').rstrip('/')
        out = []
        for a in ATTR_RE.finditer(body):
            name = a.group(1)
            v = a.group(2) if a.group(2) is not None else a.group(3) if a.group(3) is not None else a.group(4)
            import html as _h
            out.append([name, _h.unescape(v) if v is not None else ''])
        return out

    def handle_starttag(self, tag, attrs):
        el = [tag, self._attrs(), []]
        self.stack[-1][2].append(el)
        if tag not in VOID and not (tag in SVG_VOID and self.get_starttag_text().rstrip().endswith('/>')):
            self.stack.append(el)

    def handle_startendtag(self, tag, attrs):
        self.stack[-1][2].append([tag, self._attrs(), []])

    def handle_endtag(self, tag):
        for i in range(len(self.stack) - 1, 0, -1):
            if self.stack[i][0] == tag:
                del self.stack[i:]
                return

    def handle_data(self, d):
        if not d:
            return
        kids = self.stack[-1][2]
        if self.stack[-1][0] in ('style',):
            kids.append(d); return
        if d.strip() == '':
            d = ' '
        if kids and isinstance(kids[-1], str):
            kids[-1] += d
        else:
            kids.append(d)


def parse_tpl(s):
    p = TplParser(); p.feed(s); p.close()
    return p.root[2]


def strip_ws(nodes, parent=''):
    """Odstraní čistě bílé textové uzly mezi bloky (ne uvnitř inline textu)."""
    out = []
    for n in nodes:
        if isinstance(n, str):
            if n == ' ' and parent in ('#root', 'ul', 'ol', 'table', 'thead', 'tbody', 'tr', 'select', 'sc-for', 'sc-if', 'dl', 'nav', 'section', 'svg', 'helmet'):
                continue
            out.append(n)
        else:
            n[2] = strip_ws(n[2], n[0])
            out.append(n)
    return out


def load(name):
    s = open(os.path.join(SRC, name + '.dc.html'), encoding='utf-8').read()
    m = re.search(r'<x-dc>(.*)</x-dc>', s, re.S)
    body = m.group(1)
    helm = re.search(r'<helmet>(.*?)</helmet>', body, re.S)
    helmet = helm.group(1) if helm else ''
    if helm:
        body = body[:helm.start()] + body[helm.end():]
    code = re.search(r'<script type="text/x-dc"[^>]*>(.*?)</script>', s, re.S).group(1)
    head_style = ''.join(re.findall(r'<head>.*?(<style>.*?</style>).*?</head>', s, re.S))
    title = re.search(r'<title>(.*?)</title>', s, re.S).group(1)
    lang = (re.search(r'<html lang="([^"]+)"', s) or [None, 'cs'])[1]
    imports = sorted(set(re.findall(r'<dc-import name="([A-Za-z0-9_]+)"', body)))
    return dict(name=name, tpl=strip_ws(parse_tpl(body), '#root'), code=code, helmet=helmet,
                head_style=head_style, title=title, lang=lang, imports=imports)


man = json.load(open(MANIFEST, encoding='utf-8'))
blobmap = {k: v['file'] for k, v in man.items() if k.startswith('/_blob/') and isinstance(v, dict) and 'file' in v}

files = sorted(f[:-8] for f in os.listdir(SRC) if f.endswith('.dc.html') and not f.startswith('._'))
defs = {n: load(n) for n in files}
comp_names = set()
for d in defs.values():
    comp_names.update(d['imports'])
pages = [n for n in files if n not in comp_names]


def page_file(n):
    return 'index.html' if n == 'Main' else n + '.html'


missing = set()


def rewrite(text):
    text = re.sub(r'\b([A-Za-z0-9_]+)\.dc\.html', lambda m: page_file(m.group(1)) if m.group(1) in defs else m.group(0), text)

    def blob(m):
        k = m.group(0)
        if k in blobmap:
            return blobmap[k]
        missing.add(k)
        return k
    return re.sub(r'/_blob/[0-9a-f]{32}', blob, text)


def closure(n, acc):
    for i in defs[n]['imports']:
        if i not in acc:
            acc.add(i); closure(i, acc)
    return acc


os.makedirs(OUT, exist_ok=True)
for n in pages:
    d = defs[n]
    need = sorted(closure(n, set()))
    comps = {c: {'tpl': defs[c]['tpl'], 'code': defs[c]['code']} for c in need + [n]}
    styles = d['head_style'] + d['helmet'] + ''.join(
        defs[c]['head_style'] + defs[c]['helmet'] for c in need)
    data = json.dumps(comps, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
    html = f'''<!doctype html>
<html lang="{d['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{d['title']}</title>
{styles}
</head>
<body>
<div id="dc-root"></div>
<script>window.__DC_PAGE={json.dumps(n)};window.__DC={data};</script>
<script src="dc/preact.min.js"></script>
<script src="dc/dc-runtime.js"></script>
</body>
</html>
'''
    open(os.path.join(OUT, page_file(n)), 'w', encoding='utf-8').write(rewrite(html))
    print('page', page_file(n), 'components', len(need))

print('missing blobs:', sorted(missing))
