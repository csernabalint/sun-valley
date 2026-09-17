# pstack Execution & Verification Runbook

This runbook covers the disciplined execution framework adapted from Lauren Tan's (@poteto) `pstack / poteto-mode`.

---

## 1. Operating Philosophy: Verification-First

A clean build or zero TypeScript errors does NOT prove that a user flow works. The `pstack` discipline requires the agent to:
1. Break down work into linear playbooks.
2. Track state with explicit todo lists.
3. Validate runtime behavior (DOM state, form validations, interactive feedback) before declaring success.

---

## 2. Core Skills

### `/poteto-mode`
* Front door for structured engineering tasks.
* Matches the task to a playbook (Feature, Bug Fix, Refactor, UI Polish).
* Renders a live checklist in chat and checks off phases sequentially.

### `/figure-it-out`
* For novel, ill-defined, or high-volatility tasks that lack a standard playbook.
* Rapidly generates an ad-hoc, auditable plan with concrete checkpoints.

### `verification-hooks`
* Executes runtime assertions on actual UI flows:
  * Sample request form validation (tax ID, email, plant type).
  * TDS modal trigger and payload check.
  * Mobile breakpoint testing ($375\text{px}$, $768\text{px}$).
  * Accessibility and color contrast checks.
