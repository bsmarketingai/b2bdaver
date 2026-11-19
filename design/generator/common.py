import json, os
ICONS = json.load(open(os.path.join(os.path.dirname(__file__), 'icons.json')))
ROOT = '/mnt/user-data/outputs/artifacts/c7fe9eb6-e615-4a31-8210-b7a5a74b8a77/project'

def I(name, cls='ic'):
    # Phosphor regular, inline, dekorativní
    p = ICONS[name].replace('/>', '></path>') if '/>' in ICONS[name] else ICONS[name]
    p = p.replace('></path></path>', '></path>')
    return f'<svg class="{cls}" viewBox="0 0 256 256" fill="currentColor" aria-hidden="true">{p}</svg>'

# ---------- Design tokeny: NEUTRÁLNÍ (barvy a písmo se doladí) ----------
TOKENS = """
:root{
  color-scheme: light;
  /* značka – zatím neutrální šedá škála */
  --primary:#9b414b; --primary-d:#7f343d; --primary-10:#f8eeef; /* značka Daver – vínová; konverzní (--main) zůstává černá */
  --main:#27272a; --main-d:#09090b;
  --nav-bg:#9b414b; --nav-fg:#fff; --nav-hover:#7f343d;
  --footer-bg:#27272a;
  --text:rgba(24,24,27,.92); --text-weaker:rgba(24,24,27,.68); --text-muted:#71717a;
  --bg:#fff; --bg-soft:#f8f8f8; --line:#e4e4e7;
  --input-border:#d4d4d8; --input-bg-soft:#f4f4f5;
  --success:#15803d; --success-text:#15803d; --primary-text:#27272a; --info:#1f6fa8; --danger:#b91c1c;
  --flag-discount:#ffc107; --flag-discount-fg:#1e1e1e;
  --flag-akce:#c2410c; --flag-novinka:#0277bd; --flag-doporucujeme:#1f6fa8; --flag-vyprodej:#3867d6;
  --radius-xs:2px; --radius-sm:4px; --radius-md:6px; --radius-lg:8px;
  --corner-shape:squircle; /* squircle rohy: karty a tlačítka */
  --btn-radius:6px; --card-radius:8px; /* fallback bez podpory corner-shape */
  --btn-h-sm:32px; --btn-h-md:44px; --btn-h-lg:56px;
  --space-1:4px; --space-2:8px; --space-3:12px; --space-4:16px; --space-5:24px; --space-6:32px; --space-7:48px; --space-8:64px;
  --gutter-xxs:12px; --gutter-xs:16px; --gutter-s:16px; --gutter-m:24px; --gutter-l:24px; --gutter-xl:32px; --gutter-xxl:32px;
  --gutter:var(--gutter-xxs);
  --content-max:1560px;
  --section-gap:var(--space-6); --card-pad:var(--space-4); --grid-gap:var(--space-3);
  --font:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;
  --fs-h1:29px; --fs-h2:23px; --fs-h3:19px; --fs-h4:17px; --fs-body:16px; --fs-body-sm:14px; --fs-caption:13px;
  --fs-price-md:21px; --fs-price-sm:16px; --lh-body:1.5;
  --header-h:0px;
}
@supports (corner-shape:squircle){:root{--btn-radius:16px;--card-radius:24px;--radius-xs:4px;--radius-sm:12px;--radius-md:16px;--radius-lg:24px}}
@media (min-width:420px){:root{--gutter:var(--gutter-xs)}}
@media (min-width:550px){:root{--gutter:var(--gutter-s)}}
@media (min-width:820px){:root{--gutter:var(--gutter-m);--section-gap:var(--space-7);--card-pad:var(--space-5);--grid-gap:var(--space-4);--fs-h1:34px;--fs-h2:26px;--fs-h3:21px}}
@media (min-width:1000px){:root{--gutter:var(--gutter-l)}}
@media (min-width:1150px){:root{--gutter:var(--gutter-xl);--section-gap:var(--space-8);--fs-h1:42px;--fs-h2:30px;--fs-h3:23px;--fs-h4:19px;--fs-body:17px;--fs-body-sm:15px;--fs-caption:13px;--fs-price-md:23px;--fs-price-sm:17px}}
@media (min-width:1440px){:root{--gutter:var(--gutter-xxl)}}
"""

SQ_ALL = "@supports (corner-shape:squircle){*,*::before,*::after{corner-shape:squircle}}\n"
SCROLL_CSS = ".carTrack,.rowsBox,.ddList,.pickList,.sug,.drawer{scrollbar-width:thin;scrollbar-color:var(--primary) transparent}\n.carTrack::-webkit-scrollbar{height:8px}.rowsBox::-webkit-scrollbar,.ddList::-webkit-scrollbar,.pickList::-webkit-scrollbar,.sug::-webkit-scrollbar,.drawer::-webkit-scrollbar{width:8px;height:8px}\n.carTrack::-webkit-scrollbar-track,.rowsBox::-webkit-scrollbar-track,.ddList::-webkit-scrollbar-track,.pickList::-webkit-scrollbar-track,.sug::-webkit-scrollbar-track,.drawer::-webkit-scrollbar-track{background:transparent}\n.carTrack::-webkit-scrollbar-thumb,.rowsBox::-webkit-scrollbar-thumb,.ddList::-webkit-scrollbar-thumb,.pickList::-webkit-scrollbar-thumb,.sug::-webkit-scrollbar-thumb,.drawer::-webkit-scrollbar-thumb{background:var(--primary);border-radius:4px}\n"
SQ_INPUTS = "@supports (corner-shape:squircle){.qty,.miniQty,.rowQty,.searchBox,.ddBtn,.coupon input,.field input,.field select,.field textarea,.pickTools input,.perPage select,input[type=text],input[type=search],input[type=email],input[type=tel],input[type=password],input[type=number],select,textarea{corner-shape:squircle}}\n"
BASE_CSS = """
"""+SQ_INPUTS+SQ_ALL+SCROLL_CSS+"""
*,*::before,*::after{box-sizing:border-box}
html,body{margin:0}
body{font-family:var(--font);font-size:var(--fs-body);line-height:var(--lh-body);color:var(--text);background:var(--bg);-webkit-font-smoothing:antialiased}
img{max-width:100%;display:block}
h1,h2,h3,h4{margin:0;line-height:1.2;color:var(--text)}
h1{font-size:var(--fs-h1)}h2{font-size:var(--fs-h2)}h3{font-size:var(--fs-h3)}h4{font-size:var(--fs-h4)}
p{margin:0}
a{color:var(--primary-d)}a:hover{color:var(--primary-d)}
button,input,select,textarea{font:inherit;color:inherit}
.ic{width:20px;height:20px;flex:none}
.sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
.container{width:min(var(--content-max),100% - 2*var(--gutter));margin-inline:auto}
.bleed{padding-left:max(var(--gutter),env(safe-area-inset-left));padding-right:max(var(--gutter),env(safe-area-inset-right))}
.ph{display:flex;align-items:center;justify-content:center;background:var(--bg-soft);border:1px dashed var(--input-border);color:var(--text-muted);font-size:var(--fs-caption);text-align:center;padding:8px;border-radius:var(--radius-sm)}
.todo{background:#fff7d6;color:#5c4a00;padding:0 4px;border-radius:2px;font-size:.9em}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;min-height:var(--btn-h-md);padding:0 18px;border-radius:var(--btn-radius);border:1px solid transparent;font-weight:600;cursor:pointer;text-decoration:none;white-space:nowrap;transition:background .2s,border-color .2s,color .2s,transform .15s,box-shadow .2s}
.btn:active:not(:disabled),.chip:active:not(:disabled),.sortBtn:active,.iconBtn:active,.arrowBtn:active:not(:disabled){transform:scale(.96)}
.chip,.sortBtn{transition:background .2s,border-color .2s,color .2s,transform .15s,box-shadow .2s}
.chip:hover:not(:disabled):not(.on){border-color:var(--primary-d);background:var(--primary-10)}
.chip.on,.sortBtn.on,.vBtn.on{animation:stateOn .32s cubic-bezier(.34,1.56,.64,1)}
@keyframes stateOn{0%{transform:scale(.92)}60%{transform:scale(1.04)}100%{transform:scale(1)}}
@media (prefers-reduced-motion:reduce){.btn,.chip,.sortBtn{transition:none}.chip.on,.sortBtn.on,.vBtn.on{animation:none}.btn:active,.chip:active,.sortBtn:active,.iconBtn:active,.arrowBtn:active{transform:none}}
.btn-main{background:var(--main);color:#fff}.btn-main:hover{background:var(--main-d);color:#fff}
.btn-out{background:#fff;border-color:var(--input-border);color:var(--text)}.btn-out:hover{border-color:var(--primary-d);color:var(--text)}
.btn-ghost{background:transparent;color:var(--primary-d);padding:0 8px}
.btn-sm{min-height:var(--btn-h-sm);padding:0 12px;font-size:var(--fs-body-sm)}
.iconBtn{display:inline-flex;align-items:center;justify-content:center;width:44px;height:44px;border:0;background:transparent;border-radius:var(--btn-radius);cursor:pointer;color:var(--text)}
.iconBtn:hover{background:var(--primary-10)}
/* jednotná šipková tlačítka (karusely, slider, menu, galerie, výrobci) */
.arrowBtn{display:inline-flex;align-items:center;justify-content:center;width:44px;height:44px;flex:none;border:1px solid var(--line);border-radius:var(--btn-radius);background:#fff;color:var(--text);cursor:pointer;box-shadow:0 1px 3px rgba(0,0,0,.08);transition:background .15s}
.navArrowIc{display:inline-flex;align-items:center;justify-content:center;width:32px;height:44px;flex:none;border:0;background:none;color:var(--nav-fg);cursor:pointer;transition:transform .15s,opacity .15s}
.navArrowIc .ic{width:24px;height:24px}
.arrowBtn:hover{background:var(--primary-10);color:var(--text)}
.navArrow:hover .navArrowIc{opacity:.8}.navArrow.r:hover .navArrowIc{transform:translateX(2px)}.navArrow.l:hover .navArrowIc{transform:translateX(-2px)}
.navArrow:focus-visible{outline:2px solid #fff;outline-offset:-4px}
.arrowBtn:disabled{opacity:.4;cursor:not-allowed}
.section{margin-top:var(--section-gap)}
.secHead{display:flex;align-items:center;justify-content:space-between;gap:16px;margin-bottom:var(--space-4);flex-wrap:wrap}
.box{border:1px solid var(--line);border-radius:var(--card-radius);background:#fff}
#main{background:var(--bg-soft);padding-bottom:var(--section-gap)}
.subTile,.buyBox,.accItem,.rowsBox,.cmpBox,.infoSide ul,.tabPanel,.params{background:#fff}
.tabPanel{padding:24px!important;border:1px solid var(--line);border-radius:var(--card-radius)}
.tabBar{border-bottom:0!important;gap:8px!important;padding:2px 0 12px;flex-wrap:wrap}
.tabB{min-height:44px!important;padding:0 18px!important;border:1px solid var(--input-border)!important;border-radius:var(--btn-radius);background:#fff!important;color:var(--text)!important;font-weight:600;transition:background .2s,border-color .2s,color .2s,transform .15s}
.tabB:hover{border-color:var(--primary-d)!important;background:var(--primary-10)!important}
.tabB:active{transform:scale(.96)}
.tabB.on{background:var(--primary)!important;border-color:var(--primary)!important;color:#fff!important;box-shadow:none!important;animation:stateOn .32s cubic-bezier(.34,1.56,.64,1)}
.priceMain{font-size:var(--fs-price-md);font-weight:700;color:var(--text)}
.priceSub{font-size:var(--fs-caption);color:var(--text-weaker)}
:focus-visible{outline:2px solid var(--primary-d);outline-offset:2px}
/* toast vpravo nahoře */
.toastWrap{position:fixed;top:16px;right:16px;z-index:4000;display:flex;flex-direction:column;gap:8px;max-width:min(380px,calc(100vw - 32px))}
.toast{display:flex;gap:10px;align-items:flex-start;background:#fff;border:1px solid var(--line);box-shadow:0 8px 24px rgba(0,0,0,.12);border-radius:var(--radius-md);padding:12px 14px;font-size:var(--fs-body-sm);animation:tIn .2s ease}
.toast.err{border-color:#f3c2c2}
.toast ul{margin:6px 0 0;padding-left:18px}
@keyframes tIn{from{opacity:0;transform:translateY(-6px)}to{opacity:1;transform:none}}
/* modaly */
.mdOverlay{position:fixed;inset:0;z-index:3000;background:rgba(9,9,11,.55);display:flex;align-items:center;justify-content:center;padding:16px;animation:fIn .2s ease}
.mdBox{position:relative;max-height:calc(100vh - 32px);overflow:auto;border-radius:var(--radius-lg)}
@keyframes fIn{from{opacity:0}to{opacity:1}}
@media (max-width:600px){.mdOverlay.bottom{align-items:flex-end;padding:0}.mdOverlay.bottom .mdBox{width:100%;border-radius:var(--radius-lg) var(--radius-lg) 0 0}}
/* squircle – karty a tlačítka (progresivní vylepšení) */
@supports (corner-shape:squircle){.arrowBtn,.navArrowIc,.btn,.iconBtn,.hdrBtn,.box,.panel,.uspItem,.subTile,.buyBox,.opt,.tab,.accItem,.ftCard,.dlg,.rowsBox,.cmpBox,.accTable{corner-shape:var(--corner-shape)}}
@media (prefers-reduced-motion:reduce){*,*::before,*::after{animation:none!important;transition:none!important;scroll-behavior:auto!important}}
"""

