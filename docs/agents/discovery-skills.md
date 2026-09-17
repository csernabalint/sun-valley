# Discovery & Concept Validation Runbook (Matt Pocock Framework)

This runbook covers the discovery toolset designed to pressure-test ideas before committing to code.

---

## 1. `grill-me`

### Purpose
Acts as an adversarial thought partner. When you present an ambiguous idea or feature requirement, `grill-me` interrogates your intent, maps out decision branches, surfaces edge cases, and prevents premature coding.

### Key Rules
* Asks **one question at a time** to avoid cognitive overload.
* Offers **2–3 concrete options or tradeoffs** per question.
* Never generates code until the decision tree is fully pruned.

### Sample Prompt to Trigger
> *"I want to add a feature where bakeries can calculate how much filling they need per pastry type. Run `grill-me` on this."*

---

## 2. `grill-with-docs`

### Purpose
The stateful companion to `grill-me`. As the interview progresses, it updates [CONTEXT.md](file:///c:/Users/csern/Desktop/sun%20valley/CONTEXT.md) by defining new domain terms in the glossary and logging agreed technical directions into the Architecture Decision Records (ADR) section.

### Sample Prompt to Trigger
> *"Let's do a `grill-with-docs` session on whether we should require company tax ID verification before allowing TDS downloads."*

---

## 3. `prototype`

### Purpose
Spits out 2–3 disposable, radically different UI variations in isolated sandboxes to test UX before locking into an architecture.

### Archetypes Generated
1. **Dense / Technical**: For factory engineers and technologists who want immediate specs and tabular data.
2. **Visual / Narrative**: For brand immersion, agricultural heritage, and visual impact.
3. **Task-Focused / Minimal**: High-speed conversion flow with zero distractions.

---

## 4. `domain-modeling`

### Purpose
Audits the codebase and proposed copy to ensure terms align with `CONTEXT.md`.
* Banned: *"Lekvár"*, *"Dzsem"*, *"Ingyenes próba"*, *"Webshop"*.
* Enforced: *"Sütésálló gyümölcstöltelék"*, *"Üzemi próbagyártási minta"*, *"Technikai adatlap (TDS)"*, *"B2B Ajánlatkérés"*.
