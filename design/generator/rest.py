from common import *

# ======================= INFOSTRÁNKY =======================
INFO = [
 ('Onas', 'O nás', [('Kdo jsme', 'DAVER, spol. s r.o. se sídlem v Novém Mestě nad Váhom je velkoobchod s výtvarnými potřebami. Od roku 1996 zásobujeme prodejny, papírnictví, školy i ateliéry v České a Slovenské republice a jsme výhradním distributorem řady renomovaných značek.'), ('Sortiment a značky', 'Výtvarné potřeby pro děti, školy, hobby i profesionály: barvy, papíry, štětce, plátna, grafika, modelování a kreativní techniky. Značky mj. Jovi, Meyco, Darwi, Cernit, Royal & Langnickel, Talens, Van Gogh, Pebeo.'), ('Pro koho', 'Pro prodejny výtvarných potřeb a papírnictví, školy a školky, výtvarné ateliéry, kreativní dílny i firmy, které potřebují spolehlivého dodavatele s širokým skladem.')]),
 ('Kontakt', 'Kontakt', [('Fakturační údaje', 'DAVER, spol. s r.o., Piešťanská 2293/68, 915 01 Nové Mesto nad Váhom · IČO: 34149431 · IČ DPH: SK2020381935'), ('Obchodní oddělení', 'Telefon +420 775 570 418 · e-mail daver@daver.cz · Po–Pá 9:00–16:00. Fakturace a účetnictví: fakturace@daver.cz.'), ('Sklad a výdej', 'Osobní odběr na adrese Piešťanská 2293/68, Nové Mesto nad Váhom · Po–Pá 9:00–16:00.')]),
 ('ObchodniPodminky', 'Obchodní podmínky', [('1. Úvodní ustanovení', 'Tyto obchodní podmínky upravují vztahy mezi společností DAVER, spol. s r.o. a jejími obchodními partnery při nákupu zboží prostřednictvím velkoobchodního e-shopu.'), ('2. Registrace B2B zákazníka', 'Nakupovat mohou podnikatelé a organizace po registraci a schválení účtu. Ke schválení potřebujeme IČO a kontaktní údaje, účet aktivujeme obvykle do jednoho pracovního dne.'), ('3. Objednávka a uzavření smlouvy', 'Smlouva vzniká potvrzením objednávky obchodním oddělením. O potvrzení vás informujeme e-mailem.'), ('4. Ceny a platební podmínky', 'Ceny jsou uvedeny bez DPH podle cenové skupiny zákazníka. Platit lze převodem na fakturu se splatností 14 dní, dobírkou nebo při osobním odběru.'), ('5. Dodání zboží', 'Zboží skladem expedujeme do 24 hodin, objednávky do 12:00 týž den. Doprava je zdarma od 1 000 Kč bez DPH.')]),
 ('Reklamace', 'Reklamace a vrácení', [('Jak reklamovat', 'Reklamaci uplatněte e-mailem na daver@daver.cz s číslem faktury, popisem vady a fotografií. Vadné zboží vyměníme nebo dobropisujeme do 30 dnů.'), ('Reklamační formulář', 'Formulář ke stažení (PDF) vyplňte a přiložte k zásilce.')]),
 ('Doprava', 'Doprava a platba', [('Způsoby dopravy', 'Osobní odběr zdarma · PPL na adresu 129 Kč · Zásilkovna 79 Kč · Geis paletová přeprava 990 Kč (ceny bez DPH).'), ('Způsoby platby', 'Převodem na fakturu (splatnost 14 dní) zdarma · Dobírka 39 Kč · Hotově nebo kartou při osobním odběru zdarma.'), ('Doprava zdarma', 'Doprava je zdarma pro objednávky od 1 000 Kč bez DPH.')]),
 ('Spoluprace', 'Velkoobchodní spolupráce', [('Pro koho je velkoobchod', 'Velkoobchod je určen prodejnám, papírnictvím, školám, ateliérům a dalším firmám. Stačí IČO a registrace na webu.'), ('Cenové skupiny', 'Velkoobchod, Maloobchodní prodejce a Školy. Cenovou skupinu nastavujeme podle objemu odběrů.'), ('Jak začít', 'Vyplňte žádost o registraci, ozveme se s potvrzením účtu.')]),
 ('Gdpr', 'Ochrana osobních údajů', [('Správce údajů', 'Správcem osobních údajů je DAVER, spol. s r.o., Piešťanská 2293/68, 915 01 Nové Mesto nad Váhom, IČO 34149431.'), ('Cookies', 'Nezbytné cookies používáme pro fungování košíku a přihlášení. Analytické a marketingové cookies jen s vaším souhlasem.')]),
 ('Kariera', 'Kariéra', [('Volné pozice', 'Obchodní zástupce pro Moravu · Skladník/skladnice (Nové Mesto nad Váhom). Životopis posílejte na daver@daver.cz.')]),
]
side = ''.join(f'<li><a class="{{{{ s{f} }}}}" href="{f}.dc.html">{t}</a></li>' for f, t, _ in INFO)
info_css = """
.infoGrid{display:flex;flex-wrap:wrap;gap:var(--space-6);align-items:flex-start;margin-top:4px}
.infoSide{flex:1 1 240px;max-width:280px;position:sticky;top:calc(var(--header-h) + 16px)}
.infoSide ul{list-style:none;margin:0;padding:8px;border:1px solid var(--line);border-radius:var(--card-radius);display:flex;flex-direction:column;gap:4px}
.infoSide a{transition:background .2s,color .2s}
.infoSide a{display:flex;align-items:center;min-height:44px;padding:0 12px;border-radius:var(--radius-sm);color:var(--text);font-size:var(--fs-body);font-weight:500;text-decoration:none}
.infoSide a:hover{background:var(--primary-10)}
.infoSide a.on{background:var(--primary-d);color:#fff;font-weight:600}
.infoBody{flex:999 1 560px;min-width:0;max-width:860px;display:flex;flex-direction:column;gap:var(--space-5)}
.infoBody section{display:flex;flex-direction:column;gap:8px}
.infoBody p{color:var(--text-weaker)}
.isWrap{position:relative}
.isArr{display:none}
@media (max-width:819px){
 .infoSide{position:static;max-width:none;flex-basis:100%;min-width:0}
 .infoSide ul{display:flex;overflow-x:auto;gap:8px;padding:2px 0;border:0;border-radius:0;background:none;scrollbar-width:none;scroll-behavior:smooth;overscroll-behavior-x:contain}
 .infoSide ul::-webkit-scrollbar{display:none}
 .infoSide li{flex:none}
 .infoSide a{min-height:44px;padding:0 16px;border:1px solid var(--line);border-radius:var(--chip-radius,8px);white-space:nowrap;font-size:var(--fs-body);background:#fff}
 .infoSide a.on{border-color:var(--primary-d)}
 .isArr{position:absolute;top:0;bottom:0;z-index:2;display:flex;align-items:center;width:56px;padding:0 4px;border:0;cursor:pointer;color:var(--text)}
 .isArr.l{left:0;justify-content:flex-start;background:linear-gradient(90deg,#fff 45%,rgba(255,255,255,0))}
 .isArr.r{right:0;justify-content:flex-end;background:linear-gradient(270deg,#fff 45%,rgba(255,255,255,0))}
 .isArr .ic{width:24px;height:24px}
}
@supports (corner-shape:squircle){.infoSide{--chip-radius:20px}}
"""
info = {}
for f, t, secs in INFO:
    body = ''.join(f'<section><h2>{h}</h2><p>' + (txt.replace('[', '<span class="todo">[').replace(']', ']</span>')) + '</p></section>' for h, txt in secs)
    html = f'''<div class="container">
<dc-import name="Breadcrumb" current="{t}" hint-size="100%,48px"></dc-import>
<div class="infoGrid">
<nav class="infoSide" aria-label="Informace o nákupu"><div class="isWrap">
<sc-if value="{{{{ isL }}}}" hint-placeholder-val="{{{{ false }}}}"><button class="isArr l" type="button" aria-label="Předchozí stránky" onClick="{{{{ isPrev }}}}">{I('caret-left')}</button></sc-if>
<ul class="isTrack" onScroll="{{{{ isScroll }}}}">{side}</ul>
<sc-if value="{{{{ isR }}}}" hint-placeholder-val="{{{{ false }}}}"><button class="isArr r" type="button" aria-label="Další stránky" onClick="{{{{ isNext }}}}">{I('caret-right')}</button></sc-if>
</div></nav>
<article class="infoBody"><h1>{t}</h1>{body}</article>
</div></div>'''
    js = r"""
 pageState(){return {isL:false,isR:false};}
 isUpd(){const t=document.querySelector('.isTrack');if(!t)return;const m=t.scrollWidth>t.clientWidth+4;const l=m&&t.scrollLeft>4,r=m&&t.scrollLeft+t.clientWidth<t.scrollWidth-4;if(l!==this.state.isL||r!==this.state.isR)this.setState({isL:l,isR:r});}
 pageMount(){setTimeout(()=>{const t=document.querySelector('.isTrack');if(t){const a=t.querySelector('a.on');if(a&&t.scrollWidth>t.clientWidth){t.style.scrollBehavior='auto';t.scrollLeft=Math.max(0,a.offsetLeft-t.offsetLeft-56);t.style.scrollBehavior='';}}this.isUpd();},50);this.onIsRs=()=>this.isUpd();window.addEventListener('resize',this.onIsRs);}
 pageUnmount(){window.removeEventListener('resize',this.onIsRs);}
 pageVals(){const t=()=>document.querySelector('.isTrack');return {isL:this.state.isL,isR:this.state.isR,isScroll:()=>this.isUpd(),
  isPrev:()=>{const e=t();if(e)e.scrollBy({left:-e.clientWidth*0.7});},isNext:()=>{const e=t();if(e)e.scrollBy({left:e.clientWidth*0.7});},""" + ','.join(f"s{x}:'{'on' if x == f else ''}'" for x, _, _ in INFO) + "};}\n"
    h = 1700 if f != 'ObchodniPodminky' else 2000
    info[f] = shop_page(t + ' – Daver', info_css, html, js, h)

