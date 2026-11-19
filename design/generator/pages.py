from common import *

CAROUSEL_CSS = """
.car{position:relative}
.carTrack{display:grid;grid-auto-flow:column;grid-auto-columns:calc((100% - 3*var(--grid-gap))/4);gap:var(--grid-gap);overflow-x:auto;scroll-snap-type:x mandatory;scroll-behavior:smooth;padding:4px 2px 14px;scrollbar-width:thin;scrollbar-color:var(--primary) transparent}
.carTrack>*{scroll-snap-align:start;min-width:0}
.carNav{display:flex;gap:8px}
@media (max-width:1149px){.carTrack{grid-auto-columns:calc((100% - 2*var(--grid-gap))/3)}}
@media (max-width:819px){.carTrack{grid-auto-columns:calc((100% - var(--grid-gap))/2)}}
@media (max-width:549px){.carTrack{grid-auto-columns:80%}}
"""

def carousel(key, title, lst):
    return f'''<section class="section container" aria-labelledby="h{key}">
<div class="secHead"><h2 id="h{key}">{title}</h2><div class="carNav"><button class="arrowBtn" type="button" aria-label="Předchozí produkty" onClick="{{{{ car{key}Prev }}}}">{I('caret-left')}</button><button class="arrowBtn" type="button" aria-label="Další produkty" onClick="{{{{ car{key}Next }}}}">{I('caret-right')}</button></div></div>
<div class="car"><div class="carTrack" data-car="{key}">
<sc-for list="{{{{ {lst} }}}}" as="c" hint-placeholder-count="4"><dc-import name="ProductCard" p="{{{{ c }}}}" pickup="{{{{ pickup }}}}" delivery="{{{{ delivery }}}}" on-add="{{{{ addCart }}}}" hint-size="100%,560px"></dc-import></sc-for>
</div></div>
</section>'''

CAR_JS = r"""
 carMove(k,d){const t=document.querySelector('[data-car="'+k+'"]');if(t)t.scrollBy({left:d*t.clientWidth*0.9});}
"""
def car_vals(keys):
    return ''.join(f"car{k}Prev:()=>this.carMove('{k}',-1),car{k}Next:()=>this.carMove('{k}',1)," for k in keys)

pages = {}

# ======================= MAIN =======================
slides = [
    ('Velkoobchod pro prodejny a školy', 'Výtvarné potřeby pro B2B partnery', '[DOPLNIT hlavní sdělení – podmínky velkoobchodu, sortiment, registrace]', 'Registrace B2B', 'Udaje.dc.html'),
    ('Akce', 'Jovi se slevou 10 %', 'Plastelíny, fixy, voskovky a modelovací hmoty Jovi. [DOPLNIT termín akce]', 'Akční produkty', 'Kategorie.dc.html'),
    ('Štětce a pomůcky', 'Štětce Meyco, Royal & Langnickel a další', 'Sady plochých, vějířových i tupovacích štětců skladem.', 'Do kategorie', 'Kategorie.dc.html'),
    ('Modelování a keramika', 'Modelovací hmoty Darwi, Jovi a Cernit', 'Samotvrdnoucí a polymerové hmoty, nástroje a formy.', 'Do kategorie', 'Kategorie.dc.html'),
]
SL_JS = 'const SLIDES=' + json.dumps([{'k': a, 't': b, 'd': c, 'cta': d, 'href': e} for a, b, c, d, e in slides], ensure_ascii=False) + ';'

usp = [('truck', 'Doprava', 'zdarma od 1 000 Kč bez DPH'), ('storefront', 'Velkoobchodní ceny', 'po přihlášení B2B účtu'),
       ('package', 'Skladem', '100 000+ položek'),
       ('buildings', 'Na trhu od', '1996 – přes 30 let zkušeností')]
USP_HREF = {'Doprava': 'Doprava.dc.html', 'Velkoobchodní ceny': 'Spoluprace.dc.html', 'Skladem': 'Kategorie.dc.html', 'Expedice': 'Doprava.dc.html', 'Značky': 'Onas.dc.html', 'Na trhu od': 'Onas.dc.html'}
usp_html = ''.join(f'<li><a class="uspItem" href="{USP_HREF.get(t, "Onas.dc.html")}">{I(i,"ic uspIc")}<div><strong>{t}</strong><span>{d}</span></div>{I("arrow-right","ic uspGo")}</a></li>' for i, t, d in usp)

main_html = f'''<section class="hero bleed" aria-roledescription="carousel" aria-label="Hlavní sdělení" onMouseEnter="{{{{ heroPause }}}}" onMouseLeave="{{{{ heroPlay }}}}" onFocus="{{{{ heroPause }}}}" onBlur="{{{{ heroPlay }}}}" onTouchStart="{{{{ tStart }}}}" onTouchEnd="{{{{ tEnd }}}}">
<div class="container heroDesk">
<sc-for list="{{{{ slides }}}}" as="s" hint-placeholder-count="1">
<div class="{{{{ s.cls }}}}" role="group" aria-roledescription="slide" aria-label="{{{{ s.aria }}}}" aria-hidden="{{{{ s.hidden }}}}" inert="{{{{ s.inertAttr }}}}">
<div class="slideTxt"><span class="kicker">{{{{ s.k }}}}</span><h2>{{{{ s.t }}}}</h2><p>{{{{ s.d }}}}</p><a class="btn btn-light" href="{{{{ s.href }}}}">{{{{ s.cta }}}}</a></div>
<div class="ph slideImg">[FOTO: hero {{{{ s.n }}}}]</div>
</div>
</sc-for>
</div>
<div class="container heroTabs">
<button class="arrowBtn heroArr" type="button" aria-label="Předchozí slide" onClick="{{{{ heroPrev }}}}">{I('caret-left')}</button>
<sc-for list="{{{{ slides }}}}" as="s" hint-placeholder-count="4"><button class="{{{{ s.tabCls }}}}" type="button" aria-current="{{{{ s.cur }}}}" onClick="{{{{ s.go }}}}"><span class="tabNo">{{{{ s.n }}}}</span><span class="tabT">{{{{ s.t }}}}</span></button></sc-for>
<button class="arrowBtn heroArr" type="button" aria-label="Další slide" onClick="{{{{ heroNext }}}}">{I('caret-right')}</button>
</div>
<div class="heroAcc">
<sc-for list="{{{{ slides }}}}" as="s" hint-placeholder-count="4">
<div class="{{{{ s.accCls }}}}"><button class="accBtn" type="button" aria-expanded="{{{{ s.cur }}}}" onClick="{{{{ s.go }}}}"><span class="tabNo">{{{{ s.n }}}}</span>{{{{ s.t }}}}</button>
<sc-if value="{{{{ s.on }}}}" hint-placeholder-val="{{{{ false }}}}"><div class="accBody"><div class="ph slideImg">[FOTO: hero {{{{ s.n }}}}]</div><p>{{{{ s.d }}}}</p><a class="btn btn-main" href="{{{{ s.href }}}}">{{{{ s.cta }}}}</a></div></sc-if></div>
</sc-for>
</div>
</section>
<section class="container section uspSec" aria-label="Výhody nákupu"><ul class="usp">{usp_html}</ul></section>
<div class="container section"><h1 class="mainH1">Velkoobchod s výtvarnými potřebami <span class="todo">[OVĚŘIT SEO nadpis]</span></h1></div>
{carousel('A', 'Nejprodávanější', 'carA')}
{carousel('B', 'Novinky v sortimentu', 'carB')}
{carousel('C', 'Produkty v akci', 'carC')}
<section class="container section about" aria-labelledby="hAbout">
<div class="aboutTxt"><h2 id="hAbout">Svět výtvarných potřeb pod jednou střechou</h2><p class="aboutLead">Ve společnosti Daver spojujeme tradici s moderní distribucí výtvarných potřeb pro Českou a Slovenskou republiku. Jsme výhradním distributorem renomovaných značek, které přinášejí špičkovou kvalitu a inovativní produkty.</p><p class="aboutAddr">DAVER, spol. s r.o. · Piešťanská 2293/68, 915 01 Nové Mesto nad Váhom</p><a class="btn btn-out" href="Onas.dc.html">Více o firmě</a></div>
<img class="aboutImg" src="/_blob/f187ca0fbacbaa21776fddc3873cc212" alt="Malování akvarelem do skicáku">
</section>
<sc-if value="{{{{ showCookie }}}}" hint-placeholder-val="{{{{ false }}}}"><div class="mdOverlay bottom"><div class="mdBox"><dc-import name="CookieModal" on-done="{{{{ cookieDone }}}}" hint-size="640px,330px"></dc-import></div></div></sc-if>
<sc-if value="{{{{ showPromo }}}}" hint-placeholder-val="{{{{ false }}}}"><div class="mdOverlay" onClick="{{{{ promoOverlay }}}}" onKeyDown="{{{{ promoKey }}}}"><div class="mdBox"><dc-import name="PromoModal" image="{{{{ true }}}}" on-close="{{{{ promoClose }}}}" hint-size="560px,620px"></dc-import></div></div></sc-if>'''

