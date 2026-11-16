#!/usr/bin/env python3
"""Builds product pages and their printable spec sheets. Run:  python3 tools/build_products.py
Then run  node tools/make_pdfs.js  to refresh the PDF spec sheets."""
import os, sys, json, html
from urllib.parse import quote
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import layout
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
e = html.escape

PRODUCTS = [{
    'slug': 'gametime-white-strip-field-marking-powder',
    'name': 'GameTime White Strip&trade; Field Marking Powder',
    'plain': 'GameTime White Strip Field Marking Powder',
    'category': 'Field marking',
    'lead': 'Bright white, free-flowing marking powder for foul lines, batter\'s boxes and boundaries on any athletic field. Non-caustic, with no hydrated lime.',
    'meta': 'GameTime White Strip field marking powder: bright white, non-caustic ground calcium carbonate for baseball, softball, football and soccer fields. 50 lb bags by the pallet or truckload.',
    'facts': [('96.5%', 'Calcium carbonate'), ('22 micron', 'Median particle size'), ('Non-caustic', 'No hydrated lime'), ('50 lb bags', '56 to a pallet')],
    'benefits': [
        ('Non-caustic.', 'Made from ground calcium carbonate, not hydrated lime, which can burn skin, eyes and turf.'),
        ('Lays a solid line.', 'A fine, consistent grind flows through standard dry line markers without clumping or clogging.'),
        ('Bright white.', 'High-contrast lines that read clearly against dirt and grass.'),
        ('One powder, every field.', 'Baseball, softball, football, soccer and any other athletic field.'),
        ('Economical.', 'Sold by the pallet or the truckload, with single pallet orders available.')],
    'specs': [('Material', 'Ground calcium carbonate (crushed limestone)'), ('Calcium carbonate', '96.5%'), ('Magnesium carbonate', '2%'),
              ('Median particle size', '22 microns (about 200 mesh)'), ('Dry brightness (Hunter)', '84'), ('pH', '9.3 to 9.4'),
              ('Bulk density, loose', '55 lb per cubic foot'), ('Bulk density, compacted', '80 lb per cubic foot'), ('Made in', 'USA')],
    'packaging': [('Bag size', '50 lb'), ('Bags per pallet', '56'), ('Pallets per truckload', '16 (896 bags)'), ('Minimum order', 'One pallet')],
    'uses': 'Baseball, softball, football, soccer, parks and recreation, youth leagues',
    'safety': 'As with any mineral powder, avoid creating and breathing dust during application. A safety data sheet is available on request.',
    'pair': 'Apply with a dry line marker. We supply 35 lb, 50 lb and 100 lb all-steel models.',
    'pdf': 'gametime-white-strip-spec-sheet.pdf',
}]

def table(rows, cls='spec'):
    return f'<table class="{cls}"><tbody>' + ''.join(f'<tr><th scope="row">{e(a)}</th><td>{e(b)}</td></tr>' for a, b in rows) + '</tbody></table>'

def web(p):
    q = '/?product=' + quote(p['plain']) + '#quote'
    facts = ''.join(f'<div class="fact"><b>{e(a)}</b><span>{e(b)}</span></div>' for a, b in p['facts'])
    ben = ''.join(f'<li><b>{e(a)}</b> {e(b)}</li>' for a, b in p['benefits'])
    ld = json.dumps({"@context": "https://schema.org", "@type": "Product", "name": p['plain'], "description": p['meta'],
                     "category": p['category'], "brand": {"@type": "Brand", "name": "GameTime Sports Systems"},
                     "additionalProperty": [{"@type": "PropertyValue", "name": a, "value": b} for a, b in p['specs']]})
    body = f'''<div class="pagehead">
  <div class="wrap">
    <p class="crumbs"><a href="/">Home</a> / <a href="/#products">Products</a> / {e(p['category'])}</p>
    <p class="eyebrow" style="color:#F2B84B">{e(p['category'])}</p>
    <h1>{p['name']}</h1>
    <p>{e(p['lead'])}</p>
    <div class="cta-row" style="margin-top:28px"><a class="btn" href="{q}">Get a quote</a><a class="btn ghost" href="/distributors/">Find a distributor</a></div>
  </div>
</div>
<section class="facts pfacts" aria-label="Key facts"><div class="wrap">{facts}</div></section>

<section>
  <div class="wrap psplit">
    <div>
      <h2>Why groundskeepers choose it</h2>
      <ul class="checks">{ben}</ul>
      <div class="callout"><b>Recommended for:</b> {e(p['uses'])}.</div>
      <div class="callout"><b>Application:</b> {e(p['pair'])}</div>
    </div>
    <div>
      <h2>Specifications</h2>
      {table(p['specs'])}
      <p style="margin-top:16px"><a class="textlink" href="/assets/docs/{p['pdf']}">Download the spec sheet (PDF)</a></p>
      <h2 style="margin-top:40px">Packaging</h2>
      {table(p['packaging'])}
      <p class="note" style="margin-top:14px">{e(p['safety'])}</p>
    </div>
  </div>
</section>

<section class="how" style="text-align:center">
  <div class="wrap">
    <h2>Need a delivered price?</h2>
    <p style="margin:14px auto 26px;max-width:560px;color:rgba(255,255,255,.88)">Tell us how many fields you line and your delivery ZIP. We will quote it by the pallet or truckload, direct or through your local distributor.</p>
    <a class="btn" href="{q}">Get a quote</a>
  </div>
</section>'''
    path = f"/products/{p['slug']}/"
    out = os.path.join(root, 'products', p['slug'], 'index.html'); os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, 'w').write(layout.page(f"{p['plain']} | GameTime Sports Systems", p['meta'], path, body, current='Products',
                                     extra_head='<script type="application/ld+json">' + ld + '</script>'))
    print('Wrote', path)

