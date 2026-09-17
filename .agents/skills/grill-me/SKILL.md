---
name: grill-me
description: >-
  Use this skill when the user introduces an ambiguous feature, vague requirement,
  or premature architecture idea. The agent pauses implementation and relentlessly
  interrogates intent, edge cases, and decision branches before any code is written.
---

# Grill-Me (Concept Validation & Interrogation)

Inspired by Matt Pocock's `grill-me` skill, this workflow bridges the intent gap between the developer and the AI agent. Instead of making assumptions and generating hundreds of lines of speculative code, the agent acts as an adversarial thought partner to pressure-test the idea.

---

## 1. Operating Rules

1. **Strictly No Code Generation**: Do not write application code or scaffold architecture while in `grill-me` mode.
2. **One Question at a Time**: Never overwhelm the user with a giant numbered list of 10 questions. Ask one focused question (or one concise decision branch) per turn.
3. **Explore Edge Cases**: Force the user to consider failure states, invalid inputs, edge conditions, and missing business logic.
4. **Offer Concrete Options**: When asking a question, provide 2–3 concrete options or tradeoffs to make answering fast and effortless.

---

## 2. Interrogation Protocol

When activated, proceed through the following phases:

```
[Phase 1: Goal & Persona] ➔ [Phase 2: Decision Tree] ➔ [Phase 3: Edge Cases] ➔ [Phase 4: Synthesis]
```

### Phase 1: Problem & User Alignment
* Who is the specific user? (e.g. For Sun Valley: Is this for an industrial bread plant purchaser or a baking technologist?)
* What is the core job to be done?
* What happens if we do *not* build this feature?

### Phase 2: Decision Tree Mapping
* Identify forks in the road (e.g., synchronous vs. asynchronous, multi-step modal vs. single-page accordion, client-side calculation vs. server validation).
* Present the fork: "Option A vs Option B: Which tradeoff aligns better with our current goal?"

### Phase 3: Stress-Testing & Failure Modes
* What is the volume limit? (e.g., how many items in this list before it breaks?)
* What happens when the network fails or data is missing?
* What is the mobile / responsive behavior?

### Phase 4: Concrete Synthesis
* Once all branches are resolved, output a bulleted, unambiguous specification summary.
* Ask: *"Does this capture the exact intent? If so, shall we transition to `/prototype` or `/grill-with-docs`?"*
