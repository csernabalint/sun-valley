---
name: verification-hooks
description: >-
  Use this skill to rigorously test and verify real interactive UI flows (forms,
  calculators, modals, data tables, sample requests) using runtime checks, DOM inspection,
  or state assertion rather than relying solely on passing builds.
---

# Verification Hooks (Runtime Interaction Testing)

Code that compiles is not necessarily code that works. The `verification-hooks` skill enforces pstack's core verification discipline: requiring the AI agent to validate actual user interactions and UI flows with runtime verification.

---

## 1. Operating Rules

1. **Test the Happy Path and Failure Modes**: Verify not just that a form submits, but what happens when required fields (e.g. Hungarian company tax number, bakery plant email) are invalid.
2. **Verify Interactive State Changes**: Check modal open/close transitions, tab switching, calculation output updates, and loading states.
3. **Responsive Breakpoint Testing**: Inspect layout integrity at mobile ($375\text{px}$), tablet ($768\text{px}$), and desktop ($1280\text{px}$) widths.

---

## 2. Sun Valley Verification Matrix

For any UI implementation in Sun Valley Zrt., execute the following test points:

| Flow / Component | Verification Criteria |
| :--- | :--- |
| **Responsive Viewport & Overflow** | • Verify `document.documentElement.scrollWidth <= window.innerWidth` across 375px, 768px, 1024px, and 1440px.<br>• Assert zero sideways scrolling on all viewports.<br>• Ensure flex/tab containers wrap (`flex-wrap`) or provide contained horizontal scroll (`overflow-x-auto`). |
| **Typography & Diacritics Integrity** | • Verify headings use `Plus Jakarta Sans` with lining figures enabled (`font-feature-settings: "lnum" 1`).<br>• Verify numerals (`200 °C`, `1,1–1,3 Mrd Ft`) match full cap-height.<br>• Verify Hungarian `Ö` and `Ő` diacritic dots are properly aligned.<br>• Assert descenders (`g`, `y`, `p`) have bottom clearance (`leading-snug pb-1`) with zero clipping. |
| **Brand Asset Fidelity** | • Assert brand crests retain genuine PNG 0-alpha transparency on outer corners.<br>• Zero destructive CSS inversion filters (`brightness-0 invert`) on dark headers/footers.<br>• Verify legal entity `SUN VALLEY ZRT.` remains a single typographic unit. |
| **Industrial Sample Request Form** | • Required fields: Company Name, Tax ID (*Adószám*), Plant Type, Monthly volume.<br>• Strict phone format: rejects letters/scripts, requires 8–16 digits (`/^[+]?[0-9\s\-()\/]{8,25}$/`).<br>• XSS protection: tag stripping without entity double-escaping (`&amp;` must not leak into user text).<br>• Language switch wipes active validation error banners.<br>• Displays clear success feedback with reference ID (`SV-2026-XXXX`). |
| **TDS (Technical Data Sheet) Request** | • Download or modal trigger fires cleanly.<br>• Correct file/specs (Brix %, pH, shelf life) linked.<br>• No broken links or 404 redirects. |
| **Product Filter & Category Selector** | • Filters baking-stable fillings by application (puff pastry, yeast dough, cookies).<br>• Instant DOM update with no flickering or broken grids. |
| **Language & Domain Integrity** | • Zero untranslated English labels on Hungarian UI (`THERMO-STABLE` -> `SÜTÉSÁLLÓ`, etc.).<br>• Trilingual switching (HU/EN/DE) verified across all `[data-i18n]` keys. |
| **Contrast & Accessibility** | • High-contrast text on cream/burgundy surfaces (WCAG AA/AAA).<br>• Visible focus states for keyboard navigation. |