SHOP_CSS = """
/* ---------- skelet BSSHOP: hlavička ---------- */
.stickyTop{position:sticky;top:0;z-index:1000;background:#fff}
@media (min-width:1000px){.stickyTop{transition:transform .3s cubic-bezier(.4,0,.2,1);will-change:transform}
.stickyTop.navHidden{transform:translateY(calc(-1 * var(--hdr-top-h,85px)))}
.stickyTop .HeaderView{transition:opacity .2s}.stickyTop.navHidden .HeaderView{opacity:0;pointer-events:none}}
@media (prefers-reduced-motion:reduce){.stickyTop,.stickyTop .HeaderView{transition:none}}
.HeaderView{border-bottom:1px solid var(--line);background:#fff}
.hdrRow{display:flex;align-items:center;gap:20px;min-height:84px}
.LogoView{display:flex;align-items:center;gap:8px;text-decoration:none;color:var(--text);flex:none}
.logoImg{height:56px;width:auto;display:block}
.SimpleSearchView{position:relative;flex:1 1 420px;display:flex;gap:8px;max-width:720px}
.searchBox{flex:1;display:flex;align-items:center;gap:8px;border:1px solid var(--input-border);border-radius:var(--btn-radius);padding:0 4px 0 12px;height:48px;background:#fff}
.searchBtn{flex:none;min-height:0;height:38px;padding:0 18px;border-radius:max(4px,calc(var(--btn-radius) - 4px))}
@media (max-width:479px){.searchBtn{padding:0 12px}}
.searchBox:focus-within{border-color:var(--primary-d)}
.searchBox input{flex:1;border:0;outline:0;min-width:0;background:transparent;height:100%}
/* našeptávač – širší než pole, pozicovaný k řádku hlavičky; na úzkém displeji na celou šířku */
.hdrRow,.mobileSearch{position:relative}

.sug{position:absolute;top:calc(100% + 8px);left:0;width:max(100%,min(1080px,calc(100vw - 280px)));z-index:1200;background:#fff;border:1px solid var(--line);border-radius:var(--card-radius);box-shadow:0 16px 40px rgba(0,0,0,.16);padding:20px;container-type:inline-size;max-height:calc(100vh - var(--header-h) - 16px);overflow:auto;overscroll-behavior:contain}
.sugGrid{display:grid;grid-template-columns:minmax(0,2fr) minmax(220px,1fr);gap:28px}
.sugH{font-size:var(--fs-caption);text-transform:uppercase;letter-spacing:.06em;color:var(--text-muted);margin-bottom:8px}
.sugItem{display:grid;grid-template-columns:56px minmax(0,1fr) auto;grid-template-areas:"img txt buy";gap:6px 14px;align-items:center;padding:10px 0;border-bottom:1px solid var(--line)}
.sugItem>.sugPic{grid-area:img}.sugItem>.sugTxt{grid-area:txt;min-width:0}.sugItem>.sugBuy{grid-area:buy}
.sugTxt a{color:var(--text);text-decoration:none;font-size:var(--fs-body-sm);font-weight:600;line-height:1.35;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.sugTxt a:hover{text-decoration:underline}
.sugPic .ph,.sugImg{width:56px;height:56px;padding:0;font-size:10px;object-fit:contain;display:block}
.sugMeta{font-size:var(--fs-caption);color:var(--text-weaker);margin-top:2px}
.sugBuy{display:flex;align-items:center;gap:12px;justify-content:flex-end;white-space:nowrap}
.sugPrice{font-weight:700;font-size:var(--fs-body);text-align:right;line-height:1.2}.sugPrice small{display:block;font-weight:400;font-size:var(--fs-caption);color:var(--text-weaker)}
.sugAll{display:inline-flex;align-items:center;gap:6px;margin-top:10px;min-height:44px;color:var(--primary-d);font-weight:600;font-size:var(--fs-body-sm)}
.sugCats{display:flex;flex-direction:column}
.sugCat{display:block;padding:8px 0;color:var(--text);text-decoration:none;font-size:var(--fs-body-sm);border-bottom:1px solid var(--line)}
.sugCat:hover{text-decoration:underline}
.sugCat small{display:block;color:var(--text-muted);font-size:var(--fs-caption)}
.sugEmpty{grid-column:1/-1}
@container (max-width:899px){.sugGrid{grid-template-columns:1fr;gap:16px}.sugCats{flex-direction:row;flex-wrap:wrap;gap:8px}.sugCat{border:1px solid var(--line);border-radius:999px;padding:6px 14px}.sugCat small{display:none}}
@container (max-width:479px){.sugItem{grid-template-columns:48px minmax(0,1fr);grid-template-areas:"img txt" "img buy"}.sugPic .ph,.sugImg{width:48px;height:48px}.sugBuy{justify-content:space-between}.sugPrice{text-align:left}}
.sugEmpty ul{margin:8px 0;padding-left:18px;color:var(--text-weaker);font-size:var(--fs-body-sm)}
.ContactsView{display:flex;align-items:center;gap:24px;font-size:var(--fs-body-sm);line-height:1.3;flex:none}
.ctItem{display:flex;align-items:center;gap:10px;color:var(--text);text-decoration:none;min-height:44px;border-radius:var(--btn-radius)}
.ctItem:hover strong{text-decoration:underline}
.ctTxt strong{font-weight:600}
.ctItem .ic{width:24px;height:24px;flex:none;color:var(--primary-d)}
.ctTxt{display:flex;flex-direction:column}
.ctTxt small{font-size:var(--fs-caption);color:var(--text-weaker)}
.ContactsView a{color:var(--text);text-decoration:none;font-weight:600}
.dContact a{color:var(--text)}
.dContact>span{display:flex;align-items:center;gap:10px;line-height:1.3}
.dContact .ic{width:20px;height:20px;flex:none;color:var(--primary-d)}
.popWrap{position:relative;flex:none}
.hdrBtn{display:flex;align-items:center;gap:10px;min-height:44px;padding:4px 10px;border:0;background:transparent;border-radius:var(--btn-radius);cursor:pointer;text-align:left;color:var(--text)}
.hdrBtn:hover{background:var(--primary-10)}
.hdrBtn .ic{width:24px;height:24px}
.hdrBtn small{display:block;font-size:var(--fs-caption);color:var(--text-weaker)}
.mono{display:inline-flex;align-items:center;justify-content:center;width:40px;height:40px;border-radius:50%;background:var(--primary-d);color:#fff;font-weight:700;font-size:14px}
@supports (corner-shape:squircle){.mono{corner-shape:squircle;border-radius:50%}}
.cartIco{position:relative;display:inline-flex}
.cartBadge{position:absolute;top:-6px;right:-8px;min-width:18px;height:18px;padding:0 4px;border-radius:9px;background:var(--primary);color:#fff;font-size:11px;font-weight:700;display:flex;align-items:center;justify-content:center}
.cartBtn.empty .cartBadge{background:var(--text-muted)}
.cartBtn{gap:14px;padding:6px 16px 6px 12px;min-height:52px;border:1px solid var(--input-border);background:#fff;transition:border-color .15s}
.cartBtn:hover{border-color:var(--primary-d);background:#fff}
.cartBtn strong{font-size:calc(var(--fs-price-md) - 2px);color:var(--primary);line-height:1.15}
.cartBtn.empty strong{color:var(--text)}
.popScrim{display:none}
@keyframes sheetIn{from{transform:translateY(100%)}to{transform:none}}@keyframes scrimIn{from{opacity:0}to{opacity:1}}
@media (prefers-reduced-motion:reduce){.pop.popSheet,.popScrim{animation:none}}
.pop{position:absolute;top:calc(100% + 8px);right:0;z-index:1300;box-shadow:0 12px 32px rgba(0,0,0,.16);border-radius:var(--radius-md);background:#fff}
.burger,.mSearchBtn{display:none}
.mobileSearch{display:none}
/* menu kategorií – chipy přes celou šířku, posun šipkou nebo prstem */
.MenuCategoriesRwdView{background:var(--nav-bg);color:var(--nav-fg);position:relative}
.navRow{position:relative}
.catTrack{display:flex;gap:8px;overflow-x:auto;scrollbar-width:none;scroll-behavior:smooth;overscroll-behavior-x:contain;-webkit-overflow-scrolling:touch;
 padding:10px var(--gutter) 10px max(var(--gutter),calc((100% - var(--content-max))/2));scroll-padding-inline:max(var(--gutter),calc((100% - var(--content-max))/2)) var(--gutter)}
.catTrack::-webkit-scrollbar{display:none}
.catItem{flex:none}
.catBtn{display:flex;align-items:center;gap:8px;height:44px;text-decoration:none;padding:0 16px 0 6px;border-radius:var(--chip-radius,8px);border:1px solid rgba(255,255,255,.22);background:rgba(255,255,255,.08);color:var(--nav-fg);cursor:pointer;font-weight:500;font-size:var(--fs-body-sm);white-space:nowrap;transition:background .15s,color .15s}
.catBtn:hover{background:rgba(255,255,255,.18);color:var(--nav-fg)}
.catBtn.on{background:#fff;color:var(--nav-bg);border-color:#fff}
.catThumb{width:32px;height:32px;border-radius:max(3px,calc(var(--chip-radius,8px) - 6px));background:#fff;object-fit:contain;padding:2px;flex:none}

.catThumb.photo{object-fit:cover;padding:0}
.catThumb.sale{display:inline-flex;align-items:center;justify-content:center;background:var(--flag-discount);color:var(--flag-discount-fg);font-weight:800;font-size:15px;padding:0}
@supports (corner-shape:squircle){.catBtn,.catThumb{corner-shape:squircle}.MenuCategoriesRwdView{--chip-radius:20px}}
.navArrow{position:absolute;top:0;bottom:0;z-index:2;width:80px;border:0;padding:0 10px;display:flex;align-items:center;cursor:pointer;background:transparent}
.navArrow.l{left:0;justify-content:flex-start;background:linear-gradient(90deg,var(--nav-bg) 50%,rgba(155,65,75,0))}
.navArrow.r{right:0;justify-content:flex-end;background:linear-gradient(270deg,var(--nav-bg) 50%,rgba(155,65,75,0))}
@media (max-width:819px){.catBtn{height:40px;padding-right:14px}.catThumb{width:28px;height:28px}.navArrow{width:56px}}
.mega{position:absolute;left:0;right:0;top:100%;z-index:1100;background:#fff;color:var(--text);border-bottom:1px solid var(--line);box-shadow:0 16px 32px rgba(0,0,0,.12);border-radius:0 0 12px 12px;overflow:hidden}
@supports (corner-shape:squircle){.mega{border-radius:0 0 40px 40px;corner-shape:squircle}}
.megaIn{padding:20px 0 24px;max-height:calc(100vh - var(--header-h) - 24px);overflow:auto}
.megaHead{display:flex;justify-content:space-between;align-items:center;gap:16px;margin-bottom:16px}
.megaAll{flex:none;gap:6px;padding-right:14px}.megaAll .ic{width:18px;height:18px}
.megaHead h3{font-size:var(--fs-h4)}.megaHead small{font-weight:400;color:var(--text-muted);font-size:var(--fs-body-sm)}
.megaGrid{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:16px 24px}
.megaL2{display:flex;align-items:center;gap:10px;color:var(--text);text-decoration:none;font-weight:600;font-size:var(--fs-body);padding:4px;border-radius:var(--radius-sm)}
.megaL2:hover{background:var(--primary-10);color:var(--text)}
.megaL2 img,.megaL2 .ph{width:44px;height:44px;object-fit:contain;flex:none;padding:0;font-size:9px;background:#fff}
.megaL2 small{font-weight:400;color:var(--text-muted)}
.megaCol ul{list-style:none;margin:4px 0 0 58px;padding:0}
.megaCol li a{display:block;padding:5px 0;color:var(--text-weaker);text-decoration:none;font-size:var(--fs-body-sm);line-height:1.35}
.megaCol li a:hover{color:var(--text);text-decoration:underline}.megaCol li a.more{color:var(--text-muted)}
@media (max-width:1149px){.megaGrid{grid-template-columns:repeat(3,minmax(0,1fr))}}
/* drawer */
.navOverlay{position:fixed;inset:0;z-index:2500;background:rgba(9,9,11,.5);display:flex;justify-content:flex-end;animation:scrimIn .2s ease}
.drawer{width:min(360px,88vw);height:100%;background:#fff;overflow:auto;display:flex;flex-direction:column;border-radius:var(--card-radius) 0 0 var(--card-radius);box-shadow:-12px 0 40px rgba(0,0,0,.2);animation:drawerIn .24s ease-out}
@keyframes drawerIn{from{transform:translateX(100%)}to{transform:none}}
@media (prefers-reduced-motion:reduce){.drawer,.navOverlay{animation:none}}
.drawerHead{display:flex;align-items:center;justify-content:space-between;padding:12px 8px 12px 16px;border-bottom:1px solid var(--line)}
.drawerT{margin:0;font-size:var(--fs-h2);font-weight:800;line-height:1.2;letter-spacing:-.01em;color:var(--text)}
.drawer ul{list-style:none;margin:0;padding:0}
.dRow{display:flex;align-items:center;border-bottom:1px solid var(--line)}
.dRow a{flex:1;padding:12px 16px;color:var(--text);text-decoration:none;font-weight:500;min-height:44px}
.dSub a{padding-left:32px;font-weight:400;font-size:var(--fs-body)}
.dLinks{padding:8px 0}
.dLinks a{display:flex;align-items:center;gap:12px;min-height:44px;padding:0 16px;color:var(--text);text-decoration:none}
.dLinks .ic{width:20px;height:20px;flex:none;opacity:.8}
.dContact{padding:16px;background:var(--bg-soft);font-size:var(--fs-body-sm);display:flex;flex-direction:column;gap:6px;margin-top:auto}
/* dialog po přidání do košíku */
.dlg{width:min(680px,100%);background:#fff;padding:24px;border-radius:var(--card-radius)}
.dlgHead{display:flex;align-items:center;justify-content:space-between;gap:12px;margin-bottom:16px}
.dlgHead h2{font-size:var(--fs-h3);display:flex;gap:8px;align-items:center}
.dlgProd{display:grid;grid-template-columns:80px minmax(0,1fr) auto;gap:16px;align-items:center;padding:16px 0;border-block:1px solid var(--line)}
.dlgProd .ph,.dlgImg{width:80px;height:80px;object-fit:contain}
.dlgSum{padding:12px 0;font-size:var(--fs-body-sm)}
.dlgShades{border-bottom:1px solid var(--line);padding:12px 0}
.dlgShH{font-size:var(--fs-caption);color:var(--text-muted);margin-bottom:6px}
.dlgShades ul{list-style:none;margin:0;padding:0;max-height:220px;overflow:auto;display:flex;flex-direction:column;gap:4px}
.dlgShades li{display:grid;grid-template-columns:22px minmax(0,1fr) auto auto;gap:10px;align-items:center;font-size:var(--fs-body-sm);padding:4px 0}
.dlgDot{width:22px;height:22px;border-radius:7px;border:1px solid rgba(0,0,0,.15)}
.dlgShN{overflow:hidden;text-overflow:ellipsis;white-space:nowrap}.dlgShQ{color:var(--text-weaker)}.dlgShP{font-weight:600;min-width:80px;text-align:right}
.dlgAct{display:flex;gap:12px;justify-content:space-between;flex-wrap:wrap;margin-top:8px}
.freeBox{border:1px solid var(--line);border-radius:var(--radius-md);padding:12px;font-size:var(--fs-body-sm);display:flex;flex-direction:column;gap:8px}
.freeBox>span{display:flex;align-items:flex-start;gap:8px;line-height:1.4;text-wrap:pretty}.freeBox>span .ic{margin-top:1px}.freeBox>span .ic{width:20px;height:20px;flex:none}
.freeBox progress{width:100%;height:6px;appearance:none;border:0;border-radius:3px;background:var(--line);overflow:hidden}
.freeBox progress::-webkit-progress-bar{background:var(--line)}
.freeBox progress::-webkit-progress-value{background:var(--primary)}
.freeBox progress::-moz-progress-bar{background:var(--primary)}
/* nákupní asistent */
.assistFab{position:fixed;right:20px;bottom:20px;z-index:2000;width:56px;height:56px;border-radius:50%;border:0;background:var(--main);color:#fff;cursor:pointer;box-shadow:0 8px 24px rgba(0,0,0,.2);display:flex;align-items:center;justify-content:center}
.assistFab .ic{width:26px;height:26px}
.assistPanel{position:fixed;right:20px;bottom:88px;z-index:2000;width:min(360px,calc(100vw - 40px));background:#fff;border:1px solid var(--line);border-radius:var(--radius-lg);box-shadow:0 16px 40px rgba(0,0,0,.18);display:flex;flex-direction:column;overflow:hidden}
.assistHead{display:flex;align-items:center;justify-content:space-between;padding:8px 8px 8px 16px;background:var(--primary-10)}
.assistBody{padding:16px;display:flex;flex-direction:column;gap:10px;font-size:var(--fs-body-sm);max-height:320px;overflow:auto}
.bubble{padding:10px 12px;border-radius:12px;max-width:85%}
.bubble.me{align-self:flex-end;background:var(--primary-d);color:#fff}
.bubble.bot{background:var(--bg-soft)}
.assistForm{display:flex;gap:8px;padding:12px;border-top:1px solid var(--line)}
.assistForm input{flex:1;min-width:0;border:1px solid var(--input-border);border-radius:var(--btn-radius);padding:0 10px;height:44px}
/* hlavní obsah */
main{display:block;padding-bottom:var(--section-gap)}
.pageHead{margin-top:var(--space-4);display:flex;flex-direction:column;gap:var(--space-3)}
@media (max-width:1349px){.ctItem+.ctItem{display:none}}
@media (max-width:1149px){.ContactsView{gap:8px}}
.ctIcon{display:none;align-items:center;justify-content:center;width:44px;height:44px;border-radius:var(--btn-radius);color:var(--primary-d);transition:background .2s}
.ctIcon:hover{background:var(--primary-10)}.ctIcon .ic{width:24px;height:24px}
@media (max-width:999px){.ContactsView .ctItem{display:none}.ctIcon{display:inline-flex}}
@media (max-width:819px){.ctIcon{width:40px;height:40px}.ctIcon .ic{width:22px;height:22px}}
@media (max-width:339px){.ContactsView{display:none}}
@media (max-width:999px){.MenuCategoriesRwdView{display:none}.burger{display:inline-flex}}
.SimpleSearchView{min-width:0}
.HeaderView.bleed{padding-left:env(safe-area-inset-left);padding-right:env(safe-area-inset-right)}
.HeaderView .container{width:min(var(--content-max),100% - 2*var(--gutter))}
@media (max-width:1399px){.hdrRow{gap:12px}.hdrBtn:not(.cartBtn) .hdrTxt{display:none}.SimpleSearchView{flex-basis:280px}}
@media (max-width:1199px){.cartBtn .hdrTxt small{display:none}.cartBtn{gap:10px;padding:6px 12px 6px 10px}}
@media (max-width:819px){
  .hdrRow{min-height:64px;gap:4px}
  .cartBtn{padding:4px 10px;min-height:44px;gap:0}
  .HeaderView.bleed{padding-left:env(safe-area-inset-left);padding-right:env(safe-area-inset-right)}
  .burger{margin-right:0}
  .MenuCategoriesRwdView{display:none}
  .logoImg{height:40px}
  .LogoView{margin-right:auto}
  .hdrRow>.SimpleSearchView{display:none}
  .burger,.mSearchBtn{display:inline-flex}
  .hdrBtn .hdrTxt{display:none}
  .hdrBtn{padding:4px 8px}
  .mobileSearch{display:block;padding-bottom:10px}
  .mobileSearch .SimpleSearchView{max-width:none}
  .pop{position:fixed;top:72px;left:12px;right:12px}
  .pop>*{width:100%}
  .pop.popSheet{top:auto;left:0;right:0;bottom:0;z-index:2600;border-radius:var(--card-radius) var(--card-radius) 0 0;box-shadow:0 -12px 40px rgba(0,0,0,.2);max-height:85dvh;overflow:auto;animation:sheetIn .22s ease-out}
  .popScrim{display:block;position:fixed;inset:0;z-index:2550;background:rgba(9,9,11,.5);animation:scrimIn .2s ease}
  .sug{width:100%;padding:14px;top:calc(100% + 4px)}
  .mobileSearch .sug{position:fixed;top:calc(var(--sugTop,120px) + 10px);left:0;right:0;bottom:0;width:auto;max-height:none;border:0;border-top:1px solid var(--line);border-radius:0;box-shadow:none;padding:16px var(--gutter);corner-shape:round}
}
.nlSec{background:var(--bg-soft);padding:var(--section-gap) 0 calc(var(--section-gap) * .75)}
.nlBox{display:grid;grid-template-columns:auto minmax(0,1fr) minmax(0,1.1fr);gap:20px 32px;align-items:center;background:var(--primary);color:#fff;border-radius:40px;padding:32px 40px;position:relative;overflow:hidden}
.nlIco{width:72px;height:72px;border-radius:24px;background:rgba(255,255,255,.14);display:flex;align-items:center;justify-content:center}
.nlIco .ic{width:36px;height:36px}
.nlTxt h2{margin:0 0 6px;font-size:var(--fs-h3);color:#fff}
.nlTxt p{margin:0;color:rgba(255,255,255,.85);font-size:var(--fs-body-sm);max-width:52ch}
.nlForm{display:flex;flex-direction:column;gap:10px;position:relative;z-index:1}
.nlRow{display:flex;gap:8px}
.nlField{flex:1;min-width:0;display:flex;align-items:center;gap:8px;height:52px;padding:0 14px;background:#fff;border:2px solid transparent;border-radius:var(--btn-radius);color:var(--text-weaker);transition:border-color .2s}
.nlField:focus-within{border-color:#fff;box-shadow:0 0 0 3px rgba(255,255,255,.35)}
.nlField input{flex:1;min-width:0;border:0;outline:0;background:transparent;height:100%;color:var(--text);font:inherit}
.nlField input[aria-invalid=true]{color:var(--primary-d)}
.nlBtn{height:52px;min-height:52px;background:var(--cta,#27272a);color:#fff;border:0;padding:0 22px;gap:8px;white-space:nowrap}
.nlBtn:hover{background:#000}
.nlBtn .ic{width:18px;height:18px}
.nlChk{display:flex;align-items:flex-start;gap:10px;font-size:var(--fs-body-sm);color:rgba(255,255,255,.9);cursor:pointer}
.nlChk input{width:20px;height:20px;margin:2px 0 0;accent-color:#fff;flex:none}
.nlChk a{color:#fff;text-decoration:underline}
.nlErr{margin:0;font-size:var(--fs-body-sm);font-weight:600;background:#fff;color:var(--primary-d);padding:6px 12px;border-radius:10px;align-self:flex-start}
.nlDone{display:flex;gap:14px;align-items:center;background:rgba(255,255,255,.12);border-radius:20px;padding:16px 20px;position:relative;z-index:1}
.nlDone .ic{width:32px;height:32px;flex:none}.nlDone strong{display:block}.nlDone span{font-size:var(--fs-body-sm);color:rgba(255,255,255,.85)}
@supports (corner-shape:squircle){.nlBox,.nlIco,.nlDone,.nlErr{corner-shape:squircle}}
@media (max-width:1149px){.nlBox{grid-template-columns:auto minmax(0,1fr)}.nlAct{grid-column:1/-1}}
@media (max-width:599px){.nlBox{grid-template-columns:1fr;padding:24px 20px;border-radius:28px;gap:16px}.nlIco{width:56px;height:56px;border-radius:18px}.nlRow{flex-direction:column}.nlBtn{width:100%;justify-content:center}}
"""

