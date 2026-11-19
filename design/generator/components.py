from common import *

CHEAD = TOKENS + "\n*,*::before,*::after{box-sizing:border-box}\n" + SQ_INPUTS + SQ_ALL
CZK_JS = r"""const CZK=(n)=>n.toLocaleString('cs-CZ',{minimumFractionDigits:2,maximumFractionDigits:2})+' Kč';
const VAT=1.21;
const lsGet=(k)=>{try{return localStorage.getItem('daver'+k)}catch(e){return null}};
const lsSet=(k,v)=>{try{localStorage.setItem('daver'+k,v)}catch(e){}};
"""
ROOTC = "font-family:var(--font,system-ui,sans-serif);color:var(--text,#18181b);font-size:var(--fs-body,15px);line-height:1.5"
BTN = """{c} .btn{{display:inline-flex;align-items:center;justify-content:center;gap:8px;min-height:44px;padding:0 16px;border-radius:var(--btn-radius,6px);border:1px solid transparent;font:inherit;font-weight:600;cursor:pointer;text-decoration:none;white-space:nowrap}}
{c} .btn-main{{background:var(--main,#27272a);color:#fff}}{c} .btn-main:hover{{background:var(--main-d,#09090b);color:#fff}}
{c} .btn-out{{background:#fff;border-color:var(--input-border,#d4d4d8);color:inherit}}{c} .btn-out:hover{{border-color:var(--primary-d,#27272a)}}
{c} .iconBtn{{display:inline-flex;align-items:center;justify-content:center;width:44px;height:44px;border:0;background:transparent;border-radius:var(--btn-radius,6px);cursor:pointer;color:inherit}}{c} .iconBtn:hover{{background:var(--primary-10,#f4f4f5)}}
{c} .ic{{width:20px;height:20px;flex:none}}
{c} .ph{{display:flex;align-items:center;justify-content:center;background:var(--bg-soft,#f8f8f8);border:1px dashed var(--input-border,#d4d4d8);color:var(--text-muted,#71717a);font-size:12px;text-align:center;padding:6px;border-radius:4px}}
{c} .todo{{background:#fff7d6;color:#5c4a00;padding:0 4px;border-radius:2px}}
@supports (corner-shape:squircle){{{c} .btn,{c} .iconBtn{{corner-shape:var(--corner-shape,squircle)}}}}
{c} :focus-visible{{outline:2px solid var(--primary-d,#27272a);outline-offset:2px}}"""
def btn(c): return BTN.format(c=c)

comps = {}
_D = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data.json'), encoding='utf-8'))
DQ = next(p for p in _D['products'] if p['id'] == _D['ids']['jovibox'])

# ---------------- ProductCard ----------------
comps['ProductCard'] = doc('Karta produktu', CHEAD, """
.pcWrap{container-type:inline-size;height:100%;""" + ROOTC + """}
.pc{position:relative;display:flex;flex-direction:column;gap:10px;height:100%;padding:14px;background:#fff;border:1px solid var(--line,#e4e4e7);border-radius:var(--card-radius,8px);transition:box-shadow .2s,transform .2s}
@supports (corner-shape:squircle){.pc,.pcZoom{corner-shape:var(--corner-shape,squircle)}}
.pc:hover{box-shadow:0 10px 28px rgba(0,0,0,.10);transform:translateY(-2px)}
.pcFlags{position:absolute;top:12px;left:12px;z-index:2;display:flex;flex-direction:column;gap:4px;align-items:flex-start}
.pcFlag{font-size:12px;font-weight:700;padding:2px 8px;border-radius:var(--radius-xs,2px);color:#fff}
.pcFlag.discount{background:var(--flag-discount,#ffc107);color:var(--flag-discount-fg,#1e1e1e)}
.pcFlag.flag01{background:var(--flag-akce,#c2410c)}.pcFlag.flag00{background:var(--flag-novinka,#0277bd)}.pcFlag.flag02{background:var(--flag-doporucujeme,#1f6fa8)}.pcFlag.flag03{background:var(--flag-vyprodej,#3867d6)}
.pcImg{position:relative;aspect-ratio:220/200;overflow:hidden}
.pcImg .ph,.pcImg img{width:100%;height:100%;transition:transform .3s}
.pcImg img{object-fit:contain}
.pc:hover .pcImg .ph,.pc:hover .pcImg img{transform:scale(1.03)}
.pcZoom{position:absolute;top:0;right:0;z-index:3;display:flex;align-items:center;justify-content:center;width:44px;height:44px;border:1px solid var(--line,#e4e4e7);border-radius:var(--btn-radius,6px);background:rgba(255,255,255,.95);color:var(--text,#18181b);cursor:pointer;transition:border-color .15s,color .15s,box-shadow .15s,transform .15s}
.pcZoom:hover{background:#fff;border-color:var(--primary-d,#7f343d);color:var(--primary-d,#7f343d);box-shadow:0 2px 8px rgba(0,0,0,.08)}.pcZoom:active{transform:scale(.96)}
.pcZoom .ic{width:22px;height:22px}
.pcCode{position:absolute;left:8px;bottom:8px;background:rgba(255,255,255,.95);border:1px solid var(--line,#e4e4e7);border-radius:999px;padding:1px 10px;font-size:12px;opacity:0;transition:opacity .2s}
.pc:hover .pcCode,.pc:focus-within .pcCode{opacity:1}
.pcName{margin:0;font-size:var(--fs-body,15px);font-weight:600;line-height:1.35;height:calc(1.35em * 3);overflow:hidden;display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical}
.pcLink{color:var(--text,#18181b);text-decoration:none}
.pcLink::after{content:"";position:absolute;inset:0;z-index:0}
.pcLink:hover{text-decoration:underline}
.pcParams{margin:0;display:flex;flex-direction:column;gap:2px;font-size:var(--fs-body-sm,13px);height:calc(1.5em * 3)}
.pcParams div{display:flex;justify-content:space-between;gap:8px}
.pcParams dt{color:var(--text-weaker,rgba(24,24,27,.68))}.pcParams dd{margin:0;text-align:right}
.pcBottom{margin-top:auto;display:flex;flex-direction:column;gap:10px;position:relative;z-index:1}
.pcAv{position:relative;align-self:flex-start}
.avBtn{display:inline-flex;align-items:center;gap:6px;border:0;background:none;padding:2px 0;font:inherit;font-size:var(--fs-body-sm,13px);color:var(--success-text,#15803d);cursor:help}
.avBtn.blue{color:var(--info,#1f6fa8)}
.dot{width:8px;height:8px;border-radius:50%;background:currentColor}
.avPop{display:none;position:absolute;bottom:calc(100% + 6px);left:0;width:240px;background:#fff;border:1px solid var(--line,#e4e4e7);border-radius:var(--radius-md,6px);box-shadow:0 8px 20px rgba(0,0,0,.12);padding:10px 12px;font-size:13px;z-index:5}
.pcAv:hover .avPop,.pcAv:focus-within .avPop{display:block}
.avPop p{margin:0 0 4px}
.pcPrice .pm{font-size:var(--fs-price-md,20px);font-weight:700;line-height:1.2}
.pcPrice .ps{font-size:12px;color:var(--text-weaker,rgba(24,24,27,.68))}
.pcBuy{display:flex;gap:8px;align-items:stretch}
.qty{display:flex;align-items:center;min-width:120px;border:1px solid var(--input-border,#d4d4d8);border-radius:var(--btn-radius,4px);height:44px;background:#fff}
.qty button{width:36px;height:100%;border:0;background:none;font-size:18px;cursor:pointer;color:inherit}
.qty button:disabled{color:#c4c4c8;cursor:not-allowed}
.qty label{flex:1;display:flex;align-items:center;justify-content:center;gap:4px;padding:0 4px;font-size:14px;white-space:nowrap}
.qty input{field-sizing:content;width:auto;min-width:1ch;max-width:6ch;border:0;outline:0;text-align:center;font:inherit;padding:0;background:transparent}
.qty.flash{animation:fl .6s}
@keyframes fl{50%{background:var(--primary-10,#f4f4f5)}}
.pcBuy .btn{flex:1}
@container (max-width:300px){.pcBuy{flex-direction:column}.qty{justify-content:space-between}}
""" + btn('.pcWrap') + """
@media (prefers-reduced-motion:reduce){.pc,.pcImg .ph,.qty.flash{transition:none;animation:none}.pc:hover{transform:none}}
""", f'''<div class="pcWrap">
<article class="pc ProductView">
<div class="pcFlags"><sc-for list="{{{{ flags }}}}" as="f" hint-placeholder-count="1"><span class="{{{{ f.cls }}}}">{{{{ f.t }}}}</span></sc-for></div>
<div class="pcImg"><button class="pcZoom" type="button" aria-label="{{{{ zoomLabel }}}}" onClick="{{{{ quick }}}}">{I('magnifying-glass-plus')}</button><sc-if value="{{{{ hasImg }}}}" hint-placeholder-val="{{{{ true }}}}"><img src="{{{{ img }}}}" alt="{{{{ name }}}}" loading="lazy"></sc-if><sc-if value="{{{{ noImg }}}}" hint-placeholder-val="{{{{ false }}}}"><div class="ph">[FOTO]</div></sc-if><span class="pcCode">Kód {{{{ code }}}}</span></div>
<h3 class="pcName"><a class="pcLink" href="{{{{ href }}}}">{{{{ name }}}}</a></h3>

<div class="pcBottom">
<div class="pcAv"><dc-import name="Availability" stock="{{{{ stock }}}}" text="{{{{ av }}}}" size="sm" pickup="{{{{ pickup }}}}" delivery="{{{{ delivery }}}}" hint-size="160px,20px"></dc-import></div>
<div class="pcPrice"><div class="pm">{{{{ price }}}}</div><div class="ps">bez DPH · {{{{ priceVat }}}} s DPH</div></div>
<div class="pcBuy AddToCartView">
<div class="{{{{ qtyCls }}}}"><button type="button" aria-label="Snížit množství" disabled="{{{{ minDis }}}}" onClick="{{{{ dec }}}}">−</button><label><input inputmode="numeric" aria-label="Množství" size="{{{{ qtyLen }}}}" value="{{{{ qty }}}}" onChange="{{{{ setQty }}}}">{{{{ unit }}}}</label><button type="button" aria-label="Zvýšit množství" onClick="{{{{ inc }}}}">+</button></div>
<button class="btn btn-main" type="button" onClick="{{{{ add }}}}">{I('shopping-cart')}Koupit</button>
</div>
</div>
</article>
</div>''', CZK_JS + r"""
const DEMO={"id": 130, "name": "Meyco sada pěnových tupovacích štětců č. 15 25 35 mm", "code": "14217", "brand": "Meyco", "price": 36.4, "stock": 50, "av": "Skladem > 50 ks", "unit": "ks", "img": "/_blob/241d7a5e109cccbfbac2a9ff27a2141b", "flags": [{"cls": "flag00", "t": "Novinka"}], "href": "Detail.dc.html"};
class Component extends DCLogic {
 constructor(props){super(props);this.state={qty:1,flash:false};}
 componentWillUnmount(){clearTimeout(this.ft);}
 set(q){this.setState({qty:Math.max(1,q||1)});}
 renderVals(){
  const p=this.props.p||DEMO; const q=this.state.qty;
  return {
   name:p.name, code:p.code, brand:p.brand||'', img:p.img||'', hasImg:!!p.img, noImg:!p.img, href:p.href||'Detail.dc.html', unit:p.unit||'ks',
   flags:(p.flags||[]).map((f)=>({t:f.t,cls:'pcFlag '+f.cls})),
   av:p.av||'', stock:(p.stock==null?(p.blue?0:26):p.stock), blue:!!p.blue, onStock:!p.blue, avCls:'avBtn'+(p.blue?' blue':''),
   price:(p.from?'od ':'')+CZK(p.price), priceVat:(p.from?'od ':'')+CZK(p.price*VAT),
   hasPack:!!p.pack, noPack:!p.pack, packTxt:p.pack?p.pack+' ks':'',
   setPack:()=>{this.set(p.pack);this.setState({flash:true});clearTimeout(this.ft);this.ft=setTimeout(()=>this.setState({flash:false}),600);},
   pickup:this.props.pickup||'zítra', delivery:this.props.delivery||'pozítří',
   qty:q, qtyLen:Math.max(1,String(q).length), minDis:q<=1, qtyCls:'qty'+(this.state.flash?' flash':''),
   dec:()=>this.set(q-1), inc:()=>this.set(q+1),
   setQty:(e)=>{const v=parseInt(e.target.value.replace(/\D/g,''),10);this.setState({qty:isNaN(v)?1:Math.max(1,v)});},
   add:()=>{if(this.props.onAdd)this.props.onAdd(p,q);},
   zoomLabel:'Rychlý náhled: '+p.name, quick:()=>{if(this.props.onQuick)this.props.onQuick(p);}
  };
 }
}""", 300, 540, {"p": {"editor": None}, "pickup": {"editor": None}, "delivery": {"editor": None}, "onAdd": {"editor": None}, "onQuick": {"editor": None}})

