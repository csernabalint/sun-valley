# CONTEXT.md – Sun Valley Zrt. Domain Model & Glossary

This document is the single source of truth for domain terms, brand constraints, and architecture decisions for Sun Valley Zrt. AI agents must read and update this file whenever new domain terminology or architectural choices are agreed upon.

---

## 1. Company & Strategic Positioning

* **Company Name**: Sun Valley Kereskedelmi Zrt. (Est. 2009)
* **Scale & Financials**: Stable, AA+ rated industrial food-technology plant with annual turnover of 1.1–1.3 billion HUF.
* **Core Business**: Industrial fruit processing and modern thermo-stable (baking-stable) fruit preparations for commercial bakeries, pastry manufacturers, and food wholesale distributors.
* **Primary Objective of Web Presence**:
  * Demolish the small-scale "artisan / small producer" misconception.
  * Credibly project massive industrial capacity, cutting-edge technology, and supply chain reliability.
  * Drive B2B conversions: Industrial trial production samples (*üzemi próbagyártási minta*) and Technical Data Sheet (TDS) downloads.

---

## 2. Target Personas & Core Decision Drivers

1. **Industrial Bakery Technologists (*Ipari pézipari és kenyérgyári technológusok*)**
   * *Key Questions*: Does the filling boil over above 200 °C? Does it make the dough soggy? Is it mechanically pumpable and sliceable?
   * *Conversion*: TDS downloads, laboratory sample requests, baking test validation.
2. **Bread Factory & Industrial Plant Purchasers (*Kenyérgyári beszerzők*)**
   * *Key Questions*: Can Sun Valley deliver 5–20 tons consistently month-over-month? What is the container packaging (bucket, IBC container)? What are payment terms?
   * *Conversion*: Request for quote, commercial framework agreements.
3. **Food Wholesale Product Managers (*Élelmiszeripari nagykereskedelmi termékmenedzserek*)**
   * *Key Questions*: Private label options? Shelf life stability? Certification compliance (IFS, ISO)?
   * *Conversion*: Partner portal onboarding, wholesale sample kits.

---

## 3. Ubiquitous Language (Trilingual Domain Glossary)

Agents must strictly use these definitions and avoid inventing generic, consumer, or conflicting terms:

| Term (HU) | English Equivalent (EN) | German Equivalent (DE) | Definition & Context |
| :--- | :--- | :--- | :--- |
| **Sütésálló gyümölcstöltelék** | Thermo-stable / Bake-stable fruit preparation | Backstabile Fruchtzubereitung / Fruchtfüllung | High-viscosity fruit preparation engineered not to boil out, liquefy, or burn during high-temperature baking (200 °C+). |
| **Szeletelhető vegyes gyümölcsíz** | Sliceable mixed fruit block | Schnittfeste gemischte Fruchtfüllung | 10 kg block fruit filling specifically formulated for industrial slicing and automated dough encrusting. |
| **Kenhető gyümölcskészítmény** | Spreadable fruit preparation | Streichfähige Fruchtzubereitung | 5 kg bucket cold-spreadable fruit filling for sponge cakes, linzer pastries, and cold confectionery layering. |
| **Üzemi próbagyártási minta** | Industrial trial batch sample | Betriebliches Produktionsmuster / Probemuster | Sample container (5–10 kg bucket) sent directly to bakery plants for pilot test baking. |
| **Technikai adatlap (TDS)** | Technical Data Sheet (TDS) | Technisches Datenblatt (TDS) | Specification document outlining Brix degree, pH value, fruit content %, water activity ($a_w$), and allergen declarations. |
| **Kenyérgyári lépték** | Industrial plant scale | Industrieller Großmaßstab | High-volume supply capacity (>500 kg / multi-ton palletized deliveries) with strict batch homogeneity. |
| **Aszeptikus csomagolás** | Aseptic packaging | Aseptische Verpackung | Industrial packaging (e.g. 10 kg bag-in-box, 200 kg steel drum, 1000 kg IBC container) guaranteeing long shelf life without preservatives. |
| **Energiatudatos Vállalat** | Energy-Conscious Enterprise | Energiebewusstes Unternehmen | Official award in the Virtual Power Plant Program (VEP) for energy-optimized food processing in Mór. |

---

## 4. Brand Design Tokens (from `szinek.md`)

