# Delivery Content Contract

Read the section matching the requested deliverable. Match existing structure
instead of forcing these headings into every document.

## Evidence And Status

For each significant statement retain its source: approved decision, current
code/contract, configuration, performed test/review, or observed runtime result.
Use existing task records for detailed evidence; document only useful summaries
and references, not another task tracker.

Distinguish:

- Proposed: an option, not an implemented decision.
- Approved: authorized scope/decision, not proof of implementation.
- Implemented: present in the inspected revision.
- Verified: passed specified checks on known content/environment.
- Deployed/published: confirmed in the specified target environment with evidence.
- Pending/blocked: named remaining work, prerequisite, or unverified condition.

Do not claim release completion from local code/tests or claim online Nacos
consistency from repository snapshots. A deployment instruction is not evidence
that someone executed it. If requested runtime evidence is unavailable, state so.

## API Contract

Only include verified fields; surface missing evidence rather than inventing
defaults. Inspect beyond annotations where behavior depends on implementation.

| Concern | Required when relevant |
| --- | --- |
| Entry | HTTP method, service path, gateway path, rewrite/prefix rules |
| Access | Authentication, tenant/ownership permissions, actual required headers |
| Input | Parameters/body, types, requiredness, validation, defaults and limits |
| Time/data semantics | Date/time source and zone, units/precision, null/missing behavior, count meanings |
| Output | Actual serialized names, response envelope, enums, status distinctions |
| Failure | Business/HTTP errors, forbidden/not-found cases, unavailable dependencies |
| Compatibility | Changed versus preserved behavior, affected consumers, migration steps |
| Example | Valid illustrative request/response, no real identifiers or credentials |

If an API changed during implementation, update its existing contract when
authorized or clearly identify the required documentation change. Do not infer
public API compatibility from preserved Java signatures alone. Actual field,
permission, default, time-window, and fallback semantics also matter.

## Technical Handover

Cover the implemented boundary and operationally useful facts: modules/owners,
interfaces, data/cache/message effects, configuration locations, deployment
ordering, performed checks, observability, recovery, and known limitations.

Reference authoritative environment/configuration instructions rather than
copying credentials or a full sensitive configuration export. Distinguish safe
local validation from live operations requiring separate approval. For rollback,
state prerequisites and potential irreversible effects, not a generic promise
that every change can be reverted safely.

## Existing Directory And Multiple Views

Use destination instructions, indexes, and neighboring examples to choose paths.
Update only authorized related indexes. Links must resolve from the actual
document location; do not assume all destinations are in the repository.

When Markdown/HTML coexist, align version meaning, phase, dates, completed work,
risks, remaining work, and next step. Preserve historical decisions/release dates
that remain true; remove obsolete current-state claims rather than erase history.
If one view cannot be edited or validated, report the unsynchronized view.

## Completion Boundary

A useful handoff states what changed, why, evidence, limits, and next action.
It does not introduce a new acceptance decision, publish files to an external
service, archive a task, or claim an unperformed code/runtime check succeeded.
