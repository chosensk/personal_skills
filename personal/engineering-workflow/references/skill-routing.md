# Skill Routing And Compatibility

These are optional capability routes, not installed dependencies or permission
grants. Resolve available paths from the current host's skill inventory. Prefer
project conventions and one canonical copy; do not copy tool-owned templates.

## Stage Routes

First identify the host and actual stack/build configuration. Resolve commands,
test fixtures, coverage profiles, and Active project contracts from their source
files, not from cached assumptions or a generated symbol inventory. A `To fill`
guideline is not a project convention. Record missing standards only when they
affect this task; filling templates is separate work.

| Need | Candidate | Compatibility check |
| --- | --- | --- |
| Task lifecycle | Project `trellis-start` / `trellis-continue` | Reuse existing task; honor read-only request boundaries |
| Clarification | `trellis-brainstorm`, `grill-me`, `grill-with-docs` | Only material questions; documentation writes and invoked tools must be permitted |
| Specifications | Existing OpenSpec workflow or Trellis artifacts | One authority; OpenSpec propose is planning-only when its installed contract says so |
| Impact | `gitnexus-exploring`, `gitnexus-impact-analysis` | Required graph gates and UNKNOWN/HIGH/CRITICAL handling cannot be weakened |
| Planning | `planning-and-task-breakdown` | Reuse tasks; do not introduce repeated approval checkpoints beyond effective policy |
| Implementation | `trellis-before-dev`; incremental implementation methods | Small tested slices; no automatic commit or clean-worktree completion requirement |
| Tests | `tdd`, language-specific TDD guidance | Confirm testing boundaries as required; use actual project fixtures and compatible language APIs |
| Root-cause diagnosis | `diagnosing-bugs` | Original-symptom feedback loop, minimized reproduction, and regression evidence |
| Quality review | `code-review-and-quality` | Checklist only; no independent tool dispatch or implicit reviewer agents |
| Security | Stack-appropriate security skill | Actual trust boundary and configured stack, not universal JWT/CSRF defaults |
| Verification | Project `trellis-check`; adapted stack verification guidance | Module-scoped actual commands; preserve configured CI gates; no formatting writes during read-only review |
| Delivery | Project finish-work skill | No implicit commit/archive; reuse valid evidence and disclose limitations |
| Delivery document synchronization | `project-delivery-docs`, when available | Only requested or already-required deliverables; existing directory conventions and code/evidence-based status |
| Nacos release configuration preflight | Project `nacos-release-preflight`, when available | Read-only scoped environment comparison; no implicit config writes/publication or business-readiness claim |
| Author/period Git work report | `git-work-report`, when available | Explicit identity, ref, timezone/date basis; local read-only evidence, no deployment inference or implicit publication |
| Behavior preservation / compatibility comparison | `behavior-contract-audit`, when available | Reliable before-state, observable contracts and authorized differences; contributes checks without replacing formal review |

Choose no more than the applicable per-stage skill budget. With this router and
one project skill active, add at most one specialist under the default budget.
Move to the next stage rather than recursively loading all referenced skills.

For Java services, language/security/TDD skills provide techniques, while actual
source level, Spring version, persistence stack, and project test annotations
control examples. Do not introduce records, JPA, Testcontainers, a new auth model,
or bare Mockito fixtures merely because a generic skill demonstrates them.

Generated domain skills are navigation aids, not authoritative product-boundary
or quality rules. Reuse helpers only within allowed ownership boundaries; shared
code is not automatically preferable to independent product-line delivery.

## Known Compatibility Traps

- `incremental-implementation` may require a commit per slice and an entirely
  committed worktree. Use its slicing methods, not that unauthorized lifecycle.
- Generic SDD/planning skills may add human approval at every transition. Do not
  claim full execution while omitting those gates: choose a compatible project
  workflow. Explicit native planning workflows retain their own stop boundary.
- Some `tdd` versions require user-approved seams and place refactoring in review;
  stack-specific TDD may use Red/Green/Refactor. Select one governing method.
  Do not mix contradictory loops or bypass required seam approval.
- Generic `code-review` may force parallel agents, issue-tracker setup, and a
  fixed-point-to-HEAD diff. Do not select it for an uncommitted-workspace review
  or a fallback stage that prohibits delegation. Its Spec/Standards axes can be
  used as checks without running its workflow.
- gstack review may include automatic fixes, environment writes, external calls,
  or further reviewers. A read-only fallback must omit those incompatible
  operations; if the installed skill cannot honor that boundary, it is unavailable
  for that stage. Do not claim the full native workflow was executed.
- Generic verification examples may use JS/Python commands in Java projects,
  skip tests, apply formatters, ban useful DEBUG logs, or assume coverage tooling.
  Derive actual checks from the project and use examples only where applicable.

## Missing-Skill Protocol

Apply only to a skill actually selected for the current step, not every optional
name in this routing table. Resolve in this order:

1. Check the current host inventory and relevant project/global skill locations
   for the exact skill, aliases, or an existing compatible copy. Read its entry
   point where available. A present but unlisted, unreadable, or host-incompatible
   skill is not automatically absent; report the actual availability problem and
   do not reinstall over it. Do not assume a skill is missing from its name alone.
