import json
import pages as P0
from common import *

D = json.load(open(os.path.join(os.path.dirname(__file__), 'data.json'), encoding='utf-8'))
PR = {p['id']: p for p in D['products']}
IDS = D['ids']
def czk(n): return f"{n:,.2f}".replace(',', ' ').replace('.', ',').replace(' ', ' ') + ' Kč'

pages = dict(P0.pages)

# ======================= MAIN =======================
slides = [
    ('', 'Distributor výtvarných potřeb', 'Velkoobchod a distribuce výtvarných potřeb na českém a slovenském trhu od roku 1996.', 'Prohlédnout sortiment', 'Kategorie.dc.html', '/_blob/d464c423c82fd3de6b03e826671d4ea3', '50% 30%'),
    ('', 'Svět výtvarných potřeb pod jednou střechou', 'Ve společnosti Daver spojujeme tradici s moderní distribucí výtvarných potřeb pro Českou a Slovenskou republiku. Jsme výhradním distributorem renomovaných značek, které přinášejí špičkovou kvalitu a inovativní produkty.', 'Více o nás', 'Onas.dc.html', '/_blob/f187ca0fbacbaa21776fddc3873cc212', '50% 42%'),
]
SL_JS = 'const SLIDES=' + json.dumps([{'k': a, 't': b, 'd': c, 'cta': d_, 'href': e, 'img': f, 'pos': g} for a, b, c, d_, e, f, g in slides], ensure_ascii=False) + ';'
m = P0.pages['Main']
m = m[:m.index('const SLIDES=')] + SL_JS + m[m.index(';\nconst DATA=') + 1:] if ';\nconst DATA=' in m else m
# SLIDES se v původním Main vkládá před class Component – přegenerujeme stránku čistě:
import re as _re
HERO_HTML = """<section class="{{ hxCls }}" aria-roledescription="carousel" aria-label="Hlavní sdělení" onMouseEnter="{{ heroPause }}" onMouseLeave="{{ heroPlay }}" onFocus="{{ heroPause }}" onBlur="{{ heroPlay }}" onTouchStart="{{ tStart }}" onTouchEnd="{{ tEnd }}">
<sc-for list="{{ slides }}" as="s" hint-placeholder-count="1">
<div class="{{ s.hxS }}" role="group" aria-roledescription="slide" aria-label="{{ s.aria }}" aria-hidden="{{ s.hidden }}" inert="{{ s.inertAttr }}">
<img class="hxImg" src="{{ s.img }}" alt="" style="object-position:{{ s.pos }}">
<div class="hxShade" aria-hidden="true"></div>
<div class="container hxIn"><div class="hxTxt"><h2 class="hxT">{{ s.t }}</h2><p class="hxD">{{ s.d }}</p><a class="btn btn-light btn-lg hxCta" href="{{ s.href }}">{{ s.cta }}</a></div></div>
</div>
</sc-for>
<div class="container hxNav"><div class="hxBars" aria-hidden="true"><sc-for list="{{ slides }}" as="s" hint-placeholder-count="2"><span class="{{ s.barCls }}"></span></sc-for></div>
<span class="hxCount" aria-live="polite">{{ curNo }} / {{ total }}</span>
<button class="arrowBtn" type="button" aria-label="Předchozí slide" onClick="{{ heroPrev }}">""" + I('caret-left') + """</button><button class="arrowBtn" type="button" aria-label="Další slide" onClick="{{ heroNext }}">""" + I('caret-right') + """</button></div>
</section>"""
main_html = _re.sub(r'<section class="hero bleed".*?</section>', lambda m: HERO_HTML, P0.main_html, count=1, flags=_re.S)
assert 'hxNav' in main_html
main_html = main_html.replace('<p>{{ s.d }}</p><a class="btn btn-main"', '<p>{{ s.d }}</p><a class="btn btn-main"')
main_css = P0.main_css.replace(".slideImg{height:340px;background:rgba(255,255,255,.06);border-color:rgba(255,255,255,.3);color:rgba(255,255,255,.75)}",
 ".slideImg{height:340px;background:#fff;border-radius:var(--card-radius);display:flex;align-items:center;justify-content:center;padding:24px}\n.slideImg img{max-height:100%;max-width:100%;object-fit:contain}\n@supports (corner-shape:squircle){.slideImg{corner-shape:var(--corner-shape)}}")
main_css = main_css.replace(" .accBody .slideImg{height:clamp(180px,50vw,260px);background:var(--bg-soft);border-color:var(--input-border);color:var(--text-muted)}",
 " .accBody .slideImg{height:clamp(180px,50vw,260px);background:var(--bg-soft)}")
HERO_CSS = """
.hx{position:relative;min-height:clamp(460px,40vw,600px);overflow:hidden;background:#27272a;color:#fff;isolation:isolate}
.hxSlide{position:absolute;inset:0;opacity:0;visibility:hidden;transition:opacity .8s ease,visibility 0s linear .8s}
.hxSlide.on{opacity:1;visibility:visible;transition:opacity .8s ease}
.hxImg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;transform:scale(1.05);transition:transform 8s ease-out}
.hxSlide.on .hxImg{transform:scale(1)}
.hxShade{position:absolute;inset:0;background:linear-gradient(90deg,rgba(22,12,15,.86) 0%,rgba(22,12,15,.66) 38%,rgba(22,12,15,.18) 72%,rgba(22,12,15,0) 100%),linear-gradient(0deg,rgba(22,12,15,.45) 0%,rgba(22,12,15,0) 35%)}
.hxIn{position:relative;height:100%;display:flex;align-items:center;padding-top:48px;padding-bottom:104px}
.hxTxt{max-width:min(680px,62%);display:flex;flex-direction:column;gap:22px;align-items:flex-start}
.hxT{color:#fff;font-size:clamp(36px,4.4vw,64px);line-height:1.04;letter-spacing:-.02em;font-weight:800;text-wrap:balance;margin:0}
.hxD{color:rgba(255,255,255,.9);font-size:clamp(16px,1.35vw,20px);line-height:1.55;max-width:54ch;margin:0;text-wrap:pretty}
.hxCta{margin-top:6px}
.hxNav{position:absolute;left:0;right:0;bottom:28px;z-index:2;display:flex;align-items:center;gap:12px}
.hxBars{display:flex;gap:8px;flex:0 1 200px}
.hxBar{position:relative;flex:1;height:3px;border-radius:2px;background:rgba(255,255,255,.3);overflow:hidden}
.hxBar::after{content:"";position:absolute;inset:0;background:#fff;transform:scaleX(0);transform-origin:left center}
.hxBar.done::after{transform:scaleX(1)}
.hxBar.on::after{animation:hxProg 7s linear forwards}
.hx.paused .hxBar.on::after{animation-play-state:paused}
@keyframes hxProg{to{transform:scaleX(1)}}
.hxCount{margin-left:auto;margin-right:4px;font-size:var(--fs-body-sm);font-variant-numeric:tabular-nums;color:rgba(255,255,255,.85)}
@media (prefers-reduced-motion:reduce){.hxImg,.hxSlide.on .hxImg{transform:none;transition:none}.hxSlide{transition:none}.hxBar.on::after{animation:none;transform:scaleX(1)}}
@media (max-width:819px){
 .hx{min-height:560px}
 .hxShade{background:linear-gradient(0deg,rgba(22,12,15,.92) 0%,rgba(22,12,15,.72) 50%,rgba(22,12,15,.2) 100%)}
 .hxIn{align-items:flex-end;padding-bottom:96px}
 .hxTxt{max-width:100%;gap:16px}
 .hxCta{width:100%}
 .hxBars{flex-basis:120px}
}
"""
main_css = main_css + HERO_CSS
main_css += ".uspItem{background:var(--nav-bg);border-color:var(--nav-bg);color:#fff;border-radius:var(--card-radius);padding:12px 14px;gap:12px;line-height:1.3}\n.usp{grid-template-columns:repeat(4,minmax(0,1fr))}\n@media (max-width:1149px){.usp{grid-template-columns:repeat(2,minmax(0,1fr))}}\n@media (max-width:819px){.usp{grid-template-columns:repeat(2,minmax(0,1fr))}}\n@media (max-width:479px){.usp{grid-template-columns:1fr}}\n.uspItem strong{color:#fff;font-size:var(--fs-body)}\n.uspItem span{color:rgba(255,255,255,.86)}\n.uspIc{color:#fff;width:32px;height:32px;flex:none}\n.uspItem span{font-size:var(--fs-caption)}\n@supports (corner-shape:squircle){.uspItem{corner-shape:squircle}}\n.usp>li{display:flex}\n.uspItem{width:100%;position:relative;text-decoration:none;overflow:hidden;transition:transform .3s cubic-bezier(.2,.8,.2,1),box-shadow .3s,background .3s}\n.uspItem:hover,.uspItem:focus-visible{transform:translateY(-4px) scale(1.02);box-shadow:0 14px 30px rgba(127,52,61,.35);background:var(--primary-d);color:#fff}\n.uspItem .uspIc{transition:transform .35s cubic-bezier(.34,1.56,.64,1)}\n.uspItem:hover .uspIc,.uspItem:focus-visible .uspIc{transform:scale(1.18) rotate(-6deg)}\n.uspItem>div{flex:1;min-width:0}\n.uspGo{width:18px;height:18px;flex:none;opacity:0;transform:translateX(-6px);transition:opacity .25s,transform .25s;color:#fff}\n.uspItem:hover .uspGo,.uspItem:focus-visible .uspGo{opacity:1;transform:none}\n.uspItem:focus-visible{outline:3px solid var(--primary-10);outline-offset:2px}\n@media (prefers-reduced-motion:reduce){.uspItem,.uspItem .uspIc,.uspGo{transition:none}.uspItem:hover{transform:none}.uspItem:hover .uspIc{transform:none}}\n"
main_css += ".aboutImg{width:100%;height:400px;object-fit:cover;border-radius:var(--card-radius);display:block}\n@supports (corner-shape:squircle){.aboutImg{corner-shape:var(--corner-shape)}}\n.about h2{font-size:var(--fs-h1);line-height:1.15;text-wrap:balance}\n.aboutLead{font-size:var(--fs-body);color:var(--text-weaker);max-width:56ch}\n.aboutAddr{font-size:var(--fs-body-sm);color:var(--text-muted)}\n"
main_js = P0.main_js.replace("carA:[14,11,8,6,12,15,7,19].map((i)=>card(byId(i))),", "carA:CAR.A.map((i)=>card(byId(i))),") \
    .replace("carB:[18,19,20,21,22,13,16,3].map((i)=>card(byId(i))),", "carB:CAR.B.map((i)=>card(byId(i))),") \
    .replace("carC:PRODUCTS.filter((p)=>p.flags.length).map(card),", "carC:CAR.C.map((i)=>card(byId(i))),") \
    .replace("%SLIDES.length});},6000);", "%SLIDES.length});},7000);") \
    .replace("accCls:'accItem'+(i===s.slide?' on':''),", "accCls:'accItem'+(i===s.slide?' on':''),hxS:'hxSlide'+(i===s.slide?' on':''),barCls:'hxBar'+(i===s.slide?' on':(i<s.slide?' done':'')),") \
    .replace("heroPrev:()=>go(s.slide-1),", "hxCls:'hx bleed'+(s.paused?' paused':''),curNo:s.slide+1,total:SLIDES.length,heroPrev:()=>go(s.slide-1),")
for _a in ["%SLIDES.length});},7000);", "hxS:'hxSlide'", "hxCls:'hx bleed'"]: assert _a in main_js, _a
main_html = main_html.replace('<section class="container section about"', '<section class="container section" aria-label="Výrobci"><dc-import name="BrandStrip" hint-size="100%,200px"></dc-import></section>\n<section class="container section about"')
main_html = main_html.replace('<h1 class="mainH1">Velkoobchod s výtvarnými potřebami <span class="todo">[OVĚŘIT SEO nadpis]</span></h1>', '<h1 class="mainH1">Velkoobchod a distribuce výtvarných potřeb</h1>')
assert 'Velkoobchod a distribuce výtvarných potřeb</h1>' in main_html
pages['Main'] = shop_page('Daver – úvodní stránka', main_css, main_html, main_js, 4550).replace('class Component extends DCLogic {', SL_JS + '\nclass Component extends DCLogic {', 1)

