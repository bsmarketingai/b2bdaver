import json, re, hashlib

rows = json.load(open('/home/claude/img/rows.json'))

# ---- strom kategorií (z daver-strom-kategorii.md) ----
TREE_MD = open('/mnt/user-data/uploads/837c2c1f-daver-strom-kategorii.md', encoding='utf-8').read()
cats = []
sec = TREE_MD.split('## Kompletní strom')[1].split('## Prostý strom')[0]
for line in sec.splitlines():
    m = re.match(r'^### (.+) \((\d+)\)$', line)
    if m:
        cats.append({'n': m.group(1), 'c': int(m.group(2)), 'subs': []}); continue
    m = re.match(r'^(\s*)- \[(.+?)\]\(.*?\) \((\d+)\)$', line)
    if m:
        lvl = len(m.group(1)) // 2
        node = {'n': m.group(2), 'c': int(m.group(3))}
        if lvl == 0:
            node['subs'] = []; cats[-1]['subs'].append(node)
        else:
            cats[-1]['subs'][-1]['subs'].append(node)
assert len(cats) == 11, len(cats)
for _c in cats:
    if _c['n'] == '%': _c['n'] = 'Slevy a akce'; _c['sale'] = True

# ---- staré produkty se skutečnými cenami (screenshoty webu) ----
D10 = [{'cls': 'discount', 't': '-10 %'}]
OLD = [
 ('Jovi Glow přírodní plastelína 10 x 15 g 8 barev + 2 svítící ve tmě','90/10G','Jovi',58.88,450,D10,'Děti škola > Modelování > Plastelína'),
 ('Jovi Lettering akvarelové fixy oboustranné štětcový a pevný hrot 12 ks','1312DP','Jovi',97.72,25,D10,'Děti škola > Kreslení > Štětcové a akvarelové fixy'),
 ('Jovi Lettering akvarelové fixy štětcový hrot 12 ks','1312','Jovi',71.09,30,D10,'Děti škola > Kreslení > Štětcové a akvarelové fixy'),
 ('Jovi My First voskovky 8 ks','948','Jovi',75.24,30,D10,'Děti škola > Kreslení > Voskovky'),
 ('Jovi Jovidecor Glitter akrylové třpytivé fixy tenké 8 ks','1608G','Jovi',82.57,50,D10,'Děti škola > Kreslení > Třpytivé a metalické fixy'),
 ('Jovi Jovidecor Metalic akrylové fixy 2 ks zlatá a stříbrná','1602M','Jovi',23.21,300,D10,'Děti škola > Kreslení > Třpytivé a metalické fixy'),
 ('Jovi Soft Dough měkká modelovací hmota neonové barvy 5 x 110 g','405F','Jovi',123.62,150,D10,'Děti škola > Modelování > Měkké modelovací hmoty'),
 ('Jovi samotvrdnoucí modelovací hmota 1000 g bílá','86','Jovi',55.70,4000,D10,'Děti škola > Modelování > Samotvrdnoucí hmoty'),
 ('Jovi Play&Fun Mini sada s přírodní plastelínou Jurassic','2201S01','Jovi',111.40,5,D10,'Děti škola > Modelování > Modelovací sady'),
 ('Jovi Play&Fun sada na malování temperovými barvami 17 ks Super Heroes','2304','Jovi',223.05,4,D10,'Děti škola > Malování > Temperové barvy'),
 ('Darwi čistič štětců 100 ml','DA0710100001C','Darwi',79.15,10,[],None),
 ('Meyco sada pěnových tupovacích štětců č. 15 25 35 mm','14217','Meyco',36.40,50,[],None),
 ('Meyco tupovací štětce č. 2 4 6','14230','Meyco',91.37,5,[],'Štětce pomůcky > Sady štětců > Univerzální'),
 ('Meyco sada plochých štětců syntetické č. 12 16 20','14235','Meyco',69.38,30,[],'Štětce pomůcky > Sady štětců > Akryl'),
 ('Meyco sada plochých štětců syntetické č. 2 4 6 8 10','14236','Meyco',73.05,50,[],'Štětce pomůcky > Sady štětců > Akryl'),
 ('Meyco sada vějířových štětců syntetické č. 1 3 5','14243','Meyco',74.02,15,[],'Štětce pomůcky > Sady štětců > Univerzální'),
 ('Jovi samotvrdnoucí modelovací hmota 7 x 500 g v boxu s příslušenstvím','80','Jovi',343.00,30,D10,None),
 ('Darwi ROC umělecká modelovací hmota 1000 g','DA0831000000C','Darwi',95.03,10,[],None),
 ('Darwi Extra light samotvrdnoucí modelovací hmota 160 g bílá','DA0840160000C','Darwi',65.47,40,[],'Modelování keramika > Samotvrdnoucí hmoty'),
 ('Cernit sada oboustranných nástrojů 8 ks','CE906C','Cernit',189.82,5,[],None),
 ('Cernit pevná čepel na polymerovou hmotu 2 ks','CE908C','Cernit',133.63,2,[],'Modelování keramika > Modelovací nástroje > Nástroje na polymerové hmoty'),
 ('Cernit pružná čepel na polymerovou hmotu 2 ks','CE909C','Cernit',133.63,5,[],'Modelování keramika > Modelovací nástroje > Nástroje na polymerové hmoty'),
]
oldby = {o[0].lower(): o for o in OLD}