2. If absent from both scopes, explain its purpose, proposed source/ref, install
   location/scope, and any known risks or dependencies. Locate a reputable source
   with read-only discovery when permitted; do not invent a repository from a
   skill name. Inspect available instructions/helpers for unexpected commands,
   credential access, external calls, and writes. If a source cannot be identified
   or inspected, disclose that before requesting consent; do not install an
   unverified candidate under generic consent.
3. Ask the user explicitly whether to install the identified candidate, using the
   applicable confirmation format. Creating this workflow, selecting a skill,
   silence, and a vague reply are not installation consent. Ask once per distinct
   candidate/scope in a task; a refusal must not cause repeated installation prompts.
4. On explicit approval, automatically run the available trusted installer within
   the approved source/ref/destination and host permissions. For Codex, read and
   follow `skill-installer` and its helper scripts when available; honor an approved
   project destination instead of silently switching to global installation.
   Do not overwrite/upgrade existing skills, install executables/packages, change
   configuration, supply credentials, or add transitive skills without separate
   applicable approval. If the installer itself is missing, use an already trusted
   documented installation method only when its actions were covered by consent;
   otherwise report the installation blocker instead of recursively installing
   installers or inventing shell commands.
5. Verify the installer outcome, destination, readable `SKILL.md`, candidate
   identity/ref where available, and host compatibility. Read the installed skill
   before applying it. Installation success is not current-session activation or
   permission for the installed instructions' side effects. If a host refresh/new
   turn is needed, tell the user; do not claim an unavailable invocation ran.
   On installation failure, record the actual cause and use steps 6-7 when allowed;
   a different source/ref/scope requires fresh consent, not a silent retry elsewhere.
6. If the user declines, does not explicitly approve, or installation/activation
   remains unavailable, search the current installed project/global skills for an
   equivalent. Read candidate instructions, compare objective, outputs, acceptance,
   permissions, and host compatibility, and select the smallest sufficient match.
   Explain the substitution and any gap; do not present an installed alternative
   as the missing original or require installation of another skill automatically.
7. If no installed equivalent can satisfy the step, provide the objective-based
   execution brief below and continue the allowed work directly. Preserve every
   mandatory gate: if the goal requires a specified unavailable tool, scanner,
   native workflow, or evidence source, mark that dependent gate blocked and
   explain the missing prerequisite. Generic Agent reasoning is not a replacement
   for mandated OCR review, graph impact, security scanning, or programmatic checks.

Record the missing capability, consent decision, actual installation outcome or
substitution, and remaining gaps in the existing task evidence where applicable.
Do not create a second tracker. This protocol changes skill resolution, not the
formal review fallback order or authorization policy.

## Objective-Based Execution Brief

Give this brief to the executing Agent in the current conversation/task context;
it does not authorize spawning or messaging another Agent. If execution stays in
the main conversation, apply the brief yourself. Explain the missing skill's role
from known workflow contracts, not imagined contents of an unreadable skill.

```text
Step: current development stage and task scope.
Missing skill and role: the capability it was intended to contribute.
Objective: the observable outcome this step must achieve.
Inputs: authoritative specification, relevant files, available tools/evidence.
Deliverable: concrete artifact, scoped change, or verification result.
Acceptance: how to distinguish completion from an incomplete attempt.
Constraints: scope, permissions, required tools/gates, security/product boundaries.
Execution: use the available tools to achieve the objective; record real evidence.
Stop: identify any unmet mandatory prerequisite instead of inventing a pass.
```

Use the current step's completion gate in
[development-workflow.md](development-workflow.md) and evidence contract in
[gate-evidence.md](gate-evidence.md). Typical roles and outcomes:

| Missing capability | Objective and minimum deliverable |
| --- | --- |
| Clarification | Resolve material questions; record decisions and updated acceptance |
| Specification | Define behavior, constraints, MUST/MUST NOT, and boundaries in one authoritative record |
| Impact | Account for affected callers/contracts and side effects with required impact evidence |
| Planning | Produce ordered scoped tasks, verification methods, dependencies, and rollback approach |
| Incremental implementation | Deliver the smallest complete behavior slices with current verification |
| TDD / diagnosis | Establish an original-symptom or acceptance-based feedback loop and regression evidence |
| Quality review | Apply specification and quality checks through the controlling formal-review method when required |
| Security | Verify relevant trust/data-effect boundaries; disclose unavailable mandated scanners |
| Verification / handoff | Close applicable gates against current evidence and report unresolved limits |

## Conflicting Or Unusable Capability

Inspect the actual candidate before recommending it. A tool name in a skill,
an obsolete slash command, `disable-model-invocation`, or an unavailable host API
does not create an execution mechanism. Use available file-reading/routing only
when permitted; do not pretend an unavailable invocation succeeded.

Use the protocol above for an absent skill. For an installed but incompatible
specialist, choose a compatible installed alternative or objective-based method
and name the limitation; installation does not resolve an authorization conflict.
If the capability implements a mandatory gate, stop the dependent action or use
an explicitly permitted fallback. Preserve existing skills and project policy;
any repair/upgrade or Agent delegation needs its own applicable authorization.
