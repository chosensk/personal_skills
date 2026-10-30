---
name: engineering-workflow
description: "Coordinate cross-module or high-risk software development, or an explicitly requested personal engineering workflow. Route existing skills and enforce specification, authorization, verification-evidence, and formal-review gates. Skip routine factual questions and isolated low-risk edits."
---

# Engineering Workflow

Own orchestration and completion gates, not every engineering technique. Reuse
project conventions and focused skills; do not create a second workflow system.

## Establish Scope Before Action

1. Read applicable instructions and linked project rules. Host restrictions and
   explicit user limits take precedence; apply project overrides where allowed.
   This skill grants no additional execution or external-action permissions.
2. Identify intent: discussion/research, planning, implementation, review, or
   release. A read-only request creates no task records or other files.
3. Identify the authoritative task/specification and task-owned paths. Inspect
   existing changes before editing; preserve unrelated work and do not claim it.
4. Classify by risk, not file count. Authentication, data writes, SQL, messages,
   device control, production configuration, cross-module contracts, security,
   performance, stability, and unresolved acceptance require relevant gates.

## Choose The Smallest Sufficient Path

Classify by actual risk and affected contracts. Multiple operational steps alone
do not make a clear, low-risk task complex. Apply the proportional verification
and evidence-reuse rules in [gate-evidence.md](references/gate-evidence.md).

| Request | Path |
| --- | --- |
| Factual question or discussion | Answer from evidence; no development ceremony |
| Isolated, clear, low-risk edit | State acceptance briefly; edit and minimally verify |
| Ambiguous small request | Resolve material scope/acceptance questions first |
| Complex or high-risk implementation | Follow [development-workflow.md](references/development-workflow.md) |
| Formal review, including workflow documents | Follow [review-toolchain.md](references/review-toolchain.md) |
| Release, merge, commit, archive, production action | Verify applicable authorization separately; never infer it from task completion |

## Route Skills Without Importing Conflicting Workflows

Read [skill-routing.md](references/skill-routing.md) when selecting specialized
skills. Load only stage-relevant instructions; respect a project's stage limit
(use at most three active skills per stage when none is specified). This router
counts toward that limit. An audit subject is not an activated workflow.

Prefer project skills, then a single suitable user-level version. Read a selected
skill before use. Check host/tool availability instead of assuming a file on disk
is an executable skill. Never install or upgrade missing dependencies implicitly.

When a skill selected for the current step is absent from both project and global
sources, follow the missing-skill protocol in
[skill-routing.md](references/skill-routing.md): request explicit installation
consent, install only the approved candidate, or select an installed equivalent.
If no equivalent exists, give the executing Agent the step objective, deliverable,
acceptance, and constraints, then execute by objective. This fallback preserves
mandatory tool and authorization gates; it is not permission to bypass them.

If a candidate mandates conflicting commits, approvals, agents, or artifacts,
select a compatible alternative or use explicitly described methods without
claiming to execute the whole candidate. Do not silently rewrite a native
workflow's authorization boundary, particularly OpenSpec propose/apply.

## Invariants

- One authoritative specification/state; reference it from other systems.
- Agree acceptance, constraints, module boundaries, and a verification path
  before implementation. Resolve material ambiguity rather than guessing.
- Existing in-scope implementation authorization survives ordinary checkpoints;
  scope/contract changes and dangerous operations require the applicable approval.
- Work sequentially by default. No implicit subagents, branches, worktrees,
  commits, pushes, PRs, merges, archives, or production calls.
- Test and assess security throughout implementation, not only at the end.
- Review dispatch has one owner. A findings checklist cannot launch another
  review chain. Carry failure state and scope through every permitted fallback.
- Bind evidence to the reviewed/tested content and environment. Changed inputs
  invalidate dependent evidence, not automatically every unrelated check.
- Distinguish implemented, verified, reviewed, and release-ready. An unrun,
  incomplete, stale, or blocked check is never a pass. Uncommitted work alone
  does not prevent delivery; record limitations explicitly.

## Delivery

Before implementation, establish applicable checks and their evidence using
[gate-evidence.md](references/gate-evidence.md). Reuse that record during
verification and delivery; do not create another tracker. Each development step
has a completion gate, not just a suggested activity.

Report scope, authoritative record when required, actual checks/results, review
method/findings, remaining risks, and user actions. Required gates must pass on
current content before verified/reviewed readiness is claimed. Implementation
completion alone is not release authorization. These instructions are not CI
enforcement; use existing CLI/CI gates without silently installing new ones.

For maintenance, use [validation-scenarios.md](references/validation-scenarios.md)
to exercise routing, permissions, evidence, and fallback behavior. Structural
validation alone cannot demonstrate behavioral compliance.
