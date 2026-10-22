# Development Workflow

Use for complex or high-risk implementation. The eight steps are obligations,
not a waterfall: clarification revisits specifications; tests and security run
inside implementation; review fixes return to affected verification.

Use [gate-evidence.md](gate-evidence.md) to record applicable checks and completion
evidence in the authoritative task record. Gate records are sections of that
record, not eight mandatory new documents.

## 1. Align Requirements

Read existing specifications and actual implementation before drafting. Capture
What, Constraints, Acceptance Criteria, Module Boundaries, MUST/MUST NOT,
observable contracts, and non-goals. Separate observations from assumptions.

Use the existing OpenSpec/Trellis system. If none exists, follow project policy
for choosing one; without a required system, use one compact task document in an
agreed project location. Do not initialize tools as a side effect. Do not write
records for read-only discussion/research/planning requests unless explicitly
authorized. Required implementation artifacts must exist before their gate closes.

Gate: each intended behavior has observable acceptance, explicit non-goals, and
an authoritative specification location; observations and assumptions are distinct.

## 2. Resolve Material Questions

Search code, tests, configuration, and existing decisions first. Ask one
highest-value blocking question at a time, explaining the decision and tradeoff.
Record answers in the authoritative spec; no second PRD or status list.

Do not turn assumptions into accepted requirements. Minor reversible details may
be recorded as assumptions where permitted; security, contract, data-loss, and
scope decisions need explicit resolution. An arbitrary round limit is not a
reason to start work with unresolved blockers.

Gate: no material scope/contract/security decision remains unresolved; answers
are reflected in acceptance, not only in conversation history.

## 3. Analyze Impact And Establish A Baseline

Trace callers, affected consumers, storage, messages, ownership/tenant boundaries,
and failure paths. Where project rules require GitNexus, use graph exploration
and pre-edit impact with index-freshness gates. Report HIGH/CRITICAL risk before
editing; UNKNOWN remains unresolved and requires corroboration. Do not substitute
text search for a required graph gate or silently bypass unavailable tooling.

Identify existing failures and dirty paths without attributing them to this task.
Run proportional baseline checks where practical; record when a baseline cannot
be obtained. Suggest isolation only when beneficial and allowed; never create a
branch or worktree without the required authorization.

Gate: affected callers/contracts and side effects are accounted for; required
impact checks are resolved and baseline limitations are explicit.

## 4. Plan Execution And Verification Together

Define exact intended paths, ordered slices/dependencies, acceptance mapping,
test boundaries, runnable checks, relevant security checks, risks, and rollback
approach. File counts guide sizing, not correctness or permission.

Choose real commands from project build/CI configuration, not generic examples.
Distinguish configured enforcement, desired coverage targets, and measured values.
Do not activate new plugins, profiles with side effects, dependencies, or stricter
thresholds merely because a generic skill recommends them.

For authorized implementation, announce the plan and continue within scope.
Explicit proposal-only workflows still stop at their documented boundary.

Gate: every planned behavior maps to a verification method, all required tooling
and permissions have a viable path, and implementation is actually authorized.

## 5. Implement In Verified Slices

Load affected project conventions. Iterate:

1. For a bug, obtain a feedback loop that catches the original symptom; for new
   behavior, establish an acceptance-based failing test where feasible.
2. Confirm failure is the intended behavior failure, not setup/import failure.
3. Make the smallest scoped implementation; run the relevant check to green.
4. Apply small behavior-preserving cleanup only with valid tests and authorization.
   Contract/architecture changes return to the specification and impact gates.
5. Record the evidence checkpoint and advance. No automatic Git commit.

Test public behavior at agreed boundaries; use independent expected outcomes,
not implementation-shaped or tautological assertions. Honor project fixtures,
static context cleanup, database dialect, and service isolation requirements.
Do not add slow integration infrastructure when a smaller test proves the risk.

If reproduction or a valid test boundary is unavailable, report the limitation
and obtain the missing evidence/decision; do not invent a root cause or claim a
regression is covered. Existing test-boundary approval can be reused; if a chosen
native skill requires new approval, honor it or choose a compatible method.

Gate: each completed slice implements its specified behavior and has current
evidence; partial/deferred behavior stays open in the authoritative task list.

## 6. Verify And Review

Run the narrow meaningful checks first, then affected contract/integration checks
and configured project gates. Capture commands, exit status, actual results,
tested content/environment, and skipped/blocked checks with reasons.

An exit code of zero with zero relevant tests is not proof of behavior coverage.
Builds with tests skipped are not test evidence; coverage report generation is
not coverage-threshold enforcement. Known baseline failures remain disclosed.

Formal review follows [review-toolchain.md](review-toolchain.md). Review includes
both specification completeness and code quality; passing one cannot hide a
failure in the other. Reproduce or substantiate findings before editing.

Local correctness checks are not automatically a formal review. Follow project
policy to determine which tasks require formal review; explicitly requested
reviews always enter the review toolchain. Do not launch external reviewers for
every tiny edit solely because a generic checklist recommends review.

Gate: required tests/checks passed with meaningful coverage; required formal
review completed, covered the intended scope, and closed blocking findings.

## 7. Check Security And Operational Effects

Identify risks during planning, check them while coding, and close them before
delivery: credentials/PII, authentication and ownership, input boundaries, SQL,
deserialization, external calls, logs, retries/idempotency, message side effects,
configuration compatibility, and data recovery where relevant.

Use available configured scanners when required. Keyword searches are triage,
not equivalent to a secret/dependency scanner. Missing tools or scan databases
are limitations, never clean results; do not install or send sensitive source
to an external service without authorization. Preserve permitted DEBUG diagnostics
while removing secrets and temporary noisy instrumentation.

Gate: each applicable security/data-effect risk has verification or an explicitly
recorded unresolved limitation; mandatory security gates cannot be waived by a
clean build, a scanner-shaped keyword search, or an unrelated review verdict.

## 8. Close Against Acceptance

Check each MUST/MUST NOT, boundary, task checkbox, and required record against
current evidence. Re-run only evidence invalidated by edits, dependency/config
changes, or demonstrated uncertainty. Required checks cannot be omitted as an
optimization. Resolve finding dispositions and re-review affected changes.

Report implemented/verified/reviewed status separately. Block release-readiness
claims if mandatory evidence is missing. Do not require a clean worktree to
deliver; do not archive, commit, publish, merge, or push as implicit cleanup.
When explicitly authorized to commit, also perform required graph-change checks.
Archive only within the applicable lifecycle policy and current authorization.

Gate: all required current-content checks passed, applicable conditional gates
are satisfied, mandatory findings are closed, and remaining limits/user actions
are disclosed. Report a blocked or partial handoff when this condition is unmet.