# ---------- data (ze screenshotů současného webu Daver) ----------
DATA_JS_T = r"""
const P='daver';
const lsGet=(k)=>{try{return localStorage.getItem(P+k)}catch(e){return null}};
const lsSet=(k,v)=>{try{localStorage.setItem(P+k,v)}catch(e){}};
const CZK=(n)=>n.toLocaleString('cs-CZ',{minimumFractionDigits:2,maximumFractionDigits:2})+' Kč';
const VAT=1.21;
const FREE_FROM=1000; /* doprava zdarma od 1 000 Kč bez DPH */
const USER={name:'Jan Novák',ini:'JN',group:'Velkoobchod'};
const DATA=__DATA__;
const CATS=DATA.cats, PRODUCTS=DATA.products, IDS=DATA.ids, CAR=DATA.car;
const avText=(s)=>s===0?'Na objednávku':(s>5?('Skladem > '+(s>=100?Math.floor(s/50)*50:s)+' ks'):('Skladem '+s+' ks'));
const card=(p)=>Object.assign({},p,{unit:'ks',av:p.avRaw||avText(p.stock),blue:p.stock===0,max:p.stock,href:p.href||'Detail.dc.html'});
const byId=(id)=>PRODUCTS.find((p)=>p.id===id);
"""

DATA_JS = DATA_JS_T.replace("__DATA__", open(os.path.join(os.path.dirname(__file__), "data.json"), encoding="utf-8").read())

