---
name: hallmark
description: >-
  Default frontend and UI layout generator. Enforces 57 anti-slop quality gates,
  selects from 21 distinct macrostructures, and applies intentional visual styling
  to prevent generic AI templates, centered card grids, and purple gradients.
---

# Hallmark (Anti-Slop Design & Macrostructure Engine)

Hallmark acts as the frontline aesthetic gatekeeper for Sun Valley Zrt. It prevents the homogenized, low-effort look typical of LLM-generated websites by enforcing mechanical quality gates and deliberate structural archetypes.

---

## 1. The 57 Anti-Slop Gates

Before emitting any UI code, audit the layout against these gates:

### Category A: Layout & Geometry (Gates 1–12)
1. ❌ **No Centered Hero Clichés**: Never default to `text-center max-w-2xl mx-auto` with a centered headline and two pill buttons. Use asymmetric, editorial, or split-screen layouts.
2. ❌ **No Identical 3-Card Grids**: Do not use `grid-cols-1 md:grid-cols-3` where each card has an icon in a circle, a bold title, and 2 lines of text. Vary card spans, orientations, and internal hierarchies.
3. ❌ **No Floating Bento Without Hierarchy**: A bento grid must have a clear dominant primary anchor (e.g., $2\times 2$ or $2\times 1$ span) rather than evenly sized boxes.
4. ❌ **No Infinite Full-Width Banding**: Avoid alternating full-width white and light-gray stripes endlessly down the page. Use negative space, inset containers, and varied section rhythms.
5. ❌ **No Symmetrical Padding Everywhere**: Avoid identical $p-6$ on every single container. Balance tight, dense information blocks with generous breathing room.
6. ✅ **Macrostructure Selection**: Explicitly select an archetype:
   * *The Industrial Technical Sheet*: High-density specs, tabular data, crisp dividing rules, laboratory precision.
   * *The Asymmetric Editorial*: Heavy editorial serif/display headlines, offset image columns, staggered text blocks.
   * *The Horizon Splice*: Deep landscape visual split with warm agricultural earth tones.

### Category B: Color & Surfaces (Gates 13–24)
7. ❌ **No Purple/Indigo SaaS Gradients**: Strictly banned. No `from-indigo-500 to-purple-600`.
8. ❌ **No Blurry Glowing Blobs**: Do not place oversized `blur-3xl` colored circles behind text.
9. ❌ **No Unanchored Dark Mode**: Dark surfaces must not be flat charcoal (`#121212`)—use tinted deep surfaces like Sun Valley's Dombok Mélyzöldje (`#2D3628`) or Sötétbordó (`#451C1B`).
10. ✅ **Strict Palette Compliance**: Use the official Sun Valley tokens:
    * Primary accents: Mélybordó (`#5F2125`), Naplemente Narancs (`#E36527`).
    * Agricultural depth: Dombok Zöldje (`#2D3628`, `#5F6E4D`), Érett Almapiros (`#923833`).
    * Background warmth: Papíralap Krémfehér (`#F5F2EE`), Homokbézs (`#D0AE9F`).
11. ❌ **No Washed-Out Low-Contrast Text**: Text must meet WCAG AAA contrast for body copy on paper cream surfaces.

### Category C: Typography & Hierarchy (Gates 25–36)
12. ❌ **No Generic Inter/System-UI Only**: Pair a distinctive heading font (warm serif or bold industrial grotesque) with a clean, legible sans-serif for technical data.
13. ❌ **No Giant Vague One-Liners**: Headlines must deliver concrete business value (e.g. *"200 °C felett sem forr ki: Ipari sütésálló gyümölcstöltelékek közvetlenül a gyártótól"*).
14. ❌ **No Flat Heading Hierarchies**: Ensure extreme contrast between H1/H2 scale and body copy.
15. ✅ **Technical Data Formatting**: Technical specifications (Brix, pH, shelf-life, pack sizes) must use tabular monospace numerals and structured key-value badges.

### Category D: Components & Details (Gates 37–57)
16. ❌ **No Generic Lucide Icon Inside Colored Circle**: Do not decorate every paragraph with a random feather icon inside a rounded-full pastel circle.
17. ❌ **No Floating Pill CTA Duos**: Avoid the standard "Get Started" (solid pill) next to "Learn More" (outline pill). Use meaningful action verbs: *"Üzemi próbagyártási minta igénylése"*, *"Technikai adatlap (TDS) letöltése"*.
18. ❌ **No Fake Testimonial Avatars**: Do not invent fake quotes from stock photos. Use credible B2B verification badges: AA+ financial certification, IFS audit status, annual tonnage capacity.
19. ✅ **Tactile Micro-Details**: Subtle 1px borders with warm tints (`rgba(95, 33, 37, 0.15)`), fine hairline dividers, and crisp hover transitions.

---

## 2. Hallmark Generation Workflow

1. **Select Macrostructure**: Choose the structural archetype best suited for the page goal.
2. **Apply Theme**: Lock in the Sun Valley color tokens, typographic pairings, and surface materials.
3. **Execute Slop Audit**: Run through the 57 gates. If any gate fails, refactor before delivering code.