main_css = CAROUSEL_CSS + """
.hero{background:#27272a;color:#fff;padding-top:var(--space-6);padding-bottom:var(--space-4)}
.slide{display:none}
.slide.on{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.1fr);gap:var(--space-6);align-items:center;min-height:380px}
.slideTxt{display:flex;flex-direction:column;gap:14px;align-items:flex-start}
.kicker{font-size:var(--fs-caption);text-transform:uppercase;letter-spacing:.08em;color:rgba(255,255,255,.75)}
.slideTxt h2{color:#fff;font-size:var(--fs-h1)}
.slideTxt p{color:rgba(255,255,255,.85);max-width:52ch}
.slideImg{height:340px;background:rgba(255,255,255,.06);border-color:rgba(255,255,255,.3);color:rgba(255,255,255,.75)}
.btn-light{background:#fff;color:#18181b}.btn-light:hover{background:#e4e4e7;color:#18181b}
.heroTabs{display:flex;gap:12px;align-items:stretch;margin-top:var(--space-5)}
.heroArr{align-self:center;border-color:transparent}
.tab{flex:1;display:flex;gap:10px;align-items:center;text-align:left;background:#fff;color:#18181b;border:2px solid transparent;border-radius:var(--card-radius);padding:10px 12px;cursor:pointer;min-height:56px;font-size:var(--fs-body-sm)}
.tab.on{border-color:#a1a1aa;box-shadow:inset 0 -3px 0 #18181b}
.tabNo{display:inline-flex;align-items:center;justify-content:center;width:28px;height:28px;border-radius:50%;background:#f4f4f5;font-weight:700;flex:none}
.tabT{overflow:hidden;text-overflow:ellipsis;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical}
.heroAcc{display:none}
.usp{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(6,minmax(0,1fr));gap:var(--grid-gap)}
.uspItem{display:flex;gap:12px;align-items:center;border:1px solid var(--line);border-radius:var(--card-radius);padding:14px;font-size:var(--fs-body-sm)}
.uspIc{width:40px;height:40px;color:var(--primary-d)}
.uspItem strong{display:block}.uspItem span{color:var(--text-weaker)}
.about{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:var(--space-6);align-items:center}
.aboutTxt{display:flex;flex-direction:column;gap:16px;align-items:flex-start}
.aboutImg{height:320px}
@media (max-width:1149px){.usp{grid-template-columns:repeat(3,minmax(0,1fr))}}
@media (max-width:819px){
 .heroDesk,.heroTabs{display:none}
 .hero{padding:var(--space-4) var(--gutter);background:#fff;color:var(--text)}
 .heroAcc{display:flex;flex-direction:column;gap:8px}
 .accItem{border:1px solid var(--line);border-radius:var(--card-radius);overflow:hidden}
 .accBtn{display:flex;gap:10px;align-items:center;width:100%;min-height:52px;padding:8px 12px;border:0;background:#fff;font-weight:600;text-align:left;cursor:pointer}
 .accItem.on .accBtn{background:var(--primary-d);color:#fff}
 .accItem.on .tabNo{background:#fff;color:var(--primary-d)}
 .accBody{padding:12px;display:flex;flex-direction:column;gap:12px}
 .accBody .slideImg{height:clamp(180px,50vw,260px);background:var(--bg-soft);border-color:var(--input-border);color:var(--text-muted)}
 .accBody .btn{width:100%}
 .usp{grid-template-columns:repeat(2,minmax(0,1fr))}
 .about{grid-template-columns:1fr}
}
@media (max-width:419px){.usp{grid-template-columns:1fr}}
"""
main_js = CAR_JS + r"""
 pageState(){return {slide:0,paused:false,consent:true,promo:true};}
 pageMount(){
  this.setState({consent:!!lsGet('Consent'),promo:!!lsGet('Promo')});
  this.iv=setInterval(()=>{if(!this.state.paused&&!window.matchMedia('(prefers-reduced-motion: reduce)').matches)this.setState({slide:(this.state.slide+1)%SLIDES.length});},6000);
 }
 pageUnmount(){clearInterval(this.iv);}
 pageVals(){
  const s=this.state; const go=(i)=>this.setState({slide:(i+SLIDES.length)%SLIDES.length});
  return {
   slides:SLIDES.map((x,i)=>Object.assign({},x,{n:i+1,on:i===s.slide,cls:'slide'+(i===s.slide?' on':''),tabCls:'tab'+(i===s.slide?' on':''),
     accCls:'accItem'+(i===s.slide?' on':''),cur:i===s.slide?'true':'false',hidden:i===s.slide?'false':'true',inertAttr:i!==s.slide?'':undefined,
     aria:(i+1)+' z '+SLIDES.length,go:()=>go(i)})),
   heroPrev:()=>go(s.slide-1),heroNext:()=>go(s.slide+1),
   heroPause:()=>this.setState({paused:true}),heroPlay:()=>this.setState({paused:false}),
   tStart:(e)=>{this.tx=e.touches[0].clientX;}, tEnd:(e)=>{const d=e.changedTouches[0].clientX-this.tx;if(Math.abs(d)>40)go(s.slide+(d<0?1:-1));},
   carA:[14,11,8,6,12,15,7,19].map((i)=>card(byId(i))),
   carB:[18,19,20,21,22,13,16,3].map((i)=>card(byId(i))),
   carC:PRODUCTS.filter((p)=>p.flags.length).map(card),
   """ + car_vals('ABC') + r"""
   showCookie:!s.consent, showPromo:s.consent&&!s.promo,
   cookieDone:(v)=>{lsSet('Consent',JSON.stringify(v));this.setState({consent:true});},
   promoClose:()=>{lsSet('Promo','1');this.setState({promo:true});},
   promoOverlay:(e)=>{if(e.target===e.currentTarget){lsSet('Promo','1');this.setState({promo:true});}},
   promoKey:this.esc(()=>{lsSet('Promo','1');this.setState({promo:true});})
  };
 }
"""
pages['Main'] = shop_page('Daver – úvodní stránka', main_css, main_html, main_js.replace('pageState(){', 'pageState(){', 1), 4300).replace('class Component extends DCLogic {', SL_JS + '\nclass Component extends DCLogic {', 1)