# ---------- logika hlavičky (sdílená všemi obchodními stránkami) ----------
SHOP_JS = r"""
class Component extends DCLogic {
 constructor(props){
  super(props);
  this.state=Object.assign({auth:false,pop:'',q:'',nlE:'',nlC:false,nlOk:false,nlErr:'',sugOpen:false,sugTop:0,drawer:false,mega:-1,openCat:-1,
   cart:[{id:IDS.detail,qty:4},{id:IDS.cistic,qty:2}],navL:false,navR:true,quick:null,dlg:null,toast:'',toastErr:false,assist:false}, this.pageState?this.pageState():{});
  this.onAuth=()=>this.setState({auth:lsGet('AuthV1')==='in'});
  this.onDoc=(e)=>{const t=e.target; const c=(s)=>t&&t.closest&&t.closest(s);
   if(this.state.pop&&!c('.popWrap'))this.setState({pop:''});
   if(this.state.sugOpen&&!c('.SimpleSearchView'))this.setState({sugOpen:false});};
 }
 componentDidMount(){
  this.onAuth();
  window.addEventListener('daver-auth',this.onAuth); window.addEventListener('storage',this.onAuth);
  document.addEventListener('mousedown',this.onDoc);
  const h=document.querySelector('.stickyTop');
  if(h&&window.ResizeObserver){this.ro=new ResizeObserver(()=>{document.documentElement.style.setProperty('--header-h',h.offsetHeight+'px');this.navUpd();});this.ro.observe(h);}
  this.navUpd();
  this.phStart();
  this.lastY=window.scrollY||0; this.dirAcc=0;
  const hv=document.querySelector('.stickyTop .HeaderView');
  if(hv&&window.ResizeObserver){this.ro2=new ResizeObserver(()=>document.documentElement.style.setProperty('--hdr-top-h',hv.offsetHeight+'px'));this.ro2.observe(hv);}
  this.onScrollNav=()=>{const y=Math.max(0,window.scrollY||0),d=y-this.lastY;this.lastY=y;if(!d)return;
   const h=document.querySelector('.stickyTop');if(!h)return;
   /* hystereze: směr musí trvat aspoň 24 px, jinak se při zastavení scrollu stav nepřepíná */
   this.dirAcc=(Math.sign(d)===Math.sign(this.dirAcc))?this.dirAcc+d:d;
   const hidden=h.classList.contains('navHidden');
   if(y<=120){if(hidden)h.classList.remove('navHidden');return;}
   if(!hidden&&this.dirAcc>24&&window.innerWidth>=1000&&!this.state.sugOpen&&!this.state.pop)h.classList.add('navHidden');
   else if(hidden&&this.dirAcc<-24)h.classList.remove('navHidden');};
  window.addEventListener('scroll',this.onScrollNav,{passive:true});
  if(this.pageMount)this.pageMount();
 }
 phStart(){
  if(window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches)return;
  const P=['Hledám štětec na malování…','Hledám akrylové barvy Amsterdam…','Hledám skicák A4…','Hledám plátno na rámu 40 × 50…','Hledám modelovací hmotu…'];
  let i=0,c=0,dir=1,wait=0;
  this.phT=setInterval(()=>{
   if(wait>0){wait--;return;}
   const t=P[i];c+=dir;
   if(c>=t.length){dir=-1;wait=28;}
   else if(c<=0){dir=1;i=(i+1)%P.length;wait=6;}
   const txt=t.slice(0,Math.max(0,c));
   document.querySelectorAll('.searchBox input[type=search]').forEach((el)=>{if(document.activeElement!==el)el.setAttribute('placeholder',txt||' ');});
  },60);
 }
 componentWillUnmount(){
  window.removeEventListener('daver-auth',this.onAuth); window.removeEventListener('storage',this.onAuth);
  document.removeEventListener('mousedown',this.onDoc); if(this.ro)this.ro.disconnect(); clearTimeout(this.tt); clearInterval(this.phT); window.removeEventListener('scroll',this.onScrollNav); if(this.ro2)this.ro2.disconnect();
  if(this.pageUnmount)this.pageUnmount();
 }
 navUpd(){const t=document.querySelector('.catTrack');if(!t)return;const l=t.scrollLeft>4,r=t.scrollLeft+t.clientWidth<t.scrollWidth-4;if(l!==this.state.navL||r!==this.state.navR)this.setState({navL:l,navR:r});}
 setAuth(v){lsSet('AuthV1',v?'in':'out');window.dispatchEvent(new Event('daver-auth'));this.setState({auth:v});}
 toastMsg(t,err){this.setState({toast:t,toastErr:!!err});clearTimeout(this.tt);this.tt=setTimeout(()=>this.setState({toast:''}),2800);}
 addToCart(p,qty){
  qty=Math.max(1,qty||1);
  const cart=this.state.cart.slice(); const i=cart.findIndex((l)=>l.id===p.id);
  if(i>=0)cart[i]={id:p.id,qty:cart[i].qty+qty}; else cart.push({id:p.id,qty:qty});
  this.setState({cart:cart,dlg:{id:p.id,qty:qty},pop:''});
 }
 esc(fn){return (e)=>{if(e.key==='Escape'){e.stopPropagation();fn();}};}
 sugTopOf(e){const f=e&&e.target&&e.target.closest?e.target.closest('form'):null;return f?Math.round(f.getBoundingClientRect().bottom):0;}
 headerVals(){
  const s=this.state;
  const lines=s.cart.map((l)=>{const p=byId(l.id);return {name:p.name,code:p.code,qty:l.qty,unit:'ks',price:p.price,img:p.img||''};});
  const total=lines.reduce((a,l)=>a+l.price*l.qty,0);
  const count=lines.reduce((a,l)=>a+l.qty,0);
  const q=s.q.trim().toLowerCase();
  const found=q.length>=2?PRODUCTS.filter((p)=>(p.name+' '+p.code+' '+p.brand).toLowerCase().includes(q)):[];
  const cats=[];if(q.length>=2)CATS.forEach((c)=>{if(c.n.toLowerCase().includes(q))cats.push({n:c.n,path:'Kategorie 1. úrovně'});c.subs.forEach((x)=>{if(x.n.toLowerCase().includes(q))cats.push({n:x.n,path:c.n});});});
  const dl=s.dlg?byId(s.dlg.id):null;
  const close=()=>this.setState({pop:''});
  const megaCat=s.mega>=0?CATS[s.mega]:null;
  const nav=CATS.map((c,i)=>({n:c.n,img:c.img||'',thumbCls:'catThumb'+(c.photo?' photo':''),hasImg:!!c.img,noImg:!c.img,aria:c.n,mark:c.sale?'%':'',saleCls:'catThumb'+(c.sale?' sale':''),cls:'catBtn'+(s.mega===i?' on':'')+(c.n===this.curCat?' on':''),
    enter:()=>this.setState({mega:i}), toggle:()=>this.setState({mega:s.mega===i?-1:i}),
    exp:s.mega===i?'true':'false'}));
  const drawerCats=CATS.map((c,i)=>({n:c.n,hasSubs:c.subs.length>0,open:s.openCat===i,exp:s.openCat===i?'true':'false',
    label:(s.openCat===i?'Sbalit ':'Rozbalit ')+c.n, subs:c.subs.map((x)=>({n:x.n})),
    toggle:()=>this.setState({openCat:s.openCat===i?-1:i})}));
  return {
   auth:s.auth, notAuth:!s.auth, userName:USER.name, userIni:USER.ini, userGroup:USER.group,
   accExp:(s.pop==='login'||s.pop==='user')?'true':'false', cartExp:s.pop==='cart'?'true':'false',
   popLogin:s.pop==='login', popUser:s.pop==='user', popCart:s.pop==='cart',
   togglePop:()=>this.setState({pop:(s.pop==='login'||s.pop==='user')?'':(s.auth?'user':'login')}),
   toggleCart:()=>this.setState({pop:s.pop==='cart'?'':'cart'}),
   closePop:close, popKey:this.esc(close),
   doLogin:()=>this.setAuth(true), doLogout:()=>{this.setAuth(false);this.setState({pop:''});this.toastMsg('Byli jste odhlášeni.');},
   cartLines:lines, cartCount:count, cartTotal:CZK(total), cartTotalVat:CZK(total*VAT), cartCls:'hdrBtn cartBtn'+(count?'':' empty'),
   cartItemsTxt:lines.length+(lines.length===1?' položka':lines.length<5&&lines.length>0?' položky':' položek'),
   nlOk:s.nlOk, nlForm:!s.nlOk, nlEmail:s.nlE, nlConsent:s.nlC, nlHasErr:!!s.nlErr, nlErrTxt:s.nlErr, nlInvalid:s.nlErr&&s.nlErr.indexOf('e-mail')>=0?'true':'false',
   nlOnEmail:(e)=>this.setState({nlE:e.target.value,nlErr:''}), nlOnConsent:(e)=>this.setState({nlC:e.target.checked,nlErr:''}),
   nlSubmit:(e)=>{e.preventDefault();const v=s.nlE.trim();if(!/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v)){this.setState({nlErr:'Zadejte platný e-mail, např. jmeno@firma.cz.'});const i=document.getElementById('nlE');if(i)i.focus();return;}if(!s.nlC){this.setState({nlErr:'Pro přihlášení odběru potvrďte souhlas se zpracováním údajů.'});return;}this.setState({nlOk:true,nlE:v,nlErr:''});},
   q:s.q, onQ:(e)=>this.setState({q:e.target.value,sugOpen:true,sugTop:this.sugTopOf(e)}), onQFocus:(e)=>this.setState({sugOpen:true,sugTop:this.sugTopOf(e)}), sugStyle:'--sugTop:'+(s.sugTop||120)+'px',
   qKey:this.esc(()=>this.setState({sugOpen:false})), onSearch:(e)=>{e.preventDefault();},
   sugOpen:s.sugOpen&&q.length>=2, sugHas:found.length>0||cats.length>0, sugNone:found.length===0&&cats.length===0,
   sugProducts:found.slice(0,4).map((p)=>({name:p.name,href:p.href||'Detail.dc.html',img:p.img||'',hasImg:!!p.img,noImg:!p.img,meta:'Kód '+p.code+' · '+(p.avRaw||avText(p.stock)),price:(p.from?'od ':'')+CZK(p.price),
     add:()=>{this.addToCart(p,1);this.setState({sugOpen:false});}})),
   sugCats:cats.slice(0,6), sugCount:found.length, sugAllTxt:'Zobrazit všechny produkty ('+found.length+')', sugQ:s.q.trim(),
   nav:nav, megaOpen:!!megaCat, megaName:megaCat?megaCat.n:'', megaCount:megaCat?megaCat.c+' produktů':'', megaSubs:megaCat?megaCat.subs.map((x)=>({n:x.n,c:x.c,img:x.img||'',hasImg:!!x.img,noImg:!x.img,kids:(x.subs||[]).slice(0,4).map((k)=>({n:k.n})),more:(x.subs||[]).length>4,moreTxt:'+ další '+((x.subs||[]).length-4)})):[],
   megaEmpty:!!megaCat&&megaCat.subs.length===0,
   leaveNav:()=>this.setState({mega:-1}), navKey:this.esc(()=>this.setState({mega:-1})),
   navL:s.navL, navR:s.navR, navScroll:()=>this.navUpd(),
   navPrev:()=>{const t=document.querySelector('.catTrack');if(t)t.scrollBy({left:-t.clientWidth*0.7});},
   navNext:()=>{const t=document.querySelector('.catTrack');if(t)t.scrollBy({left:t.clientWidth*0.7});},
   drawer:s.drawer, openDrawer:()=>this.setState({drawer:true}), closeDrawer:()=>this.setState({drawer:false}),
   drawerKey:this.esc(()=>this.setState({drawer:false})), drawerCats:drawerCats,
   overlayClick:(e)=>{if(e.target===e.currentTarget)this.setState({drawer:false,dlg:null});},
   dlgOpen:!!dl, dlgName:dl?dl.name:'', dlgImg:dl&&dl.img?dl.img:'', dlgHasImg:!!(dl&&dl.img), dlgNoImg:!(dl&&dl.img), dlgCode:dl?dl.code:'', dlgAv:dl?avText(dl.stock):'',
   dlgQty:s.dlg?s.dlg.qty+' ks':'', dlgPrice:dl?CZK(s.dlg.shades?s.dlg.shades.reduce((a,x)=>a+x.price*x.q,0):dl.price*s.dlg.qty):'', dlgHasShades:!!(s.dlg&&s.dlg.shades), dlgShades:(s.dlg&&s.dlg.shades||[]).map((x)=>({no:x.no,n:x.n,hex:x.hex,q:x.q+' ks',sum:CZK(x.price*x.q)})), dlgShadeTitle:s.dlg&&s.dlg.shades?(s.dlg.shades.length+(s.dlg.shades.length===1?' odstín':(s.dlg.shades.length<5?' odstíny':' odstínů'))):'',
   dlgSum:'V košíku máte '+count+' ks celkem za '+CZK(total)+' bez DPH',
   closeDlg:()=>this.setState({dlg:null}), dlgKey:this.esc(()=>this.setState({dlg:null})),
   freeMsg:total>=FREE_FROM?'Máte dopravu zdarma.':'Do dopravy zdarma zbývá '+CZK(FREE_FROM-total)+' (zdarma od 1 000 Kč bez DPH)',
   freePct:FREE_FROM?Math.min(100,Math.round(total/FREE_FROM*100)):0,
   addCart:(p,qty)=>this.addToCart(p,qty),
   openQuick:(p)=>this.setState({quick:p.id,pop:''}), quickOpen:!!s.quick, quickP:s.quick?card(byId(s.quick)):null,
   closeQuick:()=>this.setState({quick:null}), quickAdd:(p,qty)=>{this.setState({quick:null});this.addToCart(p,qty);},
   quickOverlay:(e)=>{if(e.target===e.currentTarget)this.setState({quick:null});},
   assist:s.assist, toggleAssist:()=>this.setState({assist:!s.assist}), assistKey:this.esc(()=>this.setState({assist:false})),
   assistSubmit:(e)=>{e.preventDefault();},
   toast:s.toast, toastCls:'toast'+(s.toastErr?' err':''), hasToast:!!s.toast,
   pickup:'zítra', delivery:'pozítří'
  };
 }
 renderVals(){return Object.assign(this.headerVals(), this.pageVals?this.pageVals():{});}
"""

