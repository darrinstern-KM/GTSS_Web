#!/usr/bin/env python3
"""Builds the Guides pages. Run:  python3 tools/build_resources.py"""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import layout
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def table(caption, rows, total=None):
    body = ''.join(f'<tr><th scope="row">{a}</th><td>{s}</td><td>{b}</td><td>{x}</td><td>{y}</td><td>{z}</td></tr>' for a, s, b, x, y, z in rows)
    foot = f'<tfoot><tr><th scope="row">Total</th><td></td><td>{total[0]}</td><td>{total[1]}</td><td>{total[2]}</td><td>{total[3]}</td></tr></tfoot>' if total else ''
    return f'''<div class="tablewrap" tabindex="0" role="region" aria-label="{caption} coverage table"><table class="cov"><caption>{caption}</caption>
<thead><tr><th scope="col">Area</th><th scope="col">Size</th><th scope="col">Clay bricks</th><th scope="col">Bags at 2 in</th><th scope="col">Bags at 4 in</th><th scope="col">Bags at 6 in</th></tr></thead>
<tbody>{body}</tbody>{foot}</table></div>'''

HIGH = table('High-stress areas only (baseball)', [
    ('Table', '34 x 60 in', '64', '7.5', '15', '22.5'),
    ('Landing area', '32 x 60 in', '60', '7', '14', '21'),
    ("Batter's boxes*", '32 x 60 in each', '120', '14', '28', '42'),
    ("Catcher's box", '32 x 48 in', '48', '5.5', '11', '16.5')], ('292', '34', '68', '102'))
BASEBALL = table('Baseball: entire area', [
    ("Batter's boxes*", '48 x 72 in each', '216', '24', '48', '72'),
    ('Table and slope', '60 x 106 in', '199', '22', '44', '66'),
    ("Catcher's box", '43 x 69 in', '93', '10.5', '21', '31.5')])
SOFTBALL = table('Softball: entire area', [
    ("Batter's boxes*", '36 x 84 in each', '189', '21', '42', '63'),
    ('Mound', '36 x 60 in', '65', '7.5', '15', '22.5')])
LITTLE = table('Youth baseball: entire area', [
    ("Batter's boxes*", '36 x 72 in each', '162', '18', '36', '54'),
    ('Mound slope', '40 x 60 in', '75', '8', '16', '24'),
    ('Table', '12 x 40 in', '14', '2', '4', '6')])

# Mound diagram, drawn to scale: 1 unit = 1 inch. Circle radius 9 ft (108 in).
DIAGRAM = '''<svg viewBox="-150 -125 300 250" role="img" aria-labelledby="dgt dgd">
<title id="dgt">High-stress areas of a pitcher's mound</title>
<desc id="dgd">An 18 foot circle containing a 60 by 106 inch work area. The top 34 inches is the table with the pitching rubber. The bottom 32 inches is the landing area. The 40 inches between is the slope.</desc>
<circle cx="0" cy="0" r="108" fill="#F7F3EC" stroke="#14181B" stroke-width="1"/>
<rect x="-30" y="-53" width="60" height="106" fill="#fff" stroke="#14181B" stroke-width="1"/>
<rect x="-30" y="-53" width="60" height="34" fill="#D9A892"/>
<rect x="-30" y="21" width="60" height="32" fill="#D9A892"/>
<rect x="-12" y="-31" width="24" height="6" fill="#fff" stroke="#14181B" stroke-width="1"/>
<g font-family="Inter,Arial,sans-serif" font-size="8" fill="#14181B">
<text x="0" y="-41" text-anchor="middle" font-weight="600">Table</text>
<text x="0" y="4" text-anchor="middle">Slope</text>
<text x="0" y="40" text-anchor="middle" font-weight="600">Landing area</text>
<text x="0" y="-58" text-anchor="middle">60 in</text>
<text x="-36" y="-33" text-anchor="end">34 in</text>
<text x="36" y="4">40 in</text>
<text x="-36" y="40" text-anchor="end">32 in</text>
<text x="62" y="-20">106 in overall</text>
<text x="0" y="-112" text-anchor="middle">9 ft radius</text>
<text x="0" y="-21" text-anchor="middle" font-size="6">Pitching rubber</text>
</g>
<g stroke="#14181B" stroke-width=".6"><line x1="56" y1="-53" x2="56" y2="53"/><line x1="52" y1="-53" x2="60" y2="-53"/><line x1="52" y1="53" x2="60" y2="53"/></g>
<text x="0" y="120" text-anchor="middle" font-family="Inter,Arial,sans-serif" font-size="7" fill="#545D65">Shaded areas are high stress. Home plate is toward the bottom.</text>
</svg>'''

howto = {"@context": "https://schema.org", "@type": "HowTo", "name": "How to build or renovate a pitcher's mound with clay bricks",
         "description": "Six steps to rebuild the high-stress areas of a pitcher's mound using mound clay bricks and bagged mound clay.",
         "supply": [{"@type": "HowToSupply", "name": "GameTime Clay Bricks"}, {"@type": "HowToSupply", "name": "GameTime Mound Clay"}, {"@type": "HowToSupply", "name": "GameTime Pro infield conditioner"}],
         "tool": [{"@type": "HowToTool", "name": "Tamp"}, {"@type": "HowToTool", "name": "Shovel"}, {"@type": "HowToTool", "name": "Hose"}],
         "step": [{"@type": "HowToStep", "position": i + 1, "name": n, "text": t} for i, (n, t) in enumerate([
             ("Measure", "Measure out the pitcher's mound using the recommended dimensions."),
             ("Cut out", "Cut out and remove all loose dirt from the high-stress area around the mound to a depth of 3 inches."),
             ("Place bricks", "Place GameTime Clay Bricks as evenly and as close together as possible."),
             ("Water and tamp", "Water the cut area, then tamp the bricks into place."),
             ("Fill", "Fill the remaining half inch with the loose material you removed or with GameTime Mound Clay."),
             ("Level and finish", "Level and compact the new surface, then topdress with GameTime Pro infield conditioner.")])]}