# ======================= OBJEDNÁVKA =======================
CO_CSS = TOKENS + BASE_CSS + """
.co{min-height:100vh;display:flex;flex-direction:column;background:var(--bg-soft);padding-bottom:96px}
.coHead{background:#fff;border-bottom:1px solid var(--line)}
.coHeadIn{display:flex;align-items:center;justify-content:space-between;gap:16px;min-height:72px}
.coHead .logoImg{height:48px;width:auto;display:block}
.coHeadR{display:flex;align-items:center;gap:20px;font-size:var(--fs-body-sm)}
.coHeadR a{color:var(--text);font-weight:600;text-decoration:none}
.coUser{display:flex;align-items:center;gap:8px}
.coTel{display:flex;align-items:center;gap:10px}.coTel .ic{width:24px;height:24px;flex:none;color:var(--primary-d)}
.coTelTxt{display:flex;flex-direction:column;line-height:1.25}.coTelTxt small{font-size:var(--fs-caption);color:var(--text-weaker)}
.mono{display:inline-flex;align-items:center;justify-content:center;width:40px;height:40px;border-radius:50%;background:var(--primary-d);color:#fff;font-weight:700;font-size:14px}
@supports (corner-shape:squircle){.mono{corner-shape:squircle}}
.steps{display:flex;align-items:center;gap:16px;list-style:none;margin:var(--space-6) 0 0;padding:0;width:100%}
.steps li{display:flex;align-items:center;gap:12px;font-size:var(--fs-body);color:var(--text-weaker);white-space:nowrap;flex:none}
.steps a{color:inherit}
.steps .no{display:inline-flex;width:40px;height:40px;border-radius:50%;align-items:center;justify-content:center;border:1px solid var(--input-border);background:#fff;font-weight:700;font-size:var(--fs-body);flex:none}
.steps li.on{color:var(--text);font-weight:600}.steps li.on .no{background:var(--primary);color:#fff;border-color:var(--primary)}
.steps li.done .no{background:var(--primary);color:#fff;border-color:var(--primary)}.steps li.done .no .ic{width:20px;height:20px}.steps li.done a{color:var(--primary-d)}
.steps .sep{flex:1 1 auto;min-width:24px;height:2px;border-radius:1px;background:var(--input-border)}
.steps .sep.done{background:var(--primary)}
.stepTxt{font-size:var(--fs-caption);color:var(--text-weaker);margin-top:8px}
@media (max-width:819px){.steps{gap:8px}.steps li{font-size:var(--fs-body-sm);gap:8px}.steps .no{width:32px;height:32px}.steps li:not(.on) .lbl{display:none}}
.coGrid{display:grid;grid-template-columns:minmax(0,1fr) 400px;gap:var(--space-5);align-items:start;margin-top:var(--space-5)}
.panel{background:#fff;border:1px solid var(--line);border-radius:var(--card-radius);padding:var(--card-pad)}
.panel+.panel{margin-top:var(--space-4)}
.panel h2{font-size:var(--fs-h3);margin-bottom:var(--space-4)}
.sumRow{display:flex;justify-content:space-between;gap:12px;padding:6px 0;font-size:var(--fs-body-sm)}
.sumTot{border-top:1px solid var(--line);margin-top:8px;padding-top:12px;display:flex;justify-content:space-between;align-items:flex-end}
.sumTot strong{font-size:var(--fs-price-md)}
.bar{position:fixed;left:0;right:0;bottom:0;z-index:900;background:#fff;border-top:1px solid var(--line);box-shadow:0 -6px 20px rgba(0,0,0,.06)}
.barIn{display:flex;align-items:center;justify-content:space-between;gap:16px;min-height:76px}
.barR{display:flex;align-items:center;gap:20px}
.barTot{text-align:right;line-height:1.2}.barTot strong{display:block;font-size:var(--fs-price-md)}.barTot small{color:var(--text-weaker);font-size:var(--fs-caption)}
.btn-lg{min-height:var(--btn-h-lg);padding:0 28px}
.btn.loading{opacity:.7;pointer-events:none}
.coFoot{margin-top:var(--space-7);padding:24px 0;font-size:var(--fs-body-sm);color:var(--text-weaker);background:none}
.coFoot nav{display:flex;flex-wrap:wrap;gap:16px;margin-top:8px}
.field{display:flex;flex-direction:column;gap:4px}
.field label{font-size:var(--fs-body-sm);font-weight:600}
.field input,.field select,.field textarea{height:44px;border:1px solid var(--input-border);border-radius:var(--btn-radius);padding:0 12px;background:#fff;width:100%}
.field textarea{height:88px;padding:10px 12px}
.field input:focus,.field select:focus,.field textarea:focus{outline:0;border-color:var(--primary-d)}
.field .bad{border-color:var(--danger)}
.err{font-size:var(--fs-caption);color:var(--danger)}
.check{display:flex;gap:10px;align-items:flex-start;cursor:pointer;min-height:32px;font-size:var(--fs-body-sm)}
.check input{width:18px;height:18px;margin-top:2px;accent-color:var(--primary-d);flex:none}
.logo65{width:65px;height:40px;flex:none;padding:0;font-size:9px;display:block}
@media (max-width:1149px){.coGrid{grid-template-columns:1fr}}
@media (max-width:819px){.coHeadR .hours{display:none}.barIn{min-height:64px}.barBack span{display:none}.btn-lg{padding:0 16px}}
"""

DATA_CO = DATA_JS + r"""
const DELIV=[
 {id:'osobni',ic:'/_blob/9f0dfe88d68275ca1989f08b60667217',n:'Osobní odběr',d:'Výdej na adrese Piešťanská 2293/68, Nové Mesto nad Váhom · Po–Pá 9:00–16:00',price:0,ptxt:'zdarma'},
 {id:'adresa',ic:'/_blob/1b4f870fd70b411736eda2d97a1335db',n:'PPL – doručení na adresu',d:'Doručení do 1–2 pracovních dnů',price:129,ptxt:'129 Kč'},
 {id:'box',ic:'/_blob/ad2c535255d293641003571bc3932ee7',n:'Zásilkovna – výdejní místo / box',d:'Vyberte výdejní místo na mapě',price:79,ptxt:'79 Kč',pickup:true},
 {id:'paleta',ic:'/_blob/b48d303a0967485e535453f5a8b35e22',n:'Geis – paletová přeprava',d:'Pro objednávky nad 30 kg nebo rozměrné zboží',price:990,ptxt:'990 Kč'}
];
const PAY=[
 {id:'faktura',ic:'/_blob/7a951d27a6fcdeb98922c31f79e0cf9b',n:'Převodem na fakturu',d:'Splatnost 14 dní od vystavení faktury',price:0,ptxt:'zdarma'},
 {id:'dobirka',ic:'/_blob/511d0873a39d525058f9e8a1a5f6e50b',n:'Dobírka',d:'Platba při převzetí',price:39,ptxt:'39 Kč',no:['osobni']},
 {id:'prodejna',ic:'/_blob/d4ed56e71eec07769fd6dc5346182116',n:'Hotově / kartou při odběru',d:'Jen při osobním odběru',price:0,ptxt:'zdarma',only:['osobni']}
];
const PICKUPS=[
 {id:'p1',n:'Z-BOX Brno, Masarykova',a:'Masarykova 12, 602 00 Brno',t:'Po–Pá 8–18',sun:false,box:false},
 {id:'p2',n:'Z-BOX Praha 2, Náměstí Míru',a:'Náměstí Míru 9, 120 00 Praha 2',t:'nonstop',sun:true,box:true},
 {id:'p3',n:'Zásilkovna Ostrava, Nádražní',a:'Nádražní 45, 702 00 Ostrava',t:'Po–Ne 9–20',sun:true,box:false}
];
const DEMO_LINES=[{id:IDS.detail,qty:4},{id:IDS.cistic,qty:2},{id:IDS.metalic,qty:10}];
const loadCo=()=>{try{return JSON.parse(lsGet('CheckoutV1')||'null')}catch(e){return null}};
const saveCo=(o)=>lsSet('CheckoutV1',JSON.stringify(o));
const calc=(co)=>{const lines=(co&&co.lines)||DEMO_LINES;
 const items=lines.map((l)=>Object.assign({},byId(l.id),{qty:l.qty}));
 const sub=items.reduce((a,p)=>a+p.price*p.qty,0); const disc=co&&co.coupon?Math.round(sub*0.1*100)/100:0;
 const d=DELIV.find((x)=>co&&x.id===co.deliv); const p=PAY.find((x)=>co&&x.id===co.pay);
 const tot=sub-disc+(d?d.price:0)+(p?p.price:0);
 return {items:items,sub:sub,disc:disc,d:d,p:p,tot:tot};};
class Component extends DCLogic {
 constructor(props){super(props);this.state=Object.assign({auth:false,toast:null,co:null,loading:false},this.pageState?this.pageState():{});
  this.onAuth=()=>{const a=lsGet('AuthV1')==='in';this.setState({auth:a});if(this.onAuthChange)this.onAuthChange(a);};}
 componentDidMount(){this.onAuth();this.setState({co:loadCo()});window.addEventListener('daver-auth',this.onAuth);window.addEventListener('storage',this.onAuth);if(this.pageMount)this.pageMount();}
 componentWillUnmount(){window.removeEventListener('daver-auth',this.onAuth);window.removeEventListener('storage',this.onAuth);clearTimeout(this.tt);}
 toast(t,opt){this.setState({toast:Object.assign({t:t,err:false,links:[],undo:null},opt||{})});clearTimeout(this.tt);this.tt=setTimeout(()=>this.setState({toast:null}),(opt&&opt.err)?7000:3500);}
 setCo(patch){const co=Object.assign({},this.state.co||{lines:DEMO_LINES},patch);saveCo(co);this.setState({co:co});}
 baseVals(){const s=this.state;const c=calc(s.co);const t=s.toast;
  return {auth:s.auth,notAuth:!s.auth,userName:USER.name,userIni:USER.ini,
   hasToast:!!t,toastTxt:t?t.t:'',toastCls:'toast'+(t&&t.err?' err':''),toastLinks:t?t.links:[],hasLinks:!!t&&t.links.length>0,
   hasUndo:!!t&&!!t.undo,undo:()=>{if(t&&t.undo)t.undo();this.setState({toast:null});},closeToast:()=>this.setState({toast:null}),
   totTxt:CZK(c.tot),totVat:CZK(c.tot*VAT)+' s DPH',subTxt:CZK(c.sub),discTxt:'−'+CZK(c.disc),hasDisc:c.disc>0,
   dTxt:c.d?c.d.n+' · '+c.d.ptxt:'nevybráno',dIc:c.d?c.d.ic:'',pIc:c.p?c.p.ic:'',pTxt:c.p?c.p.n+' · '+c.p.ptxt:'nevybráno',btnCls:'btn btn-main btn-lg'+(s.loading?' loading':'')};}
 renderVals(){return Object.assign(this.baseVals(),this.pageVals());}
"""