def search_html(idp):
    return f'''<form class="SimpleSearchView" role="search" onSubmit="{{{{ onSearch }}}}" onKeyDown="{{{{ qKey }}}}">
<label class="sr" for="{idp}">Hledat v e-shopu</label>
<div class="searchBox">{I('magnifying-glass')}<input id="{idp}" type="search" autocomplete="off" placeholder="Hledejte název, kód nebo výrobce" value="{{{{ q }}}}" onChange="{{{{ onQ }}}}" onFocus="{{{{ onQFocus }}}}"><button class="btn btn-main searchBtn" type="submit">Hledat</button></div>
<sc-if value="{{{{ sugOpen }}}}" hint-placeholder-val="{{{{ false }}}}">
<div class="sug" role="region" aria-label="Návrhy vyhledávání" style="{{{{ sugStyle }}}}">
<sc-if value="{{{{ sugHas }}}}" hint-placeholder-val="{{{{ true }}}}">
<div class="sugGrid">
<div>
<div class="sugH">Produkty</div>
<sc-for list="{{{{ sugProducts }}}}" as="s" hint-placeholder-count="3">
<div class="sugItem"><div class="sugPic"><sc-if value="{{{{ s.hasImg }}}}" hint-placeholder-val="{{{{ true }}}}"><img class="sugImg" src="{{{{ s.img }}}}" alt="" loading="lazy"></sc-if><sc-if value="{{{{ s.noImg }}}}" hint-placeholder-val="{{{{ false }}}}"><div class="ph">[FOTO]</div></sc-if></div><div class="sugTxt"><a href="{{{{ s.href }}}}">{{{{ s.name }}}}</a><div class="sugMeta">{{{{ s.meta }}}}</div></div><div class="sugBuy"><div class="sugPrice">{{{{ s.price }}}}<small>bez DPH</small></div><button class="btn btn-main btn-sm" type="button" onClick="{{{{ s.add }}}}">Koupit</button></div></div>
</sc-for>
<a class="sugAll" href="Kategorie.dc.html">{{{{ sugAllTxt }}}}{I('arrow-right')}</a>
</div>
<div>
<div class="sugH">Kategorie</div>
<div class="sugCats"><sc-for list="{{{{ sugCats }}}}" as="c" hint-placeholder-count="2"><a class="sugCat" href="Kategorie.dc.html">{{{{ c.n }}}}<small>{{{{ c.path }}}}</small></a></sc-for></div>
</div>
</div>
</sc-if>
<sc-if value="{{{{ sugNone }}}}" hint-placeholder-val="{{{{ false }}}}">
<div class="sugEmpty"><strong>Pro „{{{{ sugQ }}}}“ jsme nic nenašli.</strong>
<ul><li>Zkuste kód produktu (např. 14235)</li><li>Zkuste výrobce (Jovi, Meyco, Darwi…)</li><li>Zadejte jen část názvu</li></ul>
<span>Poradíme po telefonu: <a href="tel:+420775570418">+420 775 570 418</a></span></div>
</sc-if>
</div>
</sc-if>
</form>'''