# ---------------- LoginPopup ----------------
comps['LoginPopup'] = doc('Přihlášení', CHEAD, """
.lp{width:320px;max-width:100%;background:#fff;border:1px solid var(--line,#e4e4e7);border-radius:var(--radius-md,6px);padding:20px;""" + ROOTC + """}
.lp h2{margin:0 0 4px;font-size:18px}.lp .lead{margin:0 0 14px;font-size:13px;color:var(--text-weaker,rgba(24,24,27,.68))}
.lpHead{display:flex;justify-content:space-between;align-items:center;gap:12px;margin:-6px -10px 4px 0}.lpHead h2{margin:0;line-height:1.25}.lpHead .iconBtn{flex:none}
.lpField{margin-bottom:12px}
.lpField label{display:block;font-size:13px;font-weight:600;margin-bottom:4px}
.lpIn{display:flex;align-items:center;gap:8px;border:1px solid var(--input-border,#d4d4d8);border-radius:var(--radius-sm,4px);height:44px;padding:0 4px 0 10px}
.lpIn{transition:border-color .15s,box-shadow .15s}.lpIn:focus-within{border-color:var(--primary-d,#7f343d);box-shadow:0 0 0 1px var(--primary-d,#7f343d),0 0 0 5px rgba(155,65,75,.2)}.lpIn input:focus,.lpIn input:focus-visible{outline:none!important;box-shadow:none}.lpIn .iconBtn:focus-visible{outline-offset:-2px}
.lpIn.bad{border-color:var(--danger,#b91c1c)}
.lpIn input{flex:1;min-width:0;border:0;outline:0;font:inherit;height:100%}
.lpIn .ic{color:var(--text-muted,#71717a)}
.lpErr{font-size:12px;color:var(--danger,#b91c1c);margin-top:4px}
.lpRow{display:flex;justify-content:space-between;align-items:center;font-size:13px;margin-bottom:14px}
.lpCheck{display:flex;align-items:center;gap:8px;cursor:pointer;min-height:44px}
.lpCheck input{width:18px;height:18px;accent-color:var(--primary-d,#27272a)}
.lp .btn-main{width:100%}
.lpFoot{margin-top:12px;font-size:13px;text-align:center}
.lpOk{text-align:center;padding:12px 0}
.lpOk .big{width:48px;height:48px;color:var(--success,#15803d);margin:0 auto 8px}
.lp a{color:var(--primary-d,#27272a)}
""" + btn('.lp'), f'''<div class="lp LoginForm" role="dialog" aria-label="Přihlášení" onKeyDown="{{{{ onKey }}}}">
<sc-if value="{{{{ notDone }}}}" hint-placeholder-val="{{{{ true }}}}">
<form onSubmit="{{{{ submit }}}}" novalidate="">
<div class="lpHead"><h2>Přihlášení</h2><button class="iconBtn" type="button" aria-label="Zavřít" onClick="{{{{ close }}}}">{I('x')}</button></div>
<p class="lead">Velkoobchodní ceny vidíte po přihlášení.</p>
<div class="lpField"><label for="lpE">E-mail</label><div class="{{{{ eCls }}}}">{I('envelope')}<input id="lpE" type="email" autocomplete="email" autoFocus="{{{{ true }}}}" aria-invalid="{{{{ eBad }}}}" value="{{{{ email }}}}" onChange="{{{{ onEmail }}}}"></div>
<sc-if value="{{{{ eBad }}}}" hint-placeholder-val="{{{{ false }}}}"><div class="lpErr" role="alert">Zadejte e-mail ve tvaru jmeno@firma.cz.</div></sc-if></div>
<div class="lpField"><label for="lpP">Heslo</label><div class="{{{{ pCls }}}}">{I('lock')}<input id="lpP" type="{{{{ pwType }}}}" autocomplete="current-password" aria-invalid="{{{{ pBad }}}}" value="{{{{ pw }}}}" onChange="{{{{ onPw }}}}"><button class="iconBtn" type="button" aria-label="Zobrazit heslo" aria-pressed="{{{{ show }}}}" onClick="{{{{ toggleShow }}}}">{I('eye')}</button></div>
<sc-if value="{{{{ pBad }}}}" hint-placeholder-val="{{{{ false }}}}"><div class="lpErr" role="alert">Heslo musí mít alespoň 4 znaky.</div></sc-if></div>
<div class="lpRow"><label class="lpCheck"><input type="checkbox" checked="{{{{ remember }}}}" onChange="{{{{ toggleRem }}}}">Zůstat přihlášen</label><a href="#zapomenute">Zapomenuté heslo?</a></div>
<button class="btn btn-main" type="submit">Přihlásit se</button>
<p class="lpFoot">Nemáte účet? <a href="Udaje.dc.html">Žádost o B2B registraci</a></p>
</form>
</sc-if>
<sc-if value="{{{{ done }}}}" hint-placeholder-val="{{{{ false }}}}">
<div class="lpOk">{I('check-circle','ic big')}<h2>Jste přihlášen</h2><p class="lead">Ceny se zobrazují podle vašich obchodních podmínek.</p><button class="btn btn-main" type="button" onClick="{{{{ close }}}}">Pokračovat v nákupu</button></div>
</sc-if>
</div>''', r"""
class Component extends DCLogic {
 constructor(props){super(props);this.state={email:'',pw:'',show:false,remember:true,tried:false,done:false};}
 renderVals(){
  const s=this.state;
  const eBad=s.tried&&!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(s.email);
  const pBad=s.tried&&s.pw.length<4;
  const close=()=>{if(this.props.onClose)this.props.onClose();};
  return {
   email:s.email,pw:s.pw,show:s.show,remember:s.remember,eBad:eBad,pBad:pBad,
   eCls:'lpIn'+(eBad?' bad':''),pCls:'lpIn'+(pBad?' bad':''),pwType:s.show?'text':'password',
   done:s.done,notDone:!s.done,
   onEmail:(e)=>this.setState({email:e.target.value}),onPw:(e)=>this.setState({pw:e.target.value}),
   toggleShow:()=>this.setState({show:!s.show}),toggleRem:()=>this.setState({remember:!s.remember}),
   close:close, onKey:(e)=>{if(e.key==='Escape'){e.stopPropagation();close();}},
   submit:(e)=>{e.preventDefault();const ok=/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(s.email)&&s.pw.length>=4;
     this.setState({tried:true});if(ok){this.setState({done:true});if(this.props.onLogin)this.props.onLogin(s.email);}}
  };
 }
}""", 320, 420, {"onClose": {"editor": None}, "onLogin": {"editor": None}})

# ---------------- UserMenu ----------------
items = [('package', 'Přehled objednávek', '#ucet'), ('receipt', 'Přehled faktur', '#ucet'), ('export', 'Export / import produktů', '#ucet'), ('heart', 'Oblíbené produkty', '#ucet'), ('scales', 'Porovnání produktů', 'Porovnani.dc.html'), ('user-gear', 'Správa účtu', '#ucet')]
li = ''.join(f'<li><a href="{h}">{I(i)}<span>{t}</span>{I("caret-right","ic chev")}</a></li>' for i, t, h in items)
comps['UserMenu'] = doc('Menu přihlášeného', CHEAD, """
.um{width:320px;max-width:100%;background:#fff;border:1px solid var(--line,#e4e4e7);border-radius:var(--radius-md,6px);padding:16px;""" + ROOTC + """}
.umHead{display:flex;align-items:center;gap:12px;padding-bottom:12px;border-bottom:1px solid var(--line,#e4e4e7)}
@media (max-width:819px){.um{width:100%;border:0;border-radius:var(--card-radius,8px) var(--card-radius,8px) 0 0;padding:28px 20px calc(20px + env(safe-area-inset-bottom));position:relative}.um::before{content:"";position:absolute;top:10px;left:50%;width:40px;height:4px;margin-left:-20px;border-radius:2px;background:var(--line,#e4e4e7)}}
.umMono{width:44px;height:44px;border-radius:50%;background:var(--primary-d,#27272a);color:#fff;display:flex;align-items:center;justify-content:center;font-weight:700}
@supports (corner-shape:squircle){.umMono{corner-shape:squircle}}
.umHead strong{display:block}.umHead small{font-size:13px;color:var(--text-weaker,rgba(24,24,27,.68))}
.grp{display:inline-block;background:var(--primary-10,#f4f4f5);color:var(--primary-d,#27272a);border-radius:999px;padding:0 8px;font-weight:600}
.umHead .iconBtn{margin-left:auto}
.um ul{list-style:none;margin:8px 0;padding:0}
.um li a{display:flex;align-items:center;gap:12px;min-height:44px;padding:0 8px;border-radius:var(--radius-sm,4px);color:var(--text,#18181b);text-decoration:none}
.um li a:hover{background:var(--primary-10,#f4f4f5)}
.um .chev{margin-left:auto;color:var(--text-muted,#71717a);width:16px;height:16px}
.umOut{display:flex;align-items:center;gap:10px;width:100%;min-height:44px;padding:0 8px;border:0;border-top:1px solid var(--line,#e4e4e7);background:none;color:var(--danger,#b91c1c);font:inherit;font-weight:600;cursor:pointer}
""" + btn('.um'), f'''<div class="um" role="dialog" aria-label="Můj účet" onKeyDown="{{{{ onKey }}}}">
<div class="umHead"><span class="umMono">{{{{ ini }}}}</span><div><strong>{{{{ userName }}}}</strong><small>Cenová skupina: <span class="grp">{{{{ group }}}}</span></small></div><button class="iconBtn" type="button" aria-label="Zavřít" onClick="{{{{ close }}}}">{I('x')}</button></div>
<ul>{li}</ul>
<button class="umOut" type="button" onClick="{{{{ logout }}}}">{I('sign-out')}Odhlásit z e-shopu</button>
</div>''', r"""
class Component extends DCLogic {
 renderVals(){
  const n=this.props.userName||'Jan Novák';
  const close=()=>{if(this.props.onClose)this.props.onClose();};
  return {userName:n, ini:n.split(' ').map((x)=>x[0]).join('').slice(0,2), group:this.props.group||'Velkoobchod',
   close:close, logout:()=>{if(this.props.onLogout)this.props.onLogout();},
   onKey:(e)=>{if(e.key==='Escape'){e.stopPropagation();close();}}};
 }
}""", 320, 420, {"userName": {"editor": "text", "default": "Jan Novák"}, "group": {"editor": "text", "default": "Velkoobchod"}, "onClose": {"editor": None}, "onLogout": {"editor": None}})

