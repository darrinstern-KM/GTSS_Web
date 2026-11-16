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
}, {
    'slug': 'gametime-h2o-abzorb',
    'name': 'GameTime H2O/Abzorb&trade; Drying Agent',
    'plain': 'GameTime H2O/Abzorb Drying Agent',
    'category': 'Infield conditioners',
    'lead': 'Calcined clay drying agent that soaks up puddles and mud so play can resume. Spread it, work it in, and get back on the field.',
    'meta': 'GameTime H2O/Abzorb calcined clay drying agent absorbs standing water on infields, mounds, home plate areas and warning tracks to cut rain delays. 50 lb bags, super sacks or bulk.',
    'facts': [('100% clay', 'Calcined montmorillonite'), ('Fast acting', 'Dries puddles and mud'), ('Stays put', 'Works into the infield'), ('50 lb bags', '56 to a pallet')],
    'benefits': [
        ('Gets games back on.', 'Absorbs standing water and mud on contact to shorten rain delays and prevent rainouts.'),
        ('Works everywhere on the field.', 'Infield skin, mound, home plate area, warning track and wet turf.'),
        ('Fine, fast gradation.', 'More surface area per pound means faster drying than a standard conditioner.'),
        ('No waste.', 'Once the field is dry, drag it into the infield mix, where it keeps managing moisture.'),
        ('Will not stick to cleats.', 'Calcined clay holds its shape instead of turning to mud.')],
    'specs': [('Material', '100% montmorillonite clay, calcined'), ('Form', 'Granules'), ('Color', 'Reddish brown'), ('Odor', 'Odorless'), ('Ships from', 'Tennessee')],
    'packaging': [('Bag size', '50 lb'), ('Bags per pallet', '56'), ('Pallets per truckload', '16 (896 bags)'), ('Super sacks', '2,000 lb'), ('Bulk', 'Available')],
    'uses': 'Baseball, softball, football, soccer, parks and recreation, youth leagues',
    'safety': 'Contains naturally occurring crystalline silica. Avoid creating and breathing dust during application. A safety data sheet is available on request.',
    'pair': 'Spread by hand or shovel over wet spots, let it absorb, then rake or drag it in. Use sparingly on slick areas during play.',
    'pdf': 'gametime-h2o-abzorb-spec-sheet.pdf',
}, {
    'slug': 'gametime-pro',
    'name': 'GameTime Pro&trade; Infield Conditioner',
    'plain': 'GameTime Pro Infield Conditioner',
    'category': 'Infield conditioners',
    'lead': 'Calcined clay infield conditioner for firm footing, true hops and a skin that drains. Built for fields that get played on hard.',
    'meta': 'GameTime Pro calcined clay infield conditioner controls moisture, improves drainage and reduces compaction on baseball and softball infields. 50 lb bags, super sacks or bulk truckloads.',
    'facts': [('100% clay', 'Calcined montmorillonite'), ('Drains', 'Permanent pore space'), ('Durable', 'Resists crushing underfoot'), ('50 lb bags', '40 to a pallet')],
    'benefits': [
        ('Manages moisture.', 'Absorbs water when the field is wet and releases it as the skin dries, so the surface stays playable longer.'),
        ('Reduces compaction.', 'Hard, stable particles keep permanent pore space in the infield mix.'),
        ('Improves drainage.', 'Water moves through the skin instead of pooling on it.'),
        ('Holds up.', 'Resists crushing underfoot, so it does not break down into dust or mud.'),
        ('Looks the part.', 'A clean, consistent red finish across the whole infield.')],
    'specs': [('Material', '100% montmorillonite clay, calcined'), ('Form', 'Granules'), ('Color', 'Reddish brown'), ('Odor', 'Odorless'), ('Ships from', 'Tennessee')],
    'packaging': [('Bag size', '50 lb'), ('Bags per pallet', '40'), ('Pallets per truckload', '22 (880 bags)'), ('Super sacks', '2,000 lb'), ('Bulk', 'Up to 24 tons'), ('Mixed pallets', 'Mix and match with other conditioners')],
    'uses': 'Baseball, softball, parks and recreation, youth leagues',
    'safety': 'Contains naturally occurring crystalline silica. Avoid creating and breathing dust during application. A safety data sheet is available on request.',
    'pair': 'Topdress the skin and drag it in, or till it into the infield mix during renovation.',
    'more': ('/#calculator', 'Work out how much you need with the material calculator'),
    'pdf': 'gametime-pro-spec-sheet.pdf',
}, {
    'slug': 'gametime-mound-clay',
    'name': 'GameTime Pitcher\'s Mound Clay',
    'plain': 'GameTime Pitcher\'s Mound Clay',
    'category': 'Mound and plate',
    'lead': 'High-density red clay for pitcher\'s mounds, bullpens, batter\'s boxes and catcher\'s boxes. Moldable straight from the bag.',
    'meta': 'GameTime Pitcher\'s Mound Clay is a high-density red clay for building and repairing pitcher\'s mounds, batter\'s boxes and other high-wear areas. One 50 lb bag covers 4 sq ft at 1 inch.',
    'facts': [('1 bag = 4 sq ft', 'At a depth of 1 inch'), ('High density', 'Packs firm and stays firm'), ('Ready to use', 'Moldable from the bag'), ('50 lb bags', '40 to a pallet')],
    'benefits': [
        ('Built for the high-wear areas.', 'The front of the rubber, the landing area, and the batter\'s and catcher\'s boxes.'),
        ('Easy to work.', 'Moldable right out of the bag, with no mixing.'),
        ('Packs tight.', 'High clay content compacts into a firm surface that resists digging out.'),
        ('Consistent.', 'Screened, uniform material from bag to bag, with low dust.'),
        ('Construct, rebuild or repair.', 'Use it alone for daily maintenance or with GameTime Clay Bricks for a full rebuild.')],
    'specs': [('Material', 'Montmorillonite clay'), ('Form', 'Granules'), ('Color', 'Reddish brown'), ('Odor', 'Odorless'), ('Coverage', 'One bag covers 4 sq ft at 1 inch deep'), ('Ships from', 'Tennessee')],
    'packaging': [('Bag size', '50 lb'), ('Bags per pallet', '40'), ('Mixed pallets', 'Mix and match with infield conditioners')],
    'uses': 'Baseball, softball, parks and recreation, youth leagues',
    'safety': 'Contains naturally occurring crystalline silica. Avoid creating and breathing dust during application. A safety data sheet is available on request.',
    'pair': 'Add in 1 inch layers, lightly water, and tamp each layer firm and level.',
    'more': ('/resources/pitchers-mound-guide/', 'See the step-by-step mound guide and coverage chart'),
    'pdf': 'gametime-mound-clay-spec-sheet.pdf',
}]

