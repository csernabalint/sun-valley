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
| **Industrial Sample Request Form** | • Required fields: Company Name, Tax ID (*Adószám*), Plant Type, Monthly volume.<br>• Validates email format and phone number.<br>• Displays clear success feedback with reference ID. |
| **TDS (Technical Data Sheet) Request** | • Download or modal trigger fires cleanly.<br>• Correct file/specs (Brix %, pH, shelf life) linked.<br>• No broken links or 404 redirects. |
| **Product Filter & Category Selector** | • Filters baking-stable fillings by application (puff pastry, yeast dough, cookies).<br>• Instant DOM update with no flickering or broken grids. |
| **Responsive Navigation** | • Clean hamburger / mobile drawer transition.<br>• No horizontal overflow on mobile screens ($375\text{px}$). |
| **Contrast & Accessibility** | • High-contrast text on cream/burgundy surfaces (WCAG AA/AAA).<br>• Visible focus states for keyboard navigation. |