# ---------------- CartPopup ----------------
comps['CartPopup'] = doc('Mini košík', CHEAD, """
.cp{width:360px;max-width:100%;background:#fff;border:1px solid var(--line,#e4e4e7);border-radius:var(--radius-md,6px);padding:16px;""" + ROOTC + """}
.cpHead{display:flex;align-items:center;justify-content:space-between;margin-bottom:8px}
.cpHead h2{margin:0;font-size:18px}.cpHead small{color:var(--text-weaker,rgba(24,24,27,.68));font-weight:400;font-size:13px;margin-left:6px}
.cpList{list-style:none;margin:0;padding:0;max-height:288px;overflow:auto}
.cpLine{display:grid;grid-template-columns:52px minmax(0,1fr) auto;gap:10px;align-items:center;padding:8px 0;border-bottom:1px solid var(--line,#e4e4e7)}
.cpLine .ph,.cpImg{width:52px;height:52px;padding:0;font-size:9px;object-fit:contain}
.cpName{font-size:13px;font-weight:600;line-height:1.3;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.cpMeta{font-size:12px;color:var(--text-weaker,rgba(24,24,27,.68))}
.cpPrice{font-weight:700;font-size:14px;white-space:nowrap}
.cpTot{display:flex;justify-content:space-between;align-items:flex-end;padding:12px 0}
.cpTot .pm{font-size:20px;font-weight:700;text-align:right}.cpTot .ps{font-size:12px;color:var(--text-weaker,rgba(24,24,27,.68));text-align:right}
.cpFree{border:1px solid var(--line,#e4e4e7);border-radius:var(--radius-md,6px);padding:10px 12px;font-size:13px;margin-bottom:12px;display:flex;gap:10px;align-items:center}
.cpFree .ic{width:22px;height:22px;flex:none}
.cpFreeIn{flex:1;display:flex;flex-direction:column;gap:6px}
.cpBar{appearance:none;-webkit-appearance:none;width:100%;height:6px;border:0;border-radius:3px;background:var(--line,#e4e4e7);overflow:hidden}
.cpBar::-webkit-progress-bar{background:var(--line,#e4e4e7);border-radius:3px}
.cpBar::-webkit-progress-value{background:var(--primary,#9b414b);border-radius:3px}
.cpBar::-moz-progress-bar{background:var(--primary,#9b414b);border-radius:3px}
.cpAct{display:flex;flex-direction:column;gap:8px}
.cpEmpty{text-align:center;padding:24px 8px;color:var(--text-weaker,rgba(24,24,27,.68))}
.cpEmpty .big{width:40px;height:40px;margin:0 auto 8px;color:var(--text-muted,#71717a)}
.cpEmpty strong{display:block;color:var(--text,#18181b)}
""" + btn('.cp'), f'''<div class="cp" role="dialog" aria-label="Nákupní košík" onKeyDown="{{{{ onKey }}}}">
<div class="cpHead"><h2>Nákupní košík<small>{{{{ countTxt }}}}</small></h2><button class="iconBtn" type="button" aria-label="Zavřít" onClick="{{{{ close }}}}">{I('x')}</button></div>
<sc-if value="{{{{ has }}}}" hint-placeholder-val="{{{{ true }}}}">
<ul class="cpList"><sc-for list="{{{{ lines }}}}" as="l" hint-placeholder-count="2"><li class="cpLine"><sc-if value="{{{{ l.hasImg }}}}" hint-placeholder-val="{{{{ true }}}}"><img class="cpImg" src="{{{{ l.img }}}}" alt=""></sc-if><sc-if value="{{{{ l.noImg }}}}" hint-placeholder-val="{{{{ false }}}}"><div class="ph">[FOTO]</div></sc-if><div><div class="cpName">{{{{ l.name }}}}</div><div class="cpMeta">{{{{ l.meta }}}}</div></div><div class="cpPrice">{{{{ l.sum }}}}</div></li></sc-for></ul>
<div class="cpTot"><span>Celkem bez DPH</span><div><div class="pm">{{{{ total }}}}</div><div class="ps">{{{{ totalVat }}}} s DPH</div></div></div>
<div class="cpFree">{I('truck')}<div class="cpFreeIn"><span>{{{{ freeMsg }}}}</span><progress class="cpBar" max="1000" value="{{{{ freeVal }}}}" aria-label="Postup k dopravě zdarma od 1 000 Kč"></progress></div></div>
<div class="cpAct"><a class="btn btn-main" href="Kosik.dc.html">Přejít do košíku</a><button class="btn btn-out" type="button" onClick="{{{{ close }}}}">Pokračovat v nákupu</button></div>
</sc-if>
<sc-if value="{{{{ empty }}}}" hint-placeholder-val="{{{{ false }}}}">
<div class="cpEmpty">{I('shopping-cart','ic big')}<strong>Košík je zatím prázdný</strong>Přidejte zboží tlačítkem Koupit u produktu.</div>
</sc-if>
</div>''', CZK_JS + r"""
const DEMO=[{"name": "Meyco sada pěnových tupovacích štětců č. 15 25 35 mm", "qty": 4, "unit": "ks", "price": 36.4, "img": "/_blob/241d7a5e109cccbfbac2a9ff27a2141b"}, {"name": "Darwi čistič štětců 100 ml", "qty": 2, "unit": "ks", "price": 79.15, "img": "/_blob/724bc3619b88778cd7d54ea70542393f"}];
class Component extends DCLogic {
 renderVals(){
  const L=this.props.lines||DEMO;
  const t=L.reduce((a,l)=>a+l.price*l.qty,0); const c=L.reduce((a,l)=>a+l.qty,0);
  const close=()=>{if(this.props.onClose)this.props.onClose();};
  return {has:L.length>0,empty:L.length===0,countTxt:c+' ks',
   lines:L.map((l)=>({name:l.name,img:l.img||'',hasImg:!!l.img,noImg:!l.img,meta:l.qty+' '+l.unit+' × '+CZK(l.price),sum:CZK(l.price*l.qty)})),
   total:CZK(t),totalVat:CZK(t*VAT),close:close,
   freeVal:Math.min(1000,Math.round(t)),freeMsg:t>=1000?'Máte dopravu zdarma.':'Do dopravy zdarma zbývá '+CZK(1000-t)+' (zdarma od 1 000 Kč bez DPH)',onKey:(e)=>{if(e.key==='Escape'){e.stopPropagation();close();}}};
 }
}""", 360, 440, {"lines": {"editor": None}, "onClose": {"editor": None}})

# ---------------- FilterChip ----------------
comps['FilterChip'] = doc('Aktivní filtr', CHEAD, """
.fc{display:inline-flex;align-items:center;gap:2px;height:32px;padding:0 2px 0 12px;border:1px solid var(--input-border,#d4d4d8);border-radius:999px;background:var(--primary-10,#f4f4f5);font-size:13px;""" + ROOTC + """}
.fc button{display:inline-flex;align-items:center;justify-content:center;width:28px;height:28px;border:0;border-radius:50%;background:none;cursor:pointer;color:inherit}
.fc button:hover{background:#fff}.fc .ic{width:14px;height:14px}
.fc button::after{content:"";position:absolute;width:44px;height:44px}
""", f'''<span class="fc">{{{{ label }}}}<button type="button" aria-label="{{{{ aria }}}}" onClick="{{{{ remove }}}}">{I('x')}</button></span>''', r"""
class Component extends DCLogic {
 renderVals(){const l=this.props.label||'Meyco';
  return {label:l,aria:'Odebrat filtr '+l,remove:()=>{if(this.props.onRemove)this.props.onRemove();}};}
}""", 120, 40, {"label": {"editor": "text", "default": "Meyco"}, "onRemove": {"editor": None}})

# ---------------- Breadcrumb ----------------
comps['Breadcrumb'] = doc('Drobečková navigace', CHEAD, """
.bc{""" + ROOTC + """;font-size:var(--fs-body-sm,13px)}
.bc ol{list-style:none;margin:0;padding:12px 0;display:flex;flex-wrap:wrap;align-items:center;gap:4px}
.bc li{display:flex;align-items:center;gap:4px}
.bc a{color:var(--text-weaker,rgba(24,24,27,.68));text-decoration:none;display:inline-flex;align-items:center;min-height:32px}
.bc a:hover{color:var(--text,#18181b);text-decoration:underline}
.bc .ic{width:16px;height:16px}.bc .sep{width:12px;height:12px;color:var(--text-muted,#71717a)}
.bc [aria-current]{color:var(--text,#18181b);font-weight:500}
""", f'''<nav class="bc BreadcrumbView" aria-label="Drobečková navigace"><ol>
<li><a href="Main.dc.html" aria-label="Úvod">{I('house')}</a></li>
<sc-if value="{{{{ hasL1 }}}}" hint-placeholder-val="{{{{ true }}}}"><li>{I('caret-right','ic sep')}<a href="{{{{ h1 }}}}">{{{{ l1 }}}}</a></li></sc-if>
<sc-if value="{{{{ hasL2 }}}}" hint-placeholder-val="{{{{ false }}}}"><li>{I('caret-right','ic sep')}<a href="{{{{ h2 }}}}">{{{{ l2 }}}}</a></li></sc-if>
<li>{I('caret-right','ic sep')}<span aria-current="page">{{{{ current }}}}</span></li>
</ol></nav>''', r"""
class Component extends DCLogic {
 renderVals(){const p=this.props; const c=p.current||'Meyco sada plochých štětců syntetické č. 12 16 20';
  return {l1:p.l1||'',h1:p.h1||'Kategorie.dc.html',l2:p.l2||'',h2:p.h2||'Kategorie.dc.html',hasL1:!!p.l1,hasL2:!!p.l2,
   current:c.length>60?c.slice(0,59)+'…':c};}
}""", 800, 48, {"l1": {"editor": "text", "default": "Štětce a pomůcky"}, "h1": {"editor": None}, "l2": {"editor": None}, "h2": {"editor": None}, "current": {"editor": "text", "default": "Sady štětců"}})