# ======================= KATEGORIE =======================
subs = ['Štětce na akvarel', 'Štětce na akryl', 'Sady štětců', 'Štětce univerzální', 'Péče o štětce', 'Válečky a aplikátory', 'Špachtle a malířské nože']
subs_html = ''.join(f'<a class="subTile" href="Kategorie.dc.html"><span class="ph">[FOTO]</span><span>{s}</span></a>' for s in subs)
kat_html = f'''<div class="container">
<dc-import name="Breadcrumb" current="Štětce a pomůcky" hint-size="100%,48px"></dc-import>
<div class="katHead"><h1>Štětce a pomůcky <small><span class="todo">[DOPLNIT]</span> produktů</small></h1>
<div class="{{{{ perexCls }}}}"><p>Štětce pro akvarel, akryl i olej, sady štětců, špachtle, válečky a pomůcky pro péči o štětce od výrobců Meyco, Royal & Langnickel, Talens, Van Gogh, Pebeo a dalších. <span class="todo">[DOPLNIT perex z webu]</span></p></div>
<button class="btn btn-ghost btn-sm" type="button" aria-expanded="{{{{ perexOpen }}}}" onClick="{{{{ togglePerex }}}}">{{{{ perexBtn }}}}</button></div>
<nav class="subGrid FlatCategoriesRwdView" aria-label="Podkategorie">{subs_html}</nav>
<div class="quick" role="group" aria-label="Rychlý filtr – výrobce"><span class="quickL">Výrobce:</span>
<sc-for list="{{{{ brandChips }}}}" as="b" hint-placeholder-count="6"><button class="{{{{ b.cls }}}}" type="button" aria-pressed="{{{{ b.pressed }}}}" onClick="{{{{ b.toggle }}}}">{{{{ b.n }}}} <small>{{{{ b.count }}}}</small></button></sc-for></div>
<div class="toolbar">
<div class="sortTabs" role="group" aria-label="Řazení"><sc-for list="{{{{ sorts }}}}" as="o" hint-placeholder-count="5"><button class="{{{{ o.cls }}}}" type="button" aria-pressed="{{{{ o.pressed }}}}" onClick="{{{{ o.pick }}}}">{{{{ o.n }}}}</button></sc-for></div>
<div class="tbRight">
<div class="viewSw" role="group" aria-label="Zobrazení"><button class="{{{{ vTileCls }}}}" type="button" aria-pressed="{{{{ isTile }}}}" onClick="{{{{ setTile }}}}">{I('squares-four')}<span>Dlaždice</span></button><button class="{{{{ vRowCls }}}}" type="button" aria-pressed="{{{{ isRow }}}}" onClick="{{{{ setRow }}}}">{I('rows')}<span>Řádky</span></button></div>
<button class="btn btn-out" type="button" aria-expanded="{{{{ filterOpen }}}}" onClick="{{{{ openFilter }}}}">{I('funnel')}Filtr ({{{{ activeCount }}}})</button>
</div></div>
<sc-if value="{{{{ hasActive }}}}" hint-placeholder-val="{{{{ false }}}}"><div class="activeBar"><sc-for list="{{{{ activeChips }}}}" as="a" hint-placeholder-count="2"><dc-import name="FilterChip" label="{{{{ a.label }}}}" on-remove="{{{{ a.remove }}}}" hint-size="120px,32px"></dc-import></sc-for><button class="btn btn-ghost btn-sm" type="button" onClick="{{{{ clearAll }}}}">Zrušit vše</button></div></sc-if>
<sc-if value="{{{{ hasItems }}}}" hint-placeholder-val="{{{{ true }}}}">
<sc-if value="{{{{ isTile }}}}" hint-placeholder-val="{{{{ true }}}}">
<div class="pGrid ProductsView"><sc-for list="{{{{ items }}}}" as="c" hint-placeholder-count="6"><dc-import name="ProductCard" p="{{{{ c }}}}" pickup="{{{{ pickup }}}}" delivery="{{{{ delivery }}}}" on-add="{{{{ addCart }}}}" hint-size="100%,560px"></dc-import></sc-for></div>
</sc-if>
<sc-if value="{{{{ isRow }}}}" hint-placeholder-val="{{{{ false }}}}">
<div class="rowsBox"><table class="rows"><thead><tr><th scope="col">Název / kód</th><th scope="col">Dostupnost</th><th scope="col" class="r">Cena bez DPH</th><th scope="col" class="r">Množství</th></tr></thead>
<tbody><sc-for list="{{{{ items }}}}" as="r" hint-placeholder-count="6"><tr><td><div class="rName"><span class="ph">[FOTO]</span><div><a href="Detail.dc.html">{{{{ r.name }}}}</a><small>Kód {{{{ r.code }}}} · {{{{ r.brand }}}}</small></div></div></td><td class="avOk">{{{{ r.av }}}}</td><td class="r"><strong>{{{{ r.priceTxt }}}}</strong><small>{{{{ r.vatTxt }}}} s DPH</small></td><td class="r"><label class="sr" for="{{{{ r.qid }}}}">Množství {{{{ r.name }}}}</label><input class="rowQty" id="{{{{ r.qid }}}}" inputmode="numeric" value="{{{{ r.rq }}}}" onChange="{{{{ r.setRq }}}}"> ks</td></tr></sc-for></tbody></table>
<div class="rowsFoot"><span>Vyplňte množství u více produktů a vložte je do košíku najednou.</span><button class="btn btn-main" type="button" onClick="{{{{ allToCart }}}}">{I('shopping-cart')}Vše do košíku</button></div></div>
</sc-if>
<div class="more"><button class="btn btn-out" type="button" disabled="{{{{ true }}}}">Zobrazit dalších 24</button><span class="todo">[ukázka: v prototypu je jen 6 produktů z webu]</span></div>
<nav class="PagingView" aria-label="Stránkování"><a class="pg" href="#p" aria-label="Předchozí stránka">{I('caret-left')}</a><a class="pg on" href="#p" aria-current="page">1</a><a class="pg" href="#p">2</a><a class="pg" href="#p">3</a><span>…</span><a class="pg" href="#p">10</a><a class="pg" href="#p" aria-label="Další stránka">{I('caret-right')}</a></nav>
</sc-if>
<sc-if value="{{{{ noItems }}}}" hint-placeholder-val="{{{{ false }}}}"><div class="empty box">{I('magnifying-glass','ic big')}<h2>Pro tento výběr tu teď nic nemáme</h2><p>Zkuste zrušit některý filtr, nebo nám zavolejte – rádi zboží objednáme.</p><div class="emptyAct"><button class="btn btn-main" type="button" onClick="{{{{ clearAll }}}}">Zrušit filtry</button><a class="btn btn-out" href="Kontakt.dc.html">Kontaktovat obchod</a></div></div></sc-if>
<section class="section seo"><h2>Jak vybrat štětec</h2><p><span class="todo">[DOPLNIT SEO text kategorie]</span></p></section>
</div>
<sc-if value="{{{{ filterOpen }}}}" hint-placeholder-val="{{{{ false }}}}">
<div class="navOverlay fOverlay" onClick="{{{{ filterOverlay }}}}" onKeyDown="{{{{ filterKey }}}}">
<div class="fDrawer" role="dialog" aria-modal="true" aria-labelledby="fT">
<div class="drawerHead"><h2 id="fT">Upřesnit výběr</h2><button class="iconBtn" type="button" aria-label="Zavřít filtr" onClick="{{{{ closeFilter }}}}">{I('x')}</button></div>
<div class="fBody">
<fieldset class="fGroup"><legend>Cena bez DPH</legend>
<div class="dual"><input type="range" min="0" max="400" step="1" value="{{{{ pMin }}}}" onChange="{{{{ setPMin }}}}" aria-label="Cena od"><input type="range" min="0" max="400" step="1" value="{{{{ pMax }}}}" onChange="{{{{ setPMax }}}}" aria-label="Cena do"></div>
<div class="fPrice"><label>Od<input inputmode="numeric" value="{{{{ pMin }}}}" onChange="{{{{ setPMin }}}}"> Kč</label><label>Do<input inputmode="numeric" value="{{{{ pMax }}}}" onChange="{{{{ setPMax }}}}"> Kč</label></div></fieldset>
<fieldset class="fGroup"><legend>Štítky</legend><sc-for list="{{{{ flagOpts }}}}" as="f" hint-placeholder-count="3"><label class="fCheck"><input type="checkbox" checked="{{{{ f.on }}}}" onChange="{{{{ f.toggle }}}}">{{{{ f.n }}}}</label></sc-for></fieldset>
<fieldset class="fGroup"><legend>Výrobce</legend><sc-for list="{{{{ brandOpts }}}}" as="b" hint-placeholder-count="6"><label class="fCheck"><input type="checkbox" checked="{{{{ b.on }}}}" onChange="{{{{ b.toggle }}}}">{{{{ b.n }}}} <small>{{{{ b.count }}}}</small></label></sc-for>
<button class="btn btn-ghost btn-sm" type="button">Více hodnot</button></fieldset>
<fieldset class="fGroup"><legend>Dostupnost</legend><label class="fCheck"><input type="checkbox" checked="{{{{ onlyStock }}}}" onChange="{{{{ toggleStock }}}}">Skladem více než 10 ks</label></fieldset>
<fieldset class="fGroup"><legend>Materiál · Tvar · Velikost</legend><span class="todo">[DOPLNIT parametry filtru z Pohody]</span></fieldset>
</div>
<div class="fFoot"><button class="btn btn-main" type="button" onClick="{{{{ closeFilter }}}}">Zobrazit {{{{ count }}}} produktů</button></div>
</div></div>
</sc-if>'''

