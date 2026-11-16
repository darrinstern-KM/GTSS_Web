#!/usr/bin/env python3
"""Builds the company and legal pages. Run:  python3 tools/build_pages.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import layout
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UPDATED = 'November 16, 2026'
MAIL = '<a href="mailto:info@gametimesportssystems.com">info@gametimesportssystems.com</a>'
TEL = '<a href="tel:18005200512">800.520.0512</a>'

def head(crumb, eyebrow, h1, intro):
    return f'''<div class="pagehead"><div class="wrap">
    <p class="crumbs"><a href="/">Home</a> / {crumb}</p>
    <p class="eyebrow" style="color:#F2B84B">{eyebrow}</p>
    <h1>{h1}</h1>
    <p>{intro}</p>
  </div></div>'''

def prose(inner): return f'<section><div class="wrap prose">{inner}</div></section>'

PAGES = {}

PAGES['about-us'] = ('About GameTime Sports Systems', 'GameTime Sports Systems is a family-owned supplier of infield conditioners, mound clay and field marking products, serving ballfields nationwide since 2008.',
  head('About', 'Our story', 'It ain\'t just dirt', 'A family-owned company that has supplied the materials under America\'s ballfields since 2008.') + prose(f'''
    <h2 style="margin-top:0">Who we are</h2>
    <p>GameTime Sports Systems provides specialized groundskeeping products used by schools, municipalities, youth leagues and ballclubs. Our clay products are on baseball and softball fields across the country.</p>
    <p>We are based in Northbrook, Illinois, and ship coast to coast, direct or through a network of distributors in 23 states. Our management team brings more than 40 years of experience serving businesses and government organizations.</p>
    <h2>What we believe</h2>
    <p>Our mission is to bring the highest quality products to every level of play. A professional club wants a field that looks the part. A parks department wants easy application and season-long performance. A school or youth league wants a consistent, safe surface. The right material does all three.</p>
    <h2>The people you will talk to</h2>
    <p>GameTime is family owned. When you call, you reach the people who own the company.</p>
    <div class="team">
      <div class="box"><h3>David</h3><p>Partner, Sales and Shipping</p></div>
      <div class="box"><h3>Darrin</h3><p>Managing Partner, Operations</p></div>
      <div class="box"><h3>Lara</h3><p>Partner, Sales</p></div>
    </div>
    <h2>Work with us</h2>
    <p><a href="/#quote">Get a quote</a>, <a href="/distributors/">find a distributor</a>, or ask about <a href="/distributors/#become">carrying the GameTime line</a>.</p>'''))

PAGES['contact-us'] = ('Contact GameTime Sports Systems', 'Contact GameTime Sports Systems for quotes, distributor referrals and product questions. Call 800.520.0512 or email info@gametimesportssystems.com.',
  head('Contact', 'Get in touch', 'Contact us', 'Questions, quotes or a field problem you want to talk through. We are glad to help.') + f'''<section><div class="wrap">
    <div class="contactgrid">
      <div class="box"><h2>Call</h2><p>{TEL}</p><p class="note">Talk to an owner, not a call center.</p></div>
      <div class="box"><h2>Email</h2><p>{MAIL}</p></div>
      <div class="box"><h2>Mail</h2><p>GameTime Sports Systems, LLC<br>3015 White Pine Drive<br>Northbrook, IL 60062</p></div>
    </div>
    <div class="key" style="margin-top:32px"><b>Need a price?</b><span>The quote form asks for the few details we need to price material and freight. <a href="/#quote" style="color:#F2B84B;font-weight:600">Get a quote</a> or <a href="/distributors/" style="color:#F2B84B;font-weight:600">find a distributor</a>.</span></div>
  </div></section>''')

PAGES['credit-terms'] = ('Credit Terms | GameTime Sports Systems', 'GameTime Sports Systems offers net 30 terms on approved credit, accepts purchase orders from schools and municipalities, and takes all major credit cards.',
  head('Credit terms', 'Ordering', 'Credit terms', 'Net 30 on approved credit, purchase orders welcome, and all major cards accepted.') + prose(f'''
    <h2 style="margin-top:0">How you can pay</h2>
    <ul>
      <li><strong>Net 30 terms</strong> on approved credit.</li>
      <li><strong>Credit cards:</strong> Visa, Mastercard, American Express and Discover.</li>
      <li><strong>Prepaid orders</strong> and checks by phone.</li>
    </ul>
    <h2>Purchase orders</h2>
    <p>We require a written purchase order, or a valid purchase order number subject to verification.</p>
    <h2>Opening a credit account</h2>
    <p>New customers requesting credit terms complete a credit application, which is subject to review and approval before the first order is released. To request an application, email {MAIL} or call {TEL}.</p>
    <h2>Prepayment</h2>
    <p>We may require prepayment for custom orders. Orders from outside the United States require prepayment before shipment.</p>
    <h2>Past due balances</h2>
    <p>Customers agree to pay invoices within the agreed terms. Past due balances are charged interest at 18% per year, or the highest rate permitted by applicable law, whichever is lower. Customers also agree to pay any fees, including attorney fees, incurred in collecting past due invoices.</p>'''))

PAGES['privacy'] = ('Privacy Policy | GameTime Sports Systems', 'How GameTime Sports Systems collects, uses and protects information. This website uses no advertising trackers or tracking cookies.',
  head('Privacy policy', 'Legal', 'Privacy policy', 'The short version: we collect only what you send us, we use it to answer you, and we never sell it.') + prose(f'''
    <p class="updated">Last updated: {UPDATED}</p>
    <h2 style="margin-top:0">Who we are</h2>
    <p>This website is operated by GameTime Sports Systems, LLC, 3015 White Pine Drive, Northbrook, IL 60062.</p>
    <h2>What we collect</h2>
    <ul>
      <li><strong>Information you send us.</strong> When you request a quote we collect your name, email address, organization, type of organization, delivery ZIP code, your message and, if you provide it, your phone number.</li>
      <li><strong>Basic server logs.</strong> Like every website, our hosting provider records technical details of each request, such as IP address, browser type and the page requested, for security and troubleshooting.</li>
    </ul>
    <p>That is all. We do not ask for payment card details on this website.</p>
    <h2>What we do not do</h2>
    <ul>
      <li>We do not use advertising trackers, tracking pixels or analytics cookies.</li>
      <li>We do not sell your personal information, and we do not share it for advertising.</li>
      <li>We do not build profiles of visitors.</li>
    </ul>
    <p>Because we do not sell or share personal information, there is nothing for you to opt out of. We honor Global Privacy Control signals in the same way.</p>
    <h2>How we use your information</h2>
    <ul>
      <li>To answer your request and prepare a quote.</li>
      <li>To refer you to a GameTime distributor in your area, when one can serve you better. We share only the details needed to fulfill your request.</li>
      <li>To send you field care tips by email, only if you ticked the box asking for them. Every email includes an unsubscribe link.</li>
      <li>To keep ordinary business records.</li>
    </ul>
    <h2>Service providers</h2>
    <p>We use a small number of providers who process information on our behalf and only under our instructions: a customer relationship system that stores quote requests, an email service for subscribers who opted in, and our website host.</p>
    <h2>Video</h2>
    <p>Some guides include a video hosted by YouTube. The video does not load, and no information is sent to YouTube, unless you choose to play it. If you do, YouTube's own privacy policy applies.</p>
    <h2>How long we keep it</h2>
    <p>We keep quote requests and customer records for as long as needed to serve you and to meet our business and legal record-keeping obligations.</p>
    <h2>Your choices</h2>
    <p>You can ask us to tell you what personal information we hold about you, to correct it, or to delete it. Email {MAIL} or call {TEL}. We will respond to every request, wherever you live. We will not treat you differently for making one.</p>
    <h2>Children</h2>
    <p>This website is for businesses and organizations. It is not directed to children under 13, and we do not knowingly collect information from them.</p>
    <h2>Security</h2>
    <p>This website is served over an encrypted connection, and we limit access to the information you send us to the people who need it to respond.</p>
    <h2>Changes</h2>
    <p>If we change this policy we will post the new version here and update the date above.</p>
    <h2>Contact</h2>
    <p>Questions about privacy: {MAIL} or {TEL}.</p>'''))

PAGES['terms-and-conditions'] = ('Terms and Conditions | GameTime Sports Systems', 'Terms of sale and website terms for GameTime Sports Systems: quotes, payment, shipping, returns, sales tax and freight claims.',
  head('Terms and conditions', 'Legal', 'Terms and conditions', 'How quotes, orders, shipping and returns work.') + prose(f'''
    <p class="updated">Last updated: {UPDATED}</p>
    <h2 style="margin-top:0">Quotes and orders</h2>
    <p>This website does not take orders or payments. Prices are provided by written quote. An order is accepted when we confirm it, and the terms on your quote and order confirmation apply to that order.</p>
    <h2>Pricing and specifications</h2>
    <p>We make every effort to honor quoted prices. We reserve the right to change prices due to increased costs and to correct errors in pricing or specifications. If a correct price is higher than the price stated, we will contact you for instructions before shipping.</p>
    <p>Product specifications on this website and on our spec sheets are typical values. Actual results for a specific lot may vary slightly without affecting product performance.</p>
    <h2>Payment</h2>
    <p>Payment terms are net 30 with credit approval. We also accept major credit cards and company checks. We do not ship C.O.D. See our <a href="/credit-terms/">credit terms</a>.</p>
    <h2>Sales tax</h2>
    <p>Sales tax is added where required. To qualify for exemption you must provide a current sales tax exemption or resale certificate. New customers should send exemption forms with the credit application or first order.</p>
    <h2>Shipping</h2>
    <p>Freight terms are stated on your quote. Arrival time depends on the method of shipment and the distance from the shipping point. If you need delivery by a specific date, tell us when you place the order.</p>
    <h2>Freight damage and shortages</h2>
    <p>If a shipment arrives short or damaged, note the shortage or damage on the freight delivery document before signing, and notify us immediately. We will gladly assist with your freight claim.</p>
    <h2>Returns</h2>
    <ul>
      <li>All returns must be authorized by us in advance. Call {TEL} for a return authorization number, and include it with all correspondence and returns.</li>
      <li>Returns must be sent within 30 days of the date the authorization is issued.</li>
      <li>Items must be returned in their original condition and packaging.</li>
      <li>Shipping charges are not refunded unless the merchandise is defective or was shipped incorrectly. Returned items are subject to return shipping charges and may be subject to a restocking fee of up to 25%.</li>
      <li>Custom orders may not be returned unless the merchandise is defective or we made an error in filling the order.</li>
    </ul>
    <p>We are not responsible for misuse, customer installation or improper storage.</p>
    <h2>Substitutions</h2>
    <p>On occasion we may ship a product that differs slightly from the one described. We will always substitute a product of equal or better quality and value. If your requirements prohibit substitution, tell us when you place the order.</p>
    <h2>Events beyond our control</h2>
    <p>We are not liable for failure to perform caused by acts of God or the elements, acts or delays of government authorities, riot, terrorism, sabotage or war, disruption of utilities, or other matters beyond our reasonable control.</p>
    <h2>Using this website</h2>
    <p>The guides, calculators and coverage charts on this website are provided for general information. Quantities are estimates. Confirm quantities and suitability for your field before ordering. GameTime, the GameTime logo and GameTime product names are trademarks of GameTime Sports Systems, LLC. Other names belong to their owners.</p>
    <h2>Contact</h2>
    <p>Questions about these terms: {MAIL} or {TEL}.</p>'''))

PAGES['accessibility'] = ('Accessibility | GameTime Sports Systems', 'GameTime Sports Systems is committed to a website everyone can use. Read our accessibility statement and tell us if you hit a barrier.',
  head('Accessibility', 'Legal', 'Accessibility statement', 'We want everyone to be able to use this website, whatever device or assistive technology they use.') + prose(f'''
    <p class="updated">Last updated: {UPDATED}</p>
    <h2 style="margin-top:0">Our standard</h2>
    <p>We aim to meet the Web Content Accessibility Guidelines (WCAG) 2.2 at Level AA.</p>
    <h2>What we have done</h2>
    <ul>
      <li>Text and controls meet color contrast requirements.</li>
      <li>Every page can be used with a keyboard, with a visible focus indicator and a link to skip to the main content.</li>
      <li>Pages use proper headings, landmarks and labels so screen readers can navigate them.</li>
      <li>Form fields have visible labels, required fields are marked in text, and errors are announced.</li>
      <li>Animations respect your device's reduced motion setting, and the homepage animation can be paused.</li>
      <li>Layouts adapt to phones and to text enlarged up to 200%.</li>
      <li>Each page is tested with automated accessibility tools on desktop and phone sizes before it is published.</li>
    </ul>
    <h2>Known limitations</h2>
    <ul>
      <li>Some guides embed a video produced by a third party. We cannot guarantee the accuracy of its captions.</li>
      <li>Our PDF spec sheets are designed for print. The same information is available as text on each product page.</li>
    </ul>
    <h2>Tell us if something does not work</h2>
    <p>If you have trouble using any part of this website, or need information in another format, email {MAIL} or call {TEL}. Tell us the page and the problem, and we will help you and fix it.</p>'''))

for slug, (title, desc, body) in PAGES.items():
    out = os.path.join(root, slug, 'index.html'); os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, 'w').write(layout.page(title, desc, f'/{slug}/', body))
    print('Wrote', f'/{slug}/')