# ---------------- Footer ----------------
links = [('Onas', 'O nás', 'buildings'), ('Kontakt', 'Kontakt', 'phone'), ('ObchodniPodminky', 'Obchodní podmínky', 'file-pdf'), ('Reklamace', 'Reklamace a vrácení', 'arrow-counter-clockwise'), ('Doprava', 'Doprava a platba', 'truck'), ('Spoluprace', 'Velkoobchodní spolupráce', 'storefront'), ('Gdpr', 'Ochrana osobních údajů', 'lock'), ('Kariera', 'Kariéra', 'user')]
buy = ''.join(f'<li><a href="{f}.dc.html">{I(i)}{t}</a></li>' for f, t, i in links[2:7])
comps['Footer'] = doc('Patička', CHEAD, """
.ft{--ft-accent:#e8a1a9;background:var(--footer-bg,#27272a);color:rgba(255,255,255,.88);""" + ROOTC.replace('color:var(--text,#18181b);', '') + """;font-size:var(--fs-body-sm,14px)}
.ftBs{display:inline-flex;align-items:center;gap:8px}.bsLogo{flex:none;width:20px;height:20px;display:block}
.ft a{color:#fff;text-decoration:none}.ft a:hover{color:#fff;text-decoration:underline}
.ftIn{width:min(var(--content-max,1560px),100% - 2*var(--gutter,24px));margin-inline:auto;padding:48px 0 24px}
.ftGrid{display:grid;grid-template-columns:minmax(0,440px) minmax(24px,1fr) minmax(0,240px) minmax(0,240px) minmax(0,300px);column-gap:40px;row-gap:32px}
.ftGrid>:nth-child(2){grid-column:3}.ftGrid>:nth-child(3){grid-column:4}.ftGrid>:nth-child(4){grid-column:5}
.ftCard{background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.14);border-radius:var(--card-radius,8px);padding:20px;display:flex;flex-direction:column;gap:10px}
@supports (corner-shape:squircle){.ftCard{corner-shape:var(--corner-shape,squircle)}}
.ftAv{position:relative;width:64px;height:64px;border-radius:50%;background:rgba(155,65,75,.45);color:#fff;display:flex;align-items:center;justify-content:center}
@supports (corner-shape:squircle){.ftAv{corner-shape:squircle}}
.ftAv .ic{width:32px;height:32px}
.ftDot{position:absolute;right:2px;bottom:2px;width:14px;height:14px;border-radius:50%;border:2px solid var(--footer-bg,#27272a);background:#a1a1aa}
.ftDot.on{background:#22c55e;animation:pu 2s infinite}
@keyframes pu{50%{box-shadow:0 0 0 6px rgba(34,197,94,.25)}}
.ftCardHead{display:flex;gap:14px;align-items:center}
.ftCard h3{margin:0;font-size:18px;line-height:1.3;color:#fff;font-weight:700}
.ftSub{display:block;color:rgba(255,255,255,.64);font-size:13px;margin-top:2px}
.ftContacts{list-style:none;margin:6px 0 0;padding:0;display:flex;flex-direction:column;gap:14px}
.ftRow{display:flex;align-items:flex-start;gap:12px}
.ftRow>.ic{width:22px;height:22px;flex:none;color:var(--ft-accent);margin-top:1px}
.ftRow>div{display:flex;flex-direction:column;line-height:1.4;min-width:0}
.ftRow span{color:rgba(255,255,255,.64);font-size:13px}
.ftRow strong{color:#fff;font-weight:600}
.ftIds{margin-top:4px}
.ftTel{font-size:22px;font-weight:700;line-height:1.15}
.ftContacts .ftRow:first-child>.ic{margin-top:2px}
.ftCard{align-self:start}
.ftTel+span{margin-top:2px}
.ftMail{font-weight:600}
.ftBtn{display:inline-flex;align-items:center;justify-content:center;gap:8px;align-self:flex-start;min-height:44px;margin-top:8px;padding:0 20px;border-radius:var(--btn-radius,6px);background:var(--primary,#9b414b);color:#fff!important;font-weight:600;text-decoration:none!important;transition:background .15s}
.ftBtn:hover{background:var(--primary-d,#7f343d)}
.ftBtn .ic{width:18px;height:18px;transition:transform .15s}.ftBtn:hover .ic{transform:translateX(3px)}
.ftMore{display:inline-flex;align-items:center;gap:6px;margin-top:6px;color:var(--ft-accent)!important;font-weight:600}
.ftMore .ic{width:16px;height:16px;transition:transform .15s}
.ftMore:hover .ic{transform:translateX(3px)}
.ftStatus{font-size:13px}
.ftCol h3{margin:0 0 14px}
.ftAcc{display:flex;width:100%;align-items:center;justify-content:space-between;background:none;border:0;color:var(--ft-accent);font:inherit;font-weight:600;font-size:20px;line-height:1.3;letter-spacing:0;text-transform:none;padding:0;cursor:default}
.ftAcc .ic{display:none}
.ftList{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:2px}
.ftList a{display:flex;align-items:center;gap:12px;min-height:38px;color:rgba(255,255,255,.88)}
.ftList a:hover{color:#fff}
.ftList .ic{width:20px;height:20px;flex:none;color:var(--ft-accent)}
.hours{width:100%;border-collapse:collapse}
.hours td{padding:4px 8px}.hours td:last-child{text-align:right}
.hours tr.today{background:#fff;color:var(--footer-bg,#27272a);font-weight:700}
.ftAddr{margin:0 0 14px}
.ftBottom{display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap;border-top:1px solid rgba(255,255,255,.14);margin-top:32px;padding-top:16px;font-size:13px}
.ftBottom nav{display:flex;gap:16px}
.ftBs{display:flex;align-items:center;gap:6px}
.todo{background:rgba(255,247,214,.15);color:#ffe9a8;padding:0 4px;border-radius:2px}
@media (max-width:1349px){.ftGrid{grid-template-columns:minmax(0,1.3fr) repeat(3,minmax(0,1fr));column-gap:32px}.ftGrid>:nth-child(n){grid-column:auto}}
@media (max-width:1149px){.ftGrid{grid-template-columns:repeat(3,minmax(0,1fr))}.ftGrid>.ftCard{grid-column:1/-1}}
@media (max-width:999px){.ftGrid{grid-template-columns:repeat(2,minmax(0,1fr))}.ftGrid>:nth-child(n){grid-column:auto}}
@media (max-width:819px){.ftGrid{grid-template-columns:1fr;gap:0}.ftCard{margin-bottom:16px}
 .ftCol{border-bottom:1px solid rgba(255,255,255,.14)}.ftCol h3{margin:0}
 .ftAcc{min-height:52px;cursor:pointer}.ftAcc .ic{display:block}
 .ftCol:not(.open) .ftBody{display:none}.ftBody{padding-bottom:16px}}
@media (max-width:549px){.ftAv{width:48px;height:48px}.ftAv .ic{width:24px;height:24px}}
@media (prefers-reduced-motion:reduce){.ftDot.on{animation:none}}
""", f'''<footer class="ft FooterView"><div class="ftIn">
<div class="ftGrid">
<div class="ftCard">
<div class="ftCardHead"><div class="ftAv" aria-hidden="true">{I('headset')}</div><div><h3>Obchodní oddělení</h3><span class="ftSub">Poradíme s výběrem i velkoobchodní objednávkou</span></div></div>
<ul class="ftContacts">
<li class="ftRow">{I('phone')}<div><a class="ftTel" href="tel:+420775570418">+420 775 570 418</a><span>Po–Pá 9:00–16:00</span></div></li>
<li class="ftRow">{I('envelope')}<div><a class="ftMail" href="mailto:daver@daver.cz">daver@daver.cz</a><span>Objednávky, obchod i dotazy k sortimentu</span></div></li>
</ul>
<a class="ftBtn" href="Kontakt.dc.html">Všechny kontakty a oddělení{I('arrow-right')}</a>
</div>
<div class="{{{{ c2 }}}}"><h3><button class="ftAcc" type="button" aria-expanded="{{{{ e2 }}}}" onClick="{{{{ t2 }}}}">Vše o nákupu{I('caret-down')}</button></h3>
<div class="ftBody"><ul class="ftList">{buy}</ul></div></div>
<div class="{{{{ c3 }}}}"><h3><button class="ftAcc" type="button" aria-expanded="{{{{ e3 }}}}" onClick="{{{{ t3 }}}}">Firma{I('caret-down')}</button></h3>
<div class="ftBody"><ul class="ftList"><li><a href="Onas.dc.html">{I('buildings')}Informace o firmě</a></li><li><a href="Kariera.dc.html">{I('user')}Volné pracovní pozice</a></li><li><a href="Kontakt.dc.html">{I('phone')}Všechny kontakty</a></li><li><a href="#facebook">{I('facebook-logo')}Sledujte nás</a></li></ul></div></div>
<div class="{{{{ c4 }}}}"><h3><button class="ftAcc" type="button" aria-expanded="{{{{ e4 }}}}" onClick="{{{{ t4 }}}}">Sídlo{I('caret-down')}</button></h3>
<div class="ftBody"><div class="ftRow ftAddr">{I('map-pin')}<div><strong>DAVER, spol. s r.o.</strong><span>Piešťanská 2293/68<br>915 01 Nové Mesto nad Váhom</span><span class="ftIds">IČO 34149431 · IČ DPH SK2020381935</span><a class="ftMore" href="https://www.google.com/maps/search/?api=1&amp;query=Pie%C5%A1%C5%A5ansk%C3%A1+2293%2F68+Nov%C3%A9+Mesto+nad+V%C3%A1hom">Navigovat{I('arrow-right')}</a></div></div></div></div>
</div>
<div class="ftBottom"><span>© {{{{ year }}}} DAVER, spol. s r.o.</span><nav aria-label="Právní"><a href="Gdpr.dc.html">Cookies</a><a href="ObchodniPodminky.dc.html">Obchodní podmínky</a></nav><span class="ftBs"><svg class="bsLogo" width="20" height="20" aria-hidden="true" focusable="false" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M20.1228 5H2.00244V17.7249H20.1228V5Z" fill="white"/><path fill-rule="evenodd" clip-rule="evenodd" d="M4.7119 6.28384C5.47559 6.28384 6.09741 6.92694 6.09741 7.719C6.09741 8.51105 5.47795 9.15415 4.7119 9.15415C3.94586 9.15415 3.3264 8.51105 3.3264 7.719C3.3264 6.92694 3.94586 6.28384 4.7119 6.28384ZM2.00236 13.1357V5H12.5142C11.1713 6.5912 9.97021 8.20132 8.65327 10.0597C7.93214 11.0764 8.16858 10.8707 6.96749 11.3246C6.52536 11.4925 3.50136 12.5399 2 13.1333L2.00236 13.1357ZM19.9856 5C21.0945 5 22 5.90554 22 7.01442V17.985C22 19.0939 21.0945 19.9994 19.9856 19.9994H4.01679C2.90791 19.9994 2.00236 19.0939 2.00236 17.985V13.9065C3.17272 13.5566 6.06667 12.6605 6.94621 12.4666C7.02896 12.4477 7.02896 12.5068 7.01241 12.5375C6.65067 13.1759 5.62218 14.8026 5.51105 15.8831C5.44012 16.5546 5.77586 17.3111 6.48753 17.4554C7.16137 17.5901 7.96052 17.1622 8.53505 16.8454C9.71486 16.1952 13.9778 13.358 14.5405 12.2396C14.5807 12.4501 14.8455 12.6605 15.3751 12.7976C15.6754 12.8756 16.2097 12.9111 16.484 12.9868C16.666 13.0364 16.7866 13.1546 16.8008 13.3249C16.8339 13.7221 15.8172 14.0673 15.4768 14.1926C14.7793 14.4527 13.9849 14.7175 13.3441 15.0958C13.0202 15.2873 12.9067 15.7341 13.1952 16.0131C13.4647 16.2732 14.0369 16.1266 14.3561 16.051C15.4839 15.7767 17.5716 14.9444 18.3376 14.0578C18.8223 13.4951 19.0067 12.6368 18.392 12.0883C17.6993 11.4712 16.7039 11.5682 16.4958 11.3175C15.978 10.6933 17.7513 10.1661 18.4795 10.0479C19.0398 9.95803 19.8224 10.01 19.969 9.44733C20.0943 8.96264 19.5624 8.82788 19.1557 8.78295C17.8175 8.634 16.1341 9.05012 14.9944 10.2063C14.8006 10.4025 14.6942 10.5822 14.5972 10.7974C14.0771 9.3504 10.6724 10.3647 10.5542 10.1235C10.4194 9.80435 12.266 7.18229 13.8619 5.00236H19.9927L19.9856 5ZM10.5093 11.762C10.9325 11.6604 11.961 11.4712 12.3416 11.7076C13.382 12.3508 9.91819 14.3297 9.42641 14.6323C7.96761 15.5237 7.43799 15.4882 8.37428 13.8166C8.90625 12.8993 9.41695 11.9583 10.5116 11.7644L10.5093 11.762Z" fill="#E30613"/></svg>BSSHOP: e-shop napojený na Pohodu</span></div>
</div></footer>''', r"""
/* Provozní doba – [DOPLNIT]; null = neznámá. Formát: [od,do] v hodinách pro Po..Ne */
const HOURS=null;
const DAYS=['Pondělí','Úterý','Středa','Čtvrtek','Pátek','Sobota','Neděle'];
class Component extends DCLogic {
 constructor(p){super(p);this.state={now:new Date(),open:0};}
 componentDidMount(){this.iv=setInterval(()=>this.setState({now:new Date()}),30000);}
 componentWillUnmount(){clearInterval(this.iv);}
 renderVals(){
  const n=this.state.now; const di=(n.getDay()+6)%7; const o=this.state.open;
  let status='Provozní doba: [DOPLNIT]', on=false;
  if(HOURS){const h=HOURS[di]; const t=n.getHours()+n.getMinutes()/60; on=!!h&&t>=h[0]&&t<h[1];
   status=on?('Online · volejte, jsme tu do '+h[1]+':00'):'Offline · ozveme se v pracovní době';}
  const tg=(i)=>()=>this.setState({open:o===i?0:i});
  return {status:status, dotCls:'ftDot'+(on?' on':''), year:n.getFullYear(),
   days:DAYS.map((d,i)=>({n:d,h:HOURS?(HOURS[i]?HOURS[i][0]+':00–'+HOURS[i][1]+':00':'zavřeno'):'[DOPLNIT]',cls:i===di?'today':''})),
   c1:'ftCol'+(o===1?' open':''),c2:'ftCol'+(o===2?' open':''),c3:'ftCol'+(o===3?' open':''),c4:'ftCol'+(o===4?' open':''),
   e1:o===1?'true':'false',e2:o===2?'true':'false',e3:o===3?'true':'false',e4:o===4?'true':'false',t1:tg(1),t2:tg(2),t3:tg(3),t4:tg(4)};
 }
}""", 1440, 600)