kat_css = """
.katHead{display:flex;flex-direction:column;gap:8px;align-items:flex-start;margin-top:4px}
.katHead h1 small{font-size:var(--fs-body);font-weight:400;color:var(--text-weaker);margin-left:8px}
.perex{max-width:80ch;color:var(--text-weaker);max-height:3em;overflow:hidden}
.perex.open{max-height:none}
.subGrid{display:grid;grid-template-columns:repeat(7,minmax(0,1fr));gap:var(--grid-gap);margin-top:var(--space-5)}
.subTile{display:flex;flex-direction:column;gap:8px;align-items:center;text-align:center;padding:12px;border:1px solid var(--line);border-radius:var(--card-radius);color:var(--text);text-decoration:none;font-size:var(--fs-body-sm);font-weight:500}
.subTile:hover{border-color:var(--primary-d)}
.subTile .ph{width:80px;height:80px}
.quick{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin-top:var(--space-5)}
.quickL{font-weight:600;margin-right:4px}
.chip{display:inline-flex;align-items:center;gap:6px;min-height:36px;padding:0 14px;border:1px solid var(--input-border);border-radius:999px;background:#fff;cursor:pointer;font-size:var(--fs-body-sm)}
.chip small{color:var(--text-muted)}
.chip.on{background:var(--primary-d);border-color:var(--primary-d);color:#fff}.chip.on small{color:rgba(255,255,255,.75)}
.toolbar{display:flex;justify-content:space-between;align-items:center;gap:12px;flex-wrap:wrap;margin-top:var(--space-5);padding:8px 0;border-block:1px solid var(--line)}
.sortTabs{display:flex;flex-wrap:wrap;gap:2px}
.sortBtn{min-height:40px;padding:0 12px;border:0;background:none;border-radius:var(--radius-sm);cursor:pointer;color:var(--text-weaker)}
.sortBtn.on{color:var(--text);font-weight:600;box-shadow:inset 0 -2px 0 var(--primary-d)}
.tbRight{display:flex;gap:12px;align-items:center}
.viewSw{display:flex;border:1px solid var(--input-border);border-radius:var(--btn-radius);overflow:hidden}
.vBtn{display:flex;align-items:center;gap:6px;min-height:42px;padding:0 12px;border:0;background:#fff;cursor:pointer;font-size:var(--fs-body-sm)}
.vBtn.on{background:var(--primary-10);font-weight:600}
.activeBar{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin-top:12px}
.pGrid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:var(--grid-gap);margin-top:var(--space-5)}
.rowsBox{margin-top:var(--space-5);overflow-x:auto;border:1px solid var(--line);border-radius:var(--card-radius)}
.rows{width:100%;border-collapse:collapse;font-size:var(--fs-body-sm);min-width:640px}
.rows th{text-align:left;font-weight:600;color:var(--text-weaker);padding:10px 12px;border-bottom:1px solid var(--line);background:var(--bg-soft)}
.rows td{padding:8px 12px;border-bottom:1px solid var(--line);vertical-align:middle}
.rows .r{text-align:right}
.rows small{display:block;color:var(--text-weaker);font-size:var(--fs-caption)}
.rName{display:flex;gap:12px;align-items:center}.rName .ph{width:48px;height:48px;padding:0;font-size:9px;flex:none}
.rName a{color:var(--text);font-weight:600;text-decoration:none}
.avOk{color:var(--success-text)}
.rowQty{width:64px;height:40px;border:1px solid var(--input-border);border-radius:var(--btn-radius);text-align:right;padding:0 8px}
.rowsFoot{display:flex;justify-content:space-between;align-items:center;gap:12px;padding:12px;flex-wrap:wrap;font-size:var(--fs-body-sm);color:var(--text-weaker)}
.more{display:flex;gap:12px;align-items:center;justify-content:center;margin-top:var(--space-5);flex-wrap:wrap}
.PagingView{display:flex;gap:6px;justify-content:center;align-items:center;margin-top:var(--space-4)}
.pg{display:inline-flex;align-items:center;justify-content:center;min-width:44px;height:44px;border:1px solid var(--line);border-radius:var(--btn-radius);color:var(--text);text-decoration:none}
.pg.on{background:var(--primary-d);color:#fff;border-color:var(--primary-d)}
.empty{margin-top:var(--space-5);padding:40px 24px;text-align:center;display:flex;flex-direction:column;gap:12px;align-items:center}
.empty .big{width:40px;height:40px;color:var(--text-muted)}
.emptyAct{display:flex;gap:12px;flex-wrap:wrap;justify-content:center}
.seo p{max-width:80ch;margin-top:8px}
.fOverlay{justify-content:flex-end;z-index:2700}
.fDrawer{width:min(420px,92vw);height:100%;background:#fff;display:flex;flex-direction:column}
.fDrawer h2{font-size:var(--fs-h3)}
.fBody{flex:1;overflow:auto;padding:0 16px}
.fGroup{border:0;border-bottom:1px solid var(--line);margin:0;padding:16px 0}
.fGroup legend{font-weight:700;padding:0;margin-bottom:8px;float:left;width:100%}
.fCheck{display:flex;align-items:center;gap:10px;min-height:40px;cursor:pointer;clear:both}
.fCheck input{width:18px;height:18px;accent-color:var(--primary-d)}
.fCheck small{color:var(--text-muted)}
.dual{position:relative;height:28px;clear:both}
.dual input{position:absolute;inset:0;width:100%;pointer-events:none;appearance:none;background:none;margin:0}
.dual input::-webkit-slider-thumb{pointer-events:auto;appearance:none;width:22px;height:22px;border-radius:50%;background:var(--primary-d);border:2px solid #fff;box-shadow:0 1px 3px rgba(0,0,0,.3);cursor:pointer}
.dual input::-moz-range-thumb{pointer-events:auto;width:22px;height:22px;border-radius:50%;background:var(--primary-d);border:2px solid #fff;cursor:pointer}
.dual::before{content:"";position:absolute;left:0;right:0;top:12px;height:4px;border-radius:2px;background:var(--line)}
.fPrice{display:flex;gap:12px;margin-top:8px}
.fPrice label{display:flex;align-items:center;gap:6px;font-size:var(--fs-body-sm)}
.fPrice input{width:80px;height:40px;border:1px solid var(--input-border);border-radius:var(--btn-radius);padding:0 8px}
.fFoot{position:sticky;bottom:0;padding:12px 16px;border-top:1px solid var(--line);background:#fff}
.fFoot .btn{width:100%}
@media (max-width:1149px){.pGrid{grid-template-columns:repeat(3,minmax(0,1fr))}.subGrid{grid-template-columns:repeat(4,minmax(0,1fr))}}
@media (max-width:819px){.pGrid{grid-template-columns:repeat(2,minmax(0,1fr))}
 .subGrid{display:flex;overflow-x:auto;scroll-snap-type:x mandatory;padding-bottom:6px}.subTile{flex:0 0 140px;scroll-snap-align:start}
 .vBtn span{display:none}}
@media (max-width:419px){.pGrid{grid-template-columns:1fr}}
"""
kat_js = r"""
 pageState(){return {perex:false,view:'tile',sort:0,brands:[],flags:[],pMin:0,pMax:400,onlyStock:false,filter:false,rq:{}};}
 pageVals(){
  const s=this.state;
  const BRANDS=['Ami','Darwi','Knorr Prandell','Meyco','Pebeo','Royal & Langnickel','Sizzix','Talens','Van Gogh'];
  const base=[11,12,13,14,15,16].map(byId);
  const tog=(arr,v)=>arr.includes(v)?arr.filter((x)=>x!==v):arr.concat([v]);
  let list=base.filter((p)=>(!s.brands.length||s.brands.includes(p.brand))&&p.price>=s.pMin&&p.price<=s.pMax&&(!s.onlyStock||p.stock>10)&&(!s.flags.length||(s.flags.includes('Akční produkty')&&p.flags.length)));
  const sorts=['Doporučené','Nejprodávanější','Nejlevnější','Nejdražší','Nejnovější'];
  if(s.sort===2)list=list.slice().sort((a,b)=>a.price-b.price);
  if(s.sort===3)list=list.slice().sort((a,b)=>b.price-a.price);
  const cnt=(b)=>{const n=base.filter((p)=>p.brand===b).length;return n?String(n):'–';};
  const active=[].concat(s.brands.map((b)=>({label:b,remove:()=>this.setState({brands:s.brands.filter((x)=>x!==b)})})),
   s.flags.map((f)=>({label:f,remove:()=>this.setState({flags:s.flags.filter((x)=>x!==f)})})),
   (s.pMin>0||s.pMax<400)?[{label:s.pMin+'–'+s.pMax+' Kč',remove:()=>this.setState({pMin:0,pMax:400})}]:[],
   s.onlyStock?[{label:'Skladem > 10 ks',remove:()=>this.setState({onlyStock:false})}]:[]);
  const num=(v)=>{const n=parseInt(String(v).replace(/\D/g,''),10);return isNaN(n)?0:n;};
  return {
   perexCls:'perex'+(s.perex?' open':''),perexOpen:s.perex?'true':'false',perexBtn:s.perex?'Zobrazit méně':'Zobrazit více',togglePerex:()=>this.setState({perex:!s.perex}),
   brandChips:BRANDS.map((b)=>({n:b,count:cnt(b),cls:'chip'+(s.brands.includes(b)?' on':''),pressed:s.brands.includes(b)?'true':'false',toggle:()=>this.setState({brands:tog(s.brands,b)})})),
   brandOpts:BRANDS.map((b)=>({n:b,count:cnt(b),on:s.brands.includes(b),toggle:()=>this.setState({brands:tog(s.brands,b)})})),
   flagOpts:['Akční produkty','Novinky','Doprodej'].map((f)=>({n:f,on:s.flags.includes(f),toggle:()=>this.setState({flags:tog(s.flags,f)})})),
   sorts:sorts.map((n,i)=>({n:n,cls:'sortBtn'+(s.sort===i?' on':''),pressed:s.sort===i?'true':'false',pick:()=>this.setState({sort:i})})),
   isTile:s.view==='tile',isRow:s.view==='row',vTileCls:'vBtn'+(s.view==='tile'?' on':''),vRowCls:'vBtn'+(s.view==='row'?' on':''),
   setTile:()=>this.setState({view:'tile'}),setRow:()=>this.setState({view:'row'}),
   activeChips:active,hasActive:active.length>0,activeCount:active.length,
   clearAll:()=>this.setState({brands:[],flags:[],pMin:0,pMax:400,onlyStock:false}),
   items:list.map((p)=>Object.assign(card(p),{priceTxt:CZK(p.price),vatTxt:CZK(p.price*VAT),qid:'rq'+p.id,rq:s.rq[p.id]||0,
     setRq:(e)=>this.setState({rq:Object.assign({},s.rq,{[p.id]:num(e.target.value)})})})),
   hasItems:list.length>0,noItems:list.length===0,count:list.length,
   allToCart:()=>{const ids=Object.keys(s.rq).filter((k)=>s.rq[k]>0);
     if(!ids.length){this.toastMsg('Vyplňte množství alespoň u jednoho produktu.',true);return;}
     const cart=s.cart.slice(); ids.forEach((k)=>{const id=+k;const i=cart.findIndex((l)=>l.id===id);if(i>=0)cart[i]={id:id,qty:cart[i].qty+s.rq[k]};else cart.push({id:id,qty:s.rq[k]});});
     this.setState({cart:cart,rq:{}});this.toastMsg('Do košíku přidáno '+ids.length+' produktů.');},
   filterOpen:s.filter,openFilter:()=>this.setState({filter:true}),closeFilter:()=>this.setState({filter:false}),
   filterKey:this.esc(()=>this.setState({filter:false})),filterOverlay:(e)=>{if(e.target===e.currentTarget)this.setState({filter:false});},
   pMin:s.pMin,pMax:s.pMax,setPMin:(e)=>this.setState({pMin:Math.min(num(e.target.value),s.pMax)}),setPMax:(e)=>this.setState({pMax:Math.max(Math.min(num(e.target.value),400),s.pMin)}),
   onlyStock:s.onlyStock,toggleStock:()=>this.setState({onlyStock:!s.onlyStock})
  };
 }
"""
pages['Kategorie'] = shop_page('Štětce a pomůcky – výpis', kat_css, kat_html, kat_js, 3400, 'Štětce a pomůcky')

