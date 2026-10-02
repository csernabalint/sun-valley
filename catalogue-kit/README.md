# Katalógus-rekreációs csomag

## Státusz és korlátok

Ez saját alapimplementáció és helyben futtatható gyűjtőeszköz, NEM az eredeti Pantastico forráskód archívuma és NEM pixelpontos másolat. Az eredeti oldalból a két katalógus megnevezése és a letöltési lehetőség igazolható. A motor, az iframe-ek, a PDF URL-ek és az animációs paraméterek nincsenek azonosítva.

A gyűjtőt és a demót ebben a környezetben böngészőben nem futtattuk. A motor külön npm-telepítéssel érkezik; a ZIP nem tartalmaz harmadik fél letöltött könyvtárát. Nincs automatikus GitHub-módosítás.

## Indítás

Node.js és npm, illetve a példabeli kiszolgálóhoz Python 3 szükséges.

```bash
npm install
npm run vendor
npm run serve
```

Nyisd meg a helyi kiszolgáló /demo/ útvonalát a 8080-as porton. Az első telepítés után a demo helyi JavaScriptet használ, nem CDN-t. Commitold az npm install során keletkező package-lock.json-t; ismételt telepítéskor használj npm ci-t.

## Eredeti megvalósítás feltérképezése

```bash
npx playwright install chromium
npm run audit -- https://www.pantastico.com/hu/katalogus
```

Egy friss, nem bejelentkezett böngésző nyílik. Nyisd meg mindkét katalógust, lapozz több oldalt, ellenőrizd a nagyítást, a teljes képernyőt és a mobilnézetet. A terminálban Enter ment pillanatképet, mobile és desktop váltja a viewportot, done lezárja a gyűjtést. A mobile parancs csak méretet változtat, nem teljes érintéses készülékemuláció.

Csak a kézzel bejárt működéshez ténylegesen betöltődő, sikeres GET-válaszokat menti. Nem tölt le minden lehetséges katalógusoldalt, nem hajt végre hozzáférés-megkerülést, nem crawlolja a teljes webhelyet. Nem kattint automatikusan gombokra. Ne adj meg személyes adatot és ne jelentkezz be; a kézi kattintásoknak lehet mellékhatása. Service worker tiltva van, ami egyes oldalak működését megváltoztathatja.

Fájlkorlát: 25 MB; összes mentési keret: 200 MB. A kimaradó válaszokat a manifest jelzi. A PDF letöltési események nem feltétlenül jelennek meg Response bodyként; ilyen esetben használd a normál böngészős letöltést. Nem próbálja automatikusan kikövetkeztetni és letölteni a source mapeket.

## Mit kapsz a futtatásból?

- audit-output/manifest.json: URL, MIME-típus, HTTP-státusz, mentett fájl, méret, SHA-256 és hibák.
- audit-output/assets/: a megfigyelt HTML-, JS-, CSS-, kép-, font-, média- és kisebb PDF-válaszok.
- audit-output/snapshots/: az oldal és iframe-ek aktuális DOM-ja, teljes oldali képernyőképek, scriptlista, képek, linkek, CSS-szabályok, számított animációk, Web Animations API keyframe-ek és canvas/SVG elemek.

A hálózati fájlmentés külön originről betöltött publikus fájlokat is rögzíthet; a CSSOM egyes külső stylesheet-eket biztonsági okból nem enged olvasni. A hiány a blockedStylesheets mezőben látható. Egy pillanatkép nem garantálja rövid animációk elkapását. Canvas/WebGL és requestAnimationFrame animációkból a keyframe-lista nem állítja vissza az algoritmust; ehhez az adott JS bundle elemzése kell. Minifikált kliensbundle nem azonos az eredeti komponensforrással, és szerveroldali kódot nem kapsz.

A mentett HTML és assetek nem alkotnak automatikusan működő offline klónt: URL-ek, importok, API-k, szerverfüggőségek és third-party embedek új bekötést igényelnek.

