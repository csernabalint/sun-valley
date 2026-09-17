---
name: poteto-mode
description: >-
  Use this skill to orchestrate disciplined, playbook-driven engineering workflows
  (Feature, Bug Fix, Refactor, UI Polish). Enforces step-by-step checklist tracking,
  phase transitions, and runtime verification before declaring completion.
---

# Poteto-Mode (Disciplined Playbook Orchestration)

Inspired by Lauren Tan's (@poteto) `pstack / poteto-mode`, this skill transforms the AI agent from a loose text generator into a rigorous, verification-first software engineer.

---

## 1. Operating Rules

1. **Mandatory Todo Checklist**: Never execute multi-step tasks without an explicit, tracked todo list in context.
2. **One Phase at a Time**: Do not jump ahead to implementation before completing the specification and verification strategy.
3. **No Unverified Claims**: Never state *"everything works as expected"* without showing runtime test output or browser DOM proof.

---

## 2. Core Playbooks

### Playbook: Feature Implementation
```markdown
- [ ] Phase 1: Requirement & Domain Check (Verify against CONTEXT.md)
- [ ] Phase 2: Implementation Plan (Files, dependencies, components)
- [ ] Phase 3: Anti-Slop Layout Check (If UI-related, apply Hallmark gates)
- [ ] Phase 4: Core Implementation (Clean, typed code)
- [ ] Phase 5: Runtime Verification (Interactive flow test via verification-hooks)
- [ ] Phase 6: Documentation & ADR (Update CONTEXT.md if needed)
```

### Playbook: UI / Polish Execution
```markdown
- [ ] Phase 1: Macrostructure & Theme Audit (Hallmark 57 gates)
- [ ] Phase 2: Color Token Enforcement (Sun Valley brand variables)
- [ ] Phase 3: Typographic Rhythm & Contrast Check (WCAG AAA)
- [ ] Phase 4: Responsive & Mobile Verification
- [ ] Phase 5: Interaction & Feedback Polish (Focus states, hover, loading spinners)
```

### Playbook: Bug Fix
```markdown
- [ ] Phase 1: Reproduction (Isolate input, state, or broken flow)
- [ ] Phase 2: Root Cause Analysis (Trace failure to source)
- [ ] Phase 3: Minimal Surgical Fix (No unrelated refactors)
- [ ] Phase 4: Regression Test & Verification
```

---

## 3. Execution Protocol

1. Match the user request to the appropriate playbook.
2. Render the initial checklist in the conversation.
3. Progressively update the checklist (`[x]`) as each phase is completed and verified.
