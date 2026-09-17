---
name: grill-with-docs
description: >-
  Use this skill for stateful interrogation sessions. It combines the rigorous questioning
  of grill-me with automatic documentation updates, recording decisions directly into
  CONTEXT.md as Architecture Decision Records (ADRs) and maintaining the domain glossary.
---

# Grill-with-Docs (Documentation-Aware Interrogation)

An evolution of `grill-me` designed for long-term consistency. As the agent interviews the developer, it continuously records outcomes in [CONTEXT.md](file:///c:/Users/csern/Desktop/sun%20valley/CONTEXT.md), locking down terminology and logging architecture decisions to prevent future context drift.

---

## 1. Operating Rules

1. **Active Context Referencing**: Always inspect `CONTEXT.md` before asking a question. Do not re-ask questions that have already been resolved.
2. **Synchronize Business Language**: If a new domain concept emerges (e.g. *Brix fok mérés*, *aszeptikus konténer standard*), formalize its definition immediately in the glossary.
3. **Draft ADRs**: When an architectural fork is decided (e.g. choice of UI component library, state management strategy, form validation approach), document it as an ADR entry.

---

## 2. Execution Workflow

### Step 1: Read Existing Context
Inspect [CONTEXT.md](file:///c:/Users/csern/Desktop/sun%20valley/CONTEXT.md) and identify relevant entities, personas, and existing decisions.

### Step 2: Conduct Socratic Interview
Ask targeted, branch-by-branch questions (similar to `grill-me`). Present concrete options:
* E.g. *"For the sample request flow: Should we allow immediate anonymous submission or require company tax ID verification upfront?"*

### Step 3: Record Decision in `CONTEXT.md`
Once a decision is reached, update `CONTEXT.md` with:
```markdown
### ADR-XXX: [Title of Decision]
* **Date**: [YYYY-MM-DD]
* **Status**: Accepted
* **Context**: [Summary of the trade-off considered]
* **Decision**: [The chosen path and rationale]
* **Consequences**: [Impact on UI, data structure, or dependencies]
```

### Step 4: Confirm and Transition
Summarize the updated document sections and suggest next steps (e.g., prototyping or playbook execution).
