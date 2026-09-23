# Sun Valley – Fejlesztési Feladatlista & Visszajelzések (TODO.md)

**Dokumentum állapota:** Aktív végrehajtási terv  
**Utolsó frissítés:** 2026. szeptember 23. (Termékkatalógus elrendezés letisztítva, kártyán belüli oldalszámláló élesítve, német nyelv 100%-ban kivezetve, tesztmintakérés eltávolítva)  
**Forrás:** Ügyfél / Menedzsment visszajelzések és /grill-me egyeztetés  
**Érintett fő komponens:** [`scripts/compile_v2.py`](file:///c:/Users/csern/Desktop/sun-valley/scripts/compile_v2.py) -> [`index.html`](file:///c:/Users/csern/Desktop/sun-valley/index.html)

---

## 1. Vezetői Összefoglaló & Főbb Változtatási Irányok

A beérkezett visszajelzések és a lefolytatott `/grill-me` döntések alapján a weboldal arculata és struktúrája átalakul:
- **Közvetlenebb, barátságosabb hangvétel:** A merev, túlzottan steril ipari tónus helyett egy prémium manufaktúra jellegű, gasztronómiailag vonzóbb stílus.
- **Tipográfiai modell (ÉLESÍTVE):** `Montserrat, 'Montserrat Placeholder', sans-serif` a főcímekhez, kártyacímekhez és elérhetőségekhez; `Inter, sans-serif` a folyószövegekhez és navigációhoz; `Inter Tabular (tabular-nums)` a műszaki adatokhoz.
- **Harmonizált gyümölcsszínek (ÉLESÍTVE):** A korábbi sötétbordó helyett meleg gyümölcspiros (**`#a3392e`**), a gomboknál **`#872c24`** hover állapot, a harsány narancs helyett mély terrakotta tónus (**`#91372d`**), sötét szövegként meleg eszpresszó (**`rgb(50, 45, 36)`**), szövegkijelöléshez barackkrém (**`#f1c7a6`**).
- **Termékkatalógus letisztítása (ÉLESÍTVE):** 
  - Felső fülsor és fenti mini-léptető eltávolítva.
  - A 3 termékkategória egy helyen váltakozik.
  - Kártyán belüli oldalszámláló (`01 / 03`, `02 / 03`, `03 / 03`) alul középen, elegáns kapszula formában.
  - Léptetés a kártyát szegélyező bal-jobb nyilakkal és az alsó indikátorpontokkal.
- **Fejléc & Navigáció precízió (ÉLESÍTVE):** "ZRT." levéve a logóból, egységes `Sun Valley` írásmód, vörös felső sáv és direkt kontaktadatok kivezetve; HU/EN nyelvváltoztató és a Kapcsolat gomb egységes 36px magasságban; német nyelv (`de`) 100%-ban kivezetve a teljes kódbázisból.
- **Hero tipográfia & térköz (ÉLESÍTVE):** A "200 °C felett sem forr ki." és az "Ipari sütésálló gyümölcstöltelékek közvetlenül a gyártótól." sorok között 14–16px elkülönülő térköz, az alcím nem bold (`font-normal`).
- **Tesztminta kérés teljes megszüntetése (ÉLESÍTVE):** Minden mintakérési hivatkozás helyett közvetlen kapcsolatfelvétel, technológiai egyeztetés és árajánlatkérés.
- **Képteljesítmény & renderelési sebesség (ÉLESÍTVE):** A korábbi több megabájtos képek WebP konverzióval és képoptimalizálással felgyorsítva, CLS és scroll jank elhárítva.

---

## 2. Részletes Feladatlista (Task Breakdown)

### 2.1. Fejléc & Navigáció (Header & Navigation)
- [x] **Fejléc cégnév és márkanév formázása:**
  - *Feladat:* A `SUN VALLEY` csupa nagybetűs írásmód helyett mindenhol **`Sun Valley`** (kizárólag az 'S' és 'V' nagybetű, a többi kisbetű; a fejlécből a `Zrt.` levéve).
  - *Státusz:* **KÉSZ** (Átvezetve a fejlécben, láblécben és modális ablakokban).
- [x] **Sun Valley felirat színének világosítása:**
  - *Feladat:* A korábbi mélybordó helyett az új, élénk gyümölcspiros (**`#a3392e`**) szín és a gomboknál a **`#872c24`** hover élesítve.
  - *Státusz:* **KÉSZ** (CSS token `--sv-burgundy` és gomb hover szabályok élesítve).
- [x] **Felső vörös sáv teljes kivezetése:**
  - *Feladat:* A fejléc feletti sötétvörös információs sáv (`#top-bar`, `var(--sv-burgundy-dark)`) megszüntetve ("headerböl vörös cucc mehet ki").
  - *Státusz:* **KÉSZ** (Top-bar konténer törölve, a fejléc letisztult egyetlen modern sávvá, a dinamikus scroll-spacer automatikusan kalibrálódik).
- [x] **Telefonszám és e-mail eltávolítása a fejlécből:**
  - *Feladat:* A `+36 30 899 8548` és az e-mail cím levéve a fejlécből és a mobil drawerből. Kizárólag a **Kapcsolat** szekcióban kapnak helyet.
  - *Státusz:* **KÉSZ**.
- [x] **Nyelvi választó átalakítása (Csak HU + EN, német törlése):**
  - *Feladat:* A trilingvális (HU/EN/DE) kapcsolóból a német (`DE`) nyelv kivezetve. Kizárólag magyar és angol nyelv érhető el ("Angol legyen csak ne német").
  - *Státusz:* **KÉSZ** (Fejléc gombok és a JS `setLanguage` motor átállítva HU/EN-re).
- [x] **Fejléc CTA optimalizálás:**
  - *Feladat:* A fejléc akciógombja a nehézkes mintaigénylés helyett közvetlenül a Kapcsolathoz navigál (`#kapcsolat`).
  - *Státusz:* **KÉSZ**.
- [x] **Fejléc szalag (Ribbon) navigáció egységesítése & „200 Celsius” levétele:**
  - *Feladat:* A több sorba törő, szétesett menüpontok egységesítése egyetlen tiszta vízszintes sorba (`whitespace-nowrap`), azonos magasságban (28px) és azonos bázisvonalon (`y: 23px`).
  - *200 Celsius levétele:* A `Technológia (200°C)` menüpontból a `(200°C)` eltávolítva mind a desktop navigációban, mind a mobilos menüben és a fordítási szótárakban (`Technológia` / `Technology`).
  - *Szótár feliratok letisztítása:* `nav_contact` egységesen `Kapcsolat` (a korábbi hosszú „Gyártóüzem & Elérhetőség” helyett), `nav_products` `Termékek & Katalógus` (angolul `Products & Catalog`).
  - *Státusz:* **KÉSZ** (CDP teszttel verifikálva).

---

### 2.2. Vizuális Alapok, Háttér & Tipográfia
- [x] **Négyzetes / Grid háttér megtartása:**
  - *Státusz:* **KÉSZ** (Megtartva; a finom 40x40px rácsvonalak színe harmonizálva az új gyümölcspiros tónushoz: `rgba(163, 57, 46, 0.035)`).
- [x] **Ribbon / Kiemelő sáv megőrzése:**
  - *Státusz:* **KÉSZ** (Megtartva).
- [x] **Betűtípuscsalád (Tipográfia) átdolgozása:**
  - *Feladat:* Modern, letisztult arculat bevezetése:
    - Címek (H1–H3), fejléc márkanév, kártyacímek, e-mail és elérhetőségek: **`Montserrat, 'Montserrat Placeholder', sans-serif`** (a korábbi `Georgia` teljes mértékben lecserélve).
    - Törzsszövegek, navigáció, gombok, űrlapok: **`Inter, sans-serif`**
    - Műszaki adatok, kódok, badge-ek: **`Inter Tabular (tabular-nums)`** (a korábbi `JetBrains Mono` kivezetve).
  - *Státusz:* **KÉSZ** (Google Fonts `Montserrat` és `Inter` élesítve, `.font-syne` átállítva Montserrat-ra).
- [x] **Színrendszer & Akcentusok frissítése:**
  - *Elsődleges piros:* **`#a3392e`** (volt `#5F2125` helyett)
  - *Gomb hover:* **`#872c24`** (kizárólag gomboknál)
  - *Kiemelő akcentus:* **`#91372d`** (volt `#E36527` narancs helyett)
  - *Természet zöld:* **`#2D3628`** (megtartva a funkcionális badge-ekhez)
  - *Fekete / Sötét szövegszín:* **`rgb(50, 45, 36)`** (`#322d24`, a hideg `rgb(28, 25, 23)` helyett meleg eszpresszó / koromfekete)
  - *Szövegkijelölés (Selection):* **`#f1c7a6`** (barackkrém kiemelés kontrasztos sötétbordó szöveggel)
  - *Státusz:* **KÉSZ** (Tailwind stone-900, tokenek, CSS `::selection` és body osztályok frissítve).
- [x] **Képi mikroszaggatás (Stutter/Lag) megszüntetése:**
  - *Megoldás:*
    - Az összes fotó átméretezve max. 1440px felbontásra, magas minőségű Lanczos szűrővel.
    - Párhuzamos WebP és progresszív JPEG generálás: a korábbi **>15 MB-os képméret lecsökkent ~1 MB-ra** (90–97%-os adatmennyiség-csökkenés).
    - Explicit `width` és `height` attribútumok, `<picture>` tagek, `loading="lazy"` és `decoding="async"` bevezetve (CLS és scroll jank elhárítva).
  - *Státusz:* **KÉSZ**.

---

### 2.3. Cégadatok & Bizalmi Sávok Finomhangolása
- [x] **Zöld sáv kivezetése:**
  - *Feladat:* A sötétzöld háttérszínű céginformációs sáv (`var(--sv-green-dark)`, `#2D3628`) teljes mértékben eltávolítva ("Zöld csík nem kell -> céginfós dolgok").
  - *Státusz:* **KÉSZ**.
- [x] **Árbevételi adat eltávolítása:**
  - *Feladat:* Az `1,1 – 1,3 Mrd Ft Éves árbevétel (Stabil tőkeerő)` statisztikai blokk és szöveges hivatkozásai lekerültek az oldalról ("Ez kerüljön le: 1,1 – 1,3 Mrd Ft").
  - *Státusz:* **KÉSZ**.

---

#### 2.4. Termékportfólió & Katalógus Újratervezés
- [x] **Háromfókuszú portfólió-struktúra kialakítása:**
  - *Kategória 1:* **Kenhető lekvárok** (Hideg technológia, linzerekhez, piskótákhoz, tortalapokhoz)
  - *Kategória 2:* **Sütésálló lekvárok** (180 °C – 220 °C, formamegtartó, buktákhoz, rétesekhez, leveles tésztákhoz)
  - *Kategória 3:* **Extra dzsemek** (Magas gyümölcstartalom, válogatott gyümölcsdarabos textúra prémium finompékárukhoz)
  - *Státusz:* **KÉSZ** (Mindhárom kategóriakártya élesítve bal oldali nagy felbontású termékfotóval, jobb oldali leírással és specifikációval).
- [x] **Egységes specifikáció az ízek mentén:**
  - *Feladat:* Az adott kategórián belül felsorolt ízek mindegyikénél azonos paraméterkészlet érvényesül.
  - *Státusz:* **KÉSZ** (Kategóriánként felsorolt ízek egységes mátrixszal).
- [x] **Kiszerelések feltüntetése:**
  - *Értékek:* `5 kg` • `10 kg` • `20 kg` • `200 kg` (vödrös, kartontömb, hordós kiszerelések).
  - *Státusz:* **KÉSZ**.
- [x] **Brix és pH értékek kivezetése a publikus kártyákról:**
  - *Feladat:* A szárazanyagtartalom (°Brix) és kémhatás (pH) mezők kivezetve a publikus termékkártyákról ("brix ph nem kell egyelőre").
  - *Státusz:* **KÉSZ**.
- [x] **Termékkatalógus elrendezésének átalakítása:**
  - *Layout:* **Bal oldalon termékfotó, jobb oldalon a specifikáció / leírás** ("termékkatalógus bal oldalon kép jobb oldalon a specvifikáció").
  - *Státusz:* **KÉSZ** (Reszponzív 12 oszlopos grid, asztalon 6-6 megosztás, mobilon zökkenőmentes törés túlcsordulás nélkül).
- [x] **Lapozható katalógus cím, paginátor és 3D lapozás animáció:**
  - *Cím & szekció:* "Termékportfólió & Minőségi Specifikációk" (főcím: "Lekvárok felhasználás szerint").
  - *Egy helyen lévő 3 kártya bal-jobb léptető nyilakkal:* A három termékkategória egyetlen fókuszált kártyahelyen jelenik meg, mindkét oldalon feltűnő, kör alakú bal és jobb oldali léptető nyilakkal (`#cat-side-prev`, `#cat-side-next`).
  - *Reszponzivitás:* Asztali nézetben a kártyát szegélyezik, mobilon a termékfotó oldalain érhetők el kényelmes hüvelykujj-eléréssel, nulla vízszintes túlcsordulással (`scrollWidth === clientWidth`).
  - *3D animáció:* Pantastico és ChatGPT ihlette könyvlapozási animáció (CSS perspective, 3D flip transform, árnyék és fény effekt, érintéses swipe és billentyűzet-navigáció).
  - *Státusz:* **KÉSZ** (Élesítve a compilerben és CDP tesztekkel verifikálva).
- [x] **Lapozható katalógus felső fülsorának kivezetése és az oldalszám kártyán belüli elhelyezése:**
  - *Feladat:* A lapozható termékkatalógus felső fülsávjának (`tab-btn-spreadable`, `tab-btn-bake-stable`, `tab-btn-extra-jam`) és a fenti mini-léptetőnek a teljes törlése.
  - *Oldalszámláló a kártyán belül:* Az oldalszám (`01 / 03`, `02 / 03`, `03 / 03`) közvetlenül a kártya alsó részén, középre igazítva kapott helyet, diszkrét kapszula formátumban.
  - *Léptetés kizárólag a bal-jobb nyilakkal:* A kártyák közötti navigáció kizárólag a kártyát kétoldalt szegélyező feltűnő nyilakkal és az alatta lévő indikátorpontokkal történik.
  - *Státusz:* **KÉSZ** (Compilerben átvezetve, tesztekkel és képernyőképekkel verifikálva).
- [x] **Német nyelv és minden német függőség teljes törlése:**
  - *Feladat:* A német nyelv (`de`) 100%-os kivezetése a teljes kódbázisból. A weboldal szigorúan kétnyelvű (magyar és angol: `HU` és `EN`).
  - *Eltávolítva:* A teljes `translations.de` szótár, a termékek `de:` mezői, a TDS modál német feliratai, a német ternary ágak és a német tesztek.
  - *Státusz:* **KÉSZ** (Verifikálva: 0 db német függőség, tiszta HU/EN működés).
- [x] **Hero címsor és alcím térköz finomhangolása:**
  - *Feladat:* A "200 °C felett sem forr ki." és az "Ipari sütésálló gyümölcstöltelékek közvetlenül a gyártótól." sorok közötti távolság növelése (különálló blokkok, 14–16px rés), az egybelógás megszüntetése.
  - *Státusz:* **KÉSZ** (CDP/Puppeteer segítségével ellenőrizve és tesztelve).
- [x] **Fejléc gombok magasságának egységesítése:**
  - *Feladat:* A HU/EN nyelvi választó konténer és a "Kapcsolat" gomb egységes magasságának biztosítása (36px).
  - *Státusz:* **KÉSZ**.
- [x] **Közvetlenebb, kézműves-ipari hangvétel:**
  - *Feladat:* A három termékcsalád leírása szakmailag precíz, de barátságosabb, gasztronómiailag vonzó stílusban megfogalmazva.
  - *Státusz:* **KÉSZ** (Magyar és angol fordításokkal).
- [x] **Referenciaoldalak szerinti megoldások vizsgálata:**
  - *[Pantastico (pantastico.com)](https://www.pantastico.com/):* Természetes összetevők, tiszta prémium megjelenés adaptálva.
  - *[Frigotti (frigotti.hu)](https://frigotti.hu/):* Tiszta vizuális kategóriabontás beépítve.
  - *[Hesi (hesi.hu/termekeink)](https://hesi.hu/termekeink/):* Áttekinthető, lényegretörő B2B termékprezentáció átvéve.
  - *Státusz:* **KÉSZ**.

---

### 2.5. Cégbemutató & Technológia Szekció Átdolgozása
- [x] **"Cégünkről & Technológiák" szekció újratervezése:**
  - *Visszajelzés:* A korábbi elrendezés széteső volt ("cégünkről -> bemutató a technológiák (elrendezés itt szutyok)").
  - *Megoldás:* Létrehozva a dedikált `#cegunkrol` szekció közvetlenül a termékek után, valamint a `#technologia` szekció aszimmetrikus ipari elrendezéssel (Hero feature panel 200 °C hőtűréssel a bal oldalon, 3 műszaki pillér egymás mellett a jobb oldalon).
  - *Státusz:* **KÉSZ** (Fejléc navigációba beillesztve, reszponzivitás és túlcsordulás-mentesség ellenőrizve).
- [x] **Andris ChatGPT-s alapjának integrálása:**
  - *Feladat:* A cégbemutató és filozófia szövegezése Andris ChatGPT-s anyagának és a magyar B2B identitásnak a szintézisével épült fel (30+ év családi alapok, móri gyártóbázis, egyedi gépsorokra méretezett lekvárok és gyümölcstöltelékek).
  - *Státusz:* **KÉSZ** (Kétnyelvű HU/EN fordításokkal ellátva).

---

### 2.6. Egyedi Fejlesztés (R&D) Szekció
- [x] **Közös fejlesztési blokk megtartása & Színritmus (Pirosas -> Zöldes -> Pirosas):**
  - *Státusz:* **KÉSZ** (01: `var(--sv-burgundy)` -> 02: `var(--sv-green-dark)` -> 03: `var(--sv-burgundy)`).
  - *Tartalom:* Az *"Az Ön Ötlete. Közös Ipari Fejlesztés."* szakasz bevezető része, a baracklekváros/kajszis kép és a lépések átfogalmazva a tesztmintakérés helyett technológiai hangolásra és validációra.

---

### 2.7. Űrlapok, Kapcsolat & Dokumentumok
- [x] **Üzemi tesztminta kérése mindenhonnan kivezetve:**
  - *Feladat:* Minden hivatkozás, gombfelirat és leírás átállítva a mintakérés helyett kapcsolatfelvételre és árajánlatkérésre (Hero CTA: *Kapcsolatfelvétel & Ajánlatkérés*, Katalógus CTA: *Érdeklődés & Ajánlatkérés*, Kapcsolat leírás: *Árajánlatkérés, beszállítói partnerség és technológiai egyeztetés*, Navigáció: *Receptúra & Fejlesztés*, TDS modal: *Technológiai finomhangolás* és *Érdeklődés & Kapcsolatfelvétel*).
  - *Státusz:* **KÉSZ**.
- [x] **Hero alcím tipográfiájának letisztítása (Ne legyen bold):**
  - *Feladat:* A "200 °C felett sem forr ki." főcím alatti "Ipari sütésálló gyümölcstöltelékek közvetlenül a gyártótól." sor átállítva `font-normal` vastagságra a tiszta hierarchia érdekében.
  - *Státusz:* **KÉSZ**.
- [x] **"Kérjen Tesztmintát Saját Gyártósorára" szekció kivezetése:**
  - *Feladat:* Az önálló, nehézkes mintaigénylő űrlapszakasz eltávolítása ("Kérjen Tesztmintát Saját Gyártósorára -> ez nem kell"). Minden hivatkozás és CTA átirányítva közvetlenül a Kapcsolathoz.
  - *Státusz:* **KÉSZ**.
- [x] **E-mail cím aktualizálása:**
  - *Új cím:* `ifj.vecsei.andras@sunvalley.hu` (a korábbi `vecsei.andras@sunvalley.hu` helyett).
  - *Státusz:* **KÉSZ** (Átvezetve a Kapcsolat szekcióban és a levélküldési hivatkozásokban).
- [x] **Kapcsolati blokk egyszerűsített, kártyamentes nézete:**
  - *Feladat:* A korábbi különálló dobozok helyett az egyedi receptúra mintájára épülő, architekturális vertikális és horizontális elválasztóvonalakkal tagolt 3 oszlopos (01 Mobil, 02 E-mail, 03 Móri üzem & telephely) struktúra zöld háttéren (`var(--sv-green-dark)`).
  - *Adatpontok szűrése:* Adószám, Cégjegyzékszám és Pénzügyi besorolás törölve ("Továbbá nem kell bele Adószám, Cégjegyzékszám, Pénzügyi besorolás").
  - *Státusz:* **KÉSZ** (Fejlesztve és CDP teszttel verifikálva).
- [x] **Értékesítési Csatornák & Logisztika kártyamentesítése:**
  - *Feladat:* Kártyák törlése, helyette 2 csatornás (01 Gyári közvetlen szállítás, 02 Országos nagyker hálózat) elválasztóvonalas mátrix világos háttéren.
  - *Státusz:* **KÉSZ** (Fejlesztve és CDP teszttel verifikálva).
- [x] **Élelmiszer-technológiai Garanciák kártyamentesítése:**
  - *Feladat:* 4 oszlopos (01–04) elválasztóvonalas mátrix, világos háttéren finom `.bg-tech-grid` rácsvonalakkal.
  - *Státusz:* **KÉSZ** (Fejlesztve és CDP teszttel verifikálva).
- [x] **Váltakozó szekció-színritmus (Vörös / Világos / Zöld):**
  - *Ritmus:* Hero (Világos + Grid) ➔ Termékek (Világos) ➔ Cégünkről (**Vörös**) ➔ Technológia (**Világos + Grid**) ➔ Egyedi receptúra (**Zöld**) ➔ Prospektus (**Vörös**) ➔ Logisztika (**Világos**) ➔ Kapcsolat (**Zöld**) ➔ Footer (**Sötétbordó**).
  - *Státusz:* **KÉSZ** (Fejlesztve és CDP teszttel verifikálva).
- [ ] **Prospektus (prezentáció) cseréje:**
  - *Feladat:* A jelenleg letölthető `Sun_Valley_B2B_Prospektus_V1_4.pptx` helyére az új hivatalos prospektus / katalógus anyag beillesztése ("Prospectus kicserélni").
  - *Státusz:* **Várakozik** (Az új anyag beérkezésére vár).
- [x] **Süti (Cookie) sáv megvalósítása:**
  - *Feladat:* Letisztult, diszkrét lebegő Cookie / GDPR sáv egyetlen „Rendben” gombbal, `localStorage` alapú állapotmegőrzéssel és kétnyelvű (HU/EN) szövegezéssel.
  - *Státusz:* **KÉSZ** (Automatizált CDP teszttel verifikálva).

---

## 3. Nyitott Kérdések & Döntési Pontok

| # | Téma | Leírás | Felelős | Státusz |
|---|---|---|---|---|
| **K-01** | Ipari laborparaméterek | Publikus kártyákról a Brix és pH levéve; igény esetén a kártya alján lévő gombbal nyílik meg a TDS specifikációs modal. | Andris / Bálint | **LEZÁRVA** |
| **K-02** | Új Prospektus fájl | Milyen formátumú (PDF vs PPTX) és tartalmú anyag váltja a V1.4 PPTX-et? | Andris / Bálint | Anyag beérkezésére vár |
| **K-03** | Betűtípus és Színek | Montserrat (címek & kapcsolat) + Inter (szöveg & tabular adatok), #a3392e (piros), #91372d (akcentus) | Design / Bálint | **LEZÁRVA & ÉLESÍTVE** |
| **K-04** | Andris ChatGPT forrás | A pontos ChatGPT-s szövegtörzs beillesztése a cégbemutató szekcióba. | Bálint | **LEZÁRVA & ÉLESÍTVE** |
| **K-05** | Süti (Cookie) sáv | Diszkrét lebegő sáv elfogadás / beállítások funkcióval. | Bálint | **LEZÁRVA & ÉLESÍTVE** |
| **K-06** | Kapcsolat & Logisztika kártyamentesítés | Kártyák lecserélve vonalas mátrixra, jogi adatok törölve a kapcsolatból, színritmus harmonizálva. | Bálint | **LEZÁRVA & ÉLESÍTVE** |

---

## 4. Fejlesztési Szabályok & Compiler Fegyelem

1. **Egységes forráskód-kezelés:** Minden HTML változtatást kötelezően a [`scripts/compile_v2.py`](file:///c:/Users/csern/Desktop/sun-valley/scripts/compile_v2.py) compiler scriptben kell elvégezni. A build futtatásával generálódik az [`index.html`](file:///c:/Users/csern/Desktop/sun-valley/index.html).
2. **Reszponzivitás és túlcsordulási garancia:** Zero horizontal overflow invariant (375px, 768px, 1024px, 1440px).
3. **Képoptimalizálási előírás:** Egyetlen publikált kép sem haladhatja meg az 500 KB-ot (cél: 100–250 KB WebP).
