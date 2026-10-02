import { chromium } from 'playwright';
import { mkdir, writeFile } from 'node:fs/promises';
import { createHash } from 'node:crypto';
import { createInterface } from 'node:readline/promises';
import { stdin, stdout } from 'node:process';

const target = process.argv[2] || 'https://www.pantastico.com/hu/katalogus';
if (!['https:', 'http:'].includes(new URL(target).protocol)) throw new Error('HTTP(S) URL kell.');
const root = 'audit-output';
await mkdir(`${root}/assets`, { recursive: true });
await mkdir(`${root}/snapshots`, { recursive: true });
const browser = await chromium.launch({ headless: false });
const context = await browser.newContext({ viewport: { width: 1440, height: 1000 }, serviceWorkers: 'block' });
const records = [], errors = [], pending = new Set(), seen = new Set();
const MAX_FILE = 25 * 1024 * 1024, MAX_TOTAL = 200 * 1024 * 1024;
let total = 0, reserved = 0, snapId = 0;

async function saveResponse(response) {
  const req = response.request();
  if (req.method() !== 'GET') return;
  const type = req.resourceType(), url = response.url();
  if (!/^https?:/.test(url)) return;
  const headers = await response.allHeaders();
  const mime = (headers['content-type'] || '').split(';')[0];
  const relevant = ['document', 'script', 'stylesheet', 'image', 'font', 'media'].includes(type)
    || /^(application\/pdf|image\/|font\/|text\/css|application\/javascript)/.test(mime);
  if (!relevant) return;
  const key = `${response.status()} ${url}`;
  if (seen.has(key)) return;
  seen.add(key);
  const record = { url, type, mime, status: response.status(), file: null };
  records.push(record);
  if (!response.ok()) { record.skipped = 'HTTP status'; return; }
  const length = Number(headers['content-length'] || 0);
  if (length > MAX_FILE) { record.skipped = '25 MB file limit'; return; }
  // Reserve a full file slot so parallel downloads cannot exceed the save budget.
  if (total + reserved + MAX_FILE > MAX_TOTAL) { record.skipped = '200 MB budget'; return; }
  reserved += MAX_FILE;
  try {
    const body = await response.body();
    if (body.length > MAX_FILE) { record.skipped = '25 MB file limit'; return; }
    let ext = ({'text/html':'.html','text/css':'.css','application/javascript':'.js','text/javascript':'.js',
      'application/pdf':'.pdf','image/png':'.png','image/jpeg':'.jpg','image/webp':'.webp',
      'image/svg+xml':'.svg','font/woff2':'.woff2'})[mime];
    if (!ext) ext = new URL(url).pathname.match(/\.[a-zA-Z0-9]{1,6}$/)?.[0] || '.bin';
    const digest = createHash('sha256').update(url).digest('hex').slice(0, 20);
    const name = `assets/${digest}${ext}`;
    await writeFile(`${root}/${name}`, body);
    total += body.length;
    Object.assign(record, { file: name, bytes: body.length, sha256: createHash('sha256').update(body).digest('hex') });
  } catch (err) { record.error = String(err); }
  finally { reserved -= MAX_FILE; }
}
context.on('response', response => {
  const job = saveResponse(response).catch(err => errors.push(String(err)));
  pending.add(job); job.finally(() => pending.delete(job));
});
context.on('page', page => page.on('pageerror', err => errors.push({ url: page.url(), error: String(err) })));
const page = await context.newPage();

async function snapshot(label) {
  const id = ++snapId;
  for (const [pi, current] of context.pages().entries()) {
    for (const [fi, frame] of current.frames().entries()) {
      const prefix = `${root}/snapshots/${id}-${pi}-${fi}`;
      try {
        await writeFile(`${prefix}.html`, await frame.content());
        const data = await frame.evaluate(() => {
          const selector = el => {
            if (!el) return null;
            return el.tagName.toLowerCase() + (el.id ? '#' + el.id : '')
              + [...el.classList].slice(0, 4).map(c => '.' + c).join('');
          };
          const styles = [], blocked = [];
          function visit(rules, source) {
            for (const rule of rules) {
              styles.push({ source, text: rule.cssText });
              if (rule.cssRules) visit(rule.cssRules, source);
            }
          }
          for (const sheet of document.styleSheets) {
            try { visit(sheet.cssRules, sheet.href || 'inline'); }
            catch (e) { blocked.push({ href: sheet.href, reason: String(e) }); }
          }
          const motion = [], visuals = [];
          for (const el of document.querySelectorAll('*')) {
            const s = getComputedStyle(el);
            if (s.animationName !== 'none' || (s.transitionDuration.split(',').some(v => parseFloat(v) > 0))) {
              motion.push({ selector: selector(el), animation: s.animation, transition: s.transition,
                transform: s.transform, transformOrigin: s.transformOrigin, perspective: s.perspective });
            }
            if (el.matches('canvas,svg,video,iframe')) visuals.push({ selector: selector(el),
              width: el.getBoundingClientRect().width, height: el.getBoundingClientRect().height,
              src: el.getAttribute('src') });
          }
          const animations = document.getAnimations().map(a => ({
            target: selector(a.effect?.target), playState: a.playState,
            timing: a.effect?.getTiming(), keyframes: a.effect?.getKeyframes()
          }));
          return { url: location.href, title: document.title, scripts: [...document.scripts].map(s => ({
              src: s.src, type: s.type, inline: s.src ? null : s.textContent })),
            links: [...document.querySelectorAll('a[href]')].map(a => ({ text: a.textContent.trim(), href: a.href })),
            images: [...document.images].map(i => ({ src: i.currentSrc || i.src, srcset: i.srcset, alt: i.alt })),
            iframes: [...document.querySelectorAll('iframe')].map(i => ({ src: i.src, title: i.title })),
            styles, blockedStylesheets: blocked, motion, animations, visuals };
        });
        await writeFile(`${prefix}.json`, JSON.stringify({ label, ...data }, null, 2));
      } catch (err) { errors.push({ label, frame: frame.url(), error: String(err) }); }
    }
    try { await current.screenshot({ path: `${root}/snapshots/${id}-${pi}.png`, fullPage: true }); }
    catch (err) { errors.push(String(err)); }
  }
}
try {
  await page.goto(target, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForTimeout(4000);
  await snapshot('initial');
  const rl = createInterface({ input: stdin, output: stdout });
  console.log('Nyisd meg mindkét katalógust, lapozz, próbáld ki a nagyítást és a teljes képernyőt.');
  console.log('Ne jelentkezz be és ne adj meg személyes adatot. Nem minden kattintás mellékhatásmentes.');
  while (true) {
    const command = await rl.question('Enter = pillanatkép; mobile = mobilnézet; desktop = asztali; done = befejezés: ');
    if (command.trim() === 'done') break;
    if (command.trim() === 'mobile' || command.trim() === 'desktop') {
      const mobile = command.trim() === 'mobile';
      for (const p of context.pages()) await p.setViewportSize(mobile ? { width: 390, height: 844 } : { width: 1440, height: 1000 });
      await page.waitForTimeout(1000);
    }
    await snapshot(command || 'manual');
  }
  rl.close();
  await snapshot('final');
} catch (err) { errors.push(String(err)); }
finally {
  await browser.close();
  while (pending.size) await Promise.allSettled([...pending]);
  await writeFile(`${root}/manifest.json`, JSON.stringify({ target, capturedAt: new Date().toISOString(),
    totalSavedBytes: total, resources: records, errors }, null, 2));
  console.log(`Mentve: ${records.filter(r => r.file).length} fájl, ${total} bájt. Lásd: ${root}/manifest.json`);
}
