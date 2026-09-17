# Antigravity Agent Customizations – Sun Valley Zrt.

This directory documents the customized AI agent system installed for the **Sun Valley Zrt.** repository.

The configuration is tailored for the earliest phase of website development—prioritizing rapid concept validation, clean requirements, anti-slop visual styling, and rigorous verification.

---

## Architecture Overview

```
sun-valley/
├── AGENTS.md                  # Project rules loaded automatically by Antigravity
├── GEMINI.md                  # Alternate root configuration entry point
├── CONTEXT.md                 # Living domain model, glossary & ADR decision log
├── szinek.md                  # Official brand color tokens extracted from business card
├── .agents/
│   └── skills/                # Antigravity progressive-disclosure skills
│       ├── grill-me/          # Matt Pocock concept stress-testing
│       ├── grill-with-docs/   # Stateful interrogation syncing CONTEXT.md & ADRs
│       ├── prototype/         # Disposable UI sandboxes & multi-variant generation
│       ├── domain-modeling/   # Domain vocabulary auditing & drift prevention
│       ├── hallmark/          # Frontline UI builder enforcing 57 anti-slop gates
│       ├── hallmark-redesign/ # Structural layout swapper preserving copy
│       ├── hallmark-study/    # Design DNA extractor from reference sites
│       ├── poteto-mode/       # Disciplined multi-phase playbooks & todo tracking
│       ├── figure-it-out/     # Dynamic ad-hoc playbooks for novel/loose tasks
│       └── verification-hooks/# Runtime verification for real user flows & forms
└── docs/
    └── agents/                # Human-readable documentation & runbooks
        ├── README.md          # This index
        ├── website-building-workflow.md # End-to-end 5-phase building lifecycle
        ├── discovery-skills.md
        ├── hallmark-anti-slop.md
        └── pstack-execution.md
```

---

## Toolsets Quick Reference

| Toolset | Skill Name | Primary Value in Early Stages |
| :--- | :--- | :--- |
| **Matt Pocock** | `grill-me` | Pressure-tests vague concepts and assumptions before code is written. |
| **Matt Pocock** | `grill-with-docs` | Stateful interrogation maintaining `CONTEXT.md` and ADR records. |
| **Matt Pocock** | `prototype` | Spits out disposable UI variations to test UX before locking architecture. |
| **Matt Pocock** | `domain-modeling` | Keeps evolving business terms consistent in `CONTEXT.md`. |
| **Hallmark** | `hallmark` | Enforces 57 anti-slop gates, distinct macrostructures, and Sun Valley brand styling. |
| **Hallmark** | `hallmark-redesign` | Swaps entire structural layouts instantly while preserving copy and assets. |
| **Hallmark** | `hallmark-study` | Extracts design DNA from visual references into an actionable `design.md`. |
| **pstack** | `poteto-mode` | Orchestrates agents with disciplined step-by-step playbooks and todo tracking. |
| **pstack** | `figure-it-out` | Generates ad-hoc, auditable execution paths when specs are loosely defined. |
| **pstack** | `verification-hooks` | Tests real UI flows and forms instead of assuming passing builds mean working code. |

---

## How to Trigger Skills in Antigravity

Because the skills are registered in `.agents/skills/`, you can trigger them naturally in chat:
* *"Activate `grill-me` on this new sample request flow."*
* *"Use `hallmark` to build the industrial product card component."*
* *"Run `hallmark-redesign` on this hero section to make it an asymmetric editorial layout."*
* *"Enter `poteto-mode` to implement the B2B inquiry form."*
* *"Run `verification-hooks` to check the mobile responsiveness and form validation."*
