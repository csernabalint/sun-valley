---
name: prototype
description: >-
  Use this skill to quickly spit out 2–3 disposable, radically different UI variations
  or interaction concepts in isolated sandboxes to test UX before locking into production architecture.
---

# Prototype (Disposable UI Exploration)

In early-phase development, committing too early to a single UI structure creates massive technical debt. The `prototype` skill rapidly generates multiple contrasting interface concepts in disposable sandboxes (`prototypes/` or single-file HTML/React widgets).

---

## 1. Operating Rules

1. **Disposable by Design**: Do not worry about backend integration, state persistence, or clean abstractions. The goal is sensory validation of layout, density, and flow.
2. **Generate Contrasting Variations**: Always generate at least 2 radically different approaches:
   * **Variation A (Dense & Technical)**: High-information density, data tables, quick specs (e.g. for factory engineers).
   * **Variation B (Visual & Narrative)**: High-impact imagery, storytelling, brand immersion, prominent CTAs.
   * **Variation C (Minimalist & Task-Focused)**: Quick conversion forms, stepper wizards, zero friction.
3. **Respect Brand Tokens**: Always use Sun Valley brand colors (`#5F2125`, `#E36527`, `#2D3628`, `#F5F2EE`) from [CONTEXT.md](file:///c:/Users/csern/Desktop/sun%20valley/CONTEXT.md).

---

## 2. Prototyping Workflow

### Step 1: Define Target Flow
Clarify the single interaction or screen to be tested (e.g., *Industrial Sample Request Form* or *Bake-Stable Fruit Product Card*).

### Step 2: Generate Isolated Files
Create standalone prototypes under a temporary directory, e.g. `prototypes/variant-a/`, `prototypes/variant-b/` or interactive generative UI widgets.

### Step 3: Compare & Evaluate
Present a side-by-side comparison table to the user:
* Visual hierarchy & cognitive load.
* Friction points for the B2B persona.
* Mobile responsiveness & ergonomics.

### Step 4: Harvest or Discard
Once the user chooses the winning variation, extract its layout geometry and discard the prototype files to keep the main repo clean.