# ---------------- CookieModal ----------------
comps['CookieModal'] = doc('Souhlas s cookies', CHEAD, """
.ck{width:640px;max-width:100%;background:#fff;border-radius:var(--radius-lg,8px);padding:24px;""" + ROOTC + """}
.ckHead{display:flex;gap:12px;align-items:center;margin-bottom:8px}.ckHead .ic{width:32px;height:32px}
.ck h2{margin:0;font-size:20px}.ck p{margin:0 0 16px;color:var(--text-weaker,rgba(24,24,27,.68))}
.ck a{color:var(--primary-d,#27272a)}
.ckSet{border:1px solid var(--line,#e4e4e7);border-radius:var(--radius-md,6px);margin-bottom:16px}
.ckRow{display:flex;justify-content:space-between;align-items:center;gap:12px;padding:10px 14px;border-bottom:1px solid var(--line,#e4e4e7);min-height:52px}
.ckRow:last-child{border-bottom:0}.ckRow small{display:block;color:var(--text-weaker,rgba(24,24,27,.68));font-size:12px}
.ckRow input{width:40px;height:22px;accent-color:var(--primary-d,#27272a)}
.ckAct{display:flex;gap:8px;flex-wrap:wrap;justify-content:flex-end}
.ckAct .first{margin-right:auto}
@media (max-width:600px){.ckAct{flex-direction:column}.ckAct .btn{width:100%}.ckAct .first{margin:0}}
""" + btn('.ck'), f'''<div class="ck" role="dialog" aria-modal="true" aria-labelledby="ckT">
<div class="ckHead">{I('cookie')}<h2 id="ckT">Na vašem soukromí nám záleží</h2></div>
<p>Cookies používáme k fungování e-shopu, měření návštěvnosti a marketingu. Podrobnosti najdete v <a href="Gdpr.dc.html">zásadách ochrany osobních údajů</a>.</p>
<sc-if value="{{{{ detail }}}}" hint-placeholder-val="{{{{ false }}}}">
<div class="ckSet">
<label class="ckRow"><span><strong>Nezbytné</strong><small>Vždy aktivní – košík, přihlášení</small></span><input type="checkbox" checked="{{{{ true }}}}" disabled="{{{{ true }}}}"></label>
<label class="ckRow"><span><strong>Analytické</strong><small>Měření návštěvnosti</small></span><input type="checkbox" checked="{{{{ an }}}}" onChange="{{{{ tAn }}}}"></label>
<label class="ckRow"><span><strong>Marketingové</strong><small>Personalizovaná reklama</small></span><input type="checkbox" checked="{{{{ mk }}}}" onChange="{{{{ tMk }}}}"></label>
</div>
</sc-if>
<div class="ckAct">
<button class="btn btn-out first" type="button" aria-expanded="{{{{ detail }}}}" onClick="{{{{ tDetail }}}}">Podrobné nastavení</button>
<sc-if value="{{{{ noDetail }}}}" hint-placeholder-val="{{{{ true }}}}"><button class="btn btn-out" type="button" onClick="{{{{ onlyNec }}}}">Pouze nezbytné</button></sc-if>
<sc-if value="{{{{ detail }}}}" hint-placeholder-val="{{{{ false }}}}"><button class="btn btn-out" type="button" onClick="{{{{ save }}}}">Uložit výběr</button></sc-if>
<button class="btn btn-main" type="button" onClick="{{{{ all }}}}">Povolit vše</button>
</div>
</div>''', r"""
class Component extends DCLogic {
 constructor(p){super(p);this.state={detail:false,an:false,mk:false};}
 done(a,m){if(this.props.onDone)this.props.onDone({analytics:a,marketing:m});}
 renderVals(){const s=this.state;
  return {detail:s.detail,noDetail:!s.detail,an:s.an,mk:s.mk,
   tDetail:()=>this.setState({detail:!s.detail}),tAn:()=>this.setState({an:!s.an}),tMk:()=>this.setState({mk:!s.mk}),
   onlyNec:()=>this.done(false,false),save:()=>this.done(s.an,s.mk),all:()=>this.done(true,true)};}
}""", 640, 330, {"onDone": {"editor": None}})

# ---------------- PromoModal ----------------
comps['PromoModal'] = doc('Akční modal', CHEAD, """
.pm{width:560px;max-width:100%;background:#fff;border-radius:var(--radius-lg,8px);overflow:hidden;position:relative;""" + ROOTC + """}
.pmImg{height:220px;border:0;border-radius:0}
.pmBody{padding:24px;display:flex;flex-direction:column;gap:12px}
.pmTag{align-self:flex-start;background:var(--flag-akce,#c2410c);color:#fff;font-size:12px;font-weight:700;padding:2px 8px;border-radius:2px}
.pm h2{margin:0;font-size:24px}.pm p{margin:0;color:var(--text-weaker,rgba(24,24,27,.68))}
.pmHi{display:flex;gap:12px;align-items:center;border:1px solid var(--line,#e4e4e7);border-radius:var(--radius-md,6px);padding:12px;font-weight:600}
.pmNote{font-size:12px}
.pmAct{display:flex;gap:16px;align-items:center;flex-wrap:wrap}
.pmAct a.lnk{color:var(--primary-d,#27272a)}
.pmClose{position:absolute;top:8px;right:8px;background:#fff!important}
""" + btn('.pm'), f'''<div class="pm" role="dialog" aria-modal="true" aria-labelledby="pmT">
<button class="iconBtn pmClose" type="button" aria-label="Zavřít" onClick="{{{{ close }}}}">{I('x')}</button>
<sc-if value="{{{{ image }}}}" hint-placeholder-val="{{{{ true }}}}"><div class="ph pmImg">[FOTO: akční vizuál]</div></sc-if>
<div class="pmBody">
<span class="pmTag">Akce</span>
<h2 id="pmT">Sleva 10 % na vybrané produkty Jovi</h2>
<p>Plastelíny, fixy, voskovky a modelovací hmoty Jovi se slevou 10 % do 31. 12. 2026.</p>
<div class="pmHi">{I('tag')}<span>Akční produkty najdete v kategorii Akce</span></div>
<p class="pmNote">Sleva platí pro přihlášené B2B zákazníky a nelze ji kombinovat s jinými akcemi.</p>
<div class="pmAct"><a class="btn btn-main" href="Kategorie.dc.html">Nakupovat</a><a class="lnk" href="Doprava.dc.html">Podmínky dopravy</a></div>
</div></div>''', r"""
class Component extends DCLogic {
 renderVals(){return {image:this.props.image??true, close:()=>{if(this.props.onClose)this.props.onClose();}};}
}""", 560, 620, {"image": {"editor": "boolean", "default": True}, "onClose": {"editor": None}})

# ---------------- FontSizeSwitch ----------------
comps['FontSizeSwitch'] = doc('Prezentační přepínač', CHEAD, """
.fss{position:fixed;left:16px;bottom:16px;z-index:2600;""" + ROOTC + """;font-size:13px}
.fssBtn{display:flex;align-items:center;justify-content:center;width:44px;height:44px;padding:0;border-radius:var(--btn-radius,12px);border:1px solid var(--line,#e4e4e7);background:#fff;box-shadow:0 6px 18px rgba(0,0,0,.14);cursor:pointer;color:var(--text,#18181b);transition:transform .15s,border-color .2s}
.fssBtn:hover{border-color:var(--primary-d,#7f343d)}.fssBtn:active{transform:scale(.94)}
.fssBtn .ic{width:22px;height:22px}
.fssHide{display:flex;align-items:center;gap:8px;width:100%;min-height:40px;margin-top:4px;padding:8px 10px;border:0;border-top:1px solid var(--line,#e4e4e7);background:none;color:var(--text-weaker,rgba(24,24,27,.68));font:inherit;font-size:13px;text-align:left;cursor:pointer;border-radius:0}
.fssHide:hover{color:var(--primary-d,#7f343d)}
.fssHide .ic{width:18px;height:18px;flex:none}
.fssBtn[aria-expanded="true"]{background:var(--primary,#9b414b);border-color:var(--primary,#9b414b);color:#fff}
.fssMenu{position:absolute;left:0;bottom:calc(100% + 8px);width:280px;background:#fff;border:1px solid var(--line,#e4e4e7);border-radius:var(--radius-lg,8px);box-shadow:0 12px 28px rgba(0,0,0,.16);padding:12px}
.fssMenu fieldset{border:0;margin:0 0 8px;padding:0}
.fssMenu legend{font-weight:700;font-size:12px;text-transform:uppercase;letter-spacing:.05em;color:var(--text-weaker,rgba(24,24,27,.68));margin-bottom:4px}
.fssMenu label{display:flex;align-items:center;gap:8px;min-height:40px;cursor:pointer}
.fssMenu input{accent-color:var(--primary-d,#27272a);width:18px;height:18px}
""", f'''<sc-if value="{{{{ shown }}}}" hint-placeholder-val="{{{{ true }}}}"><div class="fss" onKeyDown="{{{{ onKey }}}}">
<sc-if value="{{{{ open }}}}" hint-placeholder-val="{{{{ false }}}}">
<div class="fssMenu" role="dialog" aria-label="Nastavení prezentace">
<fieldset><legend>Velikost písma na celém webu</legend>
<label><input type="radio" name="fssF" checked="{{{{ std }}}}" onChange="{{{{ setStd }}}}">Standardní</label>
<label><input type="radio" name="fssF" checked="{{{{ big }}}}" onChange="{{{{ setBig }}}}">Velké (× 1,125)</label></fieldset>
<fieldset><legend>Zákazník</legend>
<label><input type="radio" name="fssA" checked="{{{{ out }}}}" onChange="{{{{ setOut }}}}">Nepřihlášen</label>
<label><input type="radio" name="fssA" checked="{{{{ inn }}}}" onChange="{{{{ setIn }}}}">Přihlášen (Jan Novák · Velkoobchod)</label></fieldset>
<fieldset><legend>Výběr varianty na detailu</legend>
<label><input type="radio" name="fssV" checked="{{{{ vSel }}}}" onChange="{{{{ setVSel }}}}">Rozbalovací seznam</label>
<label><input type="radio" name="fssV" checked="{{{{ vSw }}}}" onChange="{{{{ setVSw }}}}">Barevné vzorky</label></fieldset>
<button class="fssHide" type="button" onClick="{{{{ hide }}}}">{I('eye-slash')}Skrýt panel (vrátí se po obnovení stránky)</button>
</div>
</sc-if>
<button class="fssBtn" type="button" aria-expanded="{{{{ open }}}}" aria-label="{{{{ aria }}}}" title="{{{{ aria }}}}" onClick="{{{{ toggle }}}}">{I('text-aa')}</button>
</div></sc-if>''', r"""
const lsGet=(k)=>{try{return localStorage.getItem('daver'+k)}catch(e){return null}};
const lsSet=(k,v)=>{try{localStorage.setItem('daver'+k,v)}catch(e){}};
class Component extends DCLogic {
 constructor(p){super(p);this.state={open:false,big:false,auth:false,vui:'select',hidden:false};
  this.onAuth=()=>this.setState({auth:lsGet('AuthV1')==='in'});}
 componentDidMount(){
  const big=lsGet('FontSizeV1')==='big'; this.setState({big:big,vui:lsGet('VariantUiV1')||'select'}); this.onAuth();
  window.addEventListener('daver-auth',this.onAuth); window.addEventListener('storage',this.onAuth);
  this.mo=new MutationObserver((ms)=>{if(!this.state.big)return; ms.forEach((m)=>m.addedNodes.forEach((n)=>{if(n.nodeType===1)this.scale(n);}));});
  this.mo.observe(document.body,{childList:true,subtree:true});
  if(big)setTimeout(()=>this.apply(true),50);
 }
 componentWillUnmount(){window.removeEventListener('daver-auth',this.onAuth);window.removeEventListener('storage',this.onAuth);if(this.mo)this.mo.disconnect();}
 scale(root){
  const els=[root].concat(Array.from(root.querySelectorAll('*')));
  els.forEach((el)=>{if(el.dataset.fsOrig||el.closest('.fss'))return;
   const fs=parseFloat(getComputedStyle(el).fontSize); if(!fs)return;
   el.dataset.fsOrig=String(fs); el.dataset.fsInline=el.style.fontSize||'';});
  els.forEach((el)=>{if(el.dataset.fsOrig&&!el.dataset.fsDone){el.style.fontSize=Math.round(parseFloat(el.dataset.fsOrig)*1.125)+'px';el.dataset.fsDone='1';}});
 }
 apply(big){
  if(big){this.scale(document.body);}
  else{document.querySelectorAll('[data-fs-orig]').forEach((el)=>{el.style.fontSize=el.dataset.fsInline||'';delete el.dataset.fsOrig;delete el.dataset.fsInline;delete el.dataset.fsDone;});}
 }
 setBig(b){lsSet('FontSizeV1',b?'big':'std');this.setState({big:b});this.apply(b);}
 setVui(v){lsSet('VariantUiV1',v);window.dispatchEvent(new Event('daver-variant'));this.setState({vui:v});}
 setAuth(a){lsSet('AuthV1',a?'in':'out');window.dispatchEvent(new Event('daver-auth'));this.setState({auth:a});}
 renderVals(){const s=this.state;
  return {open:s.open,std:!s.big,big:s.big,out:!s.auth,inn:s.auth,
   shown:!s.hidden,hide:()=>this.setState({hidden:true,open:false}),aria:'Nastavení prezentace: '+(s.big?'velké písmo':'standardní písmo')+', '+(s.auth?'přihlášen':'nepřihlášen'),
   toggle:()=>this.setState({open:!s.open}), onKey:(e)=>{if(e.key==='Escape'&&s.open){e.stopPropagation();this.setState({open:false});}},
   vSel:s.vui!=='swatch',vSw:s.vui==='swatch',setVSel:()=>this.setVui('select'),setVSw:()=>this.setVui('swatch'),setStd:()=>this.setBig(false),setBig:()=>this.setBig(true),setOut:()=>this.setAuth(false),setIn:()=>this.setAuth(true)};}
}""", 300, 440)

