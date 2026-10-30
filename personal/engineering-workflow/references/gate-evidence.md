# Gate Evidence And Handoff

Read before planning complex implementation and when validating or handing off a
change. Store these fields in the existing task/specification system, not a new
global checklist. Small direct edits may use the final response as their record
where project policy permits; read-only work creates no records without permission.

## Establish Applicable Gates

Resolve each check from project rules, actual build/CI configuration, affected
contracts, and task risk. Retain the controlling source and scope:

- Required: explicitly mandated checks, configured enforcement, and checks needed
  to substantiate claimed acceptance. Failure/unavailability blocks that claim.
- Conditional: state the applicability condition. When true, treat as required;
  when false, record the reason as `not_applicable`, not a passing execution.
- Advisory: optional improvement or desired future target, explicitly separate
  from acceptance and configured enforcement.

Do not change gate classification after failure to obtain a pass. Material scope
or acceptance changes require the applicable user decision. A documented baseline
failure explains attribution; it does not silently disable a required gate.

## Proportional Verification And Reuse

Select checks by actual change risk and directly affected behavior. Run the
smallest meaningful checks that satisfy acceptance and applicable required gates;
do not run the full suite after every edit or step without a scope-based reason.

Reuse passing results when relevant content, inputs, environment, and check scope
are unchanged. Rerun only when a relevant change invalidates evidence, a check
fails and needs resolution, or new concrete risk evidence exposes a coverage gap.
Rerun or broaden only the affected checks; task length, a new workflow phase, or
general reassurance alone does not justify repeating completed checks.

This does not waive mandated full-suite/CI/security gates or retry requirements.
A failed or incomplete check remains unresolved, and evidence with unknown
relevance cannot be assumed reusable; resolve the specific uncertainty first.

## Minimal Record

Use native task fields or a compact table with equivalent semantics. Omit fields
that genuinely do not apply rather than creating a mandatory report per slice.

| Field | Required meaning |
| --- | --- |
| Acceptance / gate ID | Observable behavior or rule being verified |
| Source / classification | Controlling document/config and required/conditional/advisory status |
| Scope / content identity | Exact paths plus hashes, baseline, or equivalent reliable version identity |
| Inputs / environment | Relevant dependency/configuration versions, fixtures, test boundaries, runtime |
| Method / result | Actual command or manual procedure, exit code where applicable, relevant test count, result |
| Evidence location | Existing log/report/session output or captured result, with secrets redacted |
| Status / limitation | `not_run`, `pass`, `fail`, `blocked`, `not_applicable`, or `stale`, with reason |

Use `pass` only for a performed check that proves its declared criterion. Manual
inspection is valid evidence for suitable criteria, labeled as manual rather
than automated execution. Command exit zero alone proves neither relevant test
execution nor contract coverage. For coverage, distinguish configured threshold,
enabled profile, measured line/branch values, and aspirational target.

For review, additionally retain controlling policy, method/tool state, upstream
failures, per-file coverage and comparison mode, and findings/dispositions as
defined in [review-toolchain.md](review-toolchain.md). `completed` is a tool state;
it becomes a passing review gate only when coverage and findings permit it.

## Evidence Invalidation

Before reusing evidence, compare its inputs with current content. Code edits
invalidate checks that depend on the changed behavior. Shared fixtures, schemas,
dependency versions, runtime flags, configuration, and test-selection changes
can invalidate checks even when the reviewed source file is unchanged.

Record affected evidence as `stale`, then rerun the smallest sufficient dependent
checks. Preserve unaffected evidence. When dependency scope is uncertain, broaden
verification enough to resolve that uncertainty rather than guess. A content
hash proves identity, not test quality or tool success.

## Finding Disposition

For each actionable finding retain ID, severity, location, observed failure or
violated requirement, and evidence. A fixed finding needs current verification;
a false positive needs reasoning grounded in the code. Risk acceptance needs the
explicit user's decision and cannot waive mandatory non-waivable constraints.
Open findings never disappear through a reviewer switch or report regeneration.

## Handoff Decision

Report each status independently:

- Implemented: specified behavior exists; partial/deferred tasks remain open.
- Verified: applicable required build/test/security gates pass on current inputs.
- Reviewed: required formal method completed all declared coverage and mandatory
  finding dispositions satisfy controlling policy. If review is not required,
  say `not required`, not `passed`.
- Ready for the requested handoff: acceptance and all mandatory gates for that
  handoff are satisfied. Commit, archive, merge, deployment, and publication still
  require their applicable authorization and additional operation-specific gates.

If any required gate is fail/blocked/not_run/stale, deliver a truthful partial or
blocked handoff with the next action and owner. An unavailable optional check is
an explicit limitation, not grounds to fabricate a pass or a universal blocker.

For deterministic enforcement, use an existing CLI/CI check where available.
If the project lacks one, propose the smallest check separately; authoring this
skill does not authorize CI changes or make these prose gates tamper-proof.
