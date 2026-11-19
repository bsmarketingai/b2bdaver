# Generátor canvasu Daver.cz

Python skripty, ze kterých vznikají soubory `design/*.dc.html` (Design canvas na claude.ai).

Pořadí sestavení:

```
python3 -c "import components as c; from common import write; [write(n+'.dc.html', v.replace('></input>','>')) for n,v in c.comps.items()]"
python3 pages2.py
python3 rest.py
```

- `common.py` – tokeny, základní CSS, hlavička, data, společné JS
- `components.py` – komponenty (ProductCard, Footer, UserMenu, QuickView…)
- `pages.py` / `pages2.py` – Homepage, Kategorie, Detail, Porovnání, DetailVariant
- `rest.py` – infostránky a objednávka (Košík → Údaje → Kontrola → Děkujeme)
- `data.py` → `data.json`, `popisy.json`, `amsterdam_var.json` – produktová data
- `icons.json` – Phosphor Icons (regular)

Cesta výstupu je v `common.py` (funkce `write`), před spuštěním ji přizpůsobte.

## Statický web (index.html v kořeni repa)
Kořen repa obsahuje statický export canvasu – `index.html` (= Main) a ostatní stránky jako `*.html`,
runtime v `dc/` (Preact 10, MIT + `dc-runtime.js`). Funguje na GitHub Pages i na libovolném statickém hostingu
(lokálně přes server, např. `python3 -m http.server` v kořeni repa – z `file://` prohlížeč skripty a obrázky nenačte).

Přegenerování po změně canvasu (spouští se z kořene repa):
    python3 design/generator/export.py design assets/manifest.json .
- `.dc.html` se převedou na JSON strom, odkazy `X.dc.html` → `X.html` (Main → `index.html`),
  `/_blob/<id>` → cesta z `assets/manifest.json`. Komponenty (Footer, ProductCard…) se vkládají do stránek.