def h(s, n):
    return int(hashlib.md5(s.encode()).hexdigest(), 16) % n

def brand_of(name):
    for b in ('Royal & Langnickel', 'Van Gogh'):
        if name.startswith(b): return b
    w = name.split()[0]
    return '' if w in ('Mini',) else w

# ukázkové ceny bez DPH – odhad podle typu produktu (NEOVĚŘENO, jen prototyp)
RULES = [
 (r'grafický lis', (3900, 6900)), (r'čistič', (59, 129)), (r'štětec|špachtle', (29, 139)), (r'stojan', (690, 3900)), (r'židle', (1490, 2490)), (r'figurín', (190, 290)),
 (r'kufřík', (690, 1290)), (r'taška', (390, 790)), (r'kreslicí deska', (290, 890)), (r'hlína 10 kg|sádra 10 kg', (290, 420)),
 (r'hlína 5 kg|sádra 3 kg', (140, 230)), (r'1 kg|1000 g', (95, 260)), (r'sada|set|kit|kolekce|display', (120, 690)),
 (r'plátno|karton', (45, 180)), (r'šeps|gesso|ground', (190, 590)), (r'blok|skicák|papír', (69, 390)),
 (r'barva|inkoust|lak|médium|ředidlo', (49, 320)), (r'tužka|fixa|pero|pastel|uhel', (19, 149)),
]
def demo_price(name):
    n = name.lower()
    lo, hi = 39, 249
    for pat, rng in RULES:
        if re.search(pat, n): lo, hi = rng; break
    v = lo + h(name, max(1, hi - lo)) + [0.9, 0.5, 0.0, 0.4, 0.8][h(name + 'c', 5)]
    return round(v, 2)

products = []
for i, r in enumerate(rows):
    path = [x.strip() for x in r['path'].split('>')]
    o = oldby.get(r['name'].lower())
    webid = re.search(r'-p(\d+)/?$', r['url']).group(1)
    p = {'id': i + 1, 'name': r['name'], 'brand': (o[2] if o else brand_of(r['name'])), 'cat': path[0],
         'sub': path[1] if len(path) > 1 else '', 'sub3': path[2] if len(path) > 2 else '', 'img': r['blob'],
         'code': o[1] if o else webid, 'price': o[3] if o else demo_price(r['name']),
         'stock': o[4] if o else [0, 3, 8, 12, 25, 40, 60, 120, 250][h(r['name'] + 's', 9)],
         'flags': o[5] if o else [], 'real': bool(o)}
    products.append(p)
# skutečná data z daver-popisy-produktu.md (kód, B2B cena, dostupnost, krátký popis)
PO = json.load(open('/home/claude/gen/popisy.json', encoding='utf-8'))
def czk_num(t):
    m = re.findall(r'([\d\s]+,\d+)', t.replace('\u00a0', ' '))
    return float(m[0].replace(' ', '').replace(',', '.')) if m else None
def av_parse(t):
    t = t.strip()
    m = re.match(r'Skladem > (\d+) ks', t)
    if m: return int(m.group(1)) + 1, t
    m = re.match(r'Skladem (\d+) ks', t)
    if m: return int(m.group(1)), t
    m = re.match(r'(\d+) z (\d+) variant skladem', t)
    if m: return 10, 'Skladem (' + m.group(1) + ' z ' + m.group(2) + ' variant)'
    m = re.match(r'Očekávame (\d+)\.(\d+)\.(\d+)', t)
    if m: return 0, 'Očekáváme ' + m.group(1) + '. ' + m.group(2) + '. ' + m.group(3)
    if t == 'Na dotaz': return 0, 'Na dotaz'
    return None, None
for i, r in enumerate(rows):
    q = PO.get(r['cat'] + '/' + r['file'].split('/')[-1][:2])
    p = products[i]
    if not q or not q['code']: continue
    p['code'] = q['code'].lstrip('0') or q['code']
    pr = czk_num(q['price'])
    if pr: p['price'] = pr; p['from'] = '–' in q['price']; p['real'] = True
    st, txt = av_parse(q['av'])
    if st is not None: p['stock'] = st; p['avRaw'] = txt
    if q['short']: p['desc'] = q['short']
    if q['variants']: p['variants'] = q['variants']