PRINT_CSS = '''@page{size:Letter;margin:0}*{box-sizing:border-box}body{margin:0;font-family:Arial,Helvetica,sans-serif;color:#2A2F33;font-size:10pt;line-height:1.5}
.pg{width:8.5in;height:10.98in;display:flex;flex-direction:column;overflow:hidden}
.top{background:#14181B;color:#fff;padding:.36in .6in;display:flex;justify-content:space-between;align-items:center}.top img{height:.5in}
.top div{text-align:right;font-size:8.5pt;color:rgba(255,255,255,.85)}
.band{background:#A63F25;color:#fff;padding:.1in .6in;font-size:8pt;letter-spacing:.18em;text-transform:uppercase;font-weight:700}
.bd{padding:.4in .6in 0;flex:1}.ey{color:#A63F25;font-weight:700;letter-spacing:.16em;text-transform:uppercase;font-size:8.5pt}
h1{font-family:"Arial Narrow",Arial,sans-serif;font-size:27pt;line-height:1.02;margin:.05in 0 .1in;text-transform:uppercase;color:#14181B}
h2{font-size:12.5pt;text-transform:uppercase;margin:0 0 .07in;color:#14181B;border-bottom:2px solid #A63F25;padding-bottom:.03in}
.lead{color:#545D65;max-width:6in;margin:0 0 .22in}.cols{display:grid;grid-template-columns:1fr 1fr;gap:.4in}
table{width:100%;border-collapse:collapse;font-size:9.5pt;margin-bottom:.22in}th,td{padding:.055in .08in;text-align:left;border-bottom:1px solid #E6D8C3;vertical-align:top}th{width:46%;font-weight:700;color:#14181B}
tr:nth-child(even) th,tr:nth-child(even) td{background:#F7F3EC}
ul{margin:0 0 .2in;padding-left:.2in}li{margin-bottom:.06in}.box{background:#F7F3EC;border-left:3px solid #A63F25;padding:.1in .14in;margin-bottom:.12in;font-size:9.5pt}
.note{font-size:8.5pt;color:#545D65}.ft{background:#14181B;color:rgba(255,255,255,.85);padding:.2in .6in;display:flex;justify-content:space-between;font-size:8.5pt}.ft b{color:#F2B84B;letter-spacing:.14em;text-transform:uppercase}'''

def sheet(p):
    logo = 'file://' + os.path.join(root, 'assets/img/gametime-logo-white.svg')
    ben = ''.join(f'<li><b>{e(a)}</b> {e(b)}</li>' for a, b in p['benefits'])
    doc = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{e(p['plain'])}: Product Specification</title><style>{PRINT_CSS}</style></head><body><div class="pg">
<div class="top"><img src="{logo}" alt="GameTime Sports Systems"><div>3015 White Pine Drive, Northbrook, IL 60062<br>800.520.0512 &nbsp;|&nbsp; gametimesportssystems.com</div></div>
<div class="band">Product specification</div><div class="bd"><div class="ey">{e(p['category'])}</div><h1>{p['name']}</h1><p class="lead">{e(p['lead'])}</p>
<div class="cols"><div><h2>Specifications</h2>{table(p['specs'], '')}<h2>Packaging</h2>{table(p['packaging'], '')}</div>
<div><h2>Features</h2><ul>{ben}</ul><div class="box"><b>Recommended for:</b> {e(p['uses'])}.</div><div class="box"><b>Application:</b> {e(p['pair'])}</div></div></div>
<p class="note">{e(p['safety'])} Values shown are typical and may vary slightly between lots.</p></div>
<div class="ft"><span><b>It ain't just dirt</b></span><span>GameTime Sports Systems, LLC &nbsp;|&nbsp; Get a quote: 800.520.0512</span></div></div></body></html>'''
    open(os.path.join(root, 'tools/print', p['pdf'].replace('.pdf', '.html')), 'w').write(doc)

for p in PRODUCTS:
    web(p); sheet(p)