def co_page(title, step, main, bar_back, bar_btn, page_js, h, extra_css=''):
    steps = [('Kosik.dc.html', 'Nákupní košík'), ('Udaje.dc.html', 'Kontaktní údaje'), ('Kontrola.dc.html', 'Kontrola údajů')]
    sh = ''
    for i, (href, t) in enumerate(steps):
        cls = 'on' if i + 1 == step else ('done' if i + 1 < step else '')
        lab = f'<a class="lbl" href="{href}">{t}</a>' if i + 1 < step else f'<span class="lbl">{t}</span>'
        cur = ' aria-current="step"' if i + 1 == step else ''
        no = I('check') if i + 1 < step else str(i + 1)
        sh += (f'<li class="sep{" done" if i + 1 <= step else ""}" aria-hidden="true"></li>' if i else '') + f'<li class="{cls}"{cur}><span class="no">{no}</span>{lab}</li>'
    steps_html = f'<nav aria-label="Kroky objednávky"><ol class="steps">{sh}</ol><p class="stepTxt">Krok {step} ze 3 · {steps[step-1][1]}</p></nav>' if step else ''
    if step == 1:
        steps_html = f'<sc-if value="{{{{ hasItems }}}}" hint-placeholder-val="{{{{ true }}}}">{steps_html}</sc-if>'
    bar = '' if not bar_btn else f'''<div class="bar bleed"><div class="container barIn">{bar_back}<div class="barR"><div class="barTot"><small>Celkem bez DPH</small><strong>{{{{ totTxt }}}}</strong><small>{{{{ totVat }}}}</small></div>{bar_btn}</div></div></div>'''
    body = f'''<div class="co">
<header class="coHead bleed"><div class="container coHeadIn"><a href="Main.dc.html" aria-label="Daver – úvodní stránka"><img class="logoImg" src="/_blob/31e51e752116e4c4eaf02fb3d12e760d" alt="" width="167" height="70"></a>
<div class="coHeadR"><span class="coTel">{I('phone')}<span class="coTelTxt"><a href="tel:+420775570418">+420 775 570 418</a><small>Po–Pá 9:00–16:00</small></span></span>
<sc-if value="{{{{ auth }}}}" hint-placeholder-val="{{{{ false }}}}"><span class="coUser"><span class="mono">{{{{ userIni }}}}</span><span>Přihlášen<br><strong>{{{{ userName }}}}</strong></span></span></sc-if></div></div></header>
<main class="container">{steps_html}{main}</main>
<footer class="coFoot bleed"><div class="container"><strong>DAVER, spol. s r.o.</strong> · Piešťanská 2293/68, 915 01 Nové Mesto nad Váhom · IČO 34149431 · IČ DPH SK2020381935 · <a href="tel:+420775570418">+420 775 570 418</a> · <a href="mailto:daver@daver.cz">daver@daver.cz</a>
<nav aria-label="Informace"><a href="ObchodniPodminky.dc.html">Obchodní podmínky</a><a href="Reklamace.dc.html">Reklamace</a><a href="Doprava.dc.html">Doprava a platba</a><a href="Gdpr.dc.html">Ochrana osobních údajů</a><a href="Kontakt.dc.html">Kontakty</a></nav></div></footer>
{bar}
<div class="toastWrap" aria-live="assertive"><sc-if value="{{{{ hasToast }}}}" hint-placeholder-val="{{{{ false }}}}"><div class="{{{{ toastCls }}}}" role="alert">{I('info')}<div><span>{{{{ toastTxt }}}}</span>
<sc-if value="{{{{ hasLinks }}}}" hint-placeholder-val="{{{{ false }}}}"><ul><sc-for list="{{{{ toastLinks }}}}" as="l" hint-placeholder-count="2"><li><a href="{{{{ l.href }}}}">{{{{ l.t }}}}</a></li></sc-for></ul></sc-if>
<sc-if value="{{{{ hasUndo }}}}" hint-placeholder-val="{{{{ false }}}}"><button class="btn btn-ghost btn-sm" type="button" onClick="{{{{ undo }}}}">Vrátit zpět</button></sc-if></div>
<button class="iconBtn" type="button" aria-label="Zavřít upozornění" onClick="{{{{ closeToast }}}}">{I('x')}</button></div></sc-if></div>
<dc-import name="FontSizeSwitch" hint-size="0px,0px"></dc-import>
</div>'''
    return doc(title, CO_CSS + extra_css, '', body, DATA_CO + page_js + '\n}\n', 1440, h)

co = {}
BACK_SHOP = f'<a class="btn btn-out barBack" href="Main.dc.html">{I("arrow-left")}<span>Zpět do obchodu</span></a>'