HEADER_HTML = f'''<div class="stickyTop dcHeader">
<header class="HeaderView bleed">
<div class="container hdrRow">
<a class="LogoView" href="Main.dc.html" aria-label="Daver – úvodní stránka"><img class="logoImg" src="/_blob/31e51e752116e4c4eaf02fb3d12e760d" alt="" width="167" height="70"></a>
{search_html('q1')}
<div class="ContactsView"><a class="ctItem" href="tel:+420775570418" aria-label="Zavolat +420 775 570 418, Po–Pá 9:00–16:00">{I('phone')}<span class="ctTxt"><strong>+420 775 570 418</strong><small>Po–Pá 9:00–16:00</small></span></a><a class="ctItem" href="mailto:daver@daver.cz" aria-label="Napsat e-mail daver@daver.cz">{I('envelope')}<span class="ctTxt"><strong>daver@daver.cz</strong></span></a><a class="ctIcon" href="Kontakt.dc.html" aria-label="Kontakty" title="Kontakty">{I('phone')}</a></div>
<div class="popWrap LoginUserView" onKeyDown="{{{{ popKey }}}}">
<sc-if value="{{{{ notAuth }}}}" hint-placeholder-val="{{{{ true }}}}">
<button class="hdrBtn" type="button" aria-expanded="{{{{ accExp }}}}" aria-label="Přihlášení" onClick="{{{{ togglePop }}}}">{I('user')}<span class="hdrTxt"><strong>Přihlášení</strong><small>B2B účet</small></span></button>
</sc-if>
<sc-if value="{{{{ auth }}}}" hint-placeholder-val="{{{{ false }}}}">
<button class="hdrBtn" type="button" aria-expanded="{{{{ accExp }}}}" aria-label="Můj účet" onClick="{{{{ togglePop }}}}"><span class="mono">{{{{ userIni }}}}</span><span class="hdrTxt"><strong>{{{{ userName }}}}</strong><small>{{{{ userGroup }}}}</small></span></button>
</sc-if>
<sc-if value="{{{{ popLogin }}}}" hint-placeholder-val="{{{{ false }}}}"><div class="pop"><dc-import name="LoginPopup" on-close="{{{{ closePop }}}}" on-login="{{{{ doLogin }}}}" hint-size="320px,420px"></dc-import></div></sc-if>
<sc-if value="{{{{ popUser }}}}" hint-placeholder-val="{{{{ false }}}}"><div class="popScrim" onClick="{{{{ closePop }}}}" aria-hidden="true"></div><div class="pop popSheet"><dc-import name="UserMenu" user-name="{{{{ userName }}}}" group="{{{{ userGroup }}}}" on-close="{{{{ closePop }}}}" on-logout="{{{{ doLogout }}}}" hint-size="320px,420px"></dc-import></div></sc-if>
</div>
<div class="popWrap SimpleBasketView" onKeyDown="{{{{ popKey }}}}">
<button class="{{{{ cartCls }}}}" type="button" aria-expanded="{{{{ cartExp }}}}" aria-label="Nákupní košík" onClick="{{{{ toggleCart }}}}"><span class="cartIco">{I('shopping-cart')}<span class="cartBadge">{{{{ cartCount }}}}</span></span><span class="hdrTxt"><strong>{{{{ cartTotal }}}}</strong><small>bez DPH</small></span></button>
<sc-if value="{{{{ popCart }}}}" hint-placeholder-val="{{{{ false }}}}"><div class="pop"><dc-import name="CartPopup" lines="{{{{ cartLines }}}}" on-close="{{{{ closePop }}}}" hint-size="360px,440px"></dc-import></div></sc-if>
</div>
<button class="iconBtn burger" type="button" aria-label="Otevřít menu" aria-expanded="{{{{ drawer }}}}" onClick="{{{{ openDrawer }}}}">{I('list')}</button>
</div>
<div class="container mobileSearch">{search_html('q2')}</div>
</header>
<nav class="MenuCategoriesRwdView" aria-label="Kategorie" onMouseLeave="{{{{ leaveNav }}}}" onKeyDown="{{{{ navKey }}}}">
<div class="navRow">
<sc-if value="{{{{ navL }}}}" hint-placeholder-val="{{{{ false }}}}"><button class="navArrow l" type="button" aria-label="Předchozí kategorie" onClick="{{{{ navPrev }}}}"><span class="navArrowIc">{I('caret-left')}</span></button></sc-if>
<div class="catTrack" onScroll="{{{{ navScroll }}}}">
<sc-for list="{{{{ nav }}}}" as="c" hint-placeholder-count="11">
<div class="catItem"><a class="{{{{ c.cls }}}}" href="Kategorie.dc.html" onMouseEnter="{{{{ c.enter }}}}" onFocus="{{{{ c.enter }}}}" aria-label="{{{{ c.aria }}}}"><sc-if value="{{{{ c.hasImg }}}}" hint-placeholder-val="{{{{ true }}}}"><img class="{{{{ c.thumbCls }}}}" src="{{{{ c.img }}}}" alt=""></sc-if><sc-if value="{{{{ c.noImg }}}}" hint-placeholder-val="{{{{ false }}}}"><span class="{{{{ c.saleCls }}}}" aria-hidden="true">{{{{ c.mark }}}}</span></sc-if>{{{{ c.n }}}}</a></div>
</sc-for>
</div>
<sc-if value="{{{{ navR }}}}" hint-placeholder-val="{{{{ true }}}}"><button class="navArrow r" type="button" aria-label="Další kategorie" onClick="{{{{ navNext }}}}"><span class="navArrowIc">{I('caret-right')}</span></button></sc-if>
</div>
<sc-if value="{{{{ megaOpen }}}}" hint-placeholder-val="{{{{ false }}}}">
<div class="mega bleed"><div class="container megaIn">
<div class="megaHead"><h3>{{{{ megaName }}}} <small>{{{{ megaCount }}}}</small></h3><a class="btn btn-out megaAll" href="Kategorie.dc.html">Vše v kategorii{I('caret-right')}</a></div>
<div class="megaGrid"><sc-for list="{{{{ megaSubs }}}}" as="m" hint-placeholder-count="6"><div class="megaCol"><a class="megaL2" href="Kategorie.dc.html"><sc-if value="{{{{ m.hasImg }}}}" hint-placeholder-val="{{{{ true }}}}"><img src="{{{{ m.img }}}}" alt=""></sc-if><sc-if value="{{{{ m.noImg }}}}" hint-placeholder-val="{{{{ false }}}}"><span class="ph">[FOTO]</span></sc-if><span>{{{{ m.n }}}} <small>{{{{ m.c }}}}</small></span></a>
<ul><sc-for list="{{{{ m.kids }}}}" as="k" hint-placeholder-count="3"><li><a href="Kategorie.dc.html">{{{{ k.n }}}}</a></li></sc-for><sc-if value="{{{{ m.more }}}}" hint-placeholder-val="{{{{ false }}}}"><li><a class="more" href="Kategorie.dc.html">{{{{ m.moreTxt }}}}</a></li></sc-if></ul></div></sc-for></div>
</div></div>
</sc-if>
</nav>
</div>'''

