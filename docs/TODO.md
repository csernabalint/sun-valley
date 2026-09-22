# Sun Valley – Fejlesztési Feladatlista & Visszajelzések (TODO.md)

**Dokumentum állapota:** Aktív végrehajtási terv  
**Utolsó frissítés:** 2026. szeptember 22. (Tipográfia és Színrendszer lezárva és élesítve)  
**Forrás:** Ügyfél / Menedzsment visszajelzések és /grill-me egyeztetés  
**Érintett fő komponens:** [`scripts/compile_v2.py`](file:///c:/Users/csern/Desktop/sun-valley/scripts/compile_v2.py) -> [`index.html`](file:///c:/Users/csern/Desktop/sun-valley/index.html)

---

## 1. Vezetői Összefoglaló & Főbb Változtatási Irányok

A beérkezett visszajelzések és a lefolytatott `/grill-me` döntések alapján a weboldal arculata és struktúrája átalakul:
- **Közvetlenebb, barátságosabb hangvétel:** A merev, túlzottan steril ipari tónus helyett egy prémium manufaktúra jellegű, gasztronómiailag vonzóbb stílus.
- **Tipográfiai hibrid modell (ÉLESÍTVE):** `Georgia, 'Times New Roman', serif` a főcímekhez és kártyacímekhez; `Inter, sans-serif` a folyószövegekhez, navigációhoz és gombokhoz.
- **Harmonizált gyümölcsszínek (ÉLESÍTVE):** A korábbi sötétbordó helyett meleg gyümölcspiros (**`#a3392e`**), a gomboknál **`#872c24`** hover állapot, a harsány narancs helyett mély terrakotta tónus (**`#91372d`**).
- **Termékstruktúra radikális egyszerűsítése:** Bonyolult mátrix helyett két tiszta kategória:
  1. *Egyszerű kenhető extradzsemek*
  2. *Sütésálló dzsemek* (180–220 °C, 5–10–20–200 kg kiszerelésben)
- **Fejléc megtisztítása:** "ZRT." levéve (csak `SUN VALLEY`), vörös felső sáv és direkt kontaktadatok kivezetése a fejlécből; német nyelv törlése.
- **Képteljesítmény & renderelési sebesség:** A több megabájtos tömörítetlen képek miatti szaggatás felszámolása WebP konverzióval.

---

## 2. Részletes Feladatlista (Task Breakdown)

### 2.1. Fejléc & Navigáció (Header & Navigation)
- [x] **Fejléc cégnév módosítása:**
  - *Feladat:* A `SUN VALLEY ZRT.` feliratból a `ZRT.` utótag levéve, a fejlécben tisztán `SUN VALLEY` jelenik meg.
  - *Státusz:* **KÉSZ** (Átvezetve a `scripts/compile_v2.py`-ban és `index.html`-ben).
- [x] **Sun Valley felirat színének világosítása:**
  - *Feladat:* A korábbi mélybordó helyett az új, élénk gyümölcspiros (**`#a3392e`**) szín és a gomboknál a **`#872c24`** hover élesítve.
  - *Státusz:* **KÉSZ** (CSS token `--sv-burgundy` és gomb hover szabályok élesítve).
- [ ] **Felső vörös sáv teljes kivezetése:**
  - *Feladat:* A fejléc feletti sötétvörös információs sáv (`#top-bar`, `var(--sv-burgundy-dark)`) szűnjön meg ("headerböl vörös cucc mehet ki").
  - *Érintett:* `scripts/compile_v2.py` (top-bar konténer törlése, fejléc padding és reveal-on-scroll igazítása).
- [ ] **Telefonszám és e-mail eltávolítása a fejlécből:**
  - *Feladat:* A `+36 30 899 8548` és az e-mail cím ne jelenjen meg a fejlécben. Ezek kizárólag a **Kapcsolat** szekcióban/fülön kapjanak helyet.
- [ ] **Nyelvi választó átalakítása (Csak HU + EN, német törlése):**
  - *Feladat:* A trilingvális (HU/EN/DE) kapcsolóból a német (`DE`) nyelv kivezetése. Kizárólag magyar és angol nyelv legyen elérhető ("Angol legyen csak ne német").
  - *Érintett:* `scripts/compile_v2.py` nyelvkapcsoló gombok és szótárak.
- [ ] **Fejléc CTA optimalizálás:**
  - *Feladat:* A fejlécben lévő "Próbagyártási Minta" gomb igazítása az új egyszerűsített koncepcióhoz.

---

### 2.2. Vizuális Alapok, Háttér & Tipográfia
- [x] **Négyzetes / Grid háttér megtartása:**
  - *Státusz:* **KÉSZ** (Megtartva; a finom 40x40px rácsvonalak színe harmonizálva az új gyümölcspiros tónushoz: `rgba(163, 57, 46, 0.035)`).
- [x] **Ribbon / Kiemelő sáv megőrzése:**
  - *Státusz:* **KÉSZ** (Megtartva).
- [x] **Betűtípuscsalád (Tipográfia) lecserélése:**
  - *Feladat:* Hibrid prémium modell bevezetése:
    - Címek (H1–H3), fejléc márkanév, kártyacímek: **`Georgia, 'Times New Roman', serif`**
    - Törzsszövegek, navigáció, gombok, űrlapok: **`Inter, sans-serif`**
    - Műszaki adatok, kódok: **`JetBrains Mono`**
  - *Státusz:* **KÉSZ** (Google Fonts `Inter` behúzva, `.font-syne` átirányítva Georgiára).
- [x] **Színrendszer & Akcentusok frissítése:**
  - *Elsődleges piros:* **`#a3392e`** (volt `#5F2125` helyett)
  - *Gomb hover:* **`#872c24`** (kizárólag gomboknál)
  - *Kiemelő akcentus:* **`#91372d`** (volt `#E36527` narancs helyett)
  - *Természet zöld:* **`#2D3628`** (megtartva a funkcionális badge-ekhez)
  - *Státusz:* **KÉSZ** (Tokenek és 70+ inline színkód átírva a teljes kódbázisban).
- [ ] **Képi mikroszaggatás (Stutter/Lag) megszüntetése:**
  - *Probléma:* Görgetéskor és betöltéskor apró akadás tapasztalható ("Pici szaggatás a képek esetében").
  - *Ok-okozati feltárás:* Az `assets/` mappában lévő képek mérete extrém nagy (összesen >15 MB: `lekvaros-bukta.jpg` 5,5 MB, `retes.jpg` 2,65 MB, `apricot.jpg` 1,96 MB, `sun-valley-logo.png` 1,65 MB, `jam.jpg` 1,32 MB).
  - *Teendők:*
    - Képek átméretezése és WebP formátumra tömörítése (minőségi veszteség nélkül max 150–300 KB / kép).
    - Fix `width` és `height` attribútumok hozzáadása a layout shift (CLS) elkerülésére.
    - Szigorú `loading="lazy"` és `decoding="async"` alkalmazása.

---

### 2.3. Cégadatok & Bizalmi Sávok Finomhangolása
- [ ] **Zöld sáv kivezetése:**
  - *Feladat:* A sötétzöld háttérszínű céginformációs sáv (`var(--sv-green-dark)`, `#2D3628`) megszüntetése ("Zöld csík nem kell -> céginfós dolgok").
- [ ] **Árbevételi adat eltávolítása:**
  - *Feladat:* Az `1,1 – 1,3 Mrd Ft Éves árbevétel (Stabil tőkeerő)` statisztikai elem és szöveges hivatkozásai teljes mértékben kerüljenek le az oldalról.

---

### 2.4. Termékportfólió & Katalógus Újratervezés
- [ ] **Kétfókuszú portfólió-struktúra kialakítása:**
  - *Kategória 1:* **Egyszerű kenhető extradzsemek**
  - *Kategória 2:* **Sütésálló dzsemek** (180 °C – 220 °C-ig hőtartó)
- [ ] **Egységes specifikáció az ízek mentén:**
  - *Feladat:* Az adott kategórián belül felsorolt ízek mindegyikénél azonos paraméterkészlet érvényesüljön (nem kell ízenként eltérő egyedi táblázat).
- [ ] **Kiszerelések feltüntetése:**
  - *Értékek:* `5 kg` • `10 kg` • `20 kg` • `200 kg` (vödrös, kartontömb, hordós).
- [ ] **Brix és pH értékek ideiglenes kivezetése:**
  - *Feladat:* A szárazanyagtartalom (°Brix) és kémhatás (pH) mezők egyelőre ne jelenjenek meg a publikus termékkártyákon ("brix ph nem kell egyelőre").
- [ ] **Termékkatalógus elrendezésének átalakítása:**
  - *Layout:* **Bal oldalon termékfotó, jobb oldalon a specifikáció / leírás** ("termékkatalógus bal oldalon kép jobb oldalon a specvifikáció").
- [ ] **Közvetlenebb, kevésbé ipari hangvétel:**
  - *Feladat:* A két termékcsalád leírását közvetlenebb, kézműves-ipari egyensúlyt teremtő stílusban megfogalmazni.
- [ ] **Referenciaoldalak szerinti megoldások vizsgálata:**
  - *[Pantastico (pantastico.com)](https://www.pantastico.com/):* 100%-ban magyar sütőipari vállalat, természetes összetevők, tiszta prémium megjelenés.
  - *[Frigotti (frigotti.hu)](https://frigotti.hu/):* Fagyasztott pékáru termékkatalógus, tiszta vizuális kategóriabontás.
  - *[Hesi (hesi.hu/termekeink)](https://hesi.hu/termekeink/):* Áttekinthető, lényegretörő B2B termékprezentáció.
- [ ] ❓ **NYITOTT KÉRDÉS (Andris egyezteti):**
  - *Kérdés:* Szükség van-e a publikus weboldalon részletes ipari specifikációkra / laboratóriumi paraméterekre (TDS modal formájában), vagy a letisztult összefoglaló elégséges?

---

### 2.5. Cégbemutató & Technológia Szekció Átdolgozása
- [ ] **"Cégünkről & Technológiák" szekció újratervezése:**
  - *Visszajelzés:* A jelenlegi elrendezés széteső / nem megfelelő ("cégünkről -> bemutató a technológiák (elrendezés itt szutyok)").
  - *Feladat:* A 4 kártyás technológiai bemutató és a móri üzem ismertetőjének egybefüggő, átlátható, modern elrendezésű újraépítése.
- [ ] **Andris ChatGPT-s alapjának integrálása:**
  - *Feladat:* A szövegezés és struktúra alapjául Andris ChatGPT-s anyagának / vázlatának használata ("Legyen az andris chatgpt alapja").

---

### 2.6. Egyedi Fejlesztés (R&D) Szekció
- [ ] **Közös fejlesztési blokk megtartása:**
  - *Státusz:* Pozitív visszajelzés ("Ön közös fejlesztése design meg a kép szimpi volt -> baracklekváros kaszis -> első rész megtartása").
  - *Feladat:* Az *"Az Ön Ötlete. Közös Ipari Fejlesztés."* szakasz első bevezető részének, a baracklekváros/kajszis képnek és az alapkoncepciónak a megőrzése.

---

### 2.7. Űrlapok, Kapcsolat & Dokumentumok
- [ ] **"Kérjen Tesztmintát Saját Gyártósorára" szekció kivezetése:**
  - *Feladat:* Az önálló, nehézkes mintaigénylő űrlapszakasz eltávolítása ("Kérjen Tesztmintát Saját Gyártósorára -> ez nem kell").
- [ ] **E-mail cím aktualizálása:**
  - *Új cím:* `ifj.vecsei.andras@sunvalley.hu` (a korábbi `vecsei.andras@sunvalley.hu` helyett).
- [ ] **Kapcsolati blokk fókuszba helyezése:**
  - *Feladat:* Minden közvetlen elérhetőség (telefonszám: `+36 30 899 8548`, vezetékes: `+36 22 400 984`, e-mail: `ifj.vecsei.andras@sunvalley.hu`) dedikáltan a Kapcsolat szekcióban összpontosuljon.
- [ ] **Prospektus (prezentáció) cseréje:**
  - *Feladat:* A jelenleg letölthető `Sun_Valley_B2B_Prospektus_V1_4.pptx` helyére az új hivatalos prospektus / katalógus anyag beillesztése ("Prospectus kicserélni").
- [ ] **Süti (Cookie) sáv megvalósítása:**
  - *Feladat:* Letisztult, diszkrét Cookie / Adatvédelmi tájékoztató sáv beépítése ("Cookie").

---

## 3. Nyitott Kérdések & Döntési Pontok

| # | Téma | Leírás | Felelős | Státusz |
|---|---|---|---|---|
| **K-01** | Ipari laborparaméterek | Kell-e részletes TDS specifikáció a publikus oldalon, vagy csak a főkategóriák és kiszerelések? | Andris | Folyamatban |
| **K-02** | Új Prospektus fájl | Milyen formátumú (PDF vs PPTX) és tartalmú anyag váltja a V1.4 PPTX-et? | Andris / Bálint | Anyag beérkezésére vár |
| **K-03** | Betűtípus és Színek | Georgia (címek) + Inter (szöveg), #a3392e (piros), #91372d (akcentus) | Design / Bálint | **LEZÁRVA & ÉLESÍTVE** |
| **K-04** | Andris ChatGPT forrás | A pontos ChatGPT-s szövegtörzs beillesztése a cégbemutató szekcióba. | Andris / Bálint | Áttekintés alatt |

---

## 4. Fejlesztési Szabályok & Compiler Fegyelem

1. **Egységes forráskód-kezelés:** Minden HTML változtatást kötelezően a [`scripts/compile_v2.py`](file:///c:/Users/csern/Desktop/sun-valley/scripts/compile_v2.py) compiler scriptben kell elvégezni. A build futtatásával generálódik az [`index.html`](file:///c:/Users/csern/Desktop/sun-valley/index.html).
2. **Reszponzivitás és túlcsordulási garancia:** Zero horizontal overflow invariant (375px, 768px, 1024px, 1440px).
3. **Képoptimalizálási előírás:** Egyetlen publikált kép sem haladhatja meg az 500 KB-ot (cél: 100–250 KB WebP).
