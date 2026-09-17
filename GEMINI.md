# GEMINI.md – Sun Valley Zrt. AI Agent Guidelines

See [AGENTS.md](file:///c:/Users/csern/Desktop/sun%20valley/AGENTS.md) and [CONTEXT.md](file:///c:/Users/csern/Desktop/sun%20valley/CONTEXT.md) for full project rules, brand identity, and domain definitions.

## Key Directives
- **Discovery First**: Interrogate unclear requirements using `grill-me` or `grill-with-docs`.
- **Anti-Slop Design**: Follow `hallmark` 57 gates; strictly use Sun Valley brand palette (`#5F2125`, `#E36527`, `#2D3628`, `#F5F2EE`).
- **Typography & Brand Invariants**: Always use `Plus Jakarta Sans` (`lnum 1`) for headings (never `Syne`); preserve transparent PNG alpha on logos (no `brightness-0 invert`); keep `SUN VALLEY ZRT.` unified; maintain pure Hungarian technical copy.
- **Responsive & Overflow Invariant**: Zero horizontal overflow across 375px, 768px, 1024px, 1440px (`scrollWidth === clientWidth`).
- **Compiler Discipline**: Always modify the compiler script (`compile_v2.py`), never make edits solely to generated `.html` files.
- **Discipline & Verification**: Follow `poteto-mode` playbooks and verify interactive UI at runtime with `verification-hooks`.