P65 = 'California Proposition 65 warning: this product can expose you to crystalline silica, which is known to the State of California to cause cancer. For more information go to www.P65Warnings.ca.gov.'

def table(rows, cls='spec'):
    return f'<table class="{cls}"><tbody>' + ''.join(f'<tr><th scope="row">{e(a)}</th><td>{e(b)}</td></tr>' for a, b in rows) + '</tbody></table>'

def web(p):
    q = '/?product=' + quote(p['plain']) + '#quote'
    facts = ''.join(f'<div class="fact"><b>{e(a)}</b><span>{e(b)}</span></div>' for a, b in p['facts'])
    ben = ''.join(f'<li><b>{e(a)}</b> {e(b)}</li>' for a, b in p['benefits'])
    more = f'<p style="margin-top:20px"><a class="textlink" href="{p["more"][0]}">{e(p["more"][1])}</a></p>' if p.get('more') else ''
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
      {more}
    </div>
    <div>
      <h2>Specifications</h2>
      {table(p['specs'])}
      <p style="margin-top:16px"><a class="textlink" href="/assets/docs/{p['pdf']}">Download the spec sheet (PDF)</a></p>
      <h2 style="margin-top:40px">Packaging</h2>
      {table(p['packaging'])}
      <p class="note" style="margin-top:14px">{e(p['safety'])}</p>
      <p class="note" style="margin-top:10px">{e(P65)}</p>
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
<p class="note">{e(p['safety'])} Values shown are typical and may vary slightly between lots.</p><p class="note">{e(P65)}</p></div>
<div class="ft"><span><b>It ain't just dirt</b></span><span>GameTime Sports Systems, LLC &nbsp;|&nbsp; Get a quote: 800.520.0512</span></div></div></body></html>'''
    open(os.path.join(root, 'tools/print', p['pdf'].replace('.pdf', '.html')), 'w').write(doc)

for p in PRODUCTS:
    web(p); sheet(p)
