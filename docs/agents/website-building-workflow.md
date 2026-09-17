# Sun Valley Zrt. – End-to-End Website Building Workflow

This document outlines the standard 5-phase engineering workflow for building pages, features, and components in the Sun Valley Zrt. project using our Antigravity skills.

---

## The 5-Phase Lifecycle Overview

```
[Phase 1: Discovery & Interrogation]
  └─ grill-me / grill-with-docs ──► CONTEXT.md & ADRs
         │
[Phase 2: Anti-Slop Design & Sandboxing]
  ├─ hallmark-study (Extract DNA)
  ├─ prototype (2–3 Disposable Sandboxes)
  └─ hallmark / hallmark-redesign (Enforce 57 Gates & Macrostructures)
         │
[Phase 3: Disciplined Execution]
  └─ poteto-mode / figure-it-out ──► Step-by-Step Playbooks & Todo Tracking
         │
[Phase 4: Runtime Verification]
  └─ verification-hooks ──► Real DOM Assertions, Forms & Breakpoint Checks
         │
[Phase 5: Domain Audit & Handoff]
  └─ domain-modeling ──► Vocabulary Drift Prevention & Final CONTEXT.md Sync
```

---

## Phase 1: Discovery & Requirements Interrogation

**Goal**: Pressure-test intent, eliminate ambiguity, and lock down business logic before a single line of production code is written.

### When to Use
* Starting a new page (e.g. Homepage, Product Catalog, Technology Showcase).
* Introducing an interactive feature (e.g. Industrial Sample Request Wizard, TDS Spec Filter).

### Skills in Action
* **`grill-me`**: Interrogates intent, persona targets (bakery technologist vs. purchasing manager), volume expectations, and edge cases one question at a time.
* **`grill-with-docs`**: Records architectural directions into [CONTEXT.md](file:///c:/Users/csern/Desktop/sun%20valley/CONTEXT.md) and logs ADR entries.

### Example User Prompts
> *"I want to build the industrial sample request flow for bakeries. Run `grill-me` on this."*
> *"Let's do a `grill-with-docs` session to decide how we display product specifications (Brix, pH, packaging sizes)."*

---

## Phase 2: Anti-Slop Design & Disposable Prototyping

**Goal**: Explore multiple contrasting visual structures and reject generic AI tropes (centered 3-card grids, purple SaaS gradients).

### When to Use
* Translating approved requirements into visual interfaces.
* Designing high-impact landing pages or complex B2B data displays.

### Skills in Action
* **`hallmark-study`**: (Optional) Analyzes reference websites or screenshots to extract typographic scale, spacing ratios, and density into `docs/design.md`.
* **`prototype`**: Spits out 2–3 radically different, disposable UI sandboxes (e.g., *Variant A: High-Density Technical Spec Sheet* vs. *Variant B: Asymmetric Editorial Orchard*).
* **`hallmark`**: Enforces the 57 Anti-Slop Gates and applies official Sun Valley brand tokens (`#5F2125`, `#E36527`, `#2D3628`, `#F5F2EE`).
* **`hallmark-redesign`**: If an initial design feels too generic, instantly re-skins the structural geometry while preserving 100% of approved copy and specs.

### Example User Prompts
> *"Use `prototype` to generate 2 contrasting layouts for the Sütésálló Gyümölcstöltelék product card."*
> *"Apply `hallmark` to build the industrial homepage hero section using the Asymmetric Editorial macrostructure."*
> *"This layout feels like generic SaaS slop. Run `hallmark-redesign` to convert it into an Industrial Technical Sheet."*

---

## Phase 3: Disciplined Playbook Execution

**Goal**: Move from validated prototype to production code with strict state tracking and engineering rigor.

### When to Use
* Converting the winning prototype into permanent repository components and pages.
* Building stateful forms, interactive calculators, or data tables.

### Skills in Action
* **`poteto-mode`**: Selects the appropriate playbook (`Feature`, `UI Polish`, `Bug Fix`), initializes a tracked todo checklist, and executes phase-by-phase.
* **`figure-it-out`**: Used when a task is novel or loosely specified—generates an ad-hoc, auditable plan with clear milestones.

### Example User Prompts
> *"Activate `poteto-mode` (Feature Playbook) to implement the Industrial Sample Request component."*
> *"Run `figure-it-out` to design and implement our PDF TDS generator integration."*

---

## Phase 4: Runtime Verification

**Goal**: Prove the UI works under real runtime conditions instead of assuming a passing TypeScript compile means working software.

### When to Use
* Immediately after implementation and before closing any task.
* Verifying forms, modals, responsive breakpoints, and client-side calculations.

### Skills in Action
* **`verification-hooks`**: Executes runtime checks against Sun Valley's verification matrix:
  1. *Form Validation*: Required tax ID format, bakery volume dropdowns, error messaging on empty submit.
  2. *Interactive State*: Modals open/close without scroll-lock bugs, tabs switch cleanly.
  3. *Breakpoints*: Checks layout integrity at $375\text{px}$ (mobile), $768\text{px}$ (tablet), and $1280\text{px}$ (desktop).
  4. *Accessibility*: High contrast ratios on paper cream surfaces (WCAG AAA).

### Example User Prompts
> *"Run `verification-hooks` on the sample request form to test field validation and mobile responsiveness."*

---

## Phase 5: Domain Audit & Knowledge Capture

**Goal**: Prevent vocabulary drift and ensure terminology stays aligned with Sun Valley's B2B industrial stature.

### When to Use
* Final review before committing or presenting the feature.

### Skills in Action
* **`domain-modeling`**: Scans the new code and copy for prohibited consumer phrasing:
  * ❌ Flags *"lekvár"*, *"dzsem"*, *"ingyenes próba"*, *"webshop kosár"*.
  * ✅ Confirms *"sütésálló gyümölcstöltelék"*, *"üzemi próbagyártási minta"*, *"ajánlatkérő kosár"*.
* **`grill-with-docs`**: Finalizes any open ADRs and ensures [CONTEXT.md](file:///c:/Users/csern/Desktop/sun%20valley/CONTEXT.md) reflects the latest reality.

### Example User Prompts
> *"Run `domain-modeling` to audit our newly built product pages for vocabulary compliance."*