## Saját katalógus bekötése

A demo/app.js catalogues objektumában cseréld a title, pdf és pages mezőket. A pdf csak letöltési URL, nem kerül automatikusan renderelésre. A pages az előzetesen előállított, azonos oldalarányú oldalképek rendezett listája. Példa:

```js
bakery: {
  title: 'Saját termékkatalógus',
  pdf: 'assets/bakery/catalogue.pdf',
  pages: ['assets/bakery/page-001.webp', 'assets/bakery/page-002.webp']
}
```

A 2:3 méretarányt és az alapméreteket módosítsd a valódi kiadványhoz. Az oldalképekből nem lesz kereshető vagy képernyőolvasóval teljesen olvasható tartalom: legyen mellette megfelelően címkézett PDF vagy HTML-terméklista. Nagy katalógushoz ez a teljes képlistát használó demo kevés; tervezz lapozásközeli betöltést és memóriafelszabadítást. Élő PDF-renderelés külön, PDF.js-alapú feladat, nincs implementálva ebben a csomagban.

## Saját animációk és funkciók

- Könyvszerű lapozás, húzás és lapozási árnyék: page-flip motor.
- Kemény borító: data-density=hard és showCover.
- Borító hover: saját CSS perspektíva, rotateY, translateY és box-shadow transition.
- Mobil egyoldalas nézet: usePortrait és stretch méretezés.
- Modális olvasó: natív dialog; bezárás és fókuszvisszaadás.
- Előző/következő, billentyűzet, oldalszámláló és teljes képernyő.
- Csökkentett mozgás: a gombok animáció nélküli turn metódust használnak; húzás tiltva, CSS transition kikapcsolva.

Nem implementált: zoom/pan, teljes szöveges keresés, bélyegképsáv, dinamikus PDF-renderelés, analytics, backend. A bemutató színei, árnyékai és időzítései saját tervezési döntések, nem mért Pantastico-paraméterek.

## GitHub-integráció

Előbb nézd meg a célrepó frameworkjét, fájlszerkezetét és publikálási útvonalát. Ne cseréld le vakon a meglévő főoldalt. A demo külön útvonalként is integrálható. Relatív asset URL-eket használj, hogy projekt-alapú publikálási útvonalon se törjenek el.

A vendor könyvtár mellett tartsd meg a page-flip licencét. Ne commitold az audit-output mappát: a fájlok és URL-ek személyes adatokat, azonosítókat vagy nem újrahasznosítható harmadik fél tartalmat tartalmazhatnak. Saját képekkel, szövegekkel és márkajelzéssel dolgozz; a publikus letölthetőség nem jelent újraközlési engedélyt.

Javasolt commitok: feat(catalogue): add isolated viewer; feat(catalogue): wire own assets; test(catalogue): validate navigation and mobile layout.

## Ellenőrzési lista

- 390 px és 1440 px szélességnél nincs vízszintes túllógás.
- Első és utolsó oldal, egy- és kétoldalas nézet helyes.
- Gyors ismételt kattintás nem indít egymásra lapozásokat.
- Escape bezár, Tab a dialogban marad, fókusz visszakerül a megnyitó gombra.
- Csökkentett mozgás preferenciával nincs animált lapozás.
- Teljes képernyő, kilépés és ablakátméretezés ellenőrizve valódi böngészőben.
- Hiányzó kép vagy motor érthető hibát mutat.
- A PDF link és a saját oldalképek valóban elérhetők.
- A képes tartalomhoz akadálymentes alternatíva rendelkezésre áll.
- A motor licence és az assetek felhasználási joga ellenőrizve.

## Források

- Pantastico referencia: https://www.pantastico.com/hu/katalogus
- Lapozómotor és teljes nyílt forrás: https://github.com/Nodlik/StPageFlip
- Motor API és beállítások: https://nodlik.github.io/StPageFlip/
- Böngészős gyűjtés API: https://playwright.dev/docs/api/class-response és https://playwright.dev/docs/api/class-page
