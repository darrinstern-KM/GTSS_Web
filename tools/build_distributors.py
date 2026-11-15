#!/usr/bin/env python3
"""Rebuilds distributors/index.html from assets/data/distributors.json.
Edit the JSON file, then run:  python3 tools/build_distributors.py"""
import json, html, os, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import layout
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data = json.load(open(os.path.join(root, 'assets/data/distributors.json')))
names, dists = data['states'], data['distributors']
by = collections.OrderedDict()
for d in sorted(dists, key=lambda d: (names[d['state']], d['name'].lower())):
    by.setdefault(d['state'], []).append(d)
e = html.escape
n, ns = len(dists), len(by)
jump = ''.join(f'<a href="#{s.lower()}">{e(names[s])}</a>' for s in by)
cards = ''.join(
    f'<div class="state fade" id="{s.lower()}"><h2>{e(names[s])}</h2><ul>' +
    ''.join(f'<li><b>{e(d["name"])}</b><span>{e(d["city"])}, {s}</span></li>' for d in lst) +
    '</ul></div>\n      ' for s, lst in by.items())
ld = json.dumps({"@context": "https://schema.org", "@type": "ItemList", "name": "GameTime Sports Systems distributors",
                 "numberOfItems": n, "itemListElement": [
                     {"@type": "ListItem", "position": i + 1, "item": {"@type": "Organization", "name": d["name"],
                      "address": {"@type": "PostalAddress", "addressLocality": d["city"], "addressRegion": d["state"], "addressCountry": "US"}}}
                     for i, d in enumerate(dists)]})
body = f'''<div class="pagehead">
  <div class="wrap">
    <p class="crumbs"><a href="/">Home</a> / Distributors</p>
    <p class="eyebrow" style="color:#F2B84B">Buy local</p>
    <h1>Find a distributor</h1>
    <p>{n} distributors in {ns} states stock GameTime infield conditioners, mound clay and field marking products. No distributor near you? We ship direct.</p>
    <div class="jump" aria-label="Jump to a state">{jump}</div>
  </div>
</div>

<section>
  <div class="wrap">
    <div class="stategrid">
      {cards}</div>
    <p class="lead" style="margin-top:36px;max-width:none">Do not see your state? <a class="textlink" href="/#quote">Request a quote</a> and we will ship direct, or call <a class="textlink" href="tel:18005200512">800.520.0512</a>.</p>
  </div>
</section>

<section class="become" id="become">
  <div class="wrap">
    <div>
      <p class="eyebrow fade">Distributor opportunities</p>
      <h2 class="fade">Carry the GameTime line</h2>
      <p class="fade" style="margin-top:16px;color:rgba(255,255,255,.88)">We are adding distributors in open territories. If you serve schools, parks departments or ballfields, GameTime gives you a full field materials line under one brand.</p>
      <ul class="fade">
        <li>Infield conditioners, mixes, mound clay, warning track and marking products</li>
        <li>Bags, super sacks and bulk, with mixed pallets available</li>
        <li>Leads from this website referred to you in your territory</li>
        <li>Spec sheets and support for architects and bid documents</li>
      </ul>
    </div>
    <div class="fade">
      <a class="btn" href="/#quote">Ask about your territory</a>
      <p style="margin-top:14px;color:rgba(255,255,255,.85)">Choose "Distributor or contractor" on the form, or call <a href="tel:18005200512" style="color:#fff">800.520.0512</a>.</p>
    </div>
  </div>
</section>
'''
extra = f'<script type="application/ld+json">{ld}</script>'
page = layout.page('Find a Distributor | GameTime Sports Systems', f'Find a GameTime Sports Systems distributor near you. {n} distributors in {ns} states stock GameTime infield conditioners, mound clay and field marking products.', '/distributors/', body, current='Distributors', extra_head=extra)
os.makedirs(os.path.join(root, 'distributors'), exist_ok=True)
open(os.path.join(root, 'distributors/index.html'), 'w').write(page)
print(f'Wrote distributors/index.html: {n} distributors, {ns} states')