names = {p['name'].lower() for p in products}
nid = 151
for o in OLD:
    if o[0].lower() in names: continue
    path = [x.strip() for x in o[6].split('>')]
    products.append({'id': nid, 'name': o[0], 'brand': o[2], 'cat': path[0], 'sub': path[1], 'sub3': path[2] if len(path) > 2 else '',
                     'img': None, 'code': o[1], 'price': o[3], 'stock': o[4], 'flags': o[5], 'real': True})
    nid += 1
# pár ukázkových štítků Novinka (NEOVĚŘENO)
for p in products:
    if not p['flags'] and p['img'] and h(p['name'] + 'n', 11) == 0:
        p['flags'] = [{'cls': 'flag00', 't': 'Novinka'}]

byname = {p['name']: p for p in products}
def pid(prefix):
    for p in products:
        if p['name'].startswith(prefix): return p['id']
    raise KeyError(prefix)

# ---- atributy štětců pro filtry (z názvů produktů) ----
A = {
 'Talens série 150 štětec na akvarel syntetické Round velikost 3': dict(mat='Syntetický', tvar='Kulatý', vel=['3'], urc='Akvarel', bal='Jednotlivě', ks=1, delka='Krátká'),
 'Talens série 150 štětec na akvarel syntetické Round velikost 4': dict(mat='Syntetický', tvar='Kulatý', vel=['4'], urc='Akvarel', bal='Jednotlivě', ks=1, delka='Krátká'),
 'Darwi štětec plochý na akryl č. 04 šířka 5 mm': dict(mat='Syntetický', tvar='Plochý', vel=['4'], urc='Akryl', bal='Jednotlivě', ks=1, delka='Dlouhá', sirka='5 mm'),
 'Darwi štětec oválný na akryl č. 02 šířka 4 mm': dict(mat='Syntetický', tvar='Filbert', vel=['2'], urc='Akryl', bal='Jednotlivě', ks=1, delka='Dlouhá', sirka='4 mm'),
 'Royal & Langnickel sada vodních štětců 3 ks': dict(mat='Syntetický', tvar='Kulatý', vel=[], urc='Akvarel', bal='Sada / set', ks=3),
 'Royal & Langnickel vodní štětec velký 1 ks': dict(mat='Syntetický', tvar='Kulatý', vel=[], urc='Akvarel', bal='Jednotlivě', ks=1),
 'Royal & Langnickel miniaturní štětec Majestic Round velikost 0': dict(mat='Syntetický', tvar='Kulatý', vel=['0'], urc='Miniatury', bal='Jednotlivě', ks=1, delka='Krátká'),
 'Royal & Langnickel miniaturní štětec Majestic Flat Wisp velikost 10/0': dict(mat='Syntetický', tvar='Plochý', vel=['10/0'], urc='Miniatury', bal='Jednotlivě', ks=1, delka='Krátká'),
 'Meyco sada pěnových tupovacích štětců č. 15 25 35 mm': dict(mat='', tvar='Stippler', vel=[], urc='Univerzální', bal='Sada / set', ks=3),
 'Meyco tupovací štětce č. 2 4 6': dict(mat='Přírodní', tvar='Stippler', vel=['2', '4', '6'], urc='Univerzální', bal='Sada / set', ks=3),
 'Meyco sada plochých štětců syntetické č. 12 16 20': dict(mat='Syntetický', tvar='Plochý', vel=['12', '16', '20'], urc='Akryl', bal='Sada / set', ks=3),
 'Meyco sada plochých štětců syntetické č. 2 4 6 8 10': dict(mat='Syntetický', tvar='Plochý', vel=['2', '4', '6', '8', '10'], urc='Akryl', bal='Sada / set', ks=5),
 'Meyco sada vějířových štětců syntetické č. 1 3 5': dict(mat='Syntetický', tvar='Vějířový', vel=['1', '3', '5'], urc='Univerzální', bal='Sada / set', ks=3),
 'Darwi čistič štětců 100 ml': dict(bal='Jednotlivě'), 'Pebeo čistič štětců 75 ml': dict(bal='Jednotlivě'),
 'Sizzix aplikátor s pěnovou houbičkou': dict(bal='Jednotlivě'), 'Sizzix náhradní pěnové houbičky do aplikátoru 4 ks': dict(bal='Sada / set', ks=4),
 'Royal & Langnickel malířská špachtle LP-1': dict(bal='Jednotlivě'), 'Royal & Langnickel malířská špachtle LP-10': dict(bal='Jednotlivě'),
}
for n, a in A.items(): byname[n]['a'] = a
byname['Amsterdam akrylová barva 120 ml']['href'] = 'DetailVariant.dc.html'
# skutečné popisy z webu (zatím jen co máme)
DESC = {'Jovi samotvrdnoucí modelovací hmota 7 x 500 g v boxu s příslušenstvím': 'Samotvrdnoucí hmota, na vzduchu přirozeně ztvrdne za cca 24 hod (záleží na tloušťce výrobku), není třeba keramické vypalování. Výrobek lze dále upravovat – barvit, brousit, lepit, lakovat (stává se voděodolným). Může sloužit jako odrazový můstek pro sochaření. Tvaruje se ručně, ale mohou se využívat různé pomůcky na modelování. Aby nespotřebovaná hmota nevyschla, je třeba ji uchovat v hermeticky uzavřené nádobce nebo zabalit do igelitu. Vyrobeno ve Španělsku.'}
for n, t in DESC.items(): byname[n]['desc'] = t