STEPS = ''.join(f'<li><strong>{s["name"]}.</strong> {s["text"]}</li>' for s in howto['step'])

guide = f'''<div class="pagehead">
  <div class="wrap">
    <p class="crumbs"><a href="/">Home</a> / <a href="/resources/">Guides</a> / Pitcher's mound</p>
    <p class="eyebrow" style="color:#F2B84B">Field guide</p>
    <h1>Build or renovate a pitcher's mound</h1>
    <p>How to repair and rebuild the high-stress areas of the mound and home plate, with a coverage chart showing how many clay bricks and bags you need.</p>
    <div class="cta-row" style="margin-top:28px"><a class="btn" href="/assets/docs/gametime-pitchers-mound-guide.pdf">Download the PDF</a><a class="btn ghost" href="/#quote">Get a quote</a></div>
  </div>
</div>

<section>
  <div class="wrap guide">
    <p class="lead" style="max-width:none;margin-top:0">The front of the pitching rubber, the landing area, and the batter's and catcher's boxes take more punishment than the rest of the field combined. Use GameTime Mound Clay and GameTime Clay Bricks to construct, rebuild or repair them.</p>

    <div class="key"><b>1 bag = 4 sq ft</b><span>One 50 lb bag of GameTime Mound Clay covers 4 square feet at a depth of 1 inch.</span></div>

    <h2 id="repair">Repair or rebuild?</h2>
    <div class="two">
      <div class="box"><h3>Repairing worn spots</h3><ol>
        <li>Broom off all loose dirt from the stress area and lightly water it.</li>
        <li>Add GameTime Mound Clay in 1 inch layers.</li>
        <li>Tamp the clay to a firm, level surface.</li>
        <li>Repeat steps 2 and 3 until the new surface is level with the old surface.</li></ol></div>
      <div class="box"><h3>Rebuilding the area</h3><ol>
        <li>Remove 2 to 4 inches of existing soil from the stress area and lightly water it.</li>
        <li>Add GameTime Mound Clay in 1 inch layers.</li>
        <li>Tamp the clay to a firm, level surface, adding water as necessary.</li>
        <li>Repeat steps 2 and 3 until the new surface is level with the old surface.</li></ol></div>
    </div>

    <h2 id="bricks">Rebuilding with clay bricks: 6 steps</h2>
    <ol>{STEPS}</ol>

    <h2 id="areas">Where the high-stress areas are</h2>
    <div class="diagram">{DIAGRAM}</div>

    <h2 id="chart">Mound clay and clay brick coverage chart</h2>
    <p>Find your field type and the area you are working on. Bag counts are shown for depths of 2, 4 and 6 inches.</p>
    {HIGH}
    {BASEBALL}
    {SOFTBALL}
    {LITTLE}
    <p class="note">All quantities are approximate. *Brick and bag counts are for both batter's boxes.</p>

    <div class="key" style="margin-top:40px"><b>Ready to order?</b><span>Send us your field type and the areas you are rebuilding. We will confirm the quantity and quote it delivered. <a href="/#quote" style="color:#F2B84B;font-weight:600">Get a quote</a> or <a href="/distributors/" style="color:#F2B84B;font-weight:600">find a distributor</a>.</span></div>
  </div>
</section>'''

index = '''<div class="pagehead">
  <div class="wrap">
    <p class="crumbs"><a href="/">Home</a> / Guides</p>
    <p class="eyebrow" style="color:#F2B84B">Field guides and tools</p>
    <h1>Know-how for better fields</h1>
    <p>Practical guides and calculators from the people who supply the dirt.</p>
  </div>
</div>
<section>
  <div class="wrap">
    <h2 style="margin-bottom:28px">Start here</h2>
    <div class="cardlist">
      <a class="card fade" href="/resources/pitchers-mound-guide/"><span class="q">Guide and coverage chart</span><h3>Build or renovate a pitcher's mound</h3><p>Repair and rebuild steps, plus how many clay bricks and bags you need for baseball, softball and youth fields.</p><span class="go">Read the guide &rarr;</span></a>
      <a class="card fade d1" href="/#calculator"><span class="q">Calculator</span><h3>Infield conditioner calculator</h3><p>Enter your skinned area and depth to get tons, bags and pallets.</p><span class="go">Open the calculator &rarr;</span></a>
      <a class="card fade d2" href="/#faq"><span class="q">Quick answers</span><h3>Common questions</h3><p>Coverage rates, the difference between mix and conditioner, shipping and purchase orders.</p><span class="go">See the answers &rarr;</span></a>
    </div>
  </div>
</section>'''

def write(rel, html):
    p = os.path.join(root, rel); os.makedirs(os.path.dirname(p), exist_ok=True); open(p, 'w').write(html); print('Wrote', rel)

write('resources/pitchers-mound-guide/index.html', layout.page("How to Build or Renovate a Pitcher's Mound | GameTime Sports Systems",
      "Step-by-step guide to repairing and rebuilding a pitcher's mound and home plate area, with a mound clay and clay brick coverage chart for baseball, softball and youth fields.",
      '/resources/pitchers-mound-guide/', guide, current='Guides', extra_head='<script type="application/ld+json">' + json.dumps(howto) + '</script>'))
write('resources/index.html', layout.page('Field Guides and Calculators | GameTime Sports Systems',
      'Field maintenance guides, coverage charts and material calculators for baseball and softball fields from GameTime Sports Systems.', '/resources/', index, current='Guides'))