# ======================= KATEGORIE =======================
CAT = next(c for c in D['cats'] if c['n'] == 'Štětce pomůcky')
kat_html = f'''<div class="container">
<dc-import name="Breadcrumb" current="Štětce pomůcky" hint-size="100%,48px"></dc-import>
<div class="katHead"><h1>Štětce pomůcky <small>{CAT['c']} produktů</small></h1>
<div class="{{{{ perexCls }}}}"><p>Štětce na akvarel i akryl, sady štětců, univerzální štětce, špachtle a malířské nože, válečky a aplikátory i přípravky na péči o štětce. Výrobci Talens, Royal &amp; Langnickel, Meyco, Darwi, Pebeo, Van Gogh a další.</p></div>
<button class="btn btn-ghost btn-sm" type="button" aria-expanded="{{{{ perexOpen }}}}" onClick="{{{{ togglePerex }}}}">{{{{ perexBtn }}}}</button></div>
<nav class="subGrid FlatCategoriesRwdView" aria-label="Podkategorie"><sc-for list="{{{{ subTiles }}}}" as="t" hint-placeholder-count="7"><a class="subTile" href="Kategorie.dc.html"><sc-if value="{{{{ t.hasImg }}}}" hint-placeholder-val="{{{{ true }}}}"><img src="{{{{ t.img }}}}" alt=""></sc-if><sc-if value="{{{{ t.noImg }}}}" hint-placeholder-val="{{{{ false }}}}"><span class="ph">[FOTO]</span></sc-if><span class="subName">{{{{ t.n }}}}</span></a></sc-for></nav>
<div class="quick" role="group" aria-label="Rychlý filtr – tvar štětce"><span class="quickL">Tvar:</span>
<sc-for list="{{{{ quickChips }}}}" as="b" hint-placeholder-count="6"><button class="{{{{ b.cls }}}}" type="button" aria-pressed="{{{{ b.pressed }}}}" disabled="{{{{ b.dis }}}}" onClick="{{{{ b.toggle }}}}">{{{{ b.n }}}} <small>{{{{ b.count }}}}</small></button></sc-for></div>
<div class="toolbar">
<div class="tbLeft"><button class="btn btn-main" type="button" aria-expanded="{{{{ filterOpen }}}}" onClick="{{{{ openFilter }}}}">{I('funnel')}Filtr<span class="fBadge">{{{{ activeCount }}}}</span></button>
<div class="sortTabs" role="group" aria-label="Řazení"><sc-for list="{{{{ sorts }}}}" as="o" hint-placeholder-count="4"><button class="{{{{ o.cls }}}}" type="button" aria-pressed="{{{{ o.pressed }}}}" onClick="{{{{ o.pick }}}}">{{{{ o.n }}}}</button></sc-for></div></div>
<div class="tbRight">
<div class="viewSw" role="group" aria-label="Zobrazení"><span class="{{{{ vIndCls }}}}" aria-hidden="true"></span><button class="{{{{ vTileCls }}}}" type="button" aria-pressed="{{{{ isTile }}}}" onClick="{{{{ setTile }}}}">{I('squares-four')}<span>Dlaždicové</span></button><button class="{{{{ vRowCls }}}}" type="button" aria-pressed="{{{{ isRow }}}}" onClick="{{{{ setRow }}}}">{I('rows')}<span>Řádkové</span></button></div>
</div></div>
<sc-if value="{{{{ hasActive }}}}" hint-placeholder-val="{{{{ false }}}}"><div class="activeBar"><sc-for list="{{{{ activeChips }}}}" as="a" hint-placeholder-count="2"><dc-import name="FilterChip" label="{{{{ a.label }}}}" on-remove="{{{{ a.remove }}}}" hint-size="120px,32px"></dc-import></sc-for><button class="btn btn-ghost btn-sm" type="button" onClick="{{{{ clearAll }}}}">Zrušit vše</button></div></sc-if>
<p class="protoNote">{{{{ countTxt }}}}</p>
<sc-if value="{{{{ hasItems }}}}" hint-placeholder-val="{{{{ true }}}}">
<sc-if value="{{{{ isTile }}}}" hint-placeholder-val="{{{{ true }}}}">
<div class="pGrid ProductsView"><sc-for list="{{{{ items }}}}" as="c" hint-placeholder-count="8"><dc-import name="ProductCard" p="{{{{ c }}}}" pickup="{{{{ pickup }}}}" delivery="{{{{ delivery }}}}" on-add="{{{{ addCart }}}}" hint-size="100%,560px"></dc-import></sc-for></div>
</sc-if>
<sc-if value="{{{{ isRow }}}}" hint-placeholder-val="{{{{ false }}}}">
<div class="rowsBox"><table class="rows"><thead><tr><th scope="col">Název / kód</th><th scope="col">Dostupnost</th><th scope="col" class="r">Cena bez DPH</th><th scope="col" class="r">Množství</th></tr></thead>
<tbody><sc-for list="{{{{ items }}}}" as="r" hint-placeholder-count="8"><tr><td><div class="rName"><sc-if value="{{{{ r.hasImg }}}}" hint-placeholder-val="{{{{ true }}}}"><img src="{{{{ r.img }}}}" alt=""></sc-if><sc-if value="{{{{ r.noImg }}}}" hint-placeholder-val="{{{{ false }}}}"><span class="ph">[FOTO]</span></sc-if><div><a href="{{{{ r.href }}}}">{{{{ r.name }}}}</a><small>Kód {{{{ r.code }}}} · {{{{ r.brand }}}}</small></div></div></td><td class="{{{{ r.avCls }}}}">{{{{ r.av }}}}</td><td class="r"><strong>{{{{ r.priceTxt }}}}</strong><small>{{{{ r.vatTxt }}}} s DPH</small></td><td class="r"><label class="sr" for="{{{{ r.qid }}}}">Množství {{{{ r.name }}}}</label><input class="rowQty" id="{{{{ r.qid }}}}" inputmode="numeric" value="{{{{ r.rq }}}}" onChange="{{{{ r.setRq }}}}"> ks</td></tr></sc-for></tbody></table>
<div class="rowsFoot"><span>Vyplňte množství u více produktů a vložte je do košíku najednou.</span><button class="btn btn-main" type="button" onClick="{{{{ allToCart }}}}">{I('shopping-cart')}Vše do košíku</button></div></div>
</sc-if>
<sc-if value="{{{{ hasMore }}}}" hint-placeholder-val="{{{{ true }}}}"><div class="more"><button class="btn btn-out" type="button" onClick="{{{{ showMore }}}}">Zobrazit dalších {{{{ moreN }}}}</button></div></sc-if>
<nav class="PagingView" aria-label="Stránkování"><button class="pg" type="button" aria-label="Předchozí stránka" disabled="{{{{ prevDis }}}}" onClick="{{{{ prevPage }}}}">{I('caret-left')}</button><sc-for list="{{{{ pagesList }}}}" as="g" hint-placeholder-count="2"><button class="{{{{ g.cls }}}}" type="button" aria-current="{{{{ g.cur }}}}" onClick="{{{{ g.go }}}}">{{{{ g.n }}}}</button></sc-for><button class="pg" type="button" aria-label="Další stránka" disabled="{{{{ nextDis }}}}" onClick="{{{{ nextPage }}}}">{I('caret-right')}</button></nav>
</sc-if>
<sc-if value="{{{{ noItems }}}}" hint-placeholder-val="{{{{ false }}}}"><div class="empty box">{I('magnifying-glass','ic big')}<h2>Pro tento výběr tu teď nic nemáme</h2><p>Zkuste zrušit některý filtr, nebo nám zavolejte – rádi zboží objednáme.</p><div class="emptyAct"><button class="btn btn-main" type="button" onClick="{{{{ clearAll }}}}">Zrušit filtry</button><a class="btn btn-out" href="Kontakt.dc.html">Kontaktovat obchod</a></div></div></sc-if>
<section class="section seo"><h2>Jak vybrat štětec</h2>
<p>Správný štětec rozhoduje o výsledku víc, než se zdá. Při výběru sledujte tři věci: materiál vlasu, tvar a velikost. Pro prodejny a školy se vyplatí mít v nabídce sady pro začátečníky i jednotlivé štětce pro náročnější zákazníky.</p>
<h3>Materiál vlasu podle barvy</h3>
<ul><li><strong>Syntetický vlas</strong> – univerzální a odolný, ideální pro akryl, tempery a školní výuku. Snadno se čistí a dobře drží tvar.</li><li><strong>Přírodní vlas (veverka, kolinský sobol)</strong> – nasaje hodně vody a pigmentu, proto je nejlepší pro akvarel a lazurní malbu.</li><li><strong>Štětina</strong> – tuhá a pružná, vhodná pro olej a hustý akryl, kde chcete zachovat stopu tahu.</li></ul>
<h3>Tvar a velikost</h3>
<p><strong>Kulaté štětce</strong> jsou nejuniverzálnější: zvládnou detail, linku i menší plochy. <strong>Ploché</strong> se hodí na rovné tahy a větší plochy, <strong>kočičí jazyk</strong> (filbert) na měkké přechody a <strong>vějířové</strong> na textury, například trávu nebo listí. Velikost udává číslo – čím vyšší, tím širší štětec. Pro děti doporučujeme silnější rukojeť a velikosti 6–12.</p>
<h3>Péče o štětce</h3>
<p>Štětce vždy vymyjte hned po malbě, akryl nenechte zaschnout. Sušte je vodorovně nebo vlasem dolů a nikdy je nenechávejte stát ve vodě – vlas se zdeformuje. Životnost prodlouží čistič štětců a mýdlo na štětce.</p>
</section>
</div>
<sc-if value="{{{{ filterOpen }}}}" hint-placeholder-val="{{{{ false }}}}">
<div class="navOverlay fOverlay" onClick="{{{{ filterOverlay }}}}" onKeyDown="{{{{ filterKey }}}}">
<div class="fDrawer" role="dialog" aria-modal="true" aria-labelledby="fT">
<div class="drawerHead"><h2 id="fT">Upřesnit výběr</h2><button class="iconBtn" type="button" aria-label="Zavřít filtr" onClick="{{{{ closeFilter }}}}">{I('x')}</button></div>
<div class="fBody">
<fieldset class="fGroup"><legend>Cena bez DPH</legend>
<div class="dual"><input type="range" min="0" max="{{{{ pTop }}}}" step="1" value="{{{{ pMin }}}}" onChange="{{{{ setPMin }}}}" aria-label="Cena od"><input type="range" min="0" max="{{{{ pTop }}}}" step="1" value="{{{{ pMax }}}}" onChange="{{{{ setPMax }}}}" aria-label="Cena do"></div>
<div class="fPrice"><label>Od<input inputmode="numeric" value="{{{{ pMin }}}}" onChange="{{{{ setPMin }}}}"> Kč</label><label>Do<input inputmode="numeric" value="{{{{ pMax }}}}" onChange="{{{{ setPMax }}}}"> Kč</label></div></fieldset>
<sc-for list="{{{{ groups }}}}" as="g" hint-placeholder-count="6">
<fieldset class="fGroup"><legend>{{{{ g.title }}}}<sc-if value="{{{{ g.prop }}}}" hint-placeholder-val="{{{{ false }}}}"><span class="propTag">návrh</span></sc-if></legend>
<sc-if value="{{{{ g.searchable }}}}" hint-placeholder-val="{{{{ false }}}}"><div class="fSearch">{I('magnifying-glass')}<label class="sr" for="fs_{{{{ g.key }}}}">Hledat výrobce</label><input id="fs_{{{{ g.key }}}}" placeholder="Hledat výrobce" value="{{{{ g.q }}}}" onChange="{{{{ g.onQ }}}}"></div></sc-if>
<sc-if value="{{{{ g.isCheck }}}}" hint-placeholder-val="{{{{ true }}}}"><div class="fList"><sc-for list="{{{{ g.vals }}}}" as="v" hint-placeholder-count="4"><label class="{{{{ v.cls }}}}"><input type="checkbox" checked="{{{{ v.on }}}}" disabled="{{{{ v.dis }}}}" onChange="{{{{ v.toggle }}}}">{{{{ v.n }}}}<small>{{{{ v.count }}}}</small></label></sc-for></div></sc-if>
<sc-if value="{{{{ g.isChip }}}}" hint-placeholder-val="{{{{ false }}}}"><div class="fChips"><sc-for list="{{{{ g.vals }}}}" as="v" hint-placeholder-count="6"><button class="{{{{ v.chipCls }}}}" type="button" aria-pressed="{{{{ v.pressed }}}}" disabled="{{{{ v.dis }}}}" onClick="{{{{ v.toggle }}}}">{{{{ v.n }}}}<small>{{{{ v.count }}}}</small></button></sc-for></div></sc-if>
<sc-if value="{{{{ g.canMore }}}}" hint-placeholder-val="{{{{ false }}}}"><button class="btn btn-ghost btn-sm" type="button" aria-expanded="{{{{ g.exp }}}}" onClick="{{{{ g.toggleMore }}}}">{{{{ g.moreTxt }}}}</button></sc-if>
</fieldset>
</sc-for>
</div>
<div class="fFoot"><button class="btn btn-out" type="button" onClick="{{{{ clearAll }}}}">Zrušit vše</button><button class="btn btn-main" type="button" onClick="{{{{ closeFilter }}}}">Zobrazit {{{{ count }}}} produktů</button></div>
</div></div>
</sc-if>'''
kat_css = P0.kat_css + """
.subGrid{grid-template-columns:repeat(7,minmax(0,1fr))}
.subTile img,.subTile .ph{width:88px;height:88px;object-fit:contain}
.subTile small{color:var(--text-muted);font-weight:400;font-size:var(--fs-caption)}
.chip:disabled{opacity:.45;cursor:not-allowed}
.perPage select{height:42px;border:1px solid var(--input-border);border-radius:var(--btn-radius);padding:0 40px 0 14px;-webkit-appearance:none;appearance:none;background:#fff url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 256 256' fill='%2318181b'%3E%3Cpath d='M213.66,101.66l-80,80a8,8,0,0,1-11.32,0l-80-80A8,8,0,0,1,53.66,90.34L128,164.69l74.34-74.35a8,8,0,0,1,11.32,11.32Z'/%3E%3C/svg%3E") no-repeat right 14px center/16px 16px;cursor:pointer}
.perPage select:focus{outline:0;border-color:var(--primary-d)}
.tbLeft{display:flex;align-items:center;gap:16px;flex-wrap:wrap}
@media (max-width:819px){
 .toolbar{display:grid!important;grid-template-columns:auto 1fr;grid-template-areas:"f v" "s s";gap:10px 12px;align-items:center}
 .tbLeft,.tbRight{display:contents}
 .tbLeft>.btn{grid-area:f;justify-self:start}
 .tbRight .viewSw{grid-area:v;justify-self:end}
 .viewSw .vBtn span{display:none}.viewSw .vBtn{min-width:44px;padding:0 10px}
 .sortTabs{grid-area:s;flex-wrap:nowrap!important;overflow-x:auto;scrollbar-width:none;margin:0 calc(-1 * var(--gutter));padding:0 var(--gutter) 2px;scroll-snap-type:x proximity;-webkit-overflow-scrolling:touch}
 .sortTabs::-webkit-scrollbar{display:none}
 .sortTabs>*{flex:none;white-space:nowrap;scroll-snap-align:start}
}
.fBadge{display:inline-flex;min-width:22px;height:22px;padding:0 6px;border-radius:11px;background:#fff;color:var(--main);font-size:12px;font-weight:700;align-items:center;justify-content:center}
.protoNote{margin-top:12px;font-size:var(--fs-body-sm);color:var(--text-weaker)}
.rName img{width:48px;height:48px;object-fit:contain;flex:none}
.avBlue{color:var(--info)}
.pg{background:#fff;cursor:pointer}.pg:disabled{opacity:.4;cursor:not-allowed}
.propTag{margin-left:8px;font-size:11px;font-weight:600;text-transform:uppercase;letter-spacing:.04em;background:#fff7d6;color:#5c4a00;padding:1px 6px;border-radius:999px;vertical-align:middle}
.fSearch{display:flex;align-items:center;gap:8px;border:1px solid var(--input-border);border-radius:var(--btn-radius);padding:0 10px;height:40px;margin-bottom:8px;clear:both}
.fSearch input{border:0;outline:0;flex:1;min-width:0;height:100%}
.fList{clear:both}
.fCheck small{margin-left:auto}
.fCheck.dis{color:var(--text-muted);cursor:not-allowed}
.fChips{display:flex;flex-wrap:wrap;gap:6px;clear:both}
.fchip{display:inline-flex;align-items:center;gap:4px;min-height:36px;padding:0 12px;border:1px solid var(--input-border);border-radius:var(--btn-radius);background:#fff;cursor:pointer;font-size:var(--fs-body-sm)}
.fchip small{color:var(--text-muted)}
.fchip.on{background:var(--primary-d);border-color:var(--primary-d);color:#fff}.fchip.on small{color:rgba(255,255,255,.7)}
.fchip:disabled{opacity:.4;cursor:not-allowed}
.fFoot{display:flex;gap:8px}.fFoot .btn-main{flex:1}.fFoot .btn-out{flex:none}
@supports (corner-shape:squircle){.fchip,.perPage select{corner-shape:var(--corner-shape)}}
@media (max-width:1149px){.subGrid{grid-template-columns:repeat(4,minmax(0,1fr))}}
"""
VEL = ['30/0', '20/0', '12/0', '10/0', '5/0', '3/0', '2/0', '000', '0', '1', '2', '3', '4', '5', '6', '8', '10', '12', '16', '18', '20', '24', '1/8"', '1/4"', '1/2"']
GROUPS = [
 dict(key='av', title='Dostupnost', type='check', vals=['Skladem', 'Na objednávku'], prop=True),
 dict(key='akce', title='Akce', type='check', vals=['Ve slevě'], prop=True),
 dict(key='brand', title='Výrobce', type='check', vals=['Ami', 'Darwi', 'Knorr Prandell', 'Meyco', 'Pebeo', 'Royal & Langnickel', 'Sizzix', 'Talens', 'Van Gogh'], search=True, collapse=6),
 dict(key='mat', title='Material', type='check', vals=['Přírodní', 'Syntetický']),
 dict(key='tvar', title='Tvar', type='check', vals=['Dagger (dýkový)', 'Filbert', 'Hřebenový (comb)', 'Kulatý', 'Monogram', 'Plochý', 'Rigger / linkovací', 'Shader (plochý krátky)', 'Šikmý', 'Spotter (detailní, bodový)', 'Stippler', 'Vějířový'], collapse=6),
 dict(key='vel', title='Velikost', type='chip', vals=VEL, collapse=12),
 dict(key='urc', title='Určení', type='chip', vals=['Akvarel', 'Akryl', 'Olej', 'Univerzální', 'Miniatury'], prop=True),
 dict(key='bal', title='Balení', type='chip', vals=['Jednotlivě', 'Sada / set'], prop=True),
 dict(key='ks', title='Počet ks v sadě', type='chip', vals=['3', '4', '5', '6', '7', '8', '9', '10', '12'], prop=True),
 dict(key='delka', title='Délka násady', type='chip', vals=['Krátká', 'Dlouhá'], prop=True),
]
SUBT = [{'n': s['n'], 'c': s['c'], 'img': s.get('img')} for s in CAT['subs']]
kat_js = r"""
 pageState(){return {perex:false,view:'tile',sort:0,sel:{},more:{},fq:'',pMin:0,pMax:PTOP,filter:false,rq:{},ps:24,page:1,shown:1};}
 pageVals(){
  const s=this.state; const sel=s.sel;
  const base=DATA.listStetce.map(byId);
  const get={av:(p)=>[p.stock>0?'Skladem':'Na objednávku'],akce:(p)=>p.flags.some((f)=>f.cls==='discount')?['Ve slevě']:[],brand:(p)=>[p.brand],
   mat:(p)=>p.a&&p.a.mat?[p.a.mat]:[],tvar:(p)=>p.a&&p.a.tvar?[p.a.tvar]:[],vel:(p)=>(p.a&&p.a.vel)||[],urc:(p)=>p.a&&p.a.urc?[p.a.urc]:[],
   bal:(p)=>p.a&&p.a.bal?[p.a.bal]:[],ks:(p)=>p.a&&p.a.ks>1?[String(p.a.ks)]:[],delka:(p)=>p.a&&p.a.delka?[p.a.delka]:[]};
  const match=(p,except)=>p.price>=s.pMin&&p.price<=s.pMax&&GROUPS.every((g)=>g.key===except||!(sel[g.key]||[]).length||get[g.key](p).some((v)=>sel[g.key].includes(v)));
  const tog=(k,v)=>{const a=sel[k]||[];this.setState({sel:Object.assign({},sel,{[k]:a.includes(v)?a.filter((x)=>x!==v):a.concat([v])}),page:1,shown:1});};
  let list=base.filter((p)=>match(p,null));
  if(s.sort===1)list=list.slice().sort((a,b)=>b.stock-a.stock);
  if(s.sort===2)list=list.slice().sort((a,b)=>b.price-a.price);
  if(s.sort===3)list=list.slice().sort((a,b)=>a.price-b.price);
  const cnt=(k,v)=>base.filter((p)=>match(p,k)&&get[k](p).includes(v)).length;
  const groups=GROUPS.map((g)=>{
   let vals=g.vals.map((v)=>{const c=cnt(g.key,v);const on=(sel[g.key]||[]).includes(v);
     return {n:v,count:String(c),on:on,dis:c===0&&!on,pressed:on?'true':'false',cls:'fCheck'+(c===0&&!on?' dis':''),chipCls:'fchip'+(on?' on':''),toggle:()=>tog(g.key,v),c:c};});
   if(g.search&&s.fq)vals=vals.filter((v)=>v.n.toLowerCase().includes(s.fq.toLowerCase()));
   if(g.type==='check')vals=vals.slice().sort((a,b)=>(b.c>0)-(a.c>0));
   const lim=g.collapse||999; const exp=!!s.more[g.key];
   return {key:g.key,title:g.title,prop:!!g.prop,searchable:!!g.search,q:s.fq,onQ:(e)=>this.setState({fq:e.target.value}),
    isCheck:g.type==='check',isChip:g.type==='chip',vals:exp?vals:vals.slice(0,lim),canMore:vals.length>lim,exp:exp?'true':'false',
    moreTxt:exp?'Zobrazit méně':'Zobrazit další ('+(vals.length-lim)+')',toggleMore:()=>this.setState({more:Object.assign({},s.more,{[g.key]:!exp})})};});
  const active=[];GROUPS.forEach((g)=>(sel[g.key]||[]).forEach((v)=>active.push({label:(g.key==='vel'?'Velikost ':g.key==='ks'?'Sada ':'')+v,remove:()=>tog(g.key,v)})));
  if(s.pMin>0||s.pMax<PTOP)active.push({label:s.pMin+'–'+s.pMax+' Kč',remove:()=>this.setState({pMin:0,pMax:PTOP})});
  const ps=s.ps; const pages=Math.max(1,Math.ceil(list.length/ps)); const page=Math.min(s.page,pages);
  const start=(page-1)*ps; const shownItems=list.slice(start,start+ps*s.shown);
  const lastShownPage=Math.min(pages,page+s.shown-1);
  const num=(v)=>{const n=parseInt(String(v).replace(/\D/g,''),10);return isNaN(n)?0:n;};
  const tvarG=GROUPS.find((g)=>g.key==='tvar');
  return {
   perexCls:'perex'+(s.perex?' open':''),perexOpen:s.perex?'true':'false',perexBtn:s.perex?'Zobrazit méně':'Zobrazit více',togglePerex:()=>this.setState({perex:!s.perex}),
   subTiles:SUBT.map((t)=>({n:t.n,c:t.c,img:t.img||'',hasImg:!!t.img,noImg:!t.img})),
   quickChips:tvarG.vals.map((v)=>({v:v,c:cnt('tvar',v)})).filter((x)=>x.c>0||(sel.tvar||[]).includes(x.v)).map((x)=>{const on=(sel.tvar||[]).includes(x.v);
     return {n:x.v,count:String(x.c),cls:'chip'+(on?' on':''),pressed:on?'true':'false',dis:false,toggle:()=>tog('tvar',x.v)};}),
   sorts:['Top','Nejprodávanější','Od nejdražšího','Od nejlevnějšího'].map((n,i)=>({n:n,cls:'sortBtn'+(s.sort===i?' on':''),pressed:s.sort===i?'true':'false',pick:()=>this.setState({sort:i})})),
   isTile:s.view==='tile',isRow:s.view==='row',vIndCls:'vInd'+(s.view==='tile'?'':' r'),vTileCls:'vBtn'+(s.view==='tile'?' on':''),vRowCls:'vBtn'+(s.view==='row'?' on':''),
   setTile:()=>this.setState({view:'tile'}),setRow:()=>this.setState({view:'row'}),
   ps:String(ps),setPs:(e)=>this.setState({ps:num(e.target.value)||15,page:1,shown:1}),
   groups:groups,activeChips:active,hasActive:active.length>0,activeCount:String(active.length),
   clearAll:()=>this.setState({sel:{},pMin:0,pMax:PTOP,page:1,shown:1}),
   countTxt:'Zobrazeno '+shownItems.length+' z '+list.length+' produktů.',
   items:shownItems.map((p)=>Object.assign(card(p),{href:'DetailVariant.dc.html',priceTxt:(p.from?'od ':'')+CZK(p.price),vatTxt:(p.from?'od ':'')+CZK(p.price*VAT),qid:'rq'+p.id,rq:s.rq[p.id]||0,hasImg:!!p.img,noImg:!p.img,img:p.img||'',avCls:p.stock>0?'avOk':'avBlue',
     setRq:(e)=>this.setState({rq:Object.assign({},s.rq,{[p.id]:num(e.target.value)})})})),
   hasItems:list.length>0,noItems:list.length===0,count:String(list.length),
   hasMore:lastShownPage<pages,moreN:String(Math.min(ps,list.length-(start+shownItems.length))),showMore:()=>this.setState({shown:s.shown+1}),
   pagesList:Array.from({length:pages},(_,i)=>({n:String(i+1),cls:'pg'+(i+1>=page&&i+1<=lastShownPage?' on':''),cur:i+1===page?'page':'false',go:()=>this.setState({page:i+1,shown:1})})),
   prevDis:page<=1,nextDis:lastShownPage>=pages,prevPage:()=>this.setState({page:page-1,shown:1}),nextPage:()=>this.setState({page:lastShownPage+1,shown:1}),
   allToCart:()=>{const ids=Object.keys(s.rq).filter((k)=>s.rq[k]>0);
     if(!ids.length){this.toastMsg('Vyplňte množství alespoň u jednoho produktu.',true);return;}
     const cart=s.cart.slice(); ids.forEach((k)=>{const id=+k;const i=cart.findIndex((l)=>l.id===id);if(i>=0)cart[i]={id:id,qty:cart[i].qty+s.rq[k]};else cart.push({id:id,qty:s.rq[k]});});
     this.setState({cart:cart,rq:{}});this.toastMsg('Do košíku přidáno '+ids.length+' produktů.');},
   filterOpen:s.filter,openFilter:()=>this.setState({filter:true}),closeFilter:()=>this.setState({filter:false}),
   filterKey:this.esc(()=>this.setState({filter:false})),filterOverlay:(e)=>{if(e.target===e.currentTarget)this.setState({filter:false});},
   pTop:PTOP,pMin:s.pMin,pMax:s.pMax,setPMin:(e)=>this.setState({pMin:Math.min(num(e.target.value),s.pMax),page:1}),setPMax:(e)=>this.setState({pMax:Math.max(Math.min(num(e.target.value),PTOP),s.pMin),page:1})
  };
 }
"""
ptop = int(max(PR[i]['price'] for i in D['listStetce']) // 50 + 1) * 50
pre = 'const GROUPS=' + json.dumps([{k: v for k, v in g.items()} for g in GROUPS], ensure_ascii=False) + ';\nconst SUBT=' + json.dumps(SUBT, ensure_ascii=False) + f';\nconst PTOP={ptop};\n'
kat_css += """
.chip.on{background:var(--primary);border-color:var(--primary)}
.viewSw{position:relative;display:grid;grid-template-columns:1fr 1fr;isolation:isolate}
.vInd{position:absolute;z-index:0;top:3px;bottom:3px;left:3px;width:calc(50% - 4px);border-radius:calc(var(--btn-radius) - 3px);background:var(--primary);transition:transform .32s cubic-bezier(.34,1.3,.5,1);will-change:transform}
.vInd.r{transform:translateX(calc(100% + 2px))}
.viewSw .vBtn{position:relative;z-index:1;justify-content:center;background:transparent!important}
.viewSw .vBtn.on{color:#fff}
.viewSw .vBtn:not(.on):hover{color:var(--primary-d)}
.vBtn{transition:color .25s}
.ProductsView,.rowsBox{animation:viewIn .35s ease-out}
@keyframes viewIn{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}
@media (prefers-reduced-motion:reduce){.vInd,.ProductsView,.rowsBox{transition:none;animation:none}}
.viewSw{gap:2px;padding:3px;background:#fff}
.vBtn{min-height:38px;border-radius:calc(var(--btn-radius) - 3px);color:var(--text-weaker);transition:background .15s,color .15s}
.vBtn:hover{background:var(--primary-10);color:var(--text)}
.vBtn.on{background:var(--primary);color:#fff;font-weight:600}
.vBtn.on:hover{background:var(--primary-d);color:#fff}
.seo{max-width:80ch}
.seo h3{font-size:var(--fs-h4);margin:24px 0 6px}
.seo p,.seo li{color:var(--text-weaker);line-height:1.65}
.seo ul{margin:8px 0 0;padding-left:20px;display:flex;flex-direction:column;gap:6px}
.seo strong{color:var(--text)}
.rName a{font-size:var(--fs-body);font-weight:600;line-height:1.35;color:var(--text);text-decoration:none}
.rName a:hover{text-decoration:underline}
.rName small{display:block;font-size:var(--fs-body-sm);margin-top:2px}
.rows td{padding:10px 12px}
.rName img{width:56px;height:56px}
.sortBtn{min-height:42px;padding:0 16px;border-radius:var(--btn-radius);font-size:var(--fs-body-sm);font-weight:500;transition:background .15s,color .15s}
.sortBtn:hover{background:var(--primary-10);color:var(--text)}
.sortBtn.on{background:var(--primary);color:#fff;box-shadow:none;font-weight:600}
.sortBtn.on:hover{background:var(--primary-d);color:#fff}
.sortTabs{gap:4px}
.subGrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:var(--grid-gap);overflow:visible;padding-bottom:0}
.subTile{flex-direction:row;align-items:center;text-align:left;gap:14px;padding:10px 16px 10px 10px;min-height:76px;font-size:var(--fs-body);font-weight:600;line-height:1.3;transition:border-color .15s,box-shadow .15s}
.subTile:hover{box-shadow:0 6px 18px rgba(0,0,0,.08)}
.subTile img,.subTile .ph{width:56px;height:56px;flex:none;object-fit:contain;border-radius:var(--radius-sm);background:#fff}
.subName{min-width:0}
@media (max-width:819px){.subGrid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));overflow:visible}.subTile{flex:initial;min-height:64px;padding:8px 12px 8px 8px;gap:10px;font-size:var(--fs-body-sm)}.subTile img,.subTile .ph{width:44px;height:44px}}
@media (max-width:549px){.subGrid{grid-template-columns:1fr}}
"""
pages['Kategorie'] = shop_page('Štětce pomůcky – výpis', kat_css, kat_html, kat_js, 4000, 'Štětce pomůcky').replace('class Component extends DCLogic {', pre + 'class Component extends DCLogic {', 1)

# ======================= DETAIL =======================
dp = PR[IDS['detail']]
det_html = P0.det_html
rep = [
 ('l1="Štětce a pomůcky" h1="Kategorie.dc.html" l2="Sady štětců" h2="Kategorie.dc.html" current="Meyco sada plochých štětců syntetické č. 12 16 20"', f'l1="Štětce pomůcky" h1="Kategorie.dc.html" l2="Sady štětců" h2="Kategorie.dc.html" current="{dp["name"]}"'),
 ('<h1>Meyco sada plochých štětců syntetické č. 12 16 20</h1>', f'<h1>{dp["name"]}</h1>'),
 ('<span class="ph">[FOTO {{ imgNo }} / 4]</span>', '<img src="' + dp['img'] + '" alt="' + dp['name'] + '">'),
 ('<div class="ph lbImg">[FOTO {{ imgNo }} / 4]</div>', '<div class="lbImg"><img src="' + dp['img'] + '" alt="' + dp['name'] + '"></div>'),
 ('<div class="lbCount">{{ imgNo }} / 4</div>', '<div class="lbCount">1 / 1 <span class="todo">[další fotografie doplnit]</span></div>'),
 ('<div class="flags"><span class="flagX">Doporučujeme</span></div>\n', ''),
 ('<div class="bigPrice">69,38&nbsp;Kč <small>bez DPH</small></div>', '<div class="bigPrice">{{ dPrice }} <small>bez DPH</small></div>'),
 ('<div class="priceSub">83,95&nbsp;Kč s DPH', '<div class="priceSub">{{ dPriceVat }} s DPH'),
 ('<li class="avOk">' + I('check-circle') + 'Skladem &gt; 30 ks</li>', '<li class="avLi"><dc-import name="Availability" stock="50" text="Skladem &gt; 50 ks" size="lg" hint-size="240px,28px"></dc-import></li>'),
 ('<dl class="short"><div><dt>Výrobce</dt><dd>Meyco</dd></div><div><dt>Tvar</dt><dd>plochý</dd></div><div><dt>Velikosti</dt><dd>č. 12, 16, 20</dd></div></dl>',
  '<dl class="short"><div><dt>Výrobce</dt><dd>Meyco</dd></div><div><dt>Tvar</dt><dd>Stippler (tupovací)</dd></div><div><dt>Velikosti</dt><dd>15, 25, 35 mm</dd></div><div><dt>Počet v sadě</dt><dd>3 ks</dd></div></dl>'),
 ('<p>Sada tří plochých štětců se syntetickým vlasem ve velikostech 12, 16 a 20. <span class="todo">[DOPLNIT popis z Pohody / webu]</span></p>',
  '<div class="longDesc"><p>MEYCO penové tupovacie štetce sada č. 15 25 35 mm je sada tupovacích štetcov na techniku tupovania a vytváranie jemných farebných prechodov a textúr. Tupovaním cez šablónu vznikajú rovnomerné plochy a tieňované vzory.</p><p>Štetce sa hodia na akrylové, temperové a štruktúrovacie farby pri scrapbookingu, dekorovaní a mixed-media technikách. Pohodlne sa držia a poskytujú dobrú kontrolu. Rôzne veľkosti umožňujú tupovať plochy aj detaily.</p><p>Po práci štetce dôkladne očistite a nechajte vyschnúť. Tým si zachovajú tvar a životnosť. Vhodné sú pre tvorcov, ktorí pracujú so šablónami.</p><p><strong>Kľúčové vlastnosti:</strong></p><ul><li>Sada tupovacích štetcov na techniku tupovania</li><li>Jemné farebné prechody a tieňované vzory</li><li>Vhodné na akrylové a temperové farby</li><li>Tupovanie plôch aj detailov</li><li>Po práci očistiť a nechať vyschnúť</li><li>Rozmery (Š × D × V): 120 × 68 × 50 mm</li></ul></div>'),
 ('<tr><th scope="row">Výrobce</th><td>Meyco</td></tr><tr><th scope="row">Kód</th><td>14235</td></tr><tr><th scope="row">Tvar</th><td>plochý</td></tr><tr><th scope="row">Vlas</th><td>syntetický</td></tr><tr><th scope="row">Velikosti</th><td>č. 12, 16, 20</td></tr><tr><th scope="row">Počet v sadě</th><td>3 ks</td></tr>',
  '<tr><th scope="row">Výrobce</th><td>Meyco</td></tr><tr><th scope="row">Kód</th><td>14217</td></tr><tr><th scope="row">Tvar</th><td>Stippler (tupovací)</td></tr><tr><th scope="row">Materiál</th><td>pěna</td></tr><tr><th scope="row">Velikost</th><td>15, 25, 35 mm</td></tr><tr><th scope="row">Určení</th><td>Univerzální</td></tr><tr><th scope="row">Počet v sadě</th><td>3 ks</td></tr>'),
 ('<div class="accRow"><span class="ph">[FOTO]</span>', '<div class="accRow"><sc-if value="{{ a.hasImg }}" hint-placeholder-val="{{ true }}"><img src="{{ a.img }}" alt=""></sc-if><sc-if value="{{ a.noImg }}" hint-placeholder-val="{{ false }}"><span class="ph">[FOTO]</span></sc-if>'),
]
for a, b in rep:
    assert a in det_html, a[:60]
    det_html = det_html.replace(a, b)
# galerie: jen 1 foto – šipky a náhledy schovat
det_html = det_html.replace('<button class="arrowBtn gArr l"', '<sc-if value="{{ multi }}" hint-placeholder-val="{{ false }}"><button class="arrowBtn gArr l"').replace('onClick="{{ nextImg }}">' + I('caret-right') + '</button></div>\n<div class="thumbs">', 'onClick="{{ nextImg }}">' + I('caret-right') + '</button></sc-if></div>\n<div class="thumbs">')
det_html = det_html.replace('<div class="thumbs"><sc-for list="{{ thumbs }}"', '<div class="thumbs"><sc-for list="{{ thumbs }}"')

# --- Detail: galerie jako komponenta Gallery, příslušenství jako hromadná sekce pod popisem ---
def _cut(s, a, b, repl=''):
    i = s.find(a); assert i >= 0, a[:40]
    j = s.find(b, i); assert j >= 0, b[:40]
    return s[:i] + repl + s[j:]
det_html = _cut(det_html, '<div class="gallery">', '<section class="section acc"', '<dc-import name="Gallery" imgs="{{ gList }}" alt="' + dp['name'] + '" hint-size="100%,560px"></dc-import>\n')
det_html = _cut(det_html, '<section class="section acc"', '<section class="section" id="tabs"')
_i = det_html.find('<sc-if value="{{ lb }}" hint-placeholder-val="{{ false }}">\n<div class="lb"')
assert _i >= 0
_j = det_html.find('</sc-if>', det_html.find('lbCount', _i)) + len('</sc-if>')
det_html = det_html[:_i] + det_html[_j:]
ACC_HTML = """
<section class="section bulkSec" id="prislusenstvi" aria-labelledby="hAcc">
<div class="bulkTop"><div><h2 id="hAcc">Přikupte rovnou k produktu</h2><p>Nastavte množství kvantifikátorem a vložte vše do košíku najednou. Jednotlivé produkty můžete přidat i samostatně ikonou košíku.</p></div>
<button class="btn btn-main btn-lg" type="button" onClick="{{ accAdd }}">""" + I('shopping-cart') + """Vložit vše do košíku<span class="bulkN">{{ accCount }}</span></button></div>
<div class="rowsBox"><table class="rows bulk"><thead><tr><th scope="col">Produkt</th><th scope="col">Dostupnost</th><th scope="col" class="r">Cena bez DPH</th><th scope="col" class="r">Množství a koupit</th></tr></thead>
<tbody><sc-for list="{{ accs }}" as="r" hint-placeholder-count="3"><tr><td><a class="bulkName accName" href="{{ r.href }}"><sc-if value="{{ r.hasImg }}" hint-placeholder-val="{{ true }}"><img src="{{ r.img }}" alt=""></sc-if><sc-if value="{{ r.noImg }}" hint-placeholder-val="{{ false }}"><span class="accPh" aria-hidden="true"></span></sc-if><span>{{ r.name }}</span></a></td><td class="{{ r.avCls }}">{{ r.av }}</td><td class="r">{{ r.priceTxt }}</td><td class="r"><div class="bulkBuy"><div class="qty bq"><button type="button" aria-label="Snížit množství {{ r.name }}" disabled="{{ r.minDis }}" onClick="{{ r.dec }}">−</button><label><span class="sr">Množství {{ r.name }}</span><input id="{{ r.id }}" inputmode="numeric" size="{{ r.qLen }}" value="{{ r.q }}" onChange="{{ r.setQ }}">ks</label><button type="button" aria-label="Zvýšit množství {{ r.name }}" onClick="{{ r.inc }}">+</button></div><button class="btn btn-main bqBuy" type="button" aria-label="{{ r.buyLabel }}" title="Koupit" onClick="{{ r.buy }}">""" + I('shopping-cart') + """</button></div></td></tr></sc-for></tbody></table></div>
</section>"""
_k = det_html.find('</div></section>\n</div>\n<aside class="buyCol"')
assert _k >= 0
_k += len('</div></section>')
det_html = det_html[:_k] + ACC_HTML + det_html[_k:]
det_css = P0.det_css + """
.gBig img{width:100%;height:100%;object-fit:contain;padding:24px}
.longDesc p{margin:0 0 12px}.longDesc ul{margin:0 0 12px;padding-left:20px}.longDesc li{margin:3px 0}
.lbImg{width:min(80vw,900px);height:min(75vh,680px);background:#fff;border-radius:var(--card-radius);display:flex;align-items:center;justify-content:center;padding:24px}
.lbImg img{max-width:100%;max-height:100%;object-fit:contain}
.accRow img{width:56px;height:56px;object-fit:contain}
.thumb img{width:100%;height:100%;object-fit:contain}
"""
det_html = det_html.replace('<span class="ph">{{ t.n }}</span>', '<img src="{{ t.img }}" alt="">')
det_js = P0.det_js.replace("const s=this.state; const go=(i)=>this.setState({img:(i+4)%4}); const p=byId(14);",
                           "const s=this.state; const p=byId(IDS.detail); const IM=[p.img]; const go=(i)=>this.setState({img:(i+IM.length)%IM.length});") \
    .replace("thumbs:[0,1,2,3].map((i)=>({n:i+1,", "dPrice:CZK(p.price), dPriceVat:CZK(p.price*VAT), grpOn:isAuth(), multi:IM.length>1, thumbs:IM.map((u,i)=>({n:i+1,img:u,") \
    .replace("aq:{11:1,12:1,16:1}", "aq:{}") \
    .replace("accs:[11,12,16].map((id)=>{const a=byId(id);const q=s.aq[id]||1;\n     return {name:a.name,", "accs:[IDS.cistic,IDS.pebeoCistic,IDS.tupovaci].map((id)=>{const a=byId(id);const q=s.aq[id]||1;\n     return {name:a.name,img:a.img||'',hasImg:!!a.img,noImg:!a.img,")

assert 'IDS.detail' in det_js and 'IDS.cistic' in det_js
det_js = det_js.replace("multi:IM.length>1,", "gList:IM, multi:IM.length>1,", 1)
det_js = det_js.replace("  };\n  T.forEach((n,i)=>{vals['tab'+i]=s.tab===i;});", r"""   ,accs:ACC.map((id,i)=>{const a=byId(id);const q=s.aq[id]||0;
     return {name:a.name,href:a.href||'Detail.dc.html',img:a.img||'',hasImg:!!a.img,noImg:!a.img,av:avText(a.stock),avCls:a.stock>0?'avOk':'avBlue',priceTxt:CZK(a.price),id:'aq'+i,q:q,qLen:Math.max(1,String(q).length),minDis:!(q>0),buyLabel:'Koupit '+a.name,
      setQ:(e)=>this.setState({aq:Object.assign({},s.aq,{[id]:Math.max(0,parseInt(String(e.target.value).replace(/\D/g,''),10)||0)})}),
      dec:()=>this.setState({aq:Object.assign({},s.aq,{[id]:Math.max(0,q-1)})}),inc:()=>this.setState({aq:Object.assign({},s.aq,{[id]:q+1})}),
      buy:()=>{const n=q>0?q:1;const aq=Object.assign({},s.aq);delete aq[id];this.setState({aq:aq});this.addToCart(a,n);}};}),
   accCount:String(ACC.filter((id)=>s.aq[id]>0).length),
   accAdd:()=>{const ids=ACC.filter((id)=>s.aq[id]>0);if(!ids.length){this.toastMsg('Vyplňte množství alespoň u jednoho produktu.',true);return;}
     const cart=s.cart.slice();ids.forEach((id)=>{const j=cart.findIndex((l)=>l.id===id);if(j>=0)cart[j]={id:id,qty:cart[j].qty+s.aq[id]};else cart.push({id:id,qty:s.aq[id]});});
     const items=ids.map((id)=>{const a=byId(id);return {no:'',n:a.name,img:a.img||'',hex:'',q:s.aq[id],price:a.price};});
     this.setState({cart:cart,aq:{},pop:'',dlg:{id:ids[0],qty:ids.reduce((x,id)=>x+s.aq[id],0),shades:items,multi:true}});}
  };
  T.forEach((n,i)=>{vals['tab'+i]=s.tab===i;});""", 1)
det_js = det_js.replace("const IM=[p.img];", "const IM=[p.img,'/_blob/c16151cc66e63a519041f9c2a50eac38','/_blob/5006f279fa16e8860d22d7115444542b']; const ACC=[IDS.cistic,IDS.pebeoCistic,IDS.tupovaci];", 1)
assert 'accAdd' in det_js and 'gList:IM' in det_js and 'const ACC=' in det_js
pages['Detail'] = shop_page('Detail produktu', det_css, det_html, det_js, 2700, 'Štětce pomůcky')

# ======================= POROVNANI =======================
cmp_html = P0.cmp_html.replace('<span class="ph">[FOTO]</span><a href="Detail.dc.html">{{ c.name }}</a>', '<sc-if value="{{ c.hasImg }}" hint-placeholder-val="{{ true }}"><img src="{{ c.img }}" alt=""></sc-if><sc-if value="{{ c.noImg }}" hint-placeholder-val="{{ false }}"><span class="ph">[FOTO]</span></sc-if><a href="Detail.dc.html">{{ c.name }}</a>')
cmp_css = P0.cmp_css + ".cmpProd img{width:120px;height:120px;object-fit:contain}\n"
cmp_js = r"""
 carMove(k,d){const t=document.querySelector('[data-car="'+k+'"]');if(t)t.scrollBy({left:d*t.clientWidth*0.9});}
 pageState(){return {ids:[IDS.detail,IDS.tupovaci,IDS.ploche],onlyDiff:false};}
 pageMount(){if(lsGet('CmpDetail')==='0')this.setState({ids:[IDS.tupovaci,IDS.ploche]});}
 pageVals(){
  const s=this.state; const P=s.ids.map(byId); const A=(p,k,f)=>p.a&&p.a[k]?(f?f(p.a[k]):p.a[k]):'–';
  const R=[['Cena s DPH',(p)=>CZK(p.price*VAT)],['Dostupnost',(p)=>avText(p.stock)],['Výrobce',(p)=>p.brand],['Kód',(p)=>p.code],
   ['Tvar',(p)=>A(p,'tvar')],['Material',(p)=>A(p,'mat')||'–'],['Velikosti',(p)=>p.a&&p.a.vel&&p.a.vel.length?p.a.vel.join(', '):'–'],['Počet v sadě',(p)=>A(p,'ks',(v)=>v+' ks')],['Určení',(p)=>A(p,'urc')]];
  const rows=R.map((r)=>{const v=P.map((p)=>({t:r[1](p)}));const diff=new Set(v.map((x)=>x.t)).size>1;return {n:r[0],v:v,diff:diff,cls:diff?'diff':''};}).filter((r)=>!s.onlyDiff||r.diff);
  return {
   has:P.length>0,none:P.length===0,onlyDiff:s.onlyDiff,toggleDiff:()=>this.setState({onlyDiff:!s.onlyDiff}),
   cols:P.map((p)=>({name:p.name,img:p.img||'',hasImg:!!p.img,noImg:!p.img,price:CZK(p.price),rmLabel:'Odebrat '+p.name,buy:()=>this.addToCart(p,1),
     remove:()=>{if(p.id===IDS.detail)lsSet('CmpDetail','0');this.setState({ids:s.ids.filter((x)=>x!==p.id)});}})),
   rows:rows,
   removeAll:()=>{lsSet('CmpDetail','0');this.setState({ids:[]});},
   reset:()=>{lsSet('CmpDetail','1');this.setState({ids:[IDS.detail,IDS.tupovaci,IDS.ploche]});},
   share:()=>{try{navigator.clipboard.writeText('https://www.b2bdaver.cz/porovnani?ids='+s.ids.join(','));}catch(e){} this.toastMsg('Odkaz na porovnání zkopírován.');},
   carR:CAR.R.map((i)=>card(byId(i))),
   carRPrev:()=>this.carMove('R',-1),carRNext:()=>this.carMove('R',1)
  };
 }
"""
pages['Porovnani'] = shop_page('Porovnání produktů', cmp_css, cmp_html, cmp_js, 2500)

if __name__ == '__main__':
    for n, c in pages.items():
        write(n + '.dc.html', c.replace('></input>', '>'))
    print(list(pages))

# ======================= DETAIL – VARIANTNÍ PRODUKT (Amsterdam 120 ml) =======================
import html as _html
AV = json.load(open(os.path.join(os.path.dirname(__file__), 'amsterdam_var.json'), encoding='utf-8'))
_po = json.load(open(os.path.join(os.path.dirname(__file__), 'popisy.json'), encoding='utf-8'))['barvy-media/01']['long']
def _long(txt):
    out = []
    for blk in txt.split('\n\n'):
        ls = blk.split('\n')
        if any(l.startswith('- ') for l in ls):
            head = [l for l in ls if not l.startswith('- ')]
            if head: out.append('<p><strong>' + _html.escape(' '.join(head)) + '</strong></p>')
            out.append('<ul>' + ''.join('<li>' + _html.escape(l[2:]) + '</li>' for l in ls if l.startswith('- ')) + '</ul>')
        else: out.append('<p>' + _html.escape(blk) + '</p>')
    return ''.join(out)
VP = PR[1]
GROUPS_ORDER = []
for v in AV:
    if v['g'] not in GROUPS_ORDER: GROUPS_ORDER.append(v['g'])
dv_html = f'''<div class="container">
<dc-import name="Breadcrumb" l1="Barvy média" h1="Kategorie.dc.html" l2="Akrylové barvy" h2="Kategorie.dc.html" current="{VP['name']}" hint-size="100%,48px"></dc-import>
<div class="detGrid">
<div class="detMain">
<div class="detHead"><h1>{VP['name']}</h1>
<div class="detMeta"><button class="{{{{ copyCls }}}}" type="button" aria-label="{{{{ copyLabel }}}}" onClick="{{{{ copyCode }}}}"><span class="ccLbl">Kód</span><strong class="ccCode">{{{{ vCode }}}}</strong><span class="ccIc" aria-hidden="true"><sc-if value="{{{{ notCopied }}}}" hint-placeholder-val="{{{{ true }}}}">{I('copy')}</sc-if><sc-if value="{{{{ copied }}}}" hint-placeholder-val="{{{{ false }}}}">{I('check')}</sc-if></span><span class="ccMsg" aria-live="polite">{{{{ copiedTxt }}}}</span></button><span class="varCount">{len(AV)} odstínů · Amsterdam Standard Series</span></div></div>
<dc-import name="Gallery" imgs="{{{{ gList }}}}" alt="{VP['name']}" chip-hex="{{{{ vHex }}}}" chip-text="{{{{ chipTxt }}}}" hint-size="100%,560px"></dc-import>
<section class="section" id="tabs" aria-label="Informace o produktu">
<div class="tabBar" role="tablist"><sc-for list="{{{{ tabs }}}}" as="t" hint-placeholder-count="4"><button class="{{{{ t.cls }}}}" type="button" role="tab" aria-selected="{{{{ t.sel }}}}" onClick="{{{{ t.pick }}}}">{{{{ t.n }}}}</button></sc-for></div>
<div class="tabPanel" role="tabpanel">
<sc-if value="{{{{ tab0 }}}}" hint-placeholder-val="{{{{ true }}}}"><div class="longDesc">{_long(_po)}</div></sc-if>
<sc-if value="{{{{ tab1 }}}}" hint-placeholder-val="{{{{ false }}}}"><table class="params"><tbody><tr><th scope="row">Výrobce</th><td>Amsterdam (Royal Talens)</td></tr><tr><th scope="row">Produktová řada</th><td>Amsterdam Standard Series</td></tr><tr><th scope="row">Objem</th><td>120 ml</td></tr><tr><th scope="row">Báze</th><td>akrylová, ředitelná vodou</td></tr><tr><th scope="row">Počet odstínů</th><td>{len(AV)}</td></tr><tr><th scope="row">Vybraný odstín</th><td>{{{{ vNo }}}} {{{{ vName }}}}</td></tr></tbody></table></sc-if>
</div></section>
<section class="section bulkSec" id="hromadna" aria-labelledby="hBulk">
<div class="bulkTop"><div><h2 id="hBulk">Hromadná objednávka odstínů</h2><p>Nastavte množství u odstínů kvantifikátorem a vložte vše do košíku najednou. Jednotlivé odstíny můžete přidat i samostatně ikonou košíku.</p></div>
<button class="btn btn-main btn-lg" type="button" onClick="{{{{ bulkAdd }}}}">{I('shopping-cart')}Vložit vše do košíku<span class="bulkN">{{{{ bulkCount }}}}</span></button></div>
<div class="rowsBox"><table class="rows bulk"><thead><tr><th scope="col">Odstín</th><th scope="col">Dostupnost</th><th scope="col" class="r">Cena bez DPH</th><th scope="col" class="r">Množství a koupit</th></tr></thead>
<tbody><sc-for list="{{{{ bulkRows }}}}" as="r" hint-placeholder-count="10"><tr><td><span class="bulkName"><span class="shadeDot" style="background:{{{{ r.hex }}}}"></span>{{{{ r.no }}}} {{{{ r.n }}}}</span></td><td class="{{{{ r.avCls }}}}">{{{{ r.av }}}}</td><td class="r">{{{{ r.priceTxt }}}}</td><td class="r"><div class="bulkBuy"><div class="qty bq"><button type="button" aria-label="Snížit množství {{{{ r.n }}}}" disabled="{{{{ r.minDis }}}}" onClick="{{{{ r.dec }}}}">−</button><label><span class="sr">Množství {{{{ r.n }}}}</span><input id="{{{{ r.id }}}}" inputmode="numeric" size="{{{{ r.qLen }}}}" value="{{{{ r.q }}}}" onChange="{{{{ r.setQ }}}}">ks</label><button type="button" aria-label="Zvýšit množství {{{{ r.n }}}}" onClick="{{{{ r.inc }}}}">+</button></div><button class="btn btn-main bqBuy" type="button" aria-label="{{{{ r.buyLabel }}}}" title="Koupit" onClick="{{{{ r.buy }}}}">{I('shopping-cart')}</button></div></td></tr></sc-for></tbody></table></div>
</section>
</div>
<aside class="buyCol" aria-label="Nákup">
<div class="buyBox">
<div><div class="bigPrice">{{{{ vPrice }}}} <small>bez DPH</small></div><div class="priceSub">{{{{ vPriceVat }}}} s DPH</div></div>
<div class="varPick">
<div class="varHead"><span class="varLbl">Odstín:</span> <strong>{{{{ vNo }}}} {{{{ vName }}}}</strong></div>
<sc-if value="{{{{ isSelect }}}}" hint-placeholder-val="{{{{ true }}}}">
<div class="dd" onKeyDown="{{{{ ddKey }}}}">
<button class="ddBtn" type="button" aria-haspopup="listbox" aria-expanded="{{{{ ddOpenStr }}}}" aria-label="{{{{ ddAria }}}}" onClick="{{{{ ddToggle }}}}"><span class="shadeDot" style="background:{{{{ vHex }}}}" aria-hidden="true"></span><span class="ddVal"><strong>{{{{ vNo }}}} {{{{ vName }}}}</strong><small class="{{{{ vAvCls }}}}">{{{{ vAv }}}}</small></span><span class="ddCaret" aria-hidden="true">{I('caret-down')}</span></button>
<sc-if value="{{{{ ddOpen }}}}" hint-placeholder-val="{{{{ false }}}}">
<div class="ddPop">
<div class="ddList" role="listbox" aria-label="Odstíny"><sc-for list="{{{{ ddGroups }}}}" as="g" hint-placeholder-count="3"><div class="ddGrp" role="group" aria-label="{{{{ g.label }}}}"><div class="ddGLbl">{{{{ g.label }}}}</div><sc-for list="{{{{ g.items }}}}" as="o" hint-placeholder-count="5"><button class="{{{{ o.cls }}}}" type="button" role="option" aria-selected="{{{{ o.sel }}}}" data-dd="{{{{ o.idx }}}}" onClick="{{{{ o.pick }}}}" onMouseEnter="{{{{ o.hover }}}}"><span class="shadeDot" style="background:{{{{ o.hex }}}}" aria-hidden="true"></span><span class="ddOName">{{{{ o.no }}}} {{{{ o.n }}}}</span><span class="{{{{ o.avCls }}}}">{{{{ o.av }}}}</span><span class="ddOPrice">{{{{ o.price }}}}</span><sc-if value="{{{{ o.isSel }}}}" hint-placeholder-val="{{{{ false }}}}"><span class="ddCheck" aria-hidden="true">{I('check')}</span></sc-if></button></sc-for></div></sc-for>
<sc-if value="{{{{ swNone }}}}" hint-placeholder-val="{{{{ false }}}}"><p class="swNone">Žádný odstín neodpovídá hledání.</p></sc-if></div>
</div>
</sc-if>
</div>
</sc-if>
<sc-if value="{{{{ isSwatch }}}}" hint-placeholder-val="{{{{ false }}}}">
<div class="swGroups"><sc-for list="{{{{ swGroups }}}}" as="g" hint-placeholder-count="3"><div class="swGroup"><div class="swGLbl">{{{{ g.label }}}}</div><div class="swatches" role="radiogroup" aria-label="{{{{ g.label }}}}"><sc-for list="{{{{ g.items }}}}" as="w" hint-placeholder-count="8"><button class="{{{{ w.cls }}}}" type="button" role="radio" aria-checked="{{{{ w.on }}}}" aria-label="{{{{ w.aria }}}}" title="{{{{ w.title }}}}" style="background:{{{{ w.hex }}}}" onClick="{{{{ w.pick }}}}"></button></sc-for></div></div></sc-for>
</div>
</sc-if>
</div>
<ul class="avPanel"><li class="avLi"><dc-import name="Availability" stock="{{{{ vSt }}}}" text="{{{{ vAv }}}}" size="lg" hint-size="240px,28px"></dc-import></li><sc-if value="{{{{ vOnStock }}}}" hint-placeholder-val="{{{{ true }}}}"><li>{I('storefront')}Osobně na prodejně: <strong>zítra</strong></li><li>{I('truck')}Přepravní společností: <strong>pozítří</strong></li></sc-if></ul>
<div class="buyRow"><div class="qty"><button type="button" aria-label="Snížit množství" disabled="{{{{ minDis }}}}" onClick="{{{{ dec }}}}">−</button><label><input inputmode="numeric" aria-label="Množství" size="{{{{ qtyLen }}}}" value="{{{{ qty }}}}" onChange="{{{{ setQty }}}}">ks</label><button type="button" aria-label="Zvýšit množství" onClick="{{{{ inc }}}}">+</button></div><button class="btn btn-main btn-lg" type="button" disabled="{{{{ buyDis }}}}" onClick="{{{{ buy }}}}">{I('shopping-cart')}Koupit</button></div>
<button class="btn btn-ghost" type="button" onClick="{{{{ toBulk }}}}">{I('rows')}Objednat více odstínů najednou</button>
</div>
</aside>
</div>
</div>
'''
dv_css = P0.det_css + """
.bulkSec{margin-top:var(--section-gap)}
.bulkTop{display:flex;justify-content:space-between;align-items:flex-end;gap:16px 24px;flex-wrap:wrap;margin-bottom:16px}
.bulkTop h2{font-size:var(--fs-h2);margin-bottom:6px}
.bulkTop p{color:var(--text-weaker);max-width:60ch;margin:0}
.bulkN{display:inline-flex;align-items:center;justify-content:center;min-width:24px;height:24px;padding:0 7px;margin-left:4px;border-radius:12px;background:var(--primary);color:#fff;font-size:13px;font-weight:700}
.bulkSec{min-width:0;max-width:100%}
.bulkSec .rowsBox{max-height:none;overflow-x:auto;overflow-y:hidden;max-width:100%;padding-bottom:8px}
.gallery,.gMain,.gTrack{min-width:0;max-width:100%}
.swatches{flex-wrap:wrap;min-width:0}
@media (max-width:639px){.bulkSec .rowsBox{overflow:visible}.rows.bulk{min-width:0}.rows.bulk thead{display:none}
 .rows.bulk,.rows.bulk tbody{display:block}.rows.bulk tr{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:4px 12px;padding:12px 14px;border-bottom:1px solid var(--line)}
 .rows.bulk td{display:block;padding:0!important;border:0}.rows.bulk td:nth-child(1){grid-column:1/-1}.rows.bulk td:nth-child(2){grid-column:1}.rows.bulk td:nth-child(3){grid-column:2;grid-row:2;font-weight:600}
 .rows.bulk td:nth-child(4){grid-column:1/-1;text-align:left;margin-top:6px}.rows.bulk .bulkBuy{display:flex;justify-content:space-between}
 .bulkTop{flex-direction:column;align-items:stretch}.bulkTop .btn{width:100%;justify-content:center}}
.bulkSec .rows.bulk tbody tr:last-child td{padding-bottom:16px}
.bulkBuy{display:inline-flex;align-items:center;gap:8px;justify-content:flex-end}
.qty.bq{height:40px;min-width:120px}
.qty.bq button{width:36px}.qty.bq button:disabled{color:#c4c4c8;cursor:default}
.bqBuy{width:40px;min-height:40px;height:40px;padding:0;flex:none}
.bqBuy .ic{width:20px;height:20px}
.rows.bulk td{vertical-align:middle}
.gBig img{width:100%;height:100%;object-fit:contain;padding:24px}
.gallery.one{grid-template-columns:1fr}.gallery.one .gMain{grid-column:1}
.lb{flex-direction:column;gap:16px;padding:64px 16px 20px}
.lbStage{position:relative;display:flex;align-items:center;justify-content:center;gap:16px;flex:1;min-height:0;width:100%}
.lb .lbImg{width:min(80vw,1000px);height:100%;max-height:calc(100dvh - 220px)}
.lbNav{flex:none;background:rgba(255,255,255,.12)!important;color:#fff!important;border-color:rgba(255,255,255,.3)!important}
.lbNav:hover{background:rgba(255,255,255,.24)!important}
.lbFoot{display:flex;flex-direction:column;align-items:center;gap:10px;max-width:100%}
.lbNum{color:#fff;font-size:var(--fs-body-sm)}
.lbThumbs{display:flex;gap:10px;overflow-x:auto;scrollbar-width:none;max-width:100%;padding:2px}
.lbThumbs::-webkit-scrollbar{display:none}
.lbTh{flex:none;width:72px;height:72px;padding:4px;background:#fff;border:2px solid transparent;border-radius:var(--radius-sm);cursor:pointer;opacity:.55;transition:opacity .2s,border-color .2s,transform .15s}
.lbTh:hover{opacity:.85;transform:translateY(-2px)}
.lbTh.on{opacity:1;border-color:var(--primary)}
.lbTh img{width:100%;height:100%;object-fit:contain}
@media (max-width:819px){.lbStage{gap:0}.lbNav{position:absolute;z-index:1}.lbNav.l{left:4px}.lbNav.r{right:4px}.lb .lbImg{width:100%}.lbTh{width:56px;height:56px}}
.gTrack{display:flex;overflow-x:auto;scroll-snap-type:x mandatory;scroll-behavior:smooth;scrollbar-width:none;border:1px solid var(--line);border-radius:var(--card-radius);background:#fff;aspect-ratio:4/3;overscroll-behavior-x:contain}
.gTrack::-webkit-scrollbar{display:none}
.gSlide{flex:0 0 100%;scroll-snap-align:center;scroll-snap-stop:always;border:0;background:#fff;padding:0;cursor:zoom-in;display:flex;align-items:center;justify-content:center}
.gSlide img{width:100%;height:100%;object-fit:contain;padding:24px}
.vg .gArr{opacity:1;z-index:3;background:rgba(255,255,255,.92);box-shadow:0 2px 10px rgba(0,0,0,.12)}
.vg .thumb{transition:outline-color .2s,transform .15s}.vg .thumb:hover{transform:translateY(-2px)}
.gallery.vg{grid-template-columns:minmax(0,1fr)!important;position:relative}
.vg .gMain{grid-column:1!important;grid-row:1!important}
.vg .thumbs{position:absolute;top:12px;left:12px;z-index:2;grid-row:auto!important;flex-direction:column!important;gap:8px;overflow:visible!important;max-height:calc(100% - 24px)}
.vg .thumb{width:56px!important;height:56px!important;padding:4px;box-shadow:0 2px 8px rgba(0,0,0,.08)}
.vg .thumb{display:block;overflow:hidden;box-sizing:border-box}.vg .thumb img{display:block;width:100%;height:100%;object-fit:contain}
.vg .gArr.l{left:12px}.vg .gArr.r{right:12px}
.gDots{display:none;position:absolute;left:0;right:0;bottom:-28px;justify-content:center;align-items:center;gap:6px}
.gDot{width:8px;height:8px;border-radius:999px;border:0;padding:0;background:var(--input-border);transition:width .3s cubic-bezier(.4,0,.2,1),background .3s}
.gDot.on{width:24px;background:var(--primary)}
@media (max-width:819px){.vg .thumbs{display:none}.vg .gArr{width:40px;height:40px}.vg .gArr.l{left:8px}.vg .gArr.r{right:8px}.gDots{display:flex}.vg{margin-bottom:28px}.vg .shadeChip{bottom:12px}}
@media (prefers-reduced-motion:reduce){.gTrack{scroll-behavior:auto}.gDot{transition:none}}
.lbImg{width:min(80vw,900px);height:min(75vh,680px);background:#fff;border-radius:var(--card-radius);display:flex;align-items:center;justify-content:center;padding:24px}
.lbImg img{max-width:100%;max-height:100%;object-fit:contain}
.longDesc p{margin:0 0 12px}.longDesc ul{margin:0 0 12px;padding-left:20px}.longDesc li{margin:3px 0}
.varCount{margin-left:12px;color:var(--text-weaker)}
.shadeChip{position:absolute;left:12px;bottom:12px;display:flex;align-items:center;gap:8px;background:rgba(255,255,255,.95);border:1px solid var(--line);border-radius:12px;padding:4px 12px 4px 4px;font-size:var(--fs-body-sm);font-weight:600}
.shadeChip .shadeDot{border-radius:8px}
.shadeDot{display:inline-block;width:24px;height:24px;border-radius:8px;border:1px solid rgba(0,0,0,.15);flex:none}
.shadeDot.big{width:44px;height:44px;border-radius:14px}
.varPick{display:flex;flex-direction:column;gap:10px}
.varHead{font-size:var(--fs-body-sm)}.varLbl{color:var(--text-weaker)}
.varSelect{display:flex;gap:10px;align-items:center}
.varSelect select{flex:1;min-width:0;height:48px;border:1px solid var(--input-border);border-radius:var(--btn-radius);padding:0 12px;background:#fff;font-size:var(--fs-body-sm)}
.varSelect select:focus{outline:2px solid var(--primary-d);outline-offset:1px}
.swSearch{display:flex;align-items:center;gap:8px;border:1px solid var(--input-border);border-radius:var(--btn-radius);padding:0 10px;height:40px}
.swSearch input{flex:1;min-width:0;border:0;outline:0;height:100%;background:transparent}
.swGroups{display:flex;flex-direction:column;gap:12px;padding:2px 4px 4px 2px}
.swGLbl{font-size:var(--fs-caption);text-transform:uppercase;letter-spacing:.05em;color:var(--text-muted);margin-bottom:6px}
.swatches{display:flex;flex-wrap:wrap;gap:8px}
/* barevné vzorky – squircle s větším poloměrem */
.sw{position:relative;width:40px;height:40px;border-radius:14px;border:1px solid rgba(0,0,0,.14);cursor:pointer;padding:0;transition:transform .12s,box-shadow .12s}
.sw:hover{transform:scale(1.08)}
.sw.on{box-shadow:0 0 0 2px #fff,0 0 0 4px var(--primary-d)}
.sw.out::after{content:"";position:absolute;inset:0;border-radius:inherit;background:linear-gradient(135deg,transparent calc(50% - 1px),rgba(255,255,255,.95) calc(50% - 1px),rgba(255,255,255,.95) calc(50% + 1px),transparent calc(50% + 1px))}
.sw.out{opacity:.75}
.swNone{font-size:var(--fs-body-sm);color:var(--text-weaker)}
@supports (corner-shape:squircle){.sw,.shadeDot,.varSelect select,.shadeChip,.ddBtn,.ddPop{corner-shape:squircle}.sw,.shadeDot.big{border-radius:18px}.shadeChip{border-radius:18px}.shadeChip .shadeDot{border-radius:14px}}
.bulkHead{display:flex;justify-content:space-between;align-items:center;gap:16px;flex-wrap:wrap;margin-bottom:12px}
.bulkHead p{color:var(--text-weaker);max-width:60ch}
.rowsBox{overflow-x:auto;border:1px solid var(--line);border-radius:var(--card-radius);max-height:560px;overflow-y:auto}
.rows{width:100%;border-collapse:collapse;font-size:var(--fs-body-sm);min-width:620px}
.rows th{text-align:left;font-weight:600;color:var(--text-weaker);padding:10px 12px;border-bottom:1px solid var(--line);background:var(--bg-soft);position:sticky;top:0}
.rows td{padding:6px 12px;border-bottom:1px solid var(--line)}
.rows .r{text-align:right}
.bulkName{display:inline-flex;align-items:center;gap:10px;font-weight:600}
.rowQty{width:64px;height:36px;border:1px solid var(--input-border);border-radius:var(--btn-radius);text-align:right;padding:0 8px}
.avOk{color:var(--success-text)}.avBlue{color:var(--info)}
.tabPanel{max-width:none}
@media (prefers-reduced-motion:reduce){.sw{transition:none}.sw:hover{transform:none}}

/* vlastní dropdown odstínů */
.dd{position:relative}
.ddBtn{display:flex;align-items:center;gap:12px;width:100%;min-height:56px;padding:6px 14px 6px 6px;border:1px solid var(--input-border);border-radius:var(--card-radius);background:#fff;cursor:pointer;text-align:left;transition:border-color .15s,box-shadow .15s}
.ddBtn:hover{border-color:var(--primary-d)}
.ddBtn[aria-expanded="true"]{border-color:var(--primary-d);box-shadow:0 0 0 3px var(--primary-10)}
.ddBtn .shadeDot{width:44px;height:44px;border-radius:max(4px,calc(var(--card-radius) - 6px))}
.ddVal{flex:1;min-width:0;display:flex;flex-direction:column;line-height:1.25}
.ddVal strong{font-size:var(--fs-body-sm);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.ddVal small{font-size:var(--fs-caption)}
.ddCaret{display:flex;align-items:center;justify-content:center;width:28px;height:28px;border-radius:50%;background:var(--primary-10);color:var(--primary-d);flex:none;transition:transform .2s}
.ddBtn[aria-expanded="true"] .ddCaret{transform:rotate(180deg)}
.ddCaret .ic{width:16px;height:16px}
.ddPop{position:absolute;left:0;right:0;top:calc(100% + 6px);z-index:50;background:#fff;border:1px solid var(--line);border-radius:var(--card-radius);box-shadow:0 16px 40px rgba(0,0,0,.16);overflow:hidden;animation:ddIn .15s ease}
@keyframes ddIn{from{opacity:0;transform:translateY(-4px)}to{opacity:1;transform:none}}
.ddList{max-height:360px;overflow:auto;padding:0 0 4px;overscroll-behavior:contain}
.ddGLbl{position:sticky;top:0;margin:0;background:#fff;font-size:var(--fs-caption);text-transform:uppercase;letter-spacing:.05em;color:var(--text-muted);padding:8px 12px 6px;z-index:2;box-shadow:0 1px 0 var(--line)}
.ddOpt{display:grid;grid-template-columns:28px minmax(0,1fr) auto auto 18px;gap:10px;align-items:center;width:100%;min-height:44px;padding:6px 12px;border:0;background:transparent;cursor:pointer;text-align:left;font-size:var(--fs-body-sm)}
.ddOpt .shadeDot{width:28px;height:28px;border-radius:10px}
.ddOpt.act{background:var(--primary-10)}
.ddOpt.sel .ddOName{font-weight:700}
.ddOName{white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.ddOpt .avOk,.ddOpt .avBlue{font-size:var(--fs-caption);white-space:nowrap}
.ddOPrice{font-size:var(--fs-caption);color:var(--text-weaker);white-space:nowrap}
.ddCheck{color:var(--primary-d);display:flex}.ddCheck .ic{width:16px;height:16px}
@supports (corner-shape:squircle){.ddBtn,.ddPop,.ddOpt .shadeDot,.ddBtn .shadeDot{corner-shape:squircle}}
@media (max-width:549px){.ddOpt{grid-template-columns:28px minmax(0,1fr) 18px}.ddOpt .avOk,.ddOpt .avBlue,.ddOPrice{display:none}}
@media (prefers-reduced-motion:reduce){.ddPop{animation:none}.ddCaret{transition:none}}
"""
dv_js = r"""
 pageState(){return {v:1,ui:'select',vq:'',gi:0,tab:0,qty:1,copied:false,lb:false,bq:{},dd:false,act:1};}
 pageMount(){this.onUi=()=>this.setState({ui:lsGet('VariantUiV1')||'select'});this.onUi();window.addEventListener('daver-variant',this.onUi);window.addEventListener('storage',this.onUi);
  this.onDd=(e)=>{if(this.state.dd&&!(e.target.closest&&e.target.closest('.dd')))this.setState({dd:false,vq:''});};document.addEventListener('mousedown',this.onDd);}
 pageUnmount(){document.removeEventListener('mousedown',this.onDd);window.removeEventListener('daver-variant',this.onUi);window.removeEventListener('storage',this.onUi);clearTimeout(this.ct);}
 pageVals(){
  const s=this.state; const p=byId(1); const v=AV[s.v]; const num=(x)=>{const n=parseInt(String(x).replace(/\D/g,''),10);return isNaN(n)?0:n;};
  const avLabel=(x)=>x.no+' '+x.n+' · '+x.av;
  const syncTrack=()=>setTimeout(()=>{const t=document.querySelector('.vg .gTrack');if(t)t.scrollTo({left:this.state.gi*t.clientWidth,behavior:'auto'});},30);
  const gGo=(e,i)=>{const g=e.currentTarget.closest('.gallery');const t=g&&g.querySelector('.gTrack');if(t)t.scrollTo({left:i*t.clientWidth,behavior:'smooth'});this.setState({gi:i});};
  const q=s.vq.trim().toLowerCase();
  const groups=GORD.map((g)=>({label:g,items:AV.map((x,i)=>Object.assign({},x,{i:i})).filter((x)=>x.g===g).map((x)=>({idx:String(x.i),label:avLabel(x)}))}));
  const swGroups=GORD.map((g)=>({label:g,items:AV.map((x,i)=>Object.assign({},x,{i:i})).filter((x)=>x.g===g&&(!q||(x.no+' '+x.n).toLowerCase().includes(q))).map((x)=>({
    hex:x.hex,on:x.i===s.v?'true':'false',cls:'sw'+(x.i===s.v?' on':'')+(x.st===0?' out':''),aria:x.no+' '+x.n+', '+x.av,title:x.no+' '+x.n+' – '+x.av,pick:()=>this.setState({v:x.i})}))})).filter((g)=>g.items.length);
  const flat=AV.map((x,i)=>Object.assign({},x,{i:i})).filter((x)=>!q||(x.no+' '+x.n).toLowerCase().includes(q));
  const pickV=(i)=>{this.setState({v:i,act:i,dd:false,vq:''});const b=document.querySelector('.ddBtn');if(b)b.focus();};
  const ddGroups=GORD.map((g)=>({label:g,items:flat.filter((x)=>x.g===g).map((x)=>({idx:String(x.i),no:String(x.no),n:x.n,hex:x.hex,av:x.av,avCls:x.st>0?'avOk':'avBlue',price:CZK(x.price),
    isSel:x.i===s.v,sel:x.i===s.v?'true':'false',cls:'ddOpt'+(x.i===s.v?' sel':'')+(x.i===s.act?' act':''),pick:()=>pickV(x.i),hover:()=>this.setState({act:x.i})}))})).filter((g)=>g.items.length);
  const ddKey=(e)=>{if(!s.dd){if(e.key==='ArrowDown'||e.key==='ArrowUp'){e.preventDefault();this.setState({dd:true,act:s.v});}return;}
    const ids=flat.map((x)=>x.i);let k=ids.indexOf(s.act);
    if(e.key==='Escape'){e.stopPropagation();this.setState({dd:false,vq:''});const b=document.querySelector('.ddBtn');if(b)b.focus();}
    else if(e.key==='ArrowDown'||e.key==='ArrowUp'){e.preventDefault();k=Math.max(0,Math.min(ids.length-1,k+(e.key==='ArrowDown'?1:-1)));const n=ids[k];this.setState({act:n});setTimeout(()=>{const el=document.querySelector('[data-dd="'+n+'"]');if(el)el.scrollIntoView({block:'nearest'});},0);}
    else if(e.key==='Enter'&&k>=0){e.preventDefault();pickV(ids[k]);}};
  const T=['Popis','Parametry'];
  const bulkCount=Object.values(s.bq).filter((x)=>x>0).length;
  const vals={
   vIdx:String(s.v),vNo:String(v.no),vName:v.n,vCode:v.code,vHex:v.hex,vPrice:CZK(v.price),grpOn:isAuth(),vPriceVat:CZK(v.price*VAT),vAv:v.av,vSt:v.st,vOnStock:v.st>0,vAvCls:v.st>0?'avOk':'avBlue',
   isSelect:s.ui!=='swatch',isSwatch:s.ui==='swatch',groups:groups,swGroups:swGroups,swNone:(s.ui==='swatch'?swGroups:ddGroups).length===0,
   ddOpen:s.dd,ddOpenStr:s.dd?'true':'false',ddAria:'Odstín: '+v.no+' '+v.n+', '+v.av+'. Změnit odstín',ddToggle:()=>this.setState({dd:!s.dd,act:s.v,vq:''}),ddGroups:ddGroups,ddKey:ddKey,vq:s.vq,onVq:(e)=>this.setState({vq:e.target.value}),
   pickSel:(e)=>this.setState({v:num(e.target.value)}),
   copied:!!s.copied,notCopied:!s.copied,copyCls:'codeCopy'+(s.copied?' done':''),copiedTxt:s.copied?'Zkopírováno do schránky':'',
   copyLabel:s.copied?'Kód '+v.code+' zkopírován do schránky':'Kopírovat kód '+v.code,
   copyCode:()=>{try{navigator.clipboard.writeText(v.code);}catch(e){} this.setState({copied:true});clearTimeout(this.ct);this.ct=setTimeout(()=>this.setState({copied:false}),2200);},
   qty:s.qty,qtyLen:Math.max(1,String(s.qty).length),minDis:s.qty<=1,dec:()=>this.setState({qty:Math.max(1,s.qty-1)}),inc:()=>this.setState({qty:s.qty+1}),
   setQty:(e)=>this.setState({qty:Math.max(1,num(e.target.value)||1)}),buyDis:false,
   buy:()=>{this.addToCart(Object.assign({},p,{price:v.price}),s.qty);this.toastMsg('Odstín '+v.no+' '+v.n+' přidán do košíku.');},
   tabs:T.map((n,i)=>({n:n,cls:'tabB'+(s.tab===i?' on':''),sel:s.tab===i?'true':'false',pick:()=>this.setState({tab:i})})),
   toBulk:()=>{this.setState({tab:2});const el=document.getElementById('tabs');if(el)el.scrollIntoView({behavior:'smooth'});},
   bulkRows:AV.map((x,i)=>({no:String(x.no),n:x.n,code:x.code,hex:x.hex,av:x.av,avCls:x.st>0?'avOk':'avBlue',priceTxt:CZK(x.price),id:'bq'+i,q:s.bq[i]||0,
     qLen:Math.max(1,String(s.bq[i]||0).length),minDis:!(s.bq[i]>0),buyLabel:'Koupit '+x.no+' '+x.n,
     setQ:(e)=>this.setState({bq:Object.assign({},s.bq,{[i]:num(e.target.value)})}),
     dec:()=>this.setState({bq:Object.assign({},s.bq,{[i]:Math.max(0,(s.bq[i]||0)-1)})}),
     inc:()=>this.setState({bq:Object.assign({},s.bq,{[i]:(s.bq[i]||0)+1})}),
     buy:()=>{const q=s.bq[i]>0?s.bq[i]:1;const cart=s.cart.slice();const j=cart.findIndex((l)=>l.id===1);if(j>=0)cart[j]={id:1,qty:cart[j].qty+q};else cart.push({id:1,qty:q});
       const bq=Object.assign({},s.bq);delete bq[i];this.setState({cart:cart,bq:bq,pop:'',dlg:{id:1,qty:q,shades:[{no:x.no,n:x.n,hex:x.hex,q:q,price:x.price}]}});}})),
   bulkCount:String(bulkCount),
   bulkAdd:()=>{const ids=Object.keys(s.bq).filter((k)=>s.bq[k]>0);if(!ids.length){this.toastMsg('Vyplňte množství alespoň u jednoho odstínu.',true);return;}
     const total=ids.reduce((a,k)=>a+s.bq[k],0);const cart=s.cart.slice();const i=cart.findIndex((l)=>l.id===1);if(i>=0)cart[i]={id:1,qty:cart[i].qty+total};else cart.push({id:1,qty:total});
     const shades=ids.map((k)=>{const x=AV[k];return {no:x.no,n:x.n,hex:x.hex,q:s.bq[k],price:x.price};});
     this.setState({cart:cart,bq:{},pop:'',dlg:{id:1,qty:total,shades:shades}});},
   gList:GIM,chipTxt:v.no+' '+v.n,lb:s.lb,lbImg:GIM[s.gi]||GIM[0],openLb:()=>this.setState({lb:true}),
   gImgs:GIM.map((u,i)=>({img:u,alt:p.name+' – foto '+(i+1),label:'Fotografie '+(i+1)+' z '+GIM.length,th:'thumb'+(i===s.gi?' on':''),cur:i===s.gi?'true':'false',dot:'gDot'+(i===s.gi?' on':''),lbTh:'lbTh'+(i===s.gi?' on':''),lbGo:()=>this.setState({gi:i}),go:(e)=>gGo(e,i)})),
   lbAlt:p.name+' – foto '+(s.gi+1),lbNum:(s.gi+1)+' / '+GIM.length,lbPrev:()=>this.setState({gi:(s.gi-1+GIM.length)%GIM.length}),lbNext:()=>this.setState({gi:(s.gi+1)%GIM.length}),
   gScroll:(e)=>{const t=e.currentTarget;const i=Math.round(t.scrollLeft/Math.max(1,t.clientWidth));if(i!==this.state.gi)this.setState({gi:i});},
   gPrev:(e)=>gGo(e,(s.gi-1+GIM.length)%GIM.length),gNext:(e)=>gGo(e,(s.gi+1)%GIM.length),closeLb:()=>{this.setState({lb:false});syncTrack();},lbKey:(e)=>{if(e.key==='Escape'){e.stopPropagation();this.setState({lb:false});syncTrack();}else if(e.key==='ArrowLeft'){this.setState({gi:(s.gi-1+GIM.length)%GIM.length});}else if(e.key==='ArrowRight'){this.setState({gi:(s.gi+1)%GIM.length});}}
  };
  T.forEach((n,i)=>{vals['tab'+i]=s.tab===i;});
  return vals;
 }
"""
pre_dv = 'const AV=' + json.dumps(AV, ensure_ascii=False) + ';window.__AV=AV;applyGroup();\nconst GORD=' + json.dumps(GROUPS_ORDER, ensure_ascii=False) + ';\n' + 'const GIM=' + json.dumps([VP['img'],'/_blob/4b3e506c96fdac53c7b3749847e33b77','/_blob/76b5d08f4c869ef688374e069d43c347','/_blob/abc506dceb49e9689404cf98092e48f2']) + ';\n'
pages['DetailVariant'] = shop_page('Detail produktu s variantami', dv_css, dv_html, dv_js, 8800, 'Barvy média').replace('class Component extends DCLogic {', pre_dv + 'class Component extends DCLogic {', 1)

# sdílené CSS hromadné tabulky (bulk) i pro běžný detail
def _bulk_css(css):
    out=[]; i=0
    import re as _r
    for m in _r.finditer(r'@media[^{]*\{(?:[^{}]*\{[^{}]*\})*[^{}]*\}|[^{}@]+\{[^{}]*\}', css):
        blk=m.group(0)
        if _r.search(r'bulk|\.bq|bqBuy|\.rows|rowsBox', blk) and 'animation' not in blk and '.vInd' not in blk: out.append(blk.strip())
    return '\n'.join(out)
BULK_CSS = _bulk_css(dv_css) + "\n.accName{color:var(--text);text-decoration:none}.accName:hover span{text-decoration:underline}.accName img{width:48px;height:48px;object-fit:contain;border:1px solid var(--line);border-radius:var(--radius-sm);background:#fff;flex:none}.accName span{min-width:0}.accPh{width:48px;height:48px;flex:none;border:1px dashed var(--input-border);border-radius:var(--radius-sm);background:var(--bg-soft)}"
pages['Detail'] = shop_page('Detail produktu', det_css + BULK_CSS, det_html, det_js, 2700, 'Štětce pomůcky')

if __name__ == '__main__':
    write('Detail.dc.html', pages['Detail'].replace('></input>', '>'))
    write('DetailVariant.dc.html', pages['DetailVariant'].replace('></input>', '>'))
