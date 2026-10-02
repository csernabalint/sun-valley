import { mkdir, copyFile } from 'node:fs/promises';
await mkdir('demo/vendor', { recursive: true });
await copyFile('node_modules/page-flip/dist/js/page-flip.browser.js', 'demo/vendor/page-flip.browser.js');
await copyFile('node_modules/page-flip/LICENSE', 'demo/vendor/LICENSE-page-flip');
console.log('A helyi lapozómotor és licence bemásolva.');
