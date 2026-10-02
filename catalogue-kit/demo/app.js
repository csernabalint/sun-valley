// Sun Valley Zrt. B2B Termékkatalógus
const catalogues = {
  bakery: {
    title: 'Sun Valley B2B Termékkatalógus',
    pdf: '../../assets/Sun_Valley_B2B_Prospektus.pdf',
    pages: [
      'assets/prospectus/page-001.png',
      'assets/prospectus/page-002.png',
      'assets/prospectus/page-003.png',
      'assets/prospectus/page-004.png'
    ]
  },
  gastro: {
    title: 'Gastro & Cukrászati Katalógus',
    pdf: '../../assets/Sun_Valley_B2B_Prospektus.pdf',
    pages: [
      'assets/prospectus/page-001.png',
      'assets/prospectus/page-002.png',
      'assets/prospectus/page-003.png',
      'assets/prospectus/page-004.png'
    ]
  }
};
const dialog = document.querySelector('#viewer');
const counter = document.querySelector('#counter');
const previous = document.querySelector('#previous'), next = document.querySelector('#next');
const reduced = matchMedia('(prefers-reduced-motion: reduce)');
let flip = null, busy = false, trigger = null;
function downloadLink(link, url) {
  link.hidden = !url;
  if (url) { link.href = url; link.setAttribute('download', ''); }
  else link.removeAttribute('href');
}
for (const [id, config] of Object.entries(catalogues)) downloadLink(document.querySelector(`[data-pdf="${id}"]`), config.pdf);
function update() {
  if (!flip) return;
  const index = flip.getCurrentPageIndex(), count = flip.getPageCount();
  counter.textContent = `${index + 1} / ${count}`;
  previous.disabled = busy || index === 0;
  next.disabled = busy || index >= count - 1;
}
function demoPages(book, title) {
  for (let i = 0; i < 8; i++) {
    const el = document.createElement('section');
    el.className = 'page' + (i === 0 || i === 7 ? ' cover-page' : '');
    if (i === 0 || i === 7) el.dataset.density = 'hard';
    const content = document.createElement('div'); content.className = 'page-content';
    const label = document.createElement('small'); label.textContent = 'Saját márka – demonstráció';
    const heading = document.createElement('h3'); heading.textContent = i === 0 ? title : i === 7 ? 'Kapcsolat és rendelés' : `Termékcsoport ${i}`;
    const body = document.createElement('p'); body.textContent = 'Ezt a mintaoldalt cseréld saját termékfotókra, szövegekre vagy katalógusoldal-képekre.';
    const number = document.createElement('small'); number.textContent = String(i + 1);
    content.append(label, heading, body, number); el.append(content); book.append(el);
  }
}
async function openCatalogue(id, button) {
  const config = catalogues[id]; trigger = button;
  document.querySelector('#viewer-title').textContent = config.title;
  downloadLink(document.querySelector('#download'), config.pdf);
  document.querySelector('#error').hidden = true;
  dialog.showModal();
  if (!window.St?.PageFlip) {
    const error = document.querySelector('#error'); error.hidden = false;
    error.textContent = 'Hiányzik a helyi lapozómotor. Futtasd: npm install, majd npm run vendor.';
    previous.disabled = next.disabled = true; counter.textContent = ''; return;
  }
  const book = document.createElement('div'); book.id = 'book';
  document.querySelector('#book-slot').replaceChildren(book);
  const maxHeight = Math.max(240, Math.min(640, innerHeight - 220));
  const pageHeight = Math.min(600, maxHeight), pageWidth = pageHeight * 2 / 3;
  flip = new St.PageFlip(book, {
    width: pageWidth, height: pageHeight, size: 'stretch',
    minWidth: 150, maxWidth: pageWidth, minHeight: 225, maxHeight: pageHeight,
    showCover: true, usePortrait: true, drawShadow: !reduced.matches,
    flippingTime: 700, maxShadowOpacity: 0.3, mobileScrollSupport: false,
    useMouseEvents: !reduced.matches, disableFlipByClick: true
  });
  busy = false;
  flip.on('init', update); flip.on('flip', update); flip.on('changeOrientation', update);
  flip.on('changeState', e => { busy = e.data !== 'read'; update(); });
  if (config.pages.length) {
    for (const [i, src] of config.pages.entries()) {
      const el = document.createElement('section'); el.className = 'page';
      const img = document.createElement('img'); img.src = src;
      img.alt = `${config.title}, ${i + 1}. oldal`; img.draggable = false;
      img.addEventListener('error', () => { document.querySelector('#error').hidden = false;
        document.querySelector('#error').textContent = 'Legalább egy oldalkép nem tölthető be. Ellenőrizd az assets útvonalakat.'; });
      el.append(img); book.append(el);
    }
  } else demoPages(book, config.title);
  flip.loadFromHTML(book.querySelectorAll('.page'));
}
function move(direction) {
  if (!flip || busy) return;
  if (reduced.matches) direction > 0 ? flip.turnToNextPage() : flip.turnToPrevPage();
  else direction > 0 ? flip.flipNext() : flip.flipPrev();
}
for (const button of document.querySelectorAll('[data-catalogue]')) button.addEventListener('click', () => openCatalogue(button.dataset.catalogue, button));
previous.addEventListener('click', () => move(-1)); next.addEventListener('click', () => move(1));
document.querySelector('#close').addEventListener('click', () => dialog.close());
dialog.addEventListener('close', () => { if (flip) flip.destroy(); flip = null; busy = false; trigger?.focus(); });
dialog.addEventListener('keydown', e => {
  if (e.target.matches('input,textarea,select')) return;
  if (e.key === 'ArrowRight' || e.key === 'ArrowLeft') { e.preventDefault(); move(e.key === 'ArrowRight' ? 1 : -1); }
});
document.querySelector('#fullscreen').addEventListener('click', async () => {
  try { if (document.fullscreenElement) await document.exitFullscreen(); else await dialog.requestFullscreen(); }
  catch { document.querySelector('#error').hidden = false; document.querySelector('#error').textContent = 'A böngésző nem engedélyezte a teljes képernyőt.'; }
});
