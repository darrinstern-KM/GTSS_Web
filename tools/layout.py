"""Shared page shell for generated pages. Used by the build scripts in this folder."""
FONTS = '''<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">'''

NAV = [('Products', '/#products'), ('Calculator', '/#calculator'), ('Distributors', '/distributors/'), ('Guides', '/resources/'), ('Ordering', '/#ordering')]

def page(title, description, path, body, current=None, extra_head=''):
    nav = ''.join(f'<a href="{h}"{" aria-current=" + chr(34) + "page" + chr(34) if n == current else ""}>{n}</a>\n      ' for n, h in NAV)
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="https://gametimesportssystems.com{path}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="https://gametimesportssystems.com{path}">
{extra_head}
{FONTS}
<link rel="stylesheet" href="/assets/css/site.css">
</head>
<body>
<a class="skip" href="#main">Skip to main content</a>

<header id="top" class="solid">
  <div class="wrap bar">
    <a class="logo" href="/" aria-label="GameTime Sports Systems home"><img src="/assets/img/gametime-logo-white.svg" alt="GameTime Sports Systems" width="154" height="49"></a>
    <nav aria-label="Main">
      {nav}</nav>
    <div class="right">
      <a class="tel" href="tel:18005200512">800.520.0512</a>
      <a class="btn" href="/#quote">Get a quote</a>
    </div>
  </div>
</header>

<main id="main">
{body}
</main>

<footer>
  <div class="wrap">
    <span>&copy; <span id="yr">2026</span> GameTime Sports Systems, LLC. Northbrook, Illinois.</span>
    <nav aria-label="Footer"><a href="/distributors/">Distributors</a><a href="/resources/">Guides</a><a href="/privacy/">Privacy policy</a><a href="/terms-and-conditions/">Terms</a><a href="/accessibility/">Accessibility</a><a href="#top">Back to top</a></nav>
  </div>
</footer>

<div class="sticky" id="sticky" role="region" aria-label="Quick contact">
  <a class="btn call" href="tel:18005200512" aria-label="Call GameTime">Call</a>
  <a class="btn" href="/#quote">Get a quote</a>
</div>
<script src="/assets/js/site.js" defer></script>
</body>
</html>
'''
