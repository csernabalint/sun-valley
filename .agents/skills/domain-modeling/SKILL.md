---
name: domain-modeling
description: >-
  Use this skill to audit, extract, and maintain consistent domain terminology and business
  rules across the codebase. Ensures all UI labels, code entities, and documentation stay
  strictly aligned with CONTEXT.md, preventing vocabulary drift.
---

# Domain-Modeling (Ubiquitous Language Enforcement)

AI agents frequently suffer from "concept drift"—inventing new terms (e.g. calling an industrial sample a "free trial", or calling baking-stable filling "fruit jam"). The `domain-modeling` skill ensures domain purity across every layer of the repository.

---

## 1. Operating Rules

1. **Strict Terminology Alignment**: Every variable, component name, database entity, and UI string must align with the definitions in [CONTEXT.md](file:///c:/Users/csern/Desktop/sun%20valley/CONTEXT.md).
2. **Audit Before Merge**: Check new or modified files against the banned synonyms list:
   * ❌ Banned: *"Lekvár"* / *"Dzsem"* ➔ ✅ Mandatory: *"Sütésálló gyümölcstöltelék"* (*Bake-stable fruit filling*).
   * ❌ Banned: *"Ingyenes próba"* / *"Free trial"* ➔ ✅ Mandatory: *"Üzemi próbagyártási minta"* (*Industrial trial batch sample*).
   * ❌ Banned: *"Webshop kosár"* ➔ ✅ Mandatory: *"Ajánlatkérő kosár / Mintakérés"* (*B2B Inquiry / Sample request*).
3. **Continuous Glossary Expansion**: When new concepts arise, append them to `CONTEXT.md` with explicit definitions and translations.

---

## 2. Audit Workflow

1. **Scan Target Files**: Use grep or file inspection to detect informal, consumer-oriented (B2C), or inconsistent phrasing.
2. **Flag Violations**: Identify where code symbols or UI strings deviate from B2B industrial standards.
3. **Refactor**: Replace fuzzy abstractions with clear, domain-driven terminology.
