---
name: hallmark-study
description: >-
  Use this skill to extract design DNA from live reference websites or visual screenshots.
  Translates external design inspiration into an actionable docs/design.md specification
  without copying pixels.
---

# Hallmark Study (Design DNA Extraction)

When the user provides a reference URL or screenshot of an admired site, `hallmark-study` analyzes the underlying design rules rather than copying surface pixels. It translates visual taste into quantifiable engineering tokens and writes them to `docs/design.md`.

---

## 1. Operating Rules

1. **Rule Extraction, Not Pixel Theft**: Focus on ratios, typographic rhythm, spatial density, and structural relationships.
2. **Actionable Output**: Produce ready-to-use CSS tokens, font pairings, and layout rules.
3. **Map to Brand Context**: If studying an external reference, translate its structural strengths into Sun Valley's palette (`#5F2125`, `#E36527`, `#2D3628`, `#F5F2EE`).

---

## 2. Extraction Dimensions

When analyzing a reference, document the following in `docs/design.md`:

1. **Typographic Scale & Weight**:
   * Font families (Display vs Body vs Monospace).
   * Letter spacing (tracking) on large titles.
   * Line height ratios ($1.1$ for titles, $1.5$ for body).
2. **Spatial Density & Grids**:
   * Baseline grid rhythm (e.g. 4px / 8px).
   * Container max-widths ($1120\text{px}$, $1280\text{px}$, or edge-to-edge).
   * Micro-padding vs macro-section margins.
3. **Borders & Materiality**:
   * Hairline borders (1px tinted).
   * Shadow treatment (soft diffuse vs crisp brutalist vs no shadow).
   * Surface texture and warm tints.
4. **Interaction & State DNA**:
   * Hover transitions (scale, color shift, border reveal).
   * Active and focus outlines.