# ---------- P1 Košík ----------
kosik_main = f'''<sc-if value="{{{{ hasItems }}}}" hint-placeholder-val="{{{{ true }}}}">
<div class="coGrid">
<div>
<section class="panel"><h2>Nákupní košík</h2>
<div class="cartTbl BasketView"><sc-for list="{{{{ lines }}}}" as="l" hint-placeholder-count="3">
<div class="cl"><sc-if value="{{{{ l.hasImg }}}}" hint-placeholder-val="{{{{ true }}}}"><img class="clImg" src="{{{{ l.img }}}}" alt=""></sc-if><sc-if value="{{{{ l.noImg }}}}" hint-placeholder-val="{{{{ false }}}}"><span class="ph clImg">[FOTO]</span></sc-if><div class="clName"><a href="Detail.dc.html">{{{{ l.name }}}}</a><small>Kód {{{{ l.code }}}} · <span class="avOk">{{{{ l.av }}}}</span></small><sc-if value="{{{{ l.over }}}}" hint-placeholder-val="{{{{ false }}}}"><small class="err">Skladem je jen {{{{ l.stock }}}} ks</small></sc-if></div>
<div class="qty"><button type="button" aria-label="Snížit množství" disabled="{{{{ l.minDis }}}}" onClick="{{{{ l.dec }}}}">−</button><label><input inputmode="numeric" aria-label="Množství" size="{{{{ l.qtyLen }}}}" value="{{{{ l.qty }}}}" onChange="{{{{ l.setQ }}}}">ks</label><button type="button" aria-label="Zvýšit množství" onClick="{{{{ l.inc }}}}">+</button></div>
<div class="clPrice"><small>{{{{ l.unitTxt }}}} / ks</small><strong>{{{{ l.sumTxt }}}}</strong></div>
<button class="iconBtn" type="button" aria-label="{{{{ l.rmLabel }}}}" onClick="{{{{ l.remove }}}}">{I('trash')}</button>
</div></sc-for></div>
<div class="freeBox">{I('truck')}<div class="freeIn"><span>{{{{ freeMsg }}}}</span><progress class="freeBar" max="1000" value="{{{{ freeVal }}}}" aria-label="Postup k dopravě zdarma od 1 000 Kč"></progress></div></div>
<form class="coupon" onSubmit="{{{{ applyCoupon }}}}"><sc-if value="{{{{ noCoupon }}}}" hint-placeholder-val="{{{{ true }}}}"><label for="cpn">Máte slevový nebo dárkový kupón?</label><input id="cpn" value="{{{{ cpn }}}}" onChange="{{{{ onCpn }}}}" placeholder="Kód kupónu" aria-invalid="{{{{ cpnBad }}}}"><button class="btn btn-out" type="submit">Uplatnit</button><sc-if value="{{{{ cpnBad }}}}" hint-placeholder-val="{{{{ false }}}}"><span class="err cpnErr" role="alert">Kód neexistuje nebo už vypršel.</span></sc-if></sc-if>
<sc-if value="{{{{ hasCoupon }}}}" hint-placeholder-val="{{{{ false }}}}"><span>{I('tag')} Kupón <strong>SLEVA10</strong> uplatněn (−10 %)</span><button class="btn btn-ghost btn-sm" type="button" onClick="{{{{ rmCoupon }}}}">Odebrat</button></sc-if></form>
</section>
<div class="dpGrid"><section class="panel" id="doprava"><h2>Doprava</h2><div class="opts" role="radiogroup" aria-label="Doprava"><sc-for list="{{{{ delivs }}}}" as="o" hint-placeholder-count="4">
<label class="{{{{ o.cls }}}}"><input type="radio" name="deliv" checked="{{{{ o.on }}}}" onChange="{{{{ o.pick }}}}"><img class="logo65" src="{{{{ o.ic }}}}" alt="" width="65" height="40"><span class="optTxt"><strong>{{{{ o.n }}}}</strong><small>{{{{ o.d }}}}</small></span><span class="optPrice">{{{{ o.ptxt }}}}</span></label>
<sc-if value="{{{{ o.showPick }}}}" hint-placeholder-val="{{{{ false }}}}"><div class="optDetail"><sc-if value="{{{{ o.noPoint }}}}" hint-placeholder-val="{{{{ true }}}}"><button class="btn btn-out btn-sm" type="button" onClick="{{{{ openPick }}}}">{I('map-pin')}Vybrat odběrné místo</button></sc-if><sc-if value="{{{{ o.hasPoint }}}}" hint-placeholder-val="{{{{ false }}}}"><span>{I('map-pin')} {{{{ pointName }}}}</span><button class="btn btn-ghost btn-sm" type="button" onClick="{{{{ openPick }}}}">Změnit odběrné místo</button></sc-if></div></sc-if>
</sc-for></div></section>
<section class="panel" id="platba"><h2>Platba</h2><div class="opts" role="radiogroup" aria-label="Platba"><sc-for list="{{{{ pays }}}}" as="o" hint-placeholder-count="3">
<label class="{{{{ o.cls }}}}"><input type="radio" name="pay" checked="{{{{ o.on }}}}" disabled="{{{{ o.dis }}}}" onChange="{{{{ o.pick }}}}"><img class="logo65" src="{{{{ o.ic }}}}" alt="" width="65" height="40"><span class="optTxt"><strong>{{{{ o.n }}}}</strong><small>{{{{ o.d2 }}}}</small></span><span class="optPrice">{{{{ o.ptxt }}}}</span></label>
</sc-for></div></section></div>
</div>
<aside class="panel sumBox" aria-label="Souhrn"><h2>Souhrn objednávky</h2>
<div class="sumRow"><span>Zboží</span><span>{{{{ subTxt }}}}</span></div>
<sc-if value="{{{{ hasDisc }}}}" hint-placeholder-val="{{{{ false }}}}"><div class="sumRow"><span>Sleva SLEVA10</span><span>{{{{ discTxt }}}}</span></div></sc-if>
<div class="sumRow"><span>Doprava</span><span>{{{{ dTxt }}}}</span></div><div class="sumRow"><span>Platba</span><span>{{{{ pTxt }}}}</span></div>
<div class="sumTot"><span>Celkem bez DPH</span><div><strong>{{{{ totTxt }}}}</strong><div class="priceSub">{{{{ totVat }}}}</div></div></div></aside>
</div>
</sc-if>
<sc-if value="{{{{ noItems }}}}" hint-placeholder-val="{{{{ false }}}}"><div class="panel emptyCart">{I('shopping-cart','ic big')}<h1>Váš košík je prázdný</h1><p>Vyberte si z nabídky výtvarných potřeb.</p><div class="emptyAct"><a class="btn btn-main" href="Main.dc.html">Přejít na úvodní stránku</a><a class="btn btn-out" href="Kategorie.dc.html">Pokračovat v nákupu</a></div><button class="btn btn-ghost btn-sm" type="button" onClick="{{{{ restore }}}}">Vrátit ukázkový obsah košíku (jen prototyp)</button></div></sc-if>
<sc-if value="{{{{ pickOpen }}}}" hint-placeholder-val="{{{{ false }}}}"><div class="mdOverlay" onClick="{{{{ pickOverlay }}}}" onKeyDown="{{{{ pickKey }}}}"><div class="mdBox pickBox" role="dialog" aria-modal="true" aria-labelledby="pkT">
<div class="pickHead"><h2 id="pkT">Vyberte odběrné místo</h2><button class="iconBtn" type="button" aria-label="Zavřít" autoFocus="{{{{ true }}}}" onClick="{{{{ closePick }}}}">{I('x')}</button></div>
<div class="pickTools"><label class="sr" for="pkq">Hledat místo</label><input id="pkq" placeholder="Město, ulice nebo PSČ" value="{{{{ pq }}}}" onChange="{{{{ onPq }}}}"><label class="check"><input type="checkbox" checked="{{{{ fSun }}}}" onChange="{{{{ tSun }}}}">Otevřeno v neděli</label><label class="check"><input type="checkbox" checked="{{{{ fBox }}}}" onChange="{{{{ tBox }}}}">Boxy</label></div>
<div class="pickBody"><ul class="pickList"><sc-for list="{{{{ points }}}}" as="p" hint-placeholder-count="3"><li><button class="{{{{ p.cls }}}}" type="button" onClick="{{{{ p.pick }}}}"><strong>{{{{ p.n }}}}</strong><small>{{{{ p.a }}}} · {{{{ p.t }}}}</small></button></li></sc-for></ul><div class="ph pickMap">[MAPA – ukázka]</div></div>
<div class="pickFoot"><button class="btn btn-main" type="button" disabled="{{{{ noSel }}}}" onClick="{{{{ confirmPick }}}}">Vybrat toto odběrné místo</button></div>
</div></div></sc-if>'''
kosik_css = """
.cl{display:grid;grid-template-columns:64px minmax(0,1fr) auto 120px 44px;gap:12px;align-items:center;padding:12px 0;border-bottom:1px solid var(--line)}
.clImg{width:64px;height:64px;padding:0;font-size:9px;object-fit:contain}
.clName a{color:var(--text);font-weight:600;text-decoration:none}.clName small{display:block;font-size:var(--fs-caption);color:var(--text-weaker)}
.avOk{color:var(--success-text)}
.clPrice{text-align:right}.clPrice small{display:block;color:var(--text-weaker);font-size:var(--fs-caption)}
.qty{display:flex;align-items:center;min-width:120px;border:1px solid var(--input-border);border-radius:var(--btn-radius);height:44px;background:#fff}
.qty button{width:36px;height:100%;border:0;background:none;font-size:18px;cursor:pointer}.qty button:disabled{color:#c4c4c8}
.qty label{flex:1;display:flex;align-items:center;justify-content:center;gap:4px;padding:0 4px;white-space:nowrap}.qty input{field-sizing:content;width:auto;min-width:1ch;max-width:6ch;border:0;outline:0;text-align:center;font:inherit;padding:0;background:transparent}
.freeIn{flex:1;display:flex;flex-direction:column;gap:8px}
.freeBar{appearance:none;-webkit-appearance:none;width:100%;height:8px;border:0;border-radius:4px;background:var(--line);overflow:hidden}
.freeBar::-webkit-progress-bar{background:var(--line);border-radius:4px}
.freeBar::-webkit-progress-value{background:var(--primary);border-radius:4px}
.freeBar::-moz-progress-bar{background:var(--primary);border-radius:4px}
.freeBox{display:flex;gap:12px;align-items:center;border:1px solid var(--line);border-radius:var(--radius-md);padding:12px;margin-top:16px;font-size:var(--fs-body-sm)}
.coupon{display:flex;flex-wrap:wrap;gap:10px;align-items:center;border:1px solid var(--line);border-radius:var(--radius-md);padding:12px;margin-top:12px;font-size:var(--fs-body-sm)}
.coupon input{height:44px;border:1px solid var(--input-border);border-radius:var(--btn-radius);padding:0 12px;flex:1 1 160px;max-width:240px}
.cpnErr{flex-basis:100%}
.dpGrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(340px,1fr));gap:var(--space-4);margin-top:var(--space-4);align-items:start}
.dpGrid .panel{margin-top:0}
.opts{display:flex;flex-direction:column;gap:8px}
.opt{display:flex;align-items:center;gap:14px;padding:12px 14px;border:1px solid var(--line);border-radius:var(--card-radius);cursor:pointer;min-height:64px}
.opt input{width:18px;height:18px;accent-color:var(--primary-d);flex:none}
.opt.on{border-color:var(--primary-d);box-shadow:0 0 0 1px var(--primary-d)}
.opt.dis{opacity:.55;cursor:not-allowed}
.optTxt{flex:1;display:flex;flex-direction:column}.optTxt small{color:var(--text-weaker);font-size:var(--fs-caption)}
.optPrice{font-weight:600;white-space:nowrap}
.optDetail{display:flex;gap:12px;align-items:center;flex-wrap:wrap;padding:8px 14px 12px 46px;font-size:var(--fs-body-sm)}
.sumBox{position:sticky;top:16px}
.emptyCart{margin-top:var(--space-6);text-align:center;display:flex;flex-direction:column;gap:12px;align-items:center;padding:48px 24px}
.emptyCart .big{width:48px;height:48px;color:var(--text-muted)}
.emptyAct{display:flex;gap:12px;flex-wrap:wrap;justify-content:center}
.pickBox{width:min(880px,100%);background:#fff;display:flex;flex-direction:column}
.pickHead,.pickFoot{display:flex;justify-content:space-between;align-items:center;padding:12px 16px;border-bottom:1px solid var(--line)}
.pickFoot{border-top:1px solid var(--line);border-bottom:0;justify-content:flex-end}
.pickTools{display:flex;gap:16px;flex-wrap:wrap;align-items:center;padding:12px 16px}
.pickTools input#pkq{height:44px;border:1px solid var(--input-border);border-radius:var(--btn-radius);padding:0 12px;flex:1 1 220px}
.pickBody{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.2fr);gap:12px;padding:0 16px 16px}
.pickList{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:6px;max-height:320px;overflow:auto}
.pt{width:100%;text-align:left;border:1px solid var(--line);border-radius:var(--radius-sm);background:#fff;padding:10px 12px;cursor:pointer;display:flex;flex-direction:column}
.pt small{color:var(--text-weaker)}.pt.on{border-color:var(--primary-d);box-shadow:0 0 0 1px var(--primary-d)}
.pickMap{min-height:320px}
@media (max-width:819px){.cl{grid-template-columns:56px minmax(0,1fr) 44px}.cl .qty{grid-column:2}.cl .clPrice{grid-column:2/4;text-align:left}.clImg{width:56px;height:56px}
 .opt{flex-wrap:wrap}.opt .logo65{order:-1}.pickBody{grid-template-columns:1fr}.pickMap{min-height:160px}}
"""
kosik_js = r"""
 pageState(){return {cpn:'',cpnBad:false,pick:false,pq:'',fSun:false,fBox:false,sel:null};}
 lines(){const co=this.state.co;return (co&&co.lines)||DEMO_LINES;}
 setLines(l){this.setCo({lines:l});}
 pageVals(){
  const s=this.state;const co=s.co||{};const L=this.lines();
  const setQ=(id,q)=>{const p=byId(id);q=Math.max(1,q);this.setLines(L.map((l)=>l.id===id?{id:id,qty:q}:l));if(q>p.stock)this.toast('Skladem je jen '+p.stock+' ks – zbytek dodáme do 5 pracovních dnů.');};
  const num=(v)=>{const n=parseInt(String(v).replace(/\D/g,''),10);return isNaN(n)?1:n;};
  const payOk=(p)=>(!p.only||p.only.includes(co.deliv))&&(!p.no||!p.no.includes(co.deliv));
  const pts=PICKUPS.filter((p)=>(!s.fSun||p.sun)&&(!s.fBox||p.box)&&(p.n+p.a).toLowerCase().includes(s.pq.toLowerCase()));
  const point=PICKUPS.find((p)=>p.id===co.point);
  const sub=L.reduce((a,l)=>a+byId(l.id).price*l.qty,0);
  const goNext=(e)=>{const errs=[];
   if(!co.deliv)errs.push({t:'Vyberte způsob dopravy',href:'#doprava'});
   if(co.deliv==='box'&&!co.point)errs.push({t:'Vyberte odběrné místo',href:'#doprava'});
   if(!co.pay)errs.push({t:'Vyberte způsob platby',href:'#platba'});
   if(errs.length){e.preventDefault();this.toast('Než budete pokračovat:',{err:true,links:errs});}
   else{this.setCo({});}};
  return {
   hasItems:L.length>0,noItems:L.length===0,
   freeVal:Math.min(1000,Math.round(sub)),freeMsg:sub>=1000?'Máte dopravu zdarma.':'Do dopravy zdarma zbývá '+CZK(1000-sub)+' (zdarma od 1 000 Kč bez DPH)',
   lines:L.map((l)=>{const p=byId(l.id);return {name:p.name,img:p.img||'',hasImg:!!p.img,noImg:!p.img,code:p.code,av:avText(p.stock),stock:p.stock,over:l.qty>p.stock,qty:l.qty,qtyLen:Math.max(1,String(l.qty).length),minDis:l.qty<=1,
     unitTxt:CZK(p.price),sumTxt:CZK(p.price*l.qty),rmLabel:'Odebrat '+p.name,
     dec:()=>setQ(l.id,l.qty-1),inc:()=>setQ(l.id,l.qty+1),setQ:(e)=>setQ(l.id,num(e.target.value)),
     remove:()=>{const before=L;this.setLines(L.filter((x)=>x.id!==l.id));this.toast('Produkt odebrán z košíku.',{undo:()=>this.setLines(before)});}};}),
   restore:()=>this.setLines(DEMO_LINES),
   cpn:s.cpn,cpnBad:s.cpnBad,onCpn:(e)=>this.setState({cpn:e.target.value,cpnBad:false}),noCoupon:!co.coupon,hasCoupon:!!co.coupon,
   applyCoupon:(e)=>{e.preventDefault();if(s.cpn.trim().toUpperCase()==='SLEVA10'){this.setCo({coupon:'SLEVA10'});this.setState({cpn:''});this.toast('Kupón uplatněn.');}else this.setState({cpnBad:true});},
   rmCoupon:()=>this.setCo({coupon:null}),
   delivs:DELIV.map((d)=>({ic:d.ic,n:d.n,d:d.d,ptxt:d.ptxt,on:co.deliv===d.id,cls:'opt'+(co.deliv===d.id?' on':''),
     pick:()=>{const pay=PAY.find((p)=>p.id===co.pay);const keep=pay&&(!pay.only||pay.only.includes(d.id))&&(!pay.no||!pay.no.includes(d.id));this.setCo({deliv:d.id,pay:keep?co.pay:null});},
     showPick:!!d.pickup&&co.deliv===d.id,noPoint:!point,hasPoint:!!point})),
   pointName:point?point.n+', '+point.a:'',
   pays:PAY.map((p)=>{const ok=payOk(p);return {ic:p.ic,n:p.n,ptxt:p.ptxt,on:co.pay===p.id,dis:!ok,d2:ok?p.d:(p.only?'Dostupné jen při osobním odběru':'Nelze kombinovat s osobním odběrem'),
     cls:'opt'+(co.pay===p.id?' on':'')+(ok?'':' dis'),pick:()=>{if(ok)this.setCo({pay:p.id});}};}),
   pickOpen:s.pick,openPick:()=>this.setState({pick:true,sel:co.point||null}),closePick:()=>this.setState({pick:false}),
   pickKey:(e)=>{if(e.key==='Escape'){e.stopPropagation();this.setState({pick:false});}},pickOverlay:(e)=>{if(e.target===e.currentTarget)this.setState({pick:false});},
   pq:s.pq,onPq:(e)=>this.setState({pq:e.target.value}),fSun:s.fSun,fBox:s.fBox,tSun:()=>this.setState({fSun:!s.fSun}),tBox:()=>this.setState({fBox:!s.fBox}),
   points:pts.map((p)=>({n:p.n,a:p.a,t:p.t,cls:'pt'+(s.sel===p.id?' on':''),pick:()=>this.setState({sel:p.id})})),
   noSel:!s.sel,confirmPick:()=>{this.setCo({point:s.sel});this.setState({pick:false});},
   goNext:goNext
  };
 }
"""
co['Kosik'] = co_page('Nákupní košík', 1, kosik_main, BACK_SHOP, '<sc-if value="{{ hasItems }}" hint-placeholder-val="{{ true }}"><a class="btn btn-main btn-lg" href="Udaje.dc.html" onClick="{{ goNext }}">Pokračovat ke kontaktním údajům</a></sc-if>', kosik_js, 2400, kosik_css)