DRAWER_HTML = f'''<sc-if value="{{{{ drawer }}}}" hint-placeholder-val="{{{{ false }}}}">
<div class="navOverlay" onClick="{{{{ overlayClick }}}}" onKeyDown="{{{{ drawerKey }}}}">
<div class="drawer" role="dialog" aria-modal="true" aria-labelledby="drawerT">
<div class="drawerHead"><h2 class="drawerT" id="drawerT">Sortiment</h2><button class="iconBtn" type="button" aria-label="Zavřít menu" onClick="{{{{ closeDrawer }}}}">{I('x')}</button></div>
<ul>
<sc-for list="{{{{ drawerCats }}}}" as="c" hint-placeholder-count="11">
<li><div class="dRow"><a href="Kategorie.dc.html">{{{{ c.n }}}}</a><sc-if value="{{{{ c.hasSubs }}}}" hint-placeholder-val="{{{{ false }}}}"><button class="iconBtn exp" type="button" aria-expanded="{{{{ c.exp }}}}" aria-label="{{{{ c.label }}}}" onClick="{{{{ c.toggle }}}}">{I('caret-down')}</button></sc-if></div>
<sc-if value="{{{{ c.open }}}}" hint-placeholder-val="{{{{ false }}}}"><ul><sc-for list="{{{{ c.subs }}}}" as="x" hint-placeholder-count="4"><li class="dRow dSub"><a href="Kategorie.dc.html">{{{{ x.n }}}}</a></li></sc-for></ul></sc-if>
</li>
</sc-for>
</ul>
<div class="dLinks"><a href="Onas.dc.html">{I('buildings')}O nás</a><a href="Kontakt.dc.html">{I('phone')}Kontakt</a><a href="Doprava.dc.html">{I('truck')}Doprava a platba</a><a href="ObchodniPodminky.dc.html">{I('file-text')}Obchodní podmínky</a>
<sc-if value="{{{{ notAuth }}}}" hint-placeholder-val="{{{{ true }}}}"><a href="Udaje.dc.html">{I('sign-in')}Přihlášení / Registrace B2B</a></sc-if>
<sc-if value="{{{{ auth }}}}" hint-placeholder-val="{{{{ false }}}}"><a href="Main.dc.html">{I('user')}Můj účet · {{{{ userName }}}}</a></sc-if></div>
<div class="dContact"><span>{I('phone')} <a href="tel:+420775570418">+420 775 570 418</a></span><span>{I('clock')} Po–Pá 9:00–16:00</span><span>{I('envelope')} <a href="mailto:daver@daver.cz">daver@daver.cz</a></span></div>
</div></div>
</sc-if>'''

