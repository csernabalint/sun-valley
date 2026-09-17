---
name: figure-it-out
description: >-
  Use this skill when a task does not fit standard playbooks or when specifications
  are loosely defined. The agent formulates a bespoke, auditable execution path with
  explicit checkpoints and risk management.
---

# Figure-It-Out (Ad-Hoc Playbook Generator)

When dealing with high volatility or novel problems that have no predefined playbook, `figure-it-out` steps in. It rapidly analyzes the problem space, formulates an ad-hoc execution strategy, and presents a transparent checklist before taking action.

---

## 1. Operating Rules

1. **Synthesize Before Acting**: Break down ambiguous or sprawling tasks into 3–6 linear, testable milestones.
2. **Identify Unknowns & Risks**: Explicitly call out assumptions, missing packages, or uncertain browser behaviors.
3. **Auditable Checkpoints**: Every milestone must have a tangible artifact (file, test output, visual prototype) as proof of completion.

---

## 2. Dynamic Playbook Template

When generating an ad-hoc plan:

```markdown
### Bespoke Playbook: [Task Name]
- **Target Outcome**: [Clear definition of done]
- **Key Risks**: [Potential failure points / ambiguities]

#### Execution Milestones:
- [ ] 1. Discovery & Boundary Definition: [Scope limits and required context]
- [ ] 2. Architectural / Visual Spike: [Minimal viable spike or layout test]
- [ ] 3. Implementation: [Step-by-step modification]
- [ ] 4. Verification Checkpoint: [Runtime test or visual audit]
```