# ---------- P2 Údaje ----------
F = [('email', 'E-mail', 'email', 'email'), ('tel', 'Telefon', 'tel', 'tel'), ('jmeno', 'Jméno', 'text', 'given-name'), ('prijmeni', 'Příjmení', 'text', 'family-name')]
def fld(k, l, t='text', ac='off', extra=''):
    return f'''<div class="field" id="w_{k}"><label for="f_{k}">{l}</label>{extra}<input id="f_{k}" type="{t}" autocomplete="{ac}" class="{{{{ c_{k} }}}}" aria-invalid="{{{{ b_{k} }}}}" value="{{{{ v_{k} }}}}" onChange="{{{{ o_{k} }}}}" onBlur="{{{{ t_{k} }}}}"><sc-if value="{{{{ b_{k} }}}}" hint-placeholder-val="{{{{ false }}}}"><span class="err">{{{{ e_{k} }}}}</span></sc-if></div>'''
tel = f'''<div class="field" id="w_tel"><label for="f_tel">Telefon</label><div class="telRow"><label class="sr" for="f_pre">Předvolba</label><select id="f_pre" value="{{{{ v_pre }}}}" onChange="{{{{ o_pre }}}}"><option value="+420">+420</option><option value="+421">+421</option></select><input id="f_tel" type="tel" autocomplete="tel-national" class="{{{{ c_tel }}}}" aria-invalid="{{{{ b_tel }}}}" value="{{{{ v_tel }}}}" onChange="{{{{ o_tel }}}}" onBlur="{{{{ t_tel }}}}"></div><sc-if value="{{{{ b_tel }}}}" hint-placeholder-val="{{{{ false }}}}"><span class="err">{{{{ e_tel }}}}</span></sc-if></div>'''
udaje_main = f'''<div class="coGrid"><div>
<sc-if value="{{{{ notAuth }}}}" hint-placeholder-val="{{{{ true }}}}"><section class="panel"><h2>Jak chcete pokračovat?</h2><div class="choice">
<button class="opt" type="button" onClick="{{{{ openLogin }}}}">{I('user')}<span class="optTxt"><strong>Mám zde svůj účet</strong><small>Přihlaste se a údaje doplníme z účtu</small></span></button>
<label class="{{{{ newCls }}}}"><input type="radio" name="who" checked="{{{{ isNew }}}}" onChange="{{{{ setNew }}}}"><span class="optTxt"><strong>Jsem nový zákazník</strong><small>Objednávku můžete dokončit i bez účtu</small></span></label></div></section></sc-if>
<sc-if value="{{{{ auth }}}}" hint-placeholder-val="{{{{ false }}}}"><section class="panel loggedCard"><span class="mono">{{{{ userIni }}}}</span><div><strong>Přihlášený zákazník</strong><br>{{{{ userName }}}} · cenová skupina {{{{ group }}}}</div></section></sc-if>
<section class="panel"><h2>Kontaktní údaje</h2><div class="fGrid">
{fld('email','E-mail','email','email')}{tel}{fld('jmeno','Jméno','text','given-name')}{fld('prijmeni','Příjmení','text','family-name')}
<div class="field span2 addr" id="w_ulice"><label for="f_ulice">Ulice a číslo popisné</label><input id="f_ulice" autocomplete="off" class="{{{{ c_ulice }}}}" aria-invalid="{{{{ b_ulice }}}}" value="{{{{ v_ulice }}}}" onChange="{{{{ o_ulice }}}}" onBlur="{{{{ t_ulice }}}}">
<sc-if value="{{{{ addrOpen }}}}" hint-placeholder-val="{{{{ false }}}}"><ul class="addrSug"><sc-for list="{{{{ addrList }}}}" as="a" hint-placeholder-count="3"><li><button type="button" onClick="{{{{ a.pick }}}}">{{{{ a.t }}}}</button></li></sc-for><li class="hint">Našeptávač adres (Smartform) – ukázkové výsledky</li></ul></sc-if>
<sc-if value="{{{{ b_ulice }}}}" hint-placeholder-val="{{{{ false }}}}"><span class="err">{{{{ e_ulice }}}}</span></sc-if></div>
{fld('mesto','Město','text','address-level2')}{fld('psc','PSČ','text','postal-code')}
</div>
<sc-if value="{{{{ isNewNotAuth }}}}" hint-placeholder-val="{{{{ false }}}}"><label class="check mt"><input type="checkbox" checked="{{{{ mkAcc }}}}" onChange="{{{{ tAcc }}}}">Vytvořit si B2B účet (registraci schválí obchodní oddělení)</label>
<sc-if value="{{{{ mkAcc }}}}" hint-placeholder-val="{{{{ false }}}}"><div class="fGrid mt">{fld('heslo','Heslo (min. 6 znaků)','password','new-password')}</div></sc-if></sc-if>
</section>
<section class="panel"><label class="check"><input type="checkbox" checked="{{{{ firm }}}}" onChange="{{{{ tFirm }}}}"><strong>Nakupuji na firmu</strong></label>
<sc-if value="{{{{ firm }}}}" hint-placeholder-val="{{{{ true }}}}"><div class="fGrid mt">
<div class="field" id="w_ic"><label for="f_ic">IČ</label><div class="telRow"><input id="f_ic" inputmode="numeric" class="{{{{ c_ic }}}}" aria-invalid="{{{{ b_ic }}}}" value="{{{{ v_ic }}}}" onChange="{{{{ o_ic }}}}" onBlur="{{{{ t_ic }}}}"><button class="btn btn-out" type="button" onClick="{{{{ ares }}}}">ARES</button></div><sc-if value="{{{{ b_ic }}}}" hint-placeholder-val="{{{{ false }}}}"><span class="err">{{{{ e_ic }}}}</span></sc-if></div>
{fld('dic','DIČ')}{fld('firma','Název firmy','text','organization').replace('class="field"','class="field span2"')}
</div></sc-if></section>
<section class="panel"><label class="check"><input type="checkbox" checked="{{{{ other }}}}" onChange="{{{{ tOther }}}}"><strong>Doručit na jinou adresu</strong></label>
<sc-if value="{{{{ other }}}}" hint-placeholder-val="{{{{ false }}}}"><div class="fGrid mt">{fld('dJmeno','Jméno a příjmení / firma')}{fld('dUlice','Ulice a číslo')}{fld('dMesto','Město')}{fld('dPsc','PSČ')}</div></sc-if>
<div class="field mt"><label for="f_note">Poznámka k objednávce</label><textarea id="f_note" value="{{{{ v_note }}}}" onChange="{{{{ o_note }}}}"></textarea></div></section>
<section class="panel"><label class="check"><input type="checkbox" checked="{{{{ news }}}}" onChange="{{{{ tNews }}}}">Chci dostávat novinky a akční nabídky e-mailem</label>
<p class="consent">Odesláním objednávky souhlasíte se zasláním dotazníku spokojenosti v rámci programu Ověřeno zákazníky (Heureka) a Zboží.cz. Souhlas můžete kdykoli odvolat.</p></section>
</div>
<aside class="panel sumBox" aria-label="Souhrn"><h2>Souhrn objednávky</h2><div class="sumRow"><span>Zboží</span><span>{{{{ subTxt }}}}</span></div><div class="sumRow"><span>Doprava</span><span>{{{{ dTxt }}}}</span></div><div class="sumRow"><span>Platba</span><span>{{{{ pTxt }}}}</span></div><div class="sumTot"><span>Celkem bez DPH</span><div><strong>{{{{ totTxt }}}}</strong><div class="priceSub">{{{{ totVat }}}}</div></div></div></aside>
</div>
<sc-if value="{{{{ loginOpen }}}}" hint-placeholder-val="{{{{ false }}}}"><div class="mdOverlay" onClick="{{{{ loginOverlay }}}}"><div class="mdBox"><dc-import name="LoginPopup" on-close="{{{{ closeLogin }}}}" on-login="{{{{ doLogin }}}}" hint-size="320px,420px"></dc-import></div></div></sc-if>'''
udaje_css = """
.choice{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px}
.opt{display:flex;align-items:center;gap:14px;padding:14px;border:1px solid var(--line);border-radius:var(--card-radius);cursor:pointer;background:#fff;text-align:left;min-height:64px}
.opt input{width:18px;height:18px;accent-color:var(--primary-d)}.opt.on{border-color:var(--primary-d);box-shadow:0 0 0 1px var(--primary-d)}
.optTxt{display:flex;flex-direction:column}.optTxt small{color:var(--text-weaker);font-size:var(--fs-caption)}
.loggedCard{display:flex;gap:14px;align-items:center}
.fGrid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:16px}
.span2{grid-column:span 2}
.telRow{display:flex;gap:8px}.telRow select{width:96px;flex:none;height:44px;border:1px solid var(--input-border);border-radius:var(--btn-radius);padding:0 8px;background:#fff}
.addr{position:relative}
.addrSug{position:absolute;top:100%;left:0;right:0;z-index:20;list-style:none;margin:4px 0 0;padding:4px;background:#fff;border:1px solid var(--line);border-radius:var(--radius-md);box-shadow:0 8px 20px rgba(0,0,0,.1)}
.addrSug button{width:100%;text-align:left;border:0;background:none;padding:10px;border-radius:var(--radius-sm);cursor:pointer}.addrSug button:hover{background:var(--primary-10)}
.addrSug .hint{font-size:var(--fs-caption);color:var(--text-muted);padding:6px 10px}
.mt{margin-top:16px}
.consent{font-size:var(--fs-caption);color:var(--text-weaker);margin-top:8px}
.sumBox{position:sticky;top:16px}
@media (max-width:1149px){.fGrid{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:549px){.fGrid,.choice{grid-template-columns:1fr}.span2{grid-column:auto}}
"""
udaje_js = r"""
 pageState(){return {f:{pre:'+420'},touched:{},tried:false,isNew:true,mkAcc:false,firm:true,other:false,news:false,login:false,addrOpen:false};}
 pageMount(){const c=loadCo();if(c&&c.contact)this.setState({f:Object.assign({pre:'+420'},c.contact.f),firm:c.contact.firm!==false,other:!!c.contact.other});}
 onAuthChange(a){
  if(a)this.setState({f:Object.assign({},this.state.f,{email:'jan.novak@example.cz',tel:'603 123 456',jmeno:'Jan',prijmeni:'Novák',ulice:'Husova 18',mesto:'Brno',psc:'60200',ic:'27654321',firma:'Papírnictví Novák s.r.o.'}),firm:true});
  else if(this.state.f.firma==='[DEMO] Papírnictví Novák s.r.o.')this.setState({f:{pre:'+420'},touched:{}});
 }
 errs(){const f=this.state.f,s=this.state,E={};const v=(k)=>(f[k]||'').trim();
  if(!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(v('email')))E.email='Zadejte platný e-mail.';
  if(v('tel').replace(/\s/g,'').length<9&&v('tel')!=='603 123 456')E.tel='Zadejte telefon (9 číslic).';
  ['jmeno','prijmeni','ulice','mesto'].forEach((k)=>{if(!v(k))E[k]='Vyplňte prosím.';});
  if(!/^\d{3}\s?\d{2}$/.test(v('psc')))E.psc='PSČ má 5 číslic.';
  if(s.firm){if(!/^\d{8}$/.test(v('ic'))&&v('ic')!=='27654321')E.ic='IČ má 8 číslic.';if(!v('firma'))E.firma='Vyplňte název firmy.';}
  if(s.other){['dJmeno','dUlice','dMesto','dPsc'].forEach((k)=>{if(!v(k))E[k]='Vyplňte prosím.';});}
  if(s.mkAcc&&!s.auth&&v('heslo').length<6)E.heslo='Heslo musí mít alespoň 6 znaků.';
  return E;}
 pageVals(){
  const s=this.state;const E=this.errs();const out={};
  const LBL={email:'E-mail',tel:'Telefon',jmeno:'Jméno',prijmeni:'Příjmení',ulice:'Ulice',mesto:'Město',psc:'PSČ',ic:'IČ',firma:'Název firmy',dJmeno:'Dodací jméno',dUlice:'Dodací ulice',dMesto:'Dodací město',dPsc:'Dodací PSČ',heslo:'Heslo'};
  ['email','tel','jmeno','prijmeni','ulice','mesto','psc','ic','dic','firma','dJmeno','dUlice','dMesto','dPsc','heslo','note','pre'].forEach((k)=>{
   const bad=!!E[k]&&(s.tried||s.touched[k]);
   out['v_'+k]=s.f[k]||'';out['b_'+k]=bad;out['e_'+k]=E[k]||'';out['c_'+k]=bad?'bad':'';
   out['o_'+k]=(e)=>this.setState({f:Object.assign({},s.f,{[k]:e.target.value}),addrOpen:k==='ulice'&&e.target.value.length>=3});
   out['t_'+k]=()=>this.setState({touched:Object.assign({},s.touched,{[k]:true})});});
  const q=(s.f.ulice||'');
  return Object.assign(out,{
   group:USER.group,isNew:s.isNew,newCls:'opt'+(s.isNew?' on':''),setNew:()=>this.setState({isNew:true}),isNewNotAuth:s.isNew&&!s.auth,
   mkAcc:s.mkAcc,tAcc:()=>this.setState({mkAcc:!s.mkAcc}),firm:s.firm,tFirm:()=>this.setState({firm:!s.firm}),
   other:s.other,tOther:()=>this.setState({other:!s.other}),news:s.news,tNews:()=>this.setState({news:!s.news}),
   addrOpen:s.addrOpen,addrList:['1','2','3'].map((n)=>({t:q+' '+n+', 602 00 Brno',pick:()=>this.setState({f:Object.assign({},s.f,{ulice:q+' '+n,mesto:'Brno',psc:'60200'}),addrOpen:false})})),
   ares:()=>{const ic=(s.f.ic||'').trim();if(ic==='00000000'){this.toast('Firma s tímto IČ nebyla v ARES nalezena.',{err:true});return;}
     if(!/^\d{8}$/.test(ic)){this.setState({touched:Object.assign({},s.touched,{ic:true})});return;}
     this.setState({f:Object.assign({},s.f,{firma:'[ARES ukázka] Firma s.r.o.',dic:'CZ'+ic,ulice:'[ARES ulice]',mesto:'[ARES město]',psc:'00000'})});this.toast('Údaje doplněny z ARES (ukázka).');},
   loginOpen:s.login,openLogin:()=>this.setState({login:true}),closeLogin:()=>this.setState({login:false}),
   loginOverlay:(e)=>{if(e.target===e.currentTarget)this.setState({login:false});},
   doLogin:()=>{lsSet('AuthV1','in');window.dispatchEvent(new Event('daver-auth'));},
   goNext:(e)=>{const ks=Object.keys(E);this.setState({tried:true});
     if(ks.length){e.preventDefault();this.toast('Zkontrolujte prosím tato pole:',{err:true,links:ks.map((k)=>({t:LBL[k]+' – '+E[k],href:'#w_'+k}))});}
     else{this.setCo({contact:{f:s.f,firm:s.firm,other:s.other,news:s.news}});}}
  });
 }
"""
co['Udaje'] = co_page('Kontaktní údaje', 2, udaje_main, f'<a class="btn btn-out barBack" href="Kosik.dc.html">{I("arrow-left")}<span>Zpět do košíku</span></a>', '<a class="btn btn-main btn-lg" href="Kontrola.dc.html" onClick="{{ goNext }}">Pokračovat ke kontrole</a>', udaje_js, 2600, udaje_css)

