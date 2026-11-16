#!/usr/bin/env python3
"""Rebuilds sitemap.xml from every page in the site. Run after adding or removing pages:  python3 tools/build_sitemap.py"""
import os, subprocess, datetime
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = 'https://gametimesportssystems.com'
SKIP = {'tools', 'assets', '.git', 'node_modules'}
urls = []
for d, dirs, files in os.walk(root):
    dirs[:] = [x for x in dirs if x not in SKIP]
    if 'index.html' in files:
        rel = os.path.relpath(d, root)
        path = '/' if rel == '.' else '/' + rel.replace(os.sep, '/') + '/'
        f = os.path.join(d, 'index.html')
        try:
            mod = subprocess.check_output(['git', '-C', root, 'log', '-1', '--format=%cs', '--', f], text=True).strip()
        except Exception:
            mod = ''
        urls.append((path, mod or datetime.date.today().isoformat()))
urls.sort(key=lambda u: (u[0].count('/'), u[0]))
xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(
    f'  <url><loc>{BASE}{p}</loc><lastmod>{m}</lastmod></url>\n' for p, m in urls) + '</urlset>\n'
open(os.path.join(root, 'sitemap.xml'), 'w').write(xml)
print(f'Wrote sitemap.xml with {len(urls)} pages')