if __name__ == '__main__':
    for n, c in comps.items():
        write(n + '.dc.html', c.replace('></input>', '>'))
    print(list(comps))

# ---------------- BrandStrip – pás log výrobců ----------------
BRANDS = ['Knorr Prandell', 'Jovi', 'Talens', 'Royal & Langnickel', 'Pebeo', 'Meyco', 'Sizzix', 'Van Gogh', 'Darwi', 'Sakura', 'Cernit', 'Golden', 'Docrafts', 'Amsterdam', 'Essdee', 'Rembrandt', 'Clairefontaine', 'Ecoline', 'Leane Creatief', 'Bruynzeel', 'Efco', 'Cobra']
comps['BrandStrip'] = doc('Pás log výrobců', CHEAD, """
.bs{""" + ROOTC + """;width:100%}
.bsHead{display:flex;justify-content:space-between;align-items:center;gap:16px;flex-wrap:wrap;margin-bottom:12px}
.bsHead h2{margin:0;font-size:var(--fs-h2,24px);line-height:1.2}
.bsHead a{color:var(--primary-d,#27272a);font-size:var(--fs-body-sm,14px)}
.bsNav{display:flex;gap:8px;align-items:center}
.bsNav .iconBtn{border:1px solid var(--line,#e4e4e7);background:#fff;border-radius:var(--btn-radius,6px);box-shadow:0 1px 3px rgba(0,0,0,.08)}
.bsNav .iconBtn:hover{background:var(--primary-10,#f4f4f5)}
.bsViewport{position:relative}
.bsViewport::before,.bsViewport::after{content:"";position:absolute;top:0;bottom:0;width:96px;z-index:1;pointer-events:none}
.bsViewport::before{left:0;background:linear-gradient(90deg,var(--bs-bg,var(--bg-soft,#f8f8f8)) 10%,transparent)}
.bsViewport::after{right:0;background:linear-gradient(270deg,var(--bs-bg,var(--bg-soft,#f8f8f8)) 10%,transparent)}
.bsTrack{display:flex;gap:16px;overflow-x:auto;scrollbar-width:none;padding:16px 0;overscroll-behavior-x:contain;-webkit-overflow-scrolling:touch}
.bsTrack::-webkit-scrollbar{display:none}
.bsItem{flex:none;display:flex;align-items:center;justify-content:center;width:168px;height:80px;border-radius:var(--card-radius,8px);text-decoration:none;color:var(--text-weaker,rgba(24,24,27,.68))}
.bsItem{background:transparent}
/* logo: jednobarevné, po najetí v barvě */
.bsItem img{max-width:136px;max-height:56px;object-fit:contain;mix-blend-mode:multiply;filter:grayscale(1);opacity:.65;transition:filter .3s,opacity .3s,transform .3s}
.bsItem:hover img,.bsItem:focus-visible img{filter:none;opacity:1;transform:scale(1.06)}
/* placeholder do doby, než přijdou loga */
.bsPh{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:2px;width:136px;height:56px;border:1px dashed var(--input-border,#d4d4d8);border-radius:var(--radius-sm,4px);font-weight:700;font-size:13px;letter-spacing:.02em;text-transform:uppercase;text-align:center;line-height:1.15;color:#71717a;transition:color .3s,border-color .3s}
.bsPh small{font-weight:400;font-size:10px;text-transform:none;letter-spacing:0}
.bsItem:hover .bsPh{color:var(--text,#18181b);border-color:var(--primary-d,#27272a)}
@supports (corner-shape:squircle){.bsItem{corner-shape:var(--corner-shape,squircle)}}
@media (max-width:549px){.bsItem{width:136px;height:68px}.bsPh{width:116px;height:48px;font-size:12px}}
@media (prefers-reduced-motion:reduce){.bsItem img,.bsPh{transition:none}}
""" + btn('.bs'), f'''<section class="bs BrandsView" aria-labelledby="bsT" onMouseEnter="{{{{ hoverIn }}}}" onMouseLeave="{{{{ hoverOut }}}}" onFocus="{{{{ hoverIn }}}}" onBlur="{{{{ hoverOut }}}}">
<div class="bsHead"><h2 id="bsT">Naši výrobci</h2>
<div class="bsNav"><a href="#vyrobci">Všichni výrobci (43)</a>

<button class="iconBtn" type="button" aria-label="Předchozí výrobci" onClick="{{{{ prev }}}}" data-arrow="1">{I('caret-left')}</button>
<button class="iconBtn" type="button" aria-label="Další výrobci" onClick="{{{{ next }}}}">{I('caret-right')}</button></div></div>
<div class="bsViewport"><div class="bsTrack" data-bs="1" onTouchStart="{{{{ touch }}}}">
<sc-for list="{{{{ items }}}}" as="b" hint-placeholder-count="8">
<a class="bsItem" href="{{{{ b.href }}}}" aria-label="{{{{ b.label }}}}" aria-hidden="{{{{ b.hidden }}}}" tabIndex="{{{{ b.tab }}}}">
<sc-if value="{{{{ b.hasLogo }}}}" hint-placeholder-val="{{{{ false }}}}"><img src="{{{{ b.logo }}}}" alt=""></sc-if>
<sc-if value="{{{{ b.noLogo }}}}" hint-placeholder-val="{{{{ true }}}}"><span class="bsPh">{{{{ b.n }}}}<small>[LOGO]</small></span></sc-if>
</a>
</sc-for>
</div></div>
</section>''', r"""
/* Loga se doplní do LOGOS (url /_blob/… podle manifestu). Prázdné = placeholder. */
const BRANDS=""" + json.dumps(BRANDS, ensure_ascii=False) + r""";
const LOGOS_ALL={"Knorr Prandell": "/_blob/7964e46b49bbe85310209b3fb6f2513e", "Pebeo": "/_blob/4564541216b3ed637265a552e481d40e", "Sizzix": "/_blob/bfc375c97a273c5cd56246133ff4265d", "Sakura": "/_blob/176e0540b5a76461c64685b57d248184", "Talens": "/_blob/35823966a4225b2c1a54ebf7cd4bc2a1", "Golden": "/_blob/fbf4acd183155c752611ed204980f731", "Amsterdam": "/_blob/58683c1b00625d986f7d587a0b2be9c3", "Bruynzeel": "/_blob/a495b657fd3ddbf49c0732e7e7fd2d85", "Cobra": "/_blob/29d6a75d9d3c15b4af2df847b53673fb", "Ecoline": "/_blob/fefbb421e9f34b50bc836e15d1c45214", "Rembrandt": "/_blob/a2896ae5939161b84d53b7272a85f44d", "Van Gogh": "/_blob/5699b57ecb87decc4bd919a81ac77301"};
const LOGOS=LOGOS_ALL;
class Component extends DCLogic {
 constructor(p){super(p);this.state={hover:false,manual:false,playing:true};this.pos=0;this.last=0;
  this.tick=(ts)=>{this.raf=requestAnimationFrame(this.tick);const t=this.track();const dt=this.last?Math.min(64,ts-this.last):0;this.last=ts;
   if(!t||!this.state.playing||this.state.hover||this.state.manual||this.reduced)return;
   if(Math.abs(t.scrollLeft-this.pos)>2)this.pos=t.scrollLeft;
   const half=t.scrollWidth/2; this.pos+=(this.props.speed||14)*dt/1000; if(this.pos>=half)this.pos-=half;
   t.scrollLeft=this.pos;};}
 track(){return this.root||(this.root=document.querySelector('[data-bs="1"]'));}
 componentDidMount(){this.reduced=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;if(this.reduced)this.setState({playing:false});this.raf=requestAnimationFrame(this.tick);}
 componentWillUnmount(){cancelAnimationFrame(this.raf);clearTimeout(this.mt);}
 pauseFor(ms){this.setState({manual:true});clearTimeout(this.mt);this.mt=setTimeout(()=>{const t=this.track();if(t)this.pos=t.scrollLeft;this.setState({manual:false});},ms);}
 move(d){const t=this.track();if(!t)return;this.pauseFor(4000);const half=t.scrollWidth/2;
  if(d<0&&t.scrollLeft<t.clientWidth){t.scrollLeft+=half;}
  t.scrollBy({left:d*t.clientWidth*0.6,behavior:'smooth'});}
 renderVals(){const s=this.state; const list=(this.props.brands||BRANDS).filter((n)=>LOGOS[n]).map((n)=>({n:n,logo:LOGOS[n]}));
  const items=list.concat(list).map((b,i)=>({n:b.n,logo:b.logo,hasLogo:!!b.logo,noLogo:!b.logo,label:'Výrobce '+b.n,href:'Kategorie.dc.html',
   hidden:i>=list.length?'true':'false',tab:i>=list.length?-1:0}));
  return {items:items,hoverIn:()=>this.setState({hover:true}),hoverOut:()=>this.setState({hover:false}),
   prev:()=>this.move(-1),next:()=>this.move(1),touch:()=>this.pauseFor(5000)};}
}""", 1440, 200, {"speed": {"editor": "range", "min": 4, "max": 40, "step": 1, "unit": "px/s", "default": 14}, "brands": {"editor": None}})