DIALOG_HTML = f'''<sc-if value="{{{{ dlgOpen }}}}" hint-placeholder-val="{{{{ false }}}}">
<div class="mdOverlay" onClick="{{{{ overlayClick }}}}" onKeyDown="{{{{ dlgKey }}}}">
<div class="mdBox dlg BasketResultDialog" role="dialog" aria-modal="true" aria-labelledby="dlgT">
<div class="dlgHead"><h2 id="dlgT">{I('check-circle')} Přidáno do košíku</h2><button class="iconBtn" type="button" aria-label="Zavřít" onClick="{{{{ closeDlg }}}}">{I('x')}</button></div>
<div class="dlgProd"><sc-if value="{{{{ dlgHasImg }}}}" hint-placeholder-val="{{{{ true }}}}"><img class="dlgImg" src="{{{{ dlgImg }}}}" alt=""></sc-if><sc-if value="{{{{ dlgNoImg }}}}" hint-placeholder-val="{{{{ false }}}}"><div class="ph">[FOTO]</div></sc-if><div><strong>{{{{ dlgName }}}}</strong><div class="sugMeta">Kód {{{{ dlgCode }}}} · <span class="avOk">{{{{ dlgAv }}}}</span></div><div class="sugMeta">Množství: {{{{ dlgQty }}}}</div></div><div class="priceMain">{{{{ dlgPrice }}}}<div class="priceSub">bez DPH</div></div></div>
<sc-if value="{{{{ dlgHasShades }}}}" hint-placeholder-val="{{{{ false }}}}"><div class="dlgShades"><div class="dlgShH">Přidané odstíny · {{{{ dlgShadeTitle }}}}</div><ul><sc-for list="{{{{ dlgShades }}}}" as="x" hint-placeholder-count="3"><li><span class="dlgDot" style="background:{{{{ x.hex }}}}"></span><span class="dlgShN">{{{{ x.no }}}} {{{{ x.n }}}}</span><span class="dlgShQ">{{{{ x.q }}}}</span><span class="dlgShP">{{{{ x.sum }}}}</span></li></sc-for></ul></div></sc-if>
<p class="dlgSum">{{{{ dlgSum }}}}</p>
<div class="freeBox"><span>{I('truck')}{{{{ freeMsg }}}}</span><progress max="100" value="{{{{ freePct }}}}" aria-label="Postup k dopravě zdarma od 1 000 Kč"></progress></div>
<div class="dlgAct"><button class="btn btn-out" type="button" onClick="{{{{ closeDlg }}}}">Zpět do obchodu</button><a class="btn btn-main" href="Kosik.dc.html">Objednat zboží</a></div>
</div></div>
</sc-if>'''

ASSIST_HTML = f'''<button class="assistFab" type="button" aria-label="Nákupní asistent" aria-expanded="{{{{ assist }}}}" onClick="{{{{ toggleAssist }}}}">{I('chat-circle-dots')}</button>
<sc-if value="{{{{ assist }}}}" hint-placeholder-val="{{{{ false }}}}">
<div class="assistPanel" role="dialog" aria-label="Nákupní asistent" onKeyDown="{{{{ assistKey }}}}">
<div class="assistHead"><strong>Nákupní asistent</strong><button class="iconBtn" type="button" aria-label="Zavřít asistenta" onClick="{{{{ toggleAssist }}}}">{I('x')}</button></div>
<div class="assistBody"><div class="bubble me">Potřebuji ploché syntetické štětce pro akryl, větší velikosti.</div><div class="bubble bot">Doporučuji <a href="Detail.dc.html">Meyco sada plochých štětců syntetické č. 12 16 20</a> – 69,38 Kč bez DPH, skladem &gt; 30 ks.</div><div class="bubble bot"><span class="todo">[Ukázková konverzace – obsah a napojení doladit]</span></div></div>
<form class="assistForm" onSubmit="{{{{ assistSubmit }}}}"><label class="sr" for="asq">Dotaz pro asistenta</label><input id="asq" placeholder="Dotaz pro asistenta"><button class="iconBtn" type="submit" aria-label="Odeslat">{I('paper-plane-right')}</button></form>
</div>
</sc-if>'''

QUICK_HTML = '''<sc-if value="{{ quickOpen }}" hint-placeholder-val="{{ false }}">
<div class="mdOverlay" onClick="{{ quickOverlay }}"><div class="mdBox"><dc-import name="QuickView" p="{{ quickP }}" pickup="{{ pickup }}" delivery="{{ delivery }}" on-add="{{ quickAdd }}" on-close="{{ closeQuick }}" hint-size="960px,640px"></dc-import></div></div>
</sc-if>'''

TOAST_HTML = f'''<div class="toastWrap" aria-live="polite"><sc-if value="{{{{ hasToast }}}}" hint-placeholder-val="{{{{ false }}}}"><div class="{{{{ toastCls }}}}" role="status">{I('info')}<span>{{{{ toast }}}}</span></div></sc-if></div>'''

def doc(title, head_css, helmet_css, body, js, w, h, props=None):
    p = {"$preview": {"width": w, "height": h}}
    if props: p.update(props)
    pj = json.dumps(p, ensure_ascii=False).replace("&", "&amp;").replace("'", "&#39;")
    head_style = f"<style>{head_css}</style>\n" if head_css else ""
    return f'''<!doctype html>
<html lang="cs">
<head>
<meta charset="utf-8">
<title>{title}</title>
<script src="./support.js"></script>
{head_style}</head>
<body>
<x-dc>
<helmet>
<style>body{{margin:0}}{helmet_css}</style>
</helmet>
{body}
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{pj}'>
{js}
</script>
</body>
</html>
'''

def shop_page(title, page_css, main_html, page_js, h, cur_cat=None):
    body = f'''<div id="Master" class="MasterView"><div class="wrap">
{HEADER_HTML}
<main id="main">
{main_html}
</main>
<section class="nlSec" aria-labelledby="hNl"><div class="container"><div class="nlBox">
<div class="nlIco" aria-hidden="true">{I('envelope')}</div>
<div class="nlTxt"><h2 id="hNl">Odběr novinek e-mailem</h2><p>Pravidelný přehled novinek v sortimentu, akčních cen a výprodejů. Žádný spam, odhlásit se můžete jedním kliknutím.</p></div>
<div class="nlAct"><sc-if value="{{{{ nlOk }}}}" hint-placeholder-val="{{{{ false }}}}"><div class="nlDone" role="status">{I('check-circle')}<div><strong>Děkujeme, odběr je přihlášen.</strong><span>Potvrzení jsme poslali na {{{{ nlEmail }}}}.</span></div></div></sc-if>
<sc-if value="{{{{ nlForm }}}}" hint-placeholder-val="{{{{ true }}}}"><form class="nlForm" novalidate onSubmit="{{{{ nlSubmit }}}}">
<div class="nlRow"><label class="sr" for="nlE">Váš e-mail</label><div class="nlField">{I('envelope')}<input id="nlE" type="email" autocomplete="email" placeholder="Váš e-mail" value="{{{{ nlEmail }}}}" onChange="{{{{ nlOnEmail }}}}" aria-invalid="{{{{ nlInvalid }}}}" aria-describedby="nlErr"></div><button class="btn nlBtn" type="submit">Přihlásit odběr{I('paper-plane-right')}</button></div>
<label class="nlChk"><input type="checkbox" checked="{{{{ nlConsent }}}}" onChange="{{{{ nlOnConsent }}}}"><span>Souhlasím se <a href="Gdpr.dc.html">zpracováním osobních údajů</a>.</span></label>
<sc-if value="{{{{ nlHasErr }}}}" hint-placeholder-val="{{{{ false }}}}"><p class="nlErr" id="nlErr" role="alert">{{{{ nlErrTxt }}}}</p></sc-if>
</form></sc-if></div>
</div></div></section>
<dc-import name="Footer" hint-size="100%,600px"></dc-import>
</div>
{DRAWER_HTML}
{QUICK_HTML}
{DIALOG_HTML}
{ASSIST_HTML}
{TOAST_HTML}
<dc-import name="FontSizeSwitch" hint-size="0px,0px"></dc-import>
</div>'''
    body = body.replace('<dc-import name="ProductCard" ', '<dc-import name="ProductCard" on-quick="{{ openQuick }}" ')
    cc = ''
    js = DATA_JS + SHOP_JS.replace('class Component extends DCLogic {', 'class Component extends DCLogic {\n ' + (f"get curCat(){{return '{cur_cat}';}}" if cur_cat else '')) + page_js + "\n}\n"
    return doc(title, TOKENS + BASE_CSS + SHOP_CSS, page_css, body, js, 1440, h + 320)

def write(name, content):
    os.makedirs(ROOT, exist_ok=True)
    open(os.path.join(ROOT, name), 'w').write(content)
    return os.path.join(ROOT, name)
