# Observable Contract Matrix

## Baseline And Scope

Accept a verified commit/ref, user-provided previous source, or captured task-start
snapshot that actually represents the requested before-state. Record its identity
and the current content identity, including untracked/ignored files when in scope.
Inspect relevant staged and unstaged differences; preserve unrelated user edits.
If only HEAD is available, explicitly limit the comparison to HEAD versus current
content; do not label it task-only or pre-task unless supported by evidence.
With no usable before-state, report current behavior and the missing comparison
prerequisite. Do not invent old behavior from method names or comments.

Read governing acceptance/specifications before judging intended differences.
Use the project's required graph tools for affected symbols/callers, then actual
source and targeted searches where allowed. Record unresolved dynamic dispatch,
index freshness, UNKNOWN, or HIGH/CRITICAL impact rather than inferring safety.

## Select Relevant Rows

| Contract | Compare before and after |
| --- | --- |
| Inputs and outputs | Accepted inputs, defaults, validation, route/method, status/error codes, response fields/types, serialization, ordering and pagination |
| Access and ownership | Authentication, authorization, tenant filters, ownership checks, independent product/service boundaries |
| Time and attribution | Event versus receipt time, timezone, date rollover, statistical day, inclusive/exclusive windows, late data |
| Values and aggregation | Units, precision/rounding, null/missing/zero distinctions, invalid samples, effective counts, denominators and thresholds |
| Errors and fallback | Exception propagation, retry eligibility, timeout, partial results, empty-data behavior, recovery/fallback branches |
| Side effects | Writes, transaction scope, message destination/content/order, duplicate delivery, idempotency, caches and recomputation |
| Caller compatibility | Existing clients, sync/async expectations, schema/config defaults, persistence compatibility, observable performance/resource changes |

Skip irrelevant rows with a brief reason when their omission could be ambiguous.
For changed branches, include normal, empty/null/invalid, boundary, and failure
inputs as applicable. Follow directly affected side effects across module edges
without converting a scoped audit into unrelated cleanup.

## Evidence And Verdict

Use a compact record per material contract:

```text
Contract / representative inputs:
Before -> after:
Classification: preserved | changed | boundary correction | not established
Authorization: explicitly approved | contrary to preservation requirement | unresolved
Evidence: baseline/current locations, caller evidence, actual tests/runtime checks
Risk / remaining verification:
```

Static comparison, executed tests, and runtime observations have different strength.
Distinguish planned from executed checks; state environment and coverage for actual
results. Recommend targeted differential tests for uncertain branches when useful,
but run them only within current permissions and known side-effect boundaries.
Never use production replay or data mutation to prove compatibility implicitly.

Unapproved differences or missing required evidence prevent a clean preservation
verdict. Report exact affected inputs and users/callers where known. "No difference
found in these contracts" is narrower and more accurate than "logic unchanged"
when coverage is partial. Refresh dependent evidence if audited content changes.