# ---------- P3 Kontrola ----------
kontrola_main = f'''<sc-if value="{{{{ demo }}}}" hint-placeholder-val="{{{{ false }}}}"><p class="demoNote">Zobrazena ukázková data – projděte košík a kontaktní údaje pro vlastní obsah.</p></sc-if>
<div class="coGrid"><div>
<section class="panel"><div class="pHead"><h2>Zboží</h2><a href="Kosik.dc.html">Změnit</a></div>
<sc-for list="{{{{ items }}}}" as="i" hint-placeholder-count="3"><div class="kRow"><sc-if value="{{{{ i.hasImg }}}}" hint-placeholder-val="{{{{ true }}}}"><img class="kImg" src="{{{{ i.img }}}}" alt=""></sc-if><sc-if value="{{{{ i.noImg }}}}" hint-placeholder-val="{{{{ false }}}}"><span class="ph kImg">[FOTO]</span></sc-if><span class="kName">{{{{ i.name }}}}<small>Kód {{{{ i.code }}}}</small></span><span>{{{{ i.qty }}}} ks</span><strong>{{{{ i.sum }}}}</strong></div></sc-for>
<sc-if value="{{{{ hasDisc }}}}" hint-placeholder-val="{{{{ false }}}}"><div class="kRow"><span></span><span class="kName">Sleva SLEVA10</span><span></span><strong>{{{{ discTxt }}}}</strong></div></sc-if></section>
<section class="panel"><div class="pHead"><h2>Doprava a platba</h2><a href="Kosik.dc.html">Změnit</a></div>
<div class="kInfo"><img class="logo65" src="{{{{ dIc }}}}" alt="" width="65" height="40"><span>{{{{ dTxt }}}}<sc-if value="{{{{ hasPoint }}}}" hint-placeholder-val="{{{{ false }}}}"><small>{{{{ point }}}}</small></sc-if></span></div>
<div class="kInfo"><img class="logo65" src="{{{{ pIc }}}}" alt="" width="65" height="40"><span>{{{{ pTxt }}}}</span></div></section>
<section class="panel"><div class="pHead"><h2>Kontaktní údaje</h2><a href="Udaje.dc.html">Změnit</a></div>
<dl class="kDl"><div><dt>Jméno</dt><dd>{{{{ name }}}}</dd></div><div><dt>E-mail</dt><dd>{{{{ email }}}}</dd></div><div><dt>Telefon</dt><dd>{{{{ tel }}}}</dd></div><div><dt>Adresa</dt><dd>{{{{ addr }}}}</dd></div>
<sc-if value="{{{{ firm }}}}" hint-placeholder-val="{{{{ true }}}}"><div><dt>Firma</dt><dd>{{{{ firma }}}}</dd></div></sc-if>
<sc-if value="{{{{ other }}}}" hint-placeholder-val="{{{{ false }}}}"><div><dt>Dodací adresa</dt><dd>{{{{ dAddr }}}}</dd></div></sc-if>
<sc-if value="{{{{ hasNote }}}}" hint-placeholder-val="{{{{ false }}}}"><div><dt>Poznámka</dt><dd>{{{{ note }}}}</dd></div></sc-if></dl></section>
<section class="panel" id="vop"><label class="check"><input type="checkbox" checked="{{{{ agree }}}}" onChange="{{{{ tAgree }}}}">Souhlasím s <a href="ObchodniPodminky.dc.html">obchodními podmínkami</a> a beru na vědomí <a href="Gdpr.dc.html">zpracování osobních údajů</a>.</label>
<sc-if value="{{{{ notAuth }}}}" hint-placeholder-val="{{{{ true }}}}"><label class="check mt"><input type="checkbox">Založit mi B2B účet s těmito údaji</label></sc-if></section>
</div>
<aside class="panel sumBox" aria-label="Souhrn"><h2>K úhradě</h2><div class="sumRow"><span>Zboží</span><span>{{{{ subTxt }}}}</span></div><sc-if value="{{{{ hasDisc }}}}" hint-placeholder-val="{{{{ false }}}}"><div class="sumRow"><span>Sleva</span><span>{{{{ discTxt }}}}</span></div></sc-if><div class="sumRow"><span>Doprava</span><span>{{{{ dTxt }}}}</span></div><div class="sumRow"><span>Platba</span><span>{{{{ pTxt }}}}</span></div><div class="sumTot"><span>Celkem bez DPH</span><div><strong>{{{{ totTxt }}}}</strong><div class="priceSub">{{{{ totVat }}}}</div></div></div></aside>
</div>'''
kontrola_css = """
.demoNote{margin-top:16px;font-size:var(--fs-body-sm);color:var(--text-weaker);border:1px solid var(--line);border-radius:var(--radius-md);padding:10px 14px;background:#fff}
.pHead{display:flex;justify-content:space-between;align-items:baseline}
.kRow{display:grid;grid-template-columns:48px minmax(0,1fr) 64px 120px;gap:12px;align-items:center;padding:8px 0;border-bottom:1px solid var(--line);font-size:var(--fs-body-sm)}
.kRow strong{text-align:right}.kImg{width:48px;height:48px;padding:0;font-size:9px;object-fit:contain}
.kName small{display:block;color:var(--text-weaker)}
.kInfo{display:flex;gap:12px;align-items:center;padding:6px 0}.kInfo small{display:block;color:var(--text-weaker)}
.kDl{margin:0;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px 24px;font-size:var(--fs-body-sm)}
.kDl dt{color:var(--text-weaker)}.kDl dd{margin:0}
.mt{margin-top:12px}.sumBox{position:sticky;top:16px}
@media (max-width:549px){.kDl{grid-template-columns:1fr}.kRow{grid-template-columns:48px minmax(0,1fr) auto}.kRow>span:nth-child(3){display:none}}
"""
kontrola_js = r"""
 pageState(){return {agree:false};}
 pageVals(){
  const s=this.state;const co=s.co;const c=calc(co);const ct=co&&co.contact;
  const f=ct?ct.f:{jmeno:'Jan',prijmeni:'Novák',email:'jan.novak@example.cz',pre:'+420',tel:'603 123 456',ulice:'Husova 18',mesto:'Brno',psc:'60200',firma:'Papírnictví Novák s.r.o.',ic:'27654321'};
  const pt=co&&co.point?PICKUPS.find((p)=>p.id===co.point):null;
  return {demo:!ct||!co.deliv,
   items:c.items.map((i)=>({name:i.name,img:i.img||'',hasImg:!!i.img,noImg:!i.img,code:i.code,qty:i.qty,sum:CZK(i.price*i.qty)})),
   hasPoint:!!pt,point:pt?pt.n+', '+pt.a:'',
   name:(f.jmeno||'')+' '+(f.prijmeni||''),email:f.email||'',tel:(f.pre||'+420')+' '+(f.tel||''),addr:(f.ulice||'')+', '+(f.psc||'')+' '+(f.mesto||''),
   firm:!ct||ct.firm!==false,firma:(f.firma||'')+(f.ic?' · IČ '+f.ic:'')+(f.dic?' · DIČ '+f.dic:''),
   other:!!(ct&&ct.other),dAddr:[f.dJmeno,f.dUlice,f.dPsc,f.dMesto].filter(Boolean).join(', '),
   hasNote:!!f.note,note:f.note||'',
   agree:s.agree,tAgree:()=>this.setState({agree:!s.agree}),
   submit:(e)=>{if(!s.agree){e.preventDefault();this.toast('Pro odeslání objednávky potvrďte souhlas:',{err:true,links:[{t:'Souhlas s obchodními podmínkami',href:'#vop'}]});return;}
     this.setState({loading:true});this.setCo({orderNo:'2026'+String(Math.floor(Math.random()*90000)+10000),total:c.tot});}
  };
 }
"""
co['Kontrola'] = co_page('Kontrola údajů', 3, kontrola_main, f'<a class="btn btn-out barBack" href="Udaje.dc.html">{I("arrow-left")}<span>Zpět k údajům</span></a>', '<a class="{{ btnCls }}" href="Dekujeme.dc.html" onClick="{{ submit }}">Odeslat objednávku</a>', kontrola_js, 2000, kontrola_css)