# ======================= DETAIL =======================
det_html = f'''<div class="container">
<dc-import name="Breadcrumb" l1="Štětce a pomůcky" h1="Kategorie.dc.html" l2="Sady štětců" h2="Kategorie.dc.html" current="Meyco sada plochých štětců syntetické č. 12 16 20" hint-size="100%,48px"></dc-import>
<div class="detGrid">
<div class="detMain">
<div class="detHead"><h1>Meyco sada plochých štětců syntetické č. 12 16 20</h1>
<div class="detMeta"><button class="{{{{ copyCls }}}}" type="button" aria-label="{{{{ copyLabel }}}}" onClick="{{{{ copyCode }}}}"><span class="ccLbl">Kód</span><strong class="ccCode">{{{{ pCode }}}}</strong><span class="ccIc" aria-hidden="true"><sc-if value="{{{{ notCopied }}}}" hint-placeholder-val="{{{{ true }}}}">{I('copy')}</sc-if><sc-if value="{{{{ copied }}}}" hint-placeholder-val="{{{{ false }}}}">{I('check')}</sc-if></span><span class="ccMsg" aria-live="polite">{{{{ copiedTxt }}}}</span></button></div></div>
<div class="gallery">
<div class="gMain"><button class="gBig" type="button" aria-label="Zvětšit obrázek" onClick="{{{{ openLb }}}}"><span class="ph">[FOTO {{{{ imgNo }}}} / 4]</span></button>
<button class="arrowBtn gArr l" type="button" aria-label="Předchozí obrázek" onClick="{{{{ prevImg }}}}">{I('caret-left')}</button><button class="arrowBtn gArr r" type="button" aria-label="Další obrázek" onClick="{{{{ nextImg }}}}">{I('caret-right')}</button></div>
<div class="thumbs"><sc-for list="{{{{ thumbs }}}}" as="t" hint-placeholder-count="4"><button class="{{{{ t.cls }}}}" type="button" aria-label="{{{{ t.label }}}}" aria-current="{{{{ t.cur }}}}" onClick="{{{{ t.pick }}}}"><span class="ph">{{{{ t.n }}}}</span></button></sc-for></div>
</div>
<section class="section acc" aria-labelledby="hAcc"><h2 id="hAcc">Přikupte rovnou k produktu</h2>
<div class="accTable"><sc-for list="{{{{ accs }}}}" as="a" hint-placeholder-count="3"><div class="accRow"><span class="ph">[FOTO]</span><div><a href="Detail.dc.html">{{{{ a.name }}}}</a><small>{{{{ a.av }}}}</small></div><div class="accPrice"><strong>{{{{ a.priceTxt }}}}</strong><small>bez DPH</small></div><div class="miniQty"><button type="button" aria-label="Snížit" onClick="{{{{ a.dec }}}}">−</button><span aria-live="polite">{{{{ a.q }}}}</span><button type="button" aria-label="Zvýšit" onClick="{{{{ a.inc }}}}">+</button></div><button class="btn btn-out btn-sm" type="button" onClick="{{{{ a.buy }}}}">Přikoupit</button></div></sc-for></div></section>
<section class="section" id="tabs" aria-label="Informace o produktu">
<div class="tabBar" role="tablist"><sc-for list="{{{{ tabs }}}}" as="t" hint-placeholder-count="5"><button class="{{{{ t.cls }}}}" type="button" role="tab" aria-selected="{{{{ t.sel }}}}" onClick="{{{{ t.pick }}}}">{{{{ t.n }}}}</button></sc-for></div>
<div class="tabPanel" role="tabpanel">
<sc-if value="{{{{ tab0 }}}}" hint-placeholder-val="{{{{ true }}}}"><p>Sada tří plochých štětců se syntetickým vlasem ve velikostech 12, 16 a 20. <span class="todo">[DOPLNIT popis z Pohody / webu]</span></p></sc-if>
<sc-if value="{{{{ tab1 }}}}" hint-placeholder-val="{{{{ false }}}}"><table class="params"><tbody><tr><th scope="row">Výrobce</th><td>Meyco</td></tr><tr><th scope="row">Kód</th><td>14235</td></tr><tr><th scope="row">Tvar</th><td>plochý</td></tr><tr><th scope="row">Vlas</th><td>syntetický</td></tr><tr><th scope="row">Velikosti</th><td>č. 12, 16, 20</td></tr><tr><th scope="row">Počet v sadě</th><td>3 ks</td></tr><tr><th scope="row">Balení (karton)</th><td>12 ks</td></tr><tr><th scope="row">EAN</th><td>4006990142170</td></tr></tbody></table></sc-if>
<sc-if value="{{{{ tab2 }}}}" hint-placeholder-val="{{{{ false }}}}"><p><a href="#pdf">{I('file-pdf')} Produktový list (PDF, 240 kB)</a></p></sc-if>

<sc-if value="{{{{ tab3 }}}}" hint-placeholder-val="{{{{ false }}}}"><p>Máte dotaz k produktu? Odpovíme do 24 hodin v pracovní dny.</p><button class="btn btn-out" type="button">Položit dotaz</button></sc-if>
</div></section>
</div>
<aside class="buyCol" aria-label="Nákup">
<div class="buyBox">
<div class="flags"><span class="flagX">Doporučujeme</span></div>
<div class="bigPrice">69,38&nbsp;Kč <small>bez DPH</small></div>
<div class="priceSub">83,95&nbsp;Kč s DPH · cena pro skupinu <strong>{{{{ priceGroup }}}}</strong></div>
<ul class="avPanel"><li class="avOk">{I('check-circle')}Skladem &gt; 30 ks</li><li>{I('storefront')}Osobní odběr: zítra od 9:00</li><li>{I('truck')}Doručení: pozítří</li></ul>
<div class="buyRow"><div class="qty"><button type="button" aria-label="Snížit množství" disabled="{{{{ minDis }}}}" onClick="{{{{ dec }}}}">−</button><label><input inputmode="numeric" aria-label="Množství" size="{{{{ qtyLen }}}}" value="{{{{ qty }}}}" onChange="{{{{ setQty }}}}">ks</label><button type="button" aria-label="Zvýšit množství" onClick="{{{{ inc }}}}">+</button></div><button class="btn btn-main btn-lg" type="button" onClick="{{{{ buy }}}}">{I('shopping-cart')}Koupit</button></div>
<div class="buyLinks"><button class="btn btn-ghost" type="button" aria-pressed="{{{{ fav }}}}" onClick="{{{{ toggleFav }}}}">{I('heart')}{{{{ favTxt }}}}</button><button class="btn btn-ghost" type="button" onClick="{{{{ compare }}}}">{I('scales')}{{{{ cmpTxt }}}}</button></div>
<dl class="short"><div><dt>Výrobce</dt><dd>Meyco</dd></div><div><dt>Tvar</dt><dd>plochý</dd></div><div><dt>Velikosti</dt><dd>č. 12, 16, 20</dd></div></dl>
<button class="btn btn-ghost" type="button" onClick="{{{{ toTabs }}}}">Detailní popis {I('caret-down')}</button>
<ul class="benefits"><li>{I('storefront')}Velkoobchodní ceny pro registrované</li><li>{I('truck')}Doprava zdarma od 1 000 Kč bez DPH</li></ul>
</div>
</aside>
</div>
</div>
<sc-if value="{{{{ lb }}}}" hint-placeholder-val="{{{{ false }}}}">
<div class="lb" role="dialog" aria-modal="true" aria-label="Galerie" onKeyDown="{{{{ lbKey }}}}">
<button class="iconBtn lbClose" type="button" aria-label="Zavřít galerii" autoFocus="{{{{ true }}}}" onClick="{{{{ closeLb }}}}">{I('x')}</button>
<button class="arrowBtn lbArr l" type="button" aria-label="Předchozí obrázek" onClick="{{{{ prevImg }}}}">{I('caret-left')}</button>
<div class="ph lbImg">[FOTO {{{{ imgNo }}}} / 4]</div>
<button class="arrowBtn lbArr r" type="button" aria-label="Další obrázek" onClick="{{{{ nextImg }}}}">{I('caret-right')}</button>
<div class="lbCount">{{{{ imgNo }}}} / 4</div>
</div>
</sc-if>'''
det_css = """
.detGrid{display:grid;grid-template-columns:minmax(0,1fr) 420px;gap:var(--space-6);align-items:start}
.detGrid>*,.detMain>*{min-width:0}
.detHead{display:flex;flex-direction:column;gap:6px;margin-bottom:var(--space-4)}
.detMeta{display:flex;align-items:center;gap:6px;font-size:var(--fs-body-sm);color:var(--text-weaker);flex-wrap:wrap}
.codeCopy{display:inline-flex;align-items:center;gap:6px;min-height:36px;padding:0 6px 0 12px;border:1px solid var(--line);border-radius:999px;background:#fff;color:var(--text-weaker);font-size:var(--fs-body-sm);cursor:pointer;transition:background .2s,border-color .2s,color .2s}
.codeCopy:hover{border-color:var(--input-border);background:var(--bg-soft)}
.codeCopy .ccCode{color:var(--text);font-weight:700;letter-spacing:.02em}
.ccIc{display:inline-flex;align-items:center;justify-content:center;width:26px;height:26px;border-radius:50%;color:var(--text)}
.ccIc .ic{width:16px;height:16px}
.ccMsg{max-width:0;overflow:hidden;white-space:nowrap;opacity:0;transition:max-width .3s ease,opacity .2s ease,margin .3s ease}
.codeCopy.done{background:#ecfdf3;border-color:#86d4a3;color:var(--success-text)}
.codeCopy.done .ccIc{background:var(--success);color:#fff;animation:ccPop .35s ease}
.codeCopy.done .ccMsg{max-width:220px;opacity:1;margin-right:8px;font-weight:600}
@keyframes ccPop{0%{transform:scale(.4)}70%{transform:scale(1.15)}100%{transform:scale(1)}}
.stars{display:inline-flex;align-items:center;gap:4px;margin-left:12px}
.gallery{display:grid;grid-template-columns:96px minmax(0,1fr);gap:12px}
.gMain{position:relative;grid-column:2;grid-row:1}
.gBig{display:block;width:100%;aspect-ratio:4/3;border:1px solid var(--line);border-radius:var(--card-radius);background:#fff;padding:0;cursor:zoom-in}
.gBig .ph{width:100%;height:100%;border:0}
.gArr{position:absolute;top:50%;transform:translateY(-50%)}
.gArr.l{left:8px}.gArr.r{right:8px}
.thumbs{grid-column:1;grid-row:1;display:flex;flex-direction:column;gap:8px}
.thumbs{scrollbar-width:none;padding:2px}.thumbs::-webkit-scrollbar{display:none}
.thumb{width:96px;height:96px;padding:6px;border:1px solid var(--line);border-radius:var(--radius-sm);background:#fff;cursor:pointer}
.thumb .ph{width:100%;height:100%;padding:0}
.thumb.on{outline:2px solid var(--primary-d);outline-offset:-2px}
.accTable{display:flex;flex-direction:column;border:1px solid var(--line);border-radius:var(--card-radius);margin-top:12px}
.accRow{display:grid;grid-template-columns:56px minmax(0,1fr) auto auto auto;gap:12px;align-items:center;padding:10px 12px;border-bottom:1px solid var(--line);font-size:var(--fs-body-sm)}
.accRow:last-child{border-bottom:0}
.accRow .ph{width:56px;height:56px;padding:0;font-size:9px}
.accRow a{color:var(--text);font-weight:600;text-decoration:none}.accRow small{display:block;color:var(--text-weaker)}
.accPrice{text-align:right}
.miniQty{display:flex;align-items:center;border:1px solid var(--input-border);border-radius:var(--btn-radius)}
.miniQty button{width:32px;height:32px;border:0;background:none;cursor:pointer}
.miniQty span{min-width:24px;text-align:center}
.tabBar{display:flex;gap:4px;border-bottom:1px solid var(--line);overflow-x:auto}
.tabB{min-height:48px;padding:0 16px;border:0;background:none;cursor:pointer;color:var(--text-weaker);font-weight:500;white-space:nowrap}
.tabB.on{color:var(--text);box-shadow:inset 0 -3px 0 var(--primary-d)}
.tabPanel{padding:20px 0;max-width:80ch}
.params{border-collapse:collapse;width:100%}
.params th,.params td{text-align:left;padding:8px 12px;border-bottom:1px solid var(--line);font-size:var(--fs-body-sm)}
.params th{font-weight:500;color:var(--text-weaker);width:40%}
.buyCol{position:sticky;top:calc(var(--header-h) + 16px)}
.buyBox{border:1px solid var(--line);border-radius:var(--card-radius);padding:var(--card-pad);display:flex;flex-direction:column;gap:14px}
.flagX{display:inline-block;background:var(--flag-doporucujeme);color:#fff;font-size:12px;font-weight:700;padding:2px 8px;border-radius:2px}
.bigPrice{font-size:32px;font-weight:700;line-height:1.1}.bigPrice small{font-size:var(--fs-body-sm);font-weight:400;color:var(--text-weaker)}
.avPanel{list-style:none;margin:0;padding:12px;background:var(--bg-soft);border-radius:var(--radius-md);display:flex;flex-direction:column;gap:6px;font-size:var(--fs-body-sm)}
.avPanel li{display:flex;gap:8px;align-items:center}
.avOk{color:var(--success-text)}
.buyRow{display:flex;gap:10px}
.buyRow .btn{flex:1;min-height:var(--btn-h-lg)}
.qty{display:flex;align-items:center;min-width:132px;border:1px solid var(--input-border);border-radius:var(--btn-radius);background:#fff}
.qty button{width:40px;height:100%;border:0;background:none;font-size:18px;cursor:pointer}
.qty button:disabled{color:#c4c4c8;cursor:not-allowed}
.qty label{flex:1;display:flex;align-items:center;justify-content:center;gap:4px;padding:0 4px;white-space:nowrap}
.qty input{field-sizing:content;width:auto;min-width:1ch;max-width:6ch;border:0;outline:0;text-align:center;font:inherit;padding:0;background:transparent}
.buyLinks{display:flex;flex-wrap:wrap;gap:4px}
.short{margin:0;display:flex;flex-direction:column;gap:4px;font-size:var(--fs-body-sm)}
.short div{display:flex;justify-content:space-between}.short dt{color:var(--text-weaker)}.short dd{margin:0}
.benefits{list-style:none;margin:0;padding:12px 0 0;border-top:1px solid var(--line);display:flex;flex-direction:column;gap:8px;font-size:var(--fs-body-sm)}
.benefits li{display:flex;gap:8px;align-items:center}
.lb{position:fixed;inset:0;z-index:3500;background:rgba(9,9,11,.92);display:flex;align-items:center;justify-content:center}
.lbImg{width:min(80vw,900px);height:min(75vh,680px);background:rgba(255,255,255,.06);color:#fff;border-color:rgba(255,255,255,.3)}
.lbClose{color:#fff}.lbClose:hover{background:rgba(255,255,255,.12)}
.lbClose{position:absolute;top:16px;right:16px}.lbArr{position:absolute;top:50%}.lbArr.l{left:16px}.lbArr.r{right:16px}
.lbCount{position:absolute;bottom:20px;color:#fff;font-size:var(--fs-body-sm)}
@media (max-width:1279px){.detGrid{grid-template-columns:minmax(0,1fr) 380px}}
@media (max-width:1149px){.detGrid{grid-template-columns:minmax(0,1fr)}.detGrid{row-gap:20px}.detHead{margin-bottom:0}.buyCol{position:static;grid-row:3}
 .detMain{display:contents}.detHead{grid-row:1}.detMain>.gallery,.detMain>.gv,.detMain>dc-import{grid-row:2}
 .gallery{grid-template-columns:1fr}.gMain{grid-column:1}.thumbs{grid-column:1;grid-row:2;flex-direction:row;overflow-x:auto}.thumb{width:72px;height:72px;flex:none}
 .accRow{grid-template-columns:56px minmax(0,1fr) auto;}.accRow .miniQty{grid-column:2}.accRow .btn{grid-column:3}}
"""
det_js = r"""
 pageState(){return {copied:false,img:0,lb:false,tab:0,qty:1,fav:false,cmp:false,aq:{11:1,12:1,16:1}};}
 pageMount(){this.setState({cmp:lsGet('CmpDetail')==='1'});}
 pageVals(){
  const s=this.state; const go=(i)=>this.setState({img:(i+4)%4}); const p=byId(14);
  const T=['Popis','Parametry','Ke stažení','Diskuze'];
  const vals={
   imgNo:s.img+1, prevImg:()=>go(s.img-1), nextImg:()=>go(s.img+1),
   thumbs:[0,1,2,3].map((i)=>({n:i+1,cls:'thumb'+(i===s.img?' on':''),cur:i===s.img?'true':'false',label:'Obrázek '+(i+1),pick:()=>go(i)})),
   lb:s.lb, openLb:()=>this.setState({lb:true}), closeLb:()=>this.setState({lb:false}),
   lbKey:(e)=>{if(e.key==='Escape'){e.stopPropagation();this.setState({lb:false});} if(e.key==='ArrowLeft')go(s.img-1); if(e.key==='ArrowRight')go(s.img+1);},
   tabs:T.map((n,i)=>({n:n,cls:'tabB'+(s.tab===i?' on':''),sel:s.tab===i?'true':'false',pick:()=>this.setState({tab:i})})),
   toTabs:()=>{const el=document.getElementById('tabs');if(el)el.scrollIntoView({behavior:'smooth'});},
   qty:s.qty, qtyLen:Math.max(1,String(s.qty).length), minDis:s.qty<=1, dec:()=>this.setState({qty:Math.max(1,s.qty-1)}), inc:()=>this.setState({qty:s.qty+1}),
   setQty:(e)=>{const v=parseInt(e.target.value.replace(/\D/g,''),10);this.setState({qty:isNaN(v)?1:Math.max(1,v)});},
   buy:()=>this.addToCart(p,s.qty),
   fav:s.fav, favTxt:s.fav?'V oblíbených':'Oblíbené', toggleFav:()=>this.setState({fav:!s.fav}),
   cmpTxt:s.cmp?'V porovnání':'Porovnat',
   compare:()=>{lsSet('CmpDetail','1');this.setState({cmp:true});this.toastMsg('Přidáno do porovnání.');},
   pCode:p.code, copied:!!s.copied, notCopied:!s.copied, copyCls:'codeCopy'+(s.copied?' done':''), copiedTxt:s.copied?'Zkopírováno do schránky':'',
   copyLabel:s.copied?'Kód '+p.code+' zkopírován do schránky':'Kopírovat kód produktu '+p.code,
   copyCode:()=>{try{navigator.clipboard.writeText(p.code);}catch(e){} this.setState({copied:true});clearTimeout(this.ct);this.ct=setTimeout(()=>this.setState({copied:false}),2200);},
   priceGroup:s.auth?USER.group:'Nepřihlášený',
   accs:[11,12,16].map((id)=>{const a=byId(id);const q=s.aq[id]||1;
     return {name:a.name,av:avText(a.stock),priceTxt:CZK(a.price),q:q,
      dec:()=>this.setState({aq:Object.assign({},s.aq,{[id]:Math.max(1,q-1)})}),inc:()=>this.setState({aq:Object.assign({},s.aq,{[id]:q+1})}),
      buy:()=>this.addToCart(a,q)};})
  };
  T.forEach((n,i)=>{vals['tab'+i]=s.tab===i;});
  return vals;
 }
"""
pages['Detail'] = shop_page('Detail produktu', det_css, det_html, det_js, 2700, 'Štětce a pomůcky')

