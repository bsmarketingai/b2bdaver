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