# ---------------- QuickView – rychlý náhled produktu z výpisu ----------------
comps['QuickView'] = doc('Rychlý náhled produktu', CHEAD, """
.qv{position:relative;width:960px;max-width:100%;background:#fff;border-radius:var(--radius-lg,8px);padding:28px;""" + ROOTC + """}
.qvClose{position:absolute;top:12px;right:12px}
.qv h2{margin:0 48px 20px 0;font-size:var(--fs-h3,22px);line-height:1.25}
.qvGrid{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:32px;align-items:start}
.qvImg{position:relative;aspect-ratio:1/1;display:flex;align-items:center;justify-content:center;background:#fff;border:1px solid var(--line,#e4e4e7);border-radius:var(--card-radius,8px);padding:24px}
.qvImg img{max-width:100%;max-height:100%;object-fit:contain}
.qvImg .ph{width:100%;height:100%}
.qvFlags{position:absolute;top:12px;left:12px;display:flex;flex-direction:column;gap:4px;align-items:flex-start}
.qvFlag{font-size:13px;font-weight:700;padding:3px 10px;border-radius:var(--radius-xs,2px);color:#fff}
.qvFlag.discount{background:var(--flag-discount,#ffc107);color:var(--flag-discount-fg,#1e1e1e)}
.qvFlag.flag00{background:var(--flag-novinka,#0277bd)}.qvFlag.flag01{background:var(--flag-akce,#c2410c)}.qvFlag.flag02{background:var(--flag-doporucujeme,#1f6fa8)}.qvFlag.flag03{background:var(--flag-vyprodej,#3867d6)}
.qvSide{display:flex;flex-direction:column;gap:16px}
.qvOld{font-size:var(--fs-body-sm,14px);color:var(--text-weaker,rgba(24,24,27,.68))}
.qvOld s{margin:0 4px}.qvOld strong{color:var(--text,#18181b)}
.qvPrice{font-size:30px;font-weight:700;line-height:1.1}.qvPrice small{font-size:var(--fs-body-sm,14px);font-weight:400;color:var(--text-weaker,rgba(24,24,27,.68))}
.qvVat{font-size:var(--fs-caption,12px);color:var(--text-weaker,rgba(24,24,27,.68));margin-top:2px}
.qvVar{font-size:var(--fs-caption,12px);color:var(--text-weaker,rgba(24,24,27,.68));margin-top:6px}
.qvBuy{display:flex;gap:10px}
.qvBuy .btn{flex:1;min-height:var(--btn-h-lg,56px)}
.qty{display:flex;align-items:center;min-width:132px;border:1px solid var(--input-border,#d4d4d8);border-radius:var(--btn-radius,4px);background:#fff}
.qty button{width:40px;height:100%;border:0;background:none;font-size:18px;cursor:pointer;color:inherit}
.qty button:disabled{color:#c4c4c8;cursor:not-allowed}
.qty label{flex:1;display:flex;align-items:center;justify-content:center;gap:4px;padding:0 4px;white-space:nowrap}
.qty input{field-sizing:content;width:auto;min-width:1ch;max-width:6ch;border:0;outline:0;text-align:center;font:inherit;padding:0;background:transparent}
.qvAv{border:1px solid var(--line,#e4e4e7);border-radius:var(--card-radius,8px);padding:14px 16px;font-size:var(--fs-body-sm,14px);display:flex;flex-direction:column;gap:6px}
.qvAvHead{display:flex;justify-content:space-between;gap:12px;font-weight:600}
.qvAvHead .ok{color:var(--success-text,#15803d)}.qvAvHead .blue{color:var(--info,#1f6fa8)}
.qvAv .q{font-weight:600;margin-top:4px}
.qvRow{display:flex;justify-content:space-between;gap:12px;color:var(--text-weaker,rgba(24,24,27,.68))}.qvRow strong{color:var(--text,#18181b)}
.qvMeta{margin:0;display:flex;flex-direction:column;gap:6px;font-size:var(--fs-body-sm,14px)}
.qvMeta div{display:flex;justify-content:space-between;gap:12px;border-bottom:1px solid var(--line,#e4e4e7);padding-bottom:6px}
.qvMeta dt{color:var(--text-weaker,rgba(24,24,27,.68))}.qvMeta dd{margin:0;font-weight:600}
.qvDesc{margin:24px 0 0;padding-top:20px;border-top:1px solid var(--line,#e4e4e7);color:var(--text-weaker,rgba(24,24,27,.68));font-size:var(--fs-body-sm,14px);line-height:1.6}
.qvMore{display:inline-flex;align-items:center;gap:6px;margin-top:14px;align-self:flex-start;padding-right:14px;text-decoration:none}.qvMore .ic{width:18px;height:18px}
@supports (corner-shape:squircle){.qvImg,.qvAv{corner-shape:var(--corner-shape,squircle)}}
@media (max-width:719px){.qv{padding:20px}.qvGrid{grid-template-columns:1fr;gap:20px}.qvImg{aspect-ratio:4/3}}
""" + btn('.qv'), f'''<div class="qv ProductQuickView" role="dialog" aria-modal="true" aria-labelledby="qvT" onKeyDown="{{{{ onKey }}}}">
<button class="iconBtn qvClose" type="button" aria-label="Zavřít náhled" autoFocus="{{{{ true }}}}" onClick="{{{{ close }}}}">{I('x')}</button>
<h2 id="qvT">{{{{ name }}}}</h2>
<div class="qvGrid">
<div class="qvImg"><div class="qvFlags"><sc-for list="{{{{ flags }}}}" as="f" hint-placeholder-count="1"><span class="{{{{ f.cls }}}}">{{{{ f.t }}}}</span></sc-for></div>
<sc-if value="{{{{ hasImg }}}}" hint-placeholder-val="{{{{ true }}}}"><img src="{{{{ img }}}}" alt="{{{{ name }}}}"></sc-if><sc-if value="{{{{ noImg }}}}" hint-placeholder-val="{{{{ false }}}}"><div class="ph">[FOTO]</div></sc-if></div>
<div class="qvSide">
<div>
<sc-if value="{{{{ hasOld }}}}" hint-placeholder-val="{{{{ false }}}}"><div class="qvOld">Běžná cena<s>{{{{ oldTxt }}}}</s><strong>Ušetříte {{{{ saveTxt }}}}</strong></div></sc-if>
<div class="qvPrice">{{{{ price }}}} <small>bez DPH</small></div>
<div class="qvVat">{{{{ priceVat }}}} s DPH</div><sc-if value="{{{{ hasVar }}}}" hint-placeholder-val="{{{{ false }}}}"><div class="qvVar">{{{{ variants }}}}</div></sc-if>
</div>
<div class="qvAv AvailabilityView"><div class="qvAvHead"><span>Dostupnost</span><span class="{{{{ avCls }}}}">{{{{ av }}}}</span></div>
<sc-if value="{{{{ onStock }}}}" hint-placeholder-val="{{{{ true }}}}"><div class="q">Kdy zboží obdržím, pokud nyní objednám?</div><div class="qvRow"><span>Osobně na prodejně</span><strong>{{{{ pickup }}}}</strong></div><div class="qvRow"><span>Přepravní společností</span><strong>{{{{ delivery }}}}</strong></div></sc-if>
<sc-if value="{{{{ blue }}}}" hint-placeholder-val="{{{{ false }}}}"><div class="qvRow"><span>Naskladnění</span><strong>do 5 pracovních dnů</strong></div></sc-if></div>
<div class="qvBuy AddToCartView"><div class="qty"><button type="button" aria-label="Snížit množství" disabled="{{{{ minDis }}}}" onClick="{{{{ dec }}}}">−</button><label><input inputmode="numeric" aria-label="Množství" size="{{{{ qtyLen }}}}" value="{{{{ qty }}}}" onChange="{{{{ setQty }}}}">ks</label><button type="button" aria-label="Zvýšit množství" onClick="{{{{ inc }}}}">+</button></div>
<button class="btn btn-main" type="button" onClick="{{{{ add }}}}">{I('shopping-cart')}Koupit</button></div>
<dl class="qvMeta"><div><dt>Kód produktu</dt><dd>{{{{ code }}}}</dd></div><div><dt>Výrobce</dt><dd>{{{{ brand }}}}</dd></div></dl>
</div></div>
<p class="qvDesc">{{{{ desc }}}}</p>
<a class="btn btn-out qvMore" href="{{{{ href }}}}">Zobrazit detail produktu{I('caret-right')}</a>
</div>''', CZK_JS + r"""
const DEMO=__DEMO__;
class Component extends DCLogic {
 constructor(p){super(p);this.state={qty:1};}
 componentDidUpdate(prev){const a=prev.p&&prev.p.id,b=this.props.p&&this.props.p.id;if(a!==b)this.setState({qty:1});}
 renderVals(){
  const p=this.props.p||DEMO; const q=this.state.qty; const disc=(p.flags||[]).find((f)=>f.cls==='discount');
  const pct=disc?parseInt(disc.t.replace(/\D/g,''),10):0; const old=pct?p.price/(1-pct/100):0;
  const close=()=>{if(this.props.onClose)this.props.onClose();};
  const blue=p.stock===0;
  return {name:p.name,img:p.img||'',hasImg:!!p.img,noImg:!p.img,flags:(p.flags||[]).map((f)=>({t:f.t,cls:'qvFlag '+f.cls})),
   hasOld:!!pct,oldTxt:CZK(old),saveTxt:CZK(old-p.price)+' / '+pct+' %',price:(p.from?'od ':'')+CZK(p.price),priceVat:(p.from?'od ':'')+CZK(p.price*VAT),hasVar:!!p.variants,variants:p.variants||'',
   qty:q,qtyLen:Math.max(1,String(q).length),minDis:q<=1,dec:()=>this.setState({qty:Math.max(1,q-1)}),inc:()=>this.setState({qty:q+1}),
   setQty:(e)=>{const v=parseInt(e.target.value.replace(/\D/g,''),10);this.setState({qty:isNaN(v)?1:Math.max(1,v)});},
   add:()=>{if(this.props.onAdd)this.props.onAdd(p,q);},
   av:p.av||'',blue:blue,onStock:!blue,avCls:blue?'blue':'ok',pickup:this.props.pickup||'zítra',delivery:this.props.delivery||'pozítří',
   code:p.code||'',href:p.href||'Detail.dc.html',brand:(p.brand||'').toUpperCase(),desc:p.desc||'Kvalitní výtvarná potřeba z nabídky velkoobchodu Daver.',
   close:close,onKey:(e)=>{if(e.key==='Escape'){e.stopPropagation();close();}}};
 }
}""".replace('__DEMO__', json.dumps(dict(id=79,name=DQ['name'],code=DQ['code'],brand=DQ['brand'],price=DQ['price'],stock=DQ['stock'],av='Skladem > 30 ks',img=DQ['img'],flags=DQ['flags'],desc=DQ.get('desc','')),ensure_ascii=False)), 960, 640,
 {"p": {"editor": None}, "pickup": {"editor": None}, "delivery": {"editor": None}, "onAdd": {"editor": None}, "onClose": {"editor": None}})


# ---------------- Availability (skladovost) – velikost sm (karta) / lg (detail) ----------------
comps['Availability'] = doc('Skladovost', CHEAD, """
.avc{position:relative;display:inline-flex;""" + ROOTC + """}
.avcBtn{display:inline-flex;align-items:center;gap:6px;border:0;background:none;padding:0;font:inherit;font-weight:600;line-height:1.3;color:var(--success-text,#15803d);cursor:help;text-align:left}
.avc.blue .avcBtn{color:var(--info,#1f6fa8)}
.avcBtn .ic{flex:none}
.avc.sm .avcBtn{font-size:var(--fs-body-sm,14px)}.avc.sm .avcBtn .ic{width:16px;height:16px}
.avc.lg .avcBtn{font-size:var(--fs-body,16px);gap:8px}.avc.lg .avcBtn .ic{width:22px;height:22px}
.avcPop{display:none;position:absolute;bottom:calc(100% + 8px);left:0;width:260px;background:#fff;border:1px solid var(--line,#e4e4e7);border-radius:var(--radius-md,8px);box-shadow:0 8px 20px rgba(0,0,0,.12);padding:12px 14px;font-size:13px;font-weight:400;color:var(--text,#18181b);z-index:20}
.avc.lg .avcPop{font-size:14px;width:300px}
.avc:hover .avcPop,.avc:focus-within .avcPop{display:block}
.avcPop p{margin:0 0 6px;display:flex;gap:8px;align-items:center}.avcPop p .ic{width:16px;height:16px;color:var(--text-muted,#71717a)}
.avcPop a{color:var(--primary-d,#7f343d);font-weight:600}
@supports (corner-shape:squircle){.avcPop{border-radius:16px}}
""", f'''<div class="{{{{ cls }}}} AvailabilityView"><button class="avcBtn" type="button"><sc-if value="{{{{ ok }}}}" hint-placeholder-val="{{{{ true }}}}">{I('check-circle')}</sc-if><sc-if value="{{{{ blue }}}}" hint-placeholder-val="{{{{ false }}}}">{I('clock')}</sc-if><span>{{{{ text }}}}</span></button>
<div class="avcPop" role="tooltip"><sc-if value="{{{{ ok }}}}" hint-placeholder-val="{{{{ true }}}}"><p>{I('storefront')}<span>Osobní odběr: <strong>{{{{ pickup }}}}</strong></span></p><p>{I('truck')}<span>Doručení dopravcem: <strong>{{{{ delivery }}}}</strong></span></p></sc-if><sc-if value="{{{{ blue }}}}" hint-placeholder-val="{{{{ false }}}}"><p>{I('clock')}<span>Naskladníme do 5 pracovních dnů.</span></p></sc-if><a href="Doprava.dc.html">Doprava a platba</a></div></div>''', r"""
class Component extends DCLogic {
 renderVals(){const p=this.props; const st=(p.stock==null?26:Number(p.stock)); const blue=st<=0;
  const text=p.text||(blue?'Na objednávku':(st>5?'Skladem > '+(st>=100?Math.floor(st/50)*50:st)+' ks':'Skladem '+st+' ks'));
  return {cls:'avc '+(p.size==='lg'?'lg':'sm')+(blue?' blue':' ok'),ok:!blue,blue:blue,text:text,pickup:p.pickup||'zítra',delivery:p.delivery||'pozítří'};}
}""", 320, 40, {"stock": {"editor": "int", "default": 26}, "size": {"editor": "enum", "options": ["sm", "lg"], "default": "sm"}, "text": {"editor": None}, "pickup": {"editor": None}, "delivery": {"editor": None}})