# ======================= POROVNANI =======================
cmp_html = f'''<div class="container">
<dc-import name="Breadcrumb" current="Porovnání produktů" hint-size="100%,48px"></dc-import>
<div class="cmpHead"><h1>Porovnání produktů</h1>
<div class="cmpAct"><button class="btn btn-out btn-sm" type="button" onClick="{{{{ share }}}}">{I('share-network')}Sdílet porovnání</button><button class="btn btn-out btn-sm" type="button" onClick="{{{{ removeAll }}}}">{I('trash')}Odebrat vše</button><button class="btn btn-ghost btn-sm" type="button" onClick="{{{{ reset }}}}">Obnovit ukázku (jen prototyp)</button></div></div>
<sc-if value="{{{{ has }}}}" hint-placeholder-val="{{{{ true }}}}">
<div class="cmpBox"><table class="cmp">
<thead><tr><th scope="col" class="first"><label class="diffSw"><input type="checkbox" checked="{{{{ onlyDiff }}}}" onChange="{{{{ toggleDiff }}}}">Jen rozdíly</label></th>
<sc-for list="{{{{ cols }}}}" as="c" hint-placeholder-count="3"><th scope="col"><div class="cmpProd"><button class="iconBtn rm" type="button" aria-label="{{{{ c.rmLabel }}}}" onClick="{{{{ c.remove }}}}">{I('x')}</button><span class="ph">[FOTO]</span><a href="Detail.dc.html">{{{{ c.name }}}}</a><strong>{{{{ c.price }}}}</strong><small>bez DPH</small><button class="btn btn-main btn-sm" type="button" onClick="{{{{ c.buy }}}}">Koupit</button></div></th></sc-for></tr></thead>
<tbody><sc-for list="{{{{ rows }}}}" as="r" hint-placeholder-count="5"><tr class="{{{{ r.cls }}}}"><th scope="row" class="first">{{{{ r.n }}}}</th><sc-for list="{{{{ r.v }}}}" as="v" hint-placeholder-count="3"><td>{{{{ v.t }}}}</td></sc-for></tr></sc-for></tbody>
</table></div>
</sc-if>
<sc-if value="{{{{ none }}}}" hint-placeholder-val="{{{{ false }}}}"><div class="empty box"><h2>Porovnání je prázdné</h2><p>Produkty přidáte tlačítkem Porovnat na detailu produktu.</p><a class="btn btn-main" href="Kategorie.dc.html">Prohlížet produkty</a></div></sc-if>
</div>
{carousel('R', 'Naposledy navštívené', 'carR')}'''
cmp_css = CAROUSEL_CSS + """
.cmpHead{display:flex;justify-content:space-between;align-items:center;gap:16px;flex-wrap:wrap;margin:4px 0 var(--space-5)}
.cmpAct{display:flex;gap:8px;flex-wrap:wrap}
.cmpBox{overflow-x:auto;border:1px solid var(--line);border-radius:var(--card-radius)}
.cmp{border-collapse:separate;border-spacing:0;width:100%;min-width:720px}
.cmp th,.cmp td{padding:12px;border-bottom:1px solid var(--line);text-align:left;vertical-align:top;font-size:var(--fs-body-sm);min-width:220px}
.cmp .first{position:sticky;left:0;background:#fff;z-index:1;min-width:160px;font-weight:600;color:var(--text-weaker);box-shadow:1px 0 0 var(--line)}
.cmp tr.diff td{background:#fffbe8}
.cmpProd{position:relative;display:flex;flex-direction:column;gap:6px;align-items:flex-start}
.cmpProd .ph{width:120px;height:120px}
.cmpProd a{color:var(--text);font-weight:600;text-decoration:none}
.cmpProd small{color:var(--text-weaker);font-weight:400}
.rm{position:absolute;top:-6px;right:-6px}
.diffSw{display:flex;align-items:center;gap:8px;cursor:pointer;color:var(--text);font-weight:500}
.diffSw input{width:18px;height:18px;accent-color:var(--primary-d)}
.empty{padding:40px;text-align:center;display:flex;flex-direction:column;gap:12px;align-items:center}
"""
cmp_js = CAR_JS + r"""
 pageState(){return {ids:[14,15,16],onlyDiff:false};}
 pageMount(){if(lsGet('CmpDetail')==='0')this.setState({ids:[15,16]});}
 pageVals(){
  const s=this.state; const P=s.ids.map(byId);
  const X={14:{tvar:'plochý',ks:'3 ks',vel:'č. 12, 16, 20'},15:{tvar:'plochý',ks:'5 ks',vel:'č. 2, 4, 6, 8, 10'},16:{tvar:'vějířový',ks:'3 ks',vel:'č. 1, 3, 5'}};
  const R=[['Cena s DPH',(p)=>CZK(p.price*VAT)],['Dostupnost',(p)=>avText(p.stock)],['Výrobce',(p)=>p.brand],['Kód',(p)=>p.code],['Tvar',(p)=>X[p.id].tvar],['Vlas',()=>'syntetický'],['Počet v sadě',(p)=>X[p.id].ks],['Velikosti',(p)=>X[p.id].vel]];
  const rows=R.map((r)=>{const v=P.map((p)=>({t:r[1](p)}));const diff=new Set(v.map((x)=>x.t)).size>1;return {n:r[0],v:v,diff:diff,cls:diff?'diff':''};}).filter((r)=>!s.onlyDiff||r.diff);
  return {
   has:P.length>0,none:P.length===0,onlyDiff:s.onlyDiff,toggleDiff:()=>this.setState({onlyDiff:!s.onlyDiff}),
   cols:P.map((p)=>({name:p.name,price:CZK(p.price),rmLabel:'Odebrat '+p.name,buy:()=>this.addToCart(p,1),
     remove:()=>{if(p.id===14)lsSet('CmpDetail','0');this.setState({ids:s.ids.filter((x)=>x!==p.id)});}})),
   rows:rows,
   removeAll:()=>{lsSet('CmpDetail','0');this.setState({ids:[]});},
   reset:()=>{lsSet('CmpDetail','1');this.setState({ids:[14,15,16]});},
   share:()=>{try{navigator.clipboard.writeText('https://[DOPLNIT-domena]/porovnani?ids='+s.ids.join(','));}catch(e){} this.toastMsg('Odkaz na porovnání zkopírován.');},
   carR:[12,13,11,18,20,1,4,6].map((i)=>card(byId(i))),
   """ + car_vals('R') + r"""
  };
 }
"""
pages['Porovnani'] = shop_page('Porovnání produktů', cmp_css, cmp_html, cmp_js, 2500)

if __name__ == '__main__':
    for n, c in pages.items():
        write(n + '.dc.html', c.replace('></input>', '>'))
    print(list(pages))
