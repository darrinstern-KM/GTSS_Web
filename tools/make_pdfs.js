// Turns every tools/print/*.html into a PDF in assets/docs/. Run:  node tools/make_pdfs.js
const { chromium } = require('playwright'); const fs = require('fs'); const path = require('path');
(async () => {
  const dir = path.join(__dirname, 'print'), out = path.join(__dirname, '..', 'assets', 'docs');
  const b = await chromium.launch(); const p = await b.newPage();
  for (const f of fs.readdirSync(dir).filter(f => f.endsWith('.html'))) {
    await p.goto('file://' + path.join(dir, f)); await p.waitForTimeout(300);
    await p.pdf({ path: path.join(out, f.replace('.html', '.pdf')), format: 'Letter', printBackground: true, margin: { top: 0, right: 0, bottom: 0, left: 0 } });
    console.log('Wrote', f.replace('.html', '.pdf'));
  }
  await b.close();
})();