# ---------------- Gallery (sdílená galerie detailu) ----------------
comps['Gallery'] = doc('Galerie produktu', CHEAD, """
.gv{position:relative;display:grid;grid-template-columns:minmax(0,1fr);width:100%;min-width:0;max-width:100%;""" + ROOTC + """}
.gv .gMain{position:relative;min-width:0}
.gv .gTrack{display:flex;overflow-x:auto;scroll-snap-type:x mandatory;scroll-behavior:smooth;scrollbar-width:none;border:1px solid var(--line,#e4e4e7);border-radius:var(--card-radius,8px);background:#fff;aspect-ratio:4/3;overscroll-behavior-x:contain}
.gv .gTrack::-webkit-scrollbar{display:none}
.gv .gSlide{flex:0 0 100%;scroll-snap-align:center;scroll-snap-stop:always;border:0;background:#fff;padding:0;cursor:zoom-in;display:flex;align-items:center;justify-content:center}
.gv .gSlide img{width:100%;height:100%;object-fit:contain;padding:24px}
.gv .gArr{position:absolute;top:50%;transform:translateY(-50%);z-index:3;display:inline-flex;align-items:center;justify-content:center;width:44px;height:44px;border:1px solid var(--line,#e4e4e7);border-radius:var(--btn-radius,6px);background:rgba(255,255,255,.92);color:var(--text,#18181b);box-shadow:0 2px 10px rgba(0,0,0,.12);cursor:pointer;transition:border-color .15s,color .15s}
.gv .gArr:hover{background:#fff;border-color:var(--primary-d,#7f343d);color:var(--primary-d,#7f343d)}
.gv .gArr .ic{width:22px;height:22px}.gv .gArr.l{left:12px}.gv .gArr.r{right:12px}
.gv .thumbs{position:absolute;top:12px;left:12px;z-index:2;display:flex;flex-direction:column;gap:8px;max-height:calc(100% - 24px)}
.gv .thumb{display:block;width:56px;height:56px;padding:4px;border:1px solid var(--line,#e4e4e7);border-radius:var(--radius-sm,4px);background:#fff;cursor:pointer;overflow:hidden;box-shadow:0 2px 8px rgba(0,0,0,.08);transition:transform .15s}
.gv .thumb:hover{transform:translateY(-2px)}.gv .thumb.on{outline:2px solid var(--primary-d,#7f343d);outline-offset:-2px}
.gv .thumb img{display:block;width:100%;height:100%;object-fit:contain}
.gv .chip{position:absolute;left:12px;bottom:12px;z-index:2;display:flex;align-items:center;gap:8px;background:rgba(255,255,255,.95);border:1px solid var(--line,#e4e4e7);border-radius:12px;padding:4px 12px 4px 4px;font-size:var(--fs-body-sm,14px);font-weight:600}
.gv .chipDot{width:28px;height:28px;border-radius:8px;border:1px solid rgba(0,0,0,.15)}
.gv .gDots{display:none;justify-content:center;align-items:center;gap:6px;padding-top:14px}
.gv .gDot{width:8px;height:8px;border-radius:999px;border:0;padding:0;background:var(--input-border,#d4d4d8);transition:width .3s cubic-bezier(.4,0,.2,1),background .3s;cursor:pointer}
.gv .gDot.on{width:24px;background:var(--primary,#9b414b)}
.gv .lb{position:fixed;inset:0;z-index:3500;background:rgba(9,9,11,.92);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:16px;padding:64px 16px 20px}
.gv .lbClose{position:absolute;top:16px;right:16px;display:inline-flex;align-items:center;justify-content:center;width:44px;height:44px;border:0;border-radius:var(--btn-radius,6px);background:transparent;color:#fff;cursor:pointer}
.gv .lbClose:hover{background:rgba(255,255,255,.12)}.gv .lbClose .ic{width:24px;height:24px}
.gv .lbStage{position:relative;display:flex;align-items:center;justify-content:center;gap:16px;flex:1;min-height:0;width:100%}
.gv .lbImg{width:min(80vw,1000px);height:100%;max-height:calc(100dvh - 220px);background:#fff;border-radius:var(--card-radius,8px);display:flex;align-items:center;justify-content:center;padding:24px}
.gv .lbImg img{max-width:100%;max-height:100%;object-fit:contain}
.gv .lbNav{flex:none;display:inline-flex;align-items:center;justify-content:center;width:44px;height:44px;border:1px solid rgba(255,255,255,.3);border-radius:var(--btn-radius,6px);background:rgba(255,255,255,.12);color:#fff;cursor:pointer}
.gv .lbNav:hover{background:rgba(255,255,255,.24)}.gv .lbNav .ic{width:22px;height:22px}
.gv .lbFoot{display:flex;flex-direction:column;align-items:center;gap:10px;max-width:100%}
.gv .lbNum{color:#fff;font-size:var(--fs-body-sm,14px)}
.gv .lbThumbs{display:flex;gap:10px;overflow-x:auto;scrollbar-width:none;max-width:100%;padding:2px}
.gv .lbThumbs::-webkit-scrollbar{display:none}
.gv .lbTh{flex:none;width:72px;height:72px;padding:4px;background:#fff;border:2px solid transparent;border-radius:var(--radius-sm,4px);cursor:pointer;opacity:.55;transition:opacity .2s,border-color .2s,transform .15s}
.gv .lbTh:hover{opacity:.85;transform:translateY(-2px)}.gv .lbTh.on{opacity:1;border-color:var(--primary,#9b414b)}
.gv .lbTh img{width:100%;height:100%;object-fit:contain}
@supports (corner-shape:squircle){.gv .chip{border-radius:18px}.gv .chipDot{border-radius:14px}}
@media (max-width:819px){.gv .thumbs{display:none}.gv .gArr{width:40px;height:40px}.gv .gArr.l{left:8px}.gv .gArr.r{right:8px}.gv .gDots{display:flex}
 .gv .lbStage{gap:0}.gv .lbNav{position:absolute;z-index:1}.gv .lbNav.l{left:4px}.gv .lbNav.r{right:4px}.gv .lbImg{width:100%}.gv .lbTh{width:56px;height:56px}}
@media (prefers-reduced-motion:reduce){.gv .gTrack{scroll-behavior:auto}.gv .gDot{transition:none}}
""", f'''<div class="gv GalleryView">
<div class="gMain"><div class="gTrack" onScroll="{{{{ gScroll }}}}" aria-label="Fotografie produktu"><sc-for list="{{{{ imgs }}}}" as="g" hint-placeholder-count="3"><button class="gSlide" type="button" aria-label="{{{{ g.label }}}}" onClick="{{{{ openLb }}}}"><img src="{{{{ g.img }}}}" alt="{{{{ g.alt }}}}" loading="lazy"></button></sc-for></div>
<sc-if value="{{{{ multi }}}}" hint-placeholder-val="{{{{ true }}}}"><button class="gArr l" type="button" aria-label="Předchozí fotografie" onClick="{{{{ prev }}}}">{I('caret-left')}</button><button class="gArr r" type="button" aria-label="Další fotografie" onClick="{{{{ next }}}}">{I('caret-right')}</button>
<div class="thumbs"><sc-for list="{{{{ imgs }}}}" as="g" hint-placeholder-count="3"><button class="{{{{ g.th }}}}" type="button" aria-label="{{{{ g.label }}}}" aria-current="{{{{ g.cur }}}}" onClick="{{{{ g.go }}}}"><img src="{{{{ g.img }}}}" alt=""></button></sc-for></div></sc-if>
<sc-if value="{{{{ hasChip }}}}" hint-placeholder-val="{{{{ false }}}}"><div class="chip" aria-live="polite"><span class="chipDot" style="background:{{{{ chipHex }}}}"></span><span>{{{{ chipText }}}}</span></div></sc-if>
</div>
<sc-if value="{{{{ multi }}}}" hint-placeholder-val="{{{{ true }}}}"><div class="gDots" aria-hidden="true"><sc-for list="{{{{ imgs }}}}" as="g" hint-placeholder-count="3"><button class="{{{{ g.dot }}}}" type="button" tabindex="-1" onClick="{{{{ g.go }}}}"></button></sc-for></div></sc-if>
<sc-if value="{{{{ lb }}}}" hint-placeholder-val="{{{{ false }}}}">
<div class="lb" role="dialog" aria-modal="true" aria-label="Galerie" onKeyDown="{{{{ lbKey }}}}">
<button class="lbClose" type="button" aria-label="Zavřít galerii" autoFocus="{{{{ true }}}}" onClick="{{{{ closeLb }}}}">{I('x')}</button>
<div class="lbStage"><sc-if value="{{{{ multi }}}}" hint-placeholder-val="{{{{ true }}}}"><button class="lbNav l" type="button" aria-label="Předchozí fotografie" onClick="{{{{ lbPrev }}}}">{I('caret-left')}</button></sc-if>
<div class="lbImg"><img src="{{{{ lbImg }}}}" alt="{{{{ lbAlt }}}}"></div>
<sc-if value="{{{{ multi }}}}" hint-placeholder-val="{{{{ true }}}}"><button class="lbNav r" type="button" aria-label="Další fotografie" onClick="{{{{ lbNext }}}}">{I('caret-right')}</button></sc-if></div>
<sc-if value="{{{{ multi }}}}" hint-placeholder-val="{{{{ true }}}}"><div class="lbFoot"><div class="lbNum" aria-live="polite">{{{{ lbNum }}}}</div>
<div class="lbThumbs"><sc-for list="{{{{ imgs }}}}" as="g" hint-placeholder-count="3"><button class="{{{{ g.lbTh }}}}" type="button" aria-label="{{{{ g.label }}}}" onClick="{{{{ g.lbGo }}}}"><img src="{{{{ g.img }}}}" alt=""></button></sc-for></div></div></sc-if>
</div>
</sc-if>
</div>''', r"""
const DEF=['/_blob/aee33865f02f71b834821c165a17deb0','/_blob/4b3e506c96fdac53c7b3749847e33b77','/_blob/76b5d08f4c869ef688374e069d43c347','/_blob/abc506dceb49e9689404cf98092e48f2'];
class Component extends DCLogic {
 constructor(p){super(p);this.state={gi:0,lb:false};}
 componentWillUnmount(){clearTimeout(this.st);}
 renderVals(){
  const s=this.state,p=this.props; const L=(p.imgs&&p.imgs.length)?p.imgs:DEF; const n=L.length; const alt=p.alt||'Fotografie produktu';
  const track=()=>{const r=this.base||document;return r.querySelector?r.querySelector('.gTrack'):null;};
  const go=(i,smooth)=>{i=(i+n)%n;const t=track();if(t)t.scrollTo({left:i*t.clientWidth,behavior:smooth===false?'auto':'smooth'});this.setState({gi:i});};
  const goFrom=(e,i)=>{const g=e&&e.currentTarget&&e.currentTarget.closest?e.currentTarget.closest('.gv'):null;const t=g&&g.querySelector('.gTrack');i=(i+n)%n;if(t)t.scrollTo({left:i*t.clientWidth,behavior:'smooth'});this.setState({gi:i});};
  const sync=()=>{clearTimeout(this.st);this.st=setTimeout(()=>{const t=document.querySelectorAll('.gv .gTrack');t.forEach((x)=>x.scrollTo({left:this.state.gi*x.clientWidth,behavior:'auto'}));},30);};
  return {
   multi:n>1, hasChip:!!p.chipText, chipHex:p.chipHex||'#fff', chipText:p.chipText||'',
   imgs:L.map((u,i)=>({img:u,alt:alt+' – foto '+(i+1),label:'Fotografie '+(i+1)+' z '+n,th:'thumb'+(i===s.gi?' on':''),cur:i===s.gi?'true':'false',dot:'gDot'+(i===s.gi?' on':''),lbTh:'lbTh'+(i===s.gi?' on':''),go:(e)=>goFrom(e,i),lbGo:()=>this.setState({gi:i})})),
   gScroll:(e)=>{const t=e.currentTarget;const i=Math.round(t.scrollLeft/Math.max(1,t.clientWidth));if(i!==this.state.gi)this.setState({gi:i});},
   prev:(e)=>goFrom(e,s.gi-1), next:(e)=>goFrom(e,s.gi+1),
   lb:s.lb, openLb:()=>this.setState({lb:true}), closeLb:()=>{this.setState({lb:false});sync();},
   lbImg:L[s.gi]||L[0]||'', lbAlt:alt+' – foto '+(s.gi+1), lbNum:(s.gi+1)+' / '+n,
   lbPrev:()=>this.setState({gi:(s.gi-1+n)%n}), lbNext:()=>this.setState({gi:(s.gi+1)%n}),
   lbKey:(e)=>{if(e.key==='Escape'){e.stopPropagation();this.setState({lb:false});sync();}else if(e.key==='ArrowLeft'&&n>1){this.setState({gi:(s.gi-1+n)%n});}else if(e.key==='ArrowRight'&&n>1){this.setState({gi:(s.gi+1)%n});}}
  };
 }
}""", 720, 560, {"imgs": {"editor": None}, "alt": {"editor": "text", "default": "Fotografie produktu"}, "chipHex": {"editor": None}, "chipText": {"editor": None}})