# ---------- P4 Děkujeme ----------
dek_main = f'''<div class="thanksHead">{I('check-circle','ic big')}<h1>Děkujeme za objednávku</h1><p>Potvrzení jsme poslali na váš e-mail.</p>
<div class="orderNo">Číslo objednávky <strong>{{{{ orderNo }}}}</strong><button class="iconBtn" type="button" aria-label="Kopírovat číslo objednávky" onClick="{{{{ copyNo }}}}">{I('copy')}</button></div></div>
<div class="variant" role="group" aria-label="Varianta platby (jen prototyp)"><span>Varianta platby (jen prototyp):</span><sc-for list="{{{{ variants }}}}" as="v" hint-placeholder-count="3"><button class="{{{{ v.cls }}}}" type="button" aria-pressed="{{{{ v.on }}}}" onClick="{{{{ v.pick }}}}">{{{{ v.n }}}}</button></sc-for></div>
<div class="coGrid"><div>
<sc-if value="{{{{ isTransfer }}}}" hint-placeholder-val="{{{{ true }}}}"><section class="panel"><h2>Platba převodem</h2><div class="payGrid">
<dl class="payDl"><div><dt>Číslo účtu</dt><dd>2801234567/2010</dd></div><div><dt>IBAN</dt><dd>CZ65 2010 0000 0028 0123 4567</dd></div>
<div><dt>Variabilní symbol</dt><dd>{{{{ orderNo }}}} <button class="btn btn-ghost btn-sm" type="button" onClick="{{{{ copyNo }}}}">Kopírovat</button></dd></div>
<div><dt>Částka</dt><dd><strong>{{{{ amount }}}}</strong> <button class="btn btn-ghost btn-sm" type="button" onClick="{{{{ copyAmt }}}}">Kopírovat</button></dd></div></dl>
<div class="qr"><div class="ph qrBox">{I('qr-code','ic qrIc')}QR platba</div><small>SPAYD: {{{{ spayd }}}}</small><span class="todo">[QR se vygeneruje z SPAYD po doplnění účtu]</span></div></div>
<p class="note">Při platbě převodem na fakturu je splatnost 14 dní od vystavení faktury.</p></section></sc-if>
<sc-if value="{{{{ isCod }}}}" hint-placeholder-val="{{{{ false }}}}"><section class="panel"><h2>Platba dobírkou</h2><p>Částku <strong>{{{{ amount }}}}</strong> zaplatíte při převzetí zásilky.</p></section></sc-if>
<sc-if value="{{{{ isShop }}}}" hint-placeholder-val="{{{{ false }}}}"><section class="panel"><h2>Platba při odběru</h2><p>Zaplatíte hotově nebo kartou při vyzvednutí. Ozveme se, až bude zboží připravené.</p></section></sc-if>
<section class="panel"><h2>Co bude dál</h2><ol class="next"><li><strong>Potvrzení objednávky</strong><span>Obchodní oddělení objednávku zkontroluje.</span></li><li><strong>Expedice</strong><span>Objednávky do 12:00 odesíláme týž den.</span></li><li><strong>Doručení</strong><span>Pošleme vám informaci o zásilce.</span></li></ol></section>
<sc-if value="{{{{ notAuth }}}}" hint-placeholder-val="{{{{ true }}}}"><section class="panel"><h2>Nakupujete pravidelně?</h2><p>Požádejte o B2B účet – uvidíte velkoobchodní ceny a historii objednávek.</p><a class="btn btn-out mt" href="Spoluprace.dc.html">Požádat o B2B účet</a></section></sc-if>
<sc-if value="{{{{ auth }}}}" hint-placeholder-val="{{{{ false }}}}"><section class="panel"><p>{I('check-circle')} Objednávka je ve vašem účtu v přehledu objednávek.</p></section></sc-if>
</div>
<aside class="panel" aria-label="Shrnutí"><h2>Shrnutí objednávky</h2><sc-for list="{{{{ items }}}}" as="i" hint-placeholder-count="3"><div class="sumRow"><span>{{{{ i.qty }}}}× {{{{ i.name }}}}</span><span>{{{{ i.sum }}}}</span></div></sc-for>
<div class="sumRow"><span>Doprava</span><span>{{{{ dTxt }}}}</span></div><div class="sumTot"><span>Celkem bez DPH</span><div><strong>{{{{ totTxt }}}}</strong><div class="priceSub">{{{{ totVat }}}}</div></div></div>
<a class="btn btn-main mt" href="Main.dc.html">Zpět do obchodu</a></aside>
</div>'''
dek_css = """
.thanksHead{text-align:center;display:flex;flex-direction:column;align-items:center;gap:8px;margin-top:var(--space-6)}
.thanksHead .big{width:56px;height:56px;color:var(--success)}
.orderNo{display:flex;align-items:center;gap:8px;background:#fff;border:1px solid var(--line);border-radius:999px;padding:4px 4px 4px 16px;margin-top:8px}
.variant{display:flex;gap:8px;align-items:center;justify-content:center;flex-wrap:wrap;margin-top:var(--space-5);font-size:var(--fs-body-sm);color:var(--text-weaker)}
.vb{min-height:36px;padding:0 14px;border:1px solid var(--input-border);border-radius:999px;background:#fff;cursor:pointer}.vb.on{background:var(--primary-d);color:#fff;border-color:var(--primary-d)}
.payGrid{display:grid;grid-template-columns:minmax(0,1fr) 200px;gap:24px}
.payDl{margin:0;display:flex;flex-direction:column;gap:10px}.payDl div{display:flex;justify-content:space-between;gap:12px;border-bottom:1px solid var(--line);padding-bottom:8px}.payDl dt{color:var(--text-weaker)}.payDl dd{margin:0;text-align:right}
.qr{display:flex;flex-direction:column;gap:6px;font-size:var(--fs-caption);word-break:break-all}
.qrBox{width:200px;height:200px;flex-direction:column;gap:6px}.qrIc{width:48px;height:48px}
.note{font-size:var(--fs-body-sm);color:var(--text-weaker);margin-top:12px}
.next{margin:0;padding-left:20px;display:flex;flex-direction:column;gap:10px}.next span{display:block;color:var(--text-weaker);font-size:var(--fs-body-sm)}
.mt{margin-top:12px;width:100%}
@media (max-width:549px){.payGrid{grid-template-columns:1fr}}
"""
dek_js = r"""
 pageState(){return {variant:null};}
 pageVals(){
  const s=this.state;const co=s.co;const c=calc(co);const no=(co&&co.orderNo)||'202612345';
  const v=s.variant||(co&&co.pay==='dobirka'?'cod':co&&co.pay==='prodejna'?'shop':'transfer');
  const V=[['transfer','Převodem'],['cod','Dobírka'],['shop','Při odběru']];
  return {orderNo:no,amount:CZK(c.tot*VAT)+' s DPH',
   spayd:'SPD*1.0*ACC:CZ6520100000002801234567*AM:'+(c.tot*VAT).toFixed(2)+'*CC:CZK*X-VS:'+no,
   isTransfer:v==='transfer',isCod:v==='cod',isShop:v==='shop',
   variants:V.map((x)=>({n:x[1],on:v===x[0]?'true':'false',cls:'vb'+(v===x[0]?' on':''),pick:()=>this.setState({variant:x[0]})})),
   copyNo:()=>{try{navigator.clipboard.writeText(no);}catch(e){}this.toast('Zkopírováno: '+no);},
   copyAmt:()=>{try{navigator.clipboard.writeText((c.tot*VAT).toFixed(2));}catch(e){}this.toast('Částka zkopírována.');},
   items:c.items.map((i)=>({name:i.name,qty:i.qty,sum:CZK(i.price*i.qty)}))};
 }
"""
co['Dekujeme'] = co_page('Děkujeme za objednávku', 0, dek_main, '', '', dek_js, 1900, dek_css)

if __name__ == '__main__':
    for n, c in list(info.items()) + list(co.items()):
        write(n + '.dc.html', c.replace('></input>', '>'))
    print(list(info), list(co))
