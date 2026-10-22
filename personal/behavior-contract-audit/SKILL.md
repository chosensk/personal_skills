---
name: behavior-contract-audit
description: Compare observable behavior before and after a code change to assess preserved logic and caller compatibility. Use for unchanged-logic questions, compatibility-sensitive refactors, and behavioral regression checks, not as a replacement for formal code review.
---

# Behavior Contract Audit

Answer whether a scoped change preserves business behavior, with evidence and
explicit uncertainty. Default to read-only comparison; neither fixes nor test
execution with side effects are implicitly authorized.

## Workflow

1. Identify the requested preservation contract, task-owned files, callers, and
   intended changes. Pin both sides to reliable content identities. A dirty
   worktree's HEAD is not automatically the state before this task. Without a
   reliable baseline, analyze current behavior only and state that preservation
   has not been established.
2. Read [contract-matrix.md](references/contract-matrix.md) and select applicable
   observable contracts. Follow required project graph/impact gates; UNKNOWN or
   empty callers do not establish safety. Examine adjacent callers only where
   the scoped change directly affects their behavior.
3. Compare code, callers, specifications, and available regression/runtime
   evidence. For each relevant contract, classify preserved, changed, boundary
   correction, or not established. Separately determine whether any change is
   explicitly authorized; code alone does not establish intent or approval.
4. Lead with what changed and what remains unproved. Provide a compact matrix of
   before/after behavior, evidence, compatibility risk, and verification gaps.
   Limit preserved claims to the inputs and environment actually supported.

## Gates And Boundaries

- A boundary fix still changes behavior for some inputs. Report that change even
  when it is desirable. Passing tests do not prove universal equivalence.
- Honor project ownership, tenant/security boundaries, and product-line isolation;
  similarly named behavior is not permission to merge independent implementations.
- This capability contributes contract checks, not a second review dispatcher.
  Formal review uses effective project/global rules and their existing toolchain
  (OCR Delegate, native Codex, compatible read-only gstack where permitted).
  Do not launch reviewers, retry failed tools, or claim formal review from this
  analysis alone. Mandatory unavailable evidence remains a gate limitation.
- Report proposed corrections without applying them during this audit. Fixes,
  message replay, configuration/data changes, acceptance changes, and new trackers
  require applicable authorization. Reuse existing task evidence when available.
- For skill validation, consult [scenarios.md](references/scenarios.md); scenario
  walkthroughs are not execution evidence for a real code change.
