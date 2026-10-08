# Sun Valley Zrt. – B2B Ipari Gyümölcstechnológia

Hivatalos weboldal és interaktív digitális termékkatalógus a **Sun Valley Kereskedelmi Zrt.** számára.

- **Élő weboldal (GitHub Pages):** [https://csernabalint.github.io/sun-valley/](https://csernabalint.github.io/sun-valley/)
- **GitHub Repository:** [https://github.com/csernabalint/sun-valley](https://github.com/csernabalint/sun-valley)

---

## 🏭 A Projektről

A Sun Valley Zrt. prémium minőségű, sütésálló, kenhető és darabos gyümölcstöltelékeket, lekvárokat és dzsemeket gyárt nagyüzemi pékáru- és édesipari partnerek, pékséghálózatok és cukrászatok számára móri üzemében.

### Fő funkciók és technológia
- **Interaktív Flipbook Termékkatalógus**: Valósághű lapozás physics motorral (StPageFlip) asztali nézetben, érintésvezérelt kártyarendszerrel mobil eszközökön.
- **Kétnyelvű i18n rendszer**: Azonnali dinamikus váltás magyar (HU) és angol (EN) nyelv között teljes kifejezés- és mértékegység-szinkronnal.
- **Receptúra R&D folyamatbemutató**: Interaktív fázisválasztó egyedi ipari igények, viszkozitási és Brix-értékek kiszolgálására.
- **Előre formázott műszaki ajánlatkérő**: Egykattintásos szabványosított e-mail sablon generálás adagolási, hőtűrési és kiszerelési specifikációkkal.
- **100% Zero-Overflow Invariáns**: Szigorú reszponzivitás 375px, 768px, 1024px és 1440px felbontásokon.

---

## 📂 Mappaszerkezet

```text
├── assets/                 # Optimalizált WebP és JPG képfájlok, logók, betűtípusok
│   ├── catalog/            # Katalógus oldalak
│   └── vendor/             # Külső könyvtárak (StPageFlip, Lucide)
├── docs/                   # Tervezési dokumentáció, specifikációk és képernyőképek
├── prototypes/             # Prototípus és teszt HTML változatok
├── scripts/                # Fordító- és ellenőrző szkriptek
│   ├── compile_v2.py       # Single Source of Truth HTML fordító
│   └── run_full_verification.py # Runtime és CDP DOM ellenőrző
├── index.html              # Fordított éles egyoldalas webalkalmazás
├── AGENTS.md               # AI ügynök és fejlesztési irányelvek
├── CONTEXT.md              # Domén szótár és vállalati háttér
├── requirements.txt        # Python függőségek a teszteléshez és fordításhoz
├── robots.txt              # Keresőmotor direktívák
└── sitemap.xml             # Keresőmotor oldaltérkép
```

---

## 🛠️ Fordítás és fejlesztés

Az éles `index.html` egyetlen központi forrásból (`scripts/compile_v2.py`) fordul le a változtatások integritásának biztosítása érdekében:

```bash
# Függőségek telepítése
pip install -r requirements.txt

# Weboldal újrafordítása és szinkronizálása
python scripts/compile_v2.py

# Teljes körű automatizált verifikáció (Chrome CDP + DOM tesztek)
python scripts/run_full_verification.py
```

---

## 📄 Licenc és jogok

© 2026 Sun Valley Kereskedelmi Zrt. Minden jog fenntartva.