# obrázky kategorií: první produkt s obrázkem v dané kategorii
CAT_PHOTOS = {"Děti škola": "/_blob/b8c6cd9f7f21a2baa8d162c2ecf87999", "Barvy média": "/_blob/61f27ce5b44c07e80e9a4cf565fc76bf", "Papíry skicáky": "/_blob/602d6faceef527407c7c4d774c215019", "Štětce pomůcky": "/_blob/4bbc7fec64b2c2087536c680c8250683", "Plátna podklady": "/_blob/881b281f7c4e6a4cdc30592814c821a9", "Kreslení ilustrace": "/_blob/f91fa3b20f3e3f34b56d6b17c1ec2ebb", "Grafika tisk": "/_blob/0d99131af690ae2293a907b6b98eac54", "Modelování keramika": "/_blob/26650308d3bfbc9862c3af17d2513ae6", "Kreativní techniky": "/_blob/3a8d3c29faec8a6070940ae161c7d822", "Studio vybavení": "/_blob/5aa5c8856c47639a503f1d3dde47cded"}

def img_for(l1, l2=None):
    for p in products:
        if p['img'] and p['cat'] == l1 and (l2 is None or p['sub'] == l2): return p['img']
    return None
for c in cats:
    c['img'] = img_for(c['n'])
    if c['n'] in CAT_PHOTOS: c['img'] = CAT_PHOTOS[c['n']]; c['photo'] = True  # foto kategorie od klienta
    for s in c['subs']:
        s['img'] = img_for(c['n'], s['n'])

IDS = dict(
 detail=pid('Meyco sada pěnových tupovacích'), cistic=pid('Darwi čistič štětců'), metalic=pid('Jovi Jovidecor Metalic'),
 ploche=pid('Meyco sada plochých štětců syntetické č. 12'), ploche5=pid('Meyco sada plochých štětců syntetické č. 2'),
 tupovaci=pid('Meyco tupovací štětce'), vejir=pid('Meyco sada vějířových'),
 golden=pid('Golden Heavy Body'), jovibox=pid('Jovi samotvrdnoucí modelovací hmota 7'), talens=pid('Talens série 150 štětec na akvarel syntetické Round velikost 3'),
 cernit=pid('Cernit Number One'), pebeoCistic=pid('Pebeo čistič'),
)

def first_ids(cat_slug_idx, n):
    return [p['id'] for p in products if p['img']][cat_slug_idx * 15: cat_slug_idx * 15 + n]

CAR = dict(
 A=[products[i * 15 + 0]['id'] for i in range(10)][:8] + [IDS['detail']],
 B=[products[i * 15 + 12]['id'] for i in range(10)][:8],
 C=[p['id'] for p in products if p['flags'] and p['flags'][0]['cls'] == 'discount'],
 R=[products[i * 15 + 6]['id'] for i in range(10)][:8],
)
LIST_STETCE = [p['id'] for p in products if p['cat'] == 'Štětce pomůcky']

def slim(p):
    d = {k: p[k] for k in ('id', 'name', 'brand', 'cat', 'sub', 'sub3', 'img', 'code', 'price', 'stock', 'flags')}
    if 'a' in p: d['a'] = p['a']
    for k in ('desc', 'avRaw', 'from', 'variants', 'href'):
        if p.get(k): d[k] = p[k]
    return d

DATA = {'cats': cats, 'products': [slim(p) for p in products], 'ids': IDS, 'car': CAR, 'listStetce': LIST_STETCE}
json.dump(DATA, open('/home/claude/gen/data.json', 'w'), ensure_ascii=False)
if __name__ == '__main__':
    print(len(products), 'produktů,', sum(1 for p in products if p['real']), 'se skutečnou cenou;', 'štětce ve výpisu:', len(LIST_STETCE))
    print(IDS); print({k: len(v) for k, v in CAR.items()})
    print(len(json.dumps(DATA, ensure_ascii=False)) // 1024, 'KB JSON')
