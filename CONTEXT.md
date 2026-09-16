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

## 3. Ubiquitous Language (Domain Glossary)

Agents must strictly use these definitions and avoid inventing generic or conflicting terms:

| Term (HU) | English Equivalent | Definition & Context |
| :--- | :--- | :--- |
| **Sütésálló gyümölcstöltelék** | Thermo-stable / Bake-stable fruit filling | High-viscosity fruit preparation engineered not to boil out, liquefy, or burn during high-temperature baking (200 °C+). |
| **Üzemi próbagyártási minta** | Industrial trial batch sample | Sample container (typically 5–10 kg bucket) sent directly to industrial bakery labs for pilot production line testing. |
| **Technikai adatlap (TDS)** | Technical Data Sheet | Specification document outlining Brix degree, pH value, fruit content %, water activity ($a_w$), and allergen declarations. |
| **Kenyérgyári lépték** | Industrial plant scale | Capacity to supply multi-ton volume orders with homogeneous batch quality. |
| **Aszeptikus csomagolás** | Aseptic packaging | Industrial packaging (e.g. 10 kg bag-in-box, 200 kg steel drum, 1000 kg IBC container) ensuring long shelf life without chemical preservatives. |

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