```css
:root {
  /* Primary Brand */
  --sv-burgundy: #5F2125;         /* Mélybordó: Primary headings, accents, crest */
  --sv-burgundy-dark: #451C1B;    /* Sötétbordó: Icon backgrounds, divider strips */
  --sv-sun-orange: #E36527;       /* Naplemente Narancs: Core logo sun, active CTAs */
  --sv-sun-gold: #D48054;         /* Arany Napsugár: Secondary highlights, sun rays */
  --sv-sun-highlight: #FBBB9C;    /* Világos Arany: Halo, glow, badge accents */

  /* Nature & Orchard */
  --sv-hill-green-dark: #2D3628;  /* Dombok Mélyzöldje: Landscape layers, dark surfaces */
  --sv-hill-green-light: #5F6E4D; /* Dombok Világoszöldje: Subtle green accents */
  --sv-foliage-green: #474B3D;    /* Almafa Lombzöld: Organic textures, cards */
  --sv-apple-red: #923833;        /* Érett Almapiros: Fruit badges, alert accents */
  --sv-soil-brown: #63412C;       /* Termőföld: Earthy structural accents */
  --sv-mist-mountain: #956F5E;    /* Párás Hegyvonulat: Muted borders, neutral tints */

  /* Neutrals & Surfaces */
  --sv-paper-cream: #F5F2EE;      /* Papíralap Krémfehér: Light mode background */
  --sv-watermark-sand: #D0AE9F;   /* Homokbézs Vízjel: Decorative borders, subtle watermarks */
  --sv-icon-white: #F8F8F8;       /* Tiszta Fehér: Icon glyphs, pure highlights */
  --sv-text-dark: #000000;        /* Szénfekete: High-contrast body text */
}
```

---

## 5. Architecture Decision Records (ADR Log)

*Decisions recorded during `/grill-with-docs` sessions are appended here.*

### ADR-001: Early-Phase Volatility & Antigravity Setup
* **Date**: 2026-09-16
* **Status**: Accepted
* **Context**: The web application is in its earliest concept phase. Rigid CI/CD and fixed monolithic architectures must be avoided in favor of rapid visual prototypes, stress-tested requirements, and runtime UI validation.
* **Decision**: Configure native Antigravity skills (`.agents/skills/`) covering Matt Pocock validation workflows, Hallmark anti-slop gates, and pstack execution playbooks. Maintain `CONTEXT.md` as the living domain model.

### ADR-002: Pure Frontend B2B Marketing Site & Theme Flexibility
* **Date**: 2026-09-16
* **Status**: Accepted
* **Context**: The website is currently an early-phase introduction/marketing site for business partners. No backend, database, or authentication is required. Direct conversions happen via click-to-call phone and direct email. Colors must be flexible for fast iterative "vibe coding".
* **Decision**:
  1. Pure frontend single-page architecture (Next.js 15 client-side static/SSR, zero backend dependencies).
  2. Points of contact: Direct telephone (`+36 30 899 8548`, `+36 22 400 984`) and direct email (`vecsei.andras@sunvalley.hu`).
  3. No complex multi-step sample request databases for now—direct inquiries and modal spec viewings only.
  4. Fully responsive across all devices (iPhone/Android, tablet, laptop, desktop).
  5. 100% token-based CSS variables (never hardcoded hex codes in components) to allow rapid theme tweaking and effortless palette adjustments.

### ADR-003: Full Showcase Structure & Tech Specification
* **Date**: 2026-09-16
* **Status**: Accepted
* **Context**: Resolution of grill-me decision tree for initial website build.
* **Decision**:
  1. **Stack**: Next.js 15 (App Router), Tailwind CSS, TypeScript, Lucide React.
  2. **Macrostructure**: Industrial Technical Sheet & Laboratory Precision (hairline borders, monospace numerals, high-density spec matrices, zero AI slop).
  3. **Section Pipeline**:
     - Sticky Header with quick phone/email links & anchor navigation.
     - Industrial Hero Section focusing on 200 °C+ thermostability & corporate reliability.
     - Trust Metric Ribbon (AA+ rating, 1.1–1.3B HUF revenue, 15+ years experience).
     - Product Matrix (10 kg carton blocks & 5 kg buckets) with interactive TDS spec modals.
     - Food-Technology Engineering Advantages (sliceability, no dough soakage, VEP energy award).
     - Dual-Track Distribution (Direct factory supply vs. Authorized wholesale partners: Békás, Busa, Csubi-Ker, Pille, Galla).
     - Corporate Plant & Contact Information (Mór manufacturing site, Budapest HQ).
  4. **Content Architecture**: Hungarian-first copy with modular content dictionary for clean separation of content and presentation.
