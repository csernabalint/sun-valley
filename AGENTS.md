# AGENTS.md – Sun Valley Zrt. AI Agent Guidelines & Operating Rules

Welcome to the **Sun Valley Zrt.** repository. This project is in its earliest concept phase. Agents working here must embrace volatility: prioritizing rapid concept validation, razor-sharp requirements interrogation, and distinctive visual styling over premature architectural rigidity.

---

## 1. Operating Principles

1. **Interrogate Before Coding**: Never write hundreds of lines of speculative code based on ambiguous prompts. Activate `grill-me` or `grill-with-docs` to walk the decision tree and resolve open questions first.
2. **Reject AI Slop**: AI models naturally converge on centered hero sections, generic purple/blue gradients, and identical 3-column card grids. This is strictly prohibited. Enforce the **57 Hallmark Anti-Slop Gates** and leverage the agricultural-industrial brand palette.
3. **Domain Vocabulary Integrity**: Always respect [CONTEXT.md](file:///c:/Users/csern/Desktop/sun%20valley/CONTEXT.md). Use terms like *sütésálló gyümölcstöltelék*, *üzemi próbagyártási minta*, and *TDS*. Do not invent conflicting abstractions.
4. **Runtime Verification**: Passing a TypeScript build or syntax check is NOT proof of working code. Test interactive flows (forms, calculators, modals, responsive breakpoints) with actual DOM/runtime verification before declaring victory.

---

## 2. Sun Valley Zrt. Brand Identity & Visual Rules

* **Company Profile**: B2B Industrial food technology leader (1.1–1.3B HUF revenue, AA+ financial rating).
* **Tone**: Industrial dignity, food-grade precision, agricultural heritage, scientific reliability (thermo-stability).
* **Brand Colors (from `szinek.md` & `CONTEXT.md`)**:
  * **Primary**: Mélybordó (`#5F2125`), Sötétbordó (`#451C1B`), Naplemente Narancs (`#E36527`), Arany Napsugár (`#D48054`).
  * **Nature & Agriculture**: Dombok Mélyzöldje (`#2D3628`), Dombok Világoszöldje (`#5F6E4D`), Érett Almapiros (`#923833`).
  * **Backgrounds & Neutrals**: Papíralap Krémfehér (`#F5F2EE`), Homokbézs Vízjel (`#D0AE9F`), Szénfekete (`#000000`).
* **Design Prohibitions**:
  * ❌ No neon purple, cyan, or generic SaaS gradients.
  * ❌ No floating blurry glassmorphism spheres behind text.
  * ❌ No symmetrical 3-card feature rows.
  * ❌ No placeholder Lorem Ipsum—use authentic Hungarian industry copy (*Brix fok, sütésállóság, aszeptikus zsákos kiszerelés*).
  * ❌ **No `Syne` typeface for headings**: Always use `Plus Jakarta Sans` with `font-feature-settings: "lnum" 1, "tnum" 0` and `leading-snug pb-1` to prevent numeral height drops (e.g. `200 °C`), distorted Hungarian `Ö` diacritics, and clipped descenders (`g`, `y`, `p`).
  * ❌ **No destructive image filters on brand emblems**: Brand assets must retain genuine PNG alpha-transparency; never use `brightness-0 invert` which obliterates multi-color crests into solid white squares.
  * ❌ **No fragmented brand names**: `SUN VALLEY ZRT.` must remain a unified typographic lockup with identical font size, weight, and baseline alignment.
  * ❌ **No untranslated English labels in Hungarian UI**: Translate terms like `THERMO-STABLE` -> `SÜTÉSÁLLÓ`, `DIRECT FACTORY SUPPLY` -> `KÖZVETLEN GYÁRI SZÁLLÍTÁS`, `QC PASS` -> `MINŐSÍTETT` (exemptions: `ISO`, `HACCP`, `pH`, `Brix`).

---

## 3. Engineering & Compilation Invariants

1. **Single Source of Truth for Generated HTML**: When prototypes are managed via a compiler script (e.g. `scripts/compile_v2.py`), all edits MUST be made directly inside the compiler script. Never make manual fixes solely in `.html` files that will be wiped on the next build.
2. **Zero Horizontal Overflow Invariant**: Mobile screens ($375\text{px}$), tablets ($768\text{px}$), laptops ($1024\text{px}$), and desktops ($1440\text{px}$) must strictly satisfy `scrollWidth === clientWidth`. Never use `shrink-0` on wide rows without wrapping (`flex-wrap`) or dedicated scroll containers.
3. **Safe Form Sanitization & Ampersand Fidelity**: Never naive-replace `&` with `&amp;` when outputting to plain-text elements (`textContent`). Strip HTML tags via regex (`/<[^>]*>/g`) to block XSS while preserving legitimate business characters (`B&B Dunapataji Kenyérgyár Zrt.`).
4. **Strict Phone Validation**: Phone numbers must strictly reject alphabetic characters and scripts (`/^[+]?[0-9\s\-()\/]{8,25}$/`). Active validation error messages must be cleared upon language toggling.

---

## 4. Available Antigravity Skills

The following skills are installed in `.agents/skills/` and can be invoked on demand:

### Discovery & Concept Validation (Matt Pocock Framework)
* **`grill-me`**: Relentlessly interrogates vague requirements, walks decision trees, and surfaces edge cases before any code is written.
* **`grill-with-docs`**: Stateful interrogation that updates [CONTEXT.md](file:///c:/Users/csern/Desktop/sun%20valley/CONTEXT.md) and appends Architecture Decision Records (ADRs).
* **`prototype`**: Spits out 2–3 disposable, isolated UI sandboxes to test UX before locking into architecture.
* **`domain-modeling`**: Synchronizes code abstractions with the business terminology in `CONTEXT.md`.

### Design & Anti-Slop Layouts (Hallmark Framework)
* **`hallmark`**: Generates distinctive UI by selecting from 21 macrostructures, applying intentional themes, and enforcing the 57 Anti-Slop Gates.
* **`hallmark-redesign`**: Swaps entire structural layouts instantly while preserving 100% of copy, brand assets, and value propositions.
* **`hallmark-study`**: Extracts design DNA (typography, palette, density, micro-interactions) from reference sites or screenshots into `docs/design.md`.

### Execution & Verification (pstack Framework)
* **`poteto-mode`**: Orchestrates disciplined multi-phase playbooks (Feature, Bug, Refactor) with strict todo tracking.
* **`figure-it-out`**: Generates bespoke, auditable execution paths when specs are loosely defined.
* **`verification-hooks`**: Mandates verification of interactive flows (forms, calculators, modals) with real DOM checks.
