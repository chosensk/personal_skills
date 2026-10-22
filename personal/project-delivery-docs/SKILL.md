---
name: project-delivery-docs
description: "Synchronize project plans, implementation progress, API contracts, and handoff documents with actual code and verification evidence. Use when asked to update a proposal after development, generate technical handover, or store delivery materials under existing directory conventions. Not for generic article writing or unrequested documentation expansion."
---

# Project Delivery Docs

Produce delivery documents that match what exists, not what an earlier plan
promised. Preserve the user's directory conventions and distinguish implemented,
verified, deployed, and pending work. This skill does not implement features or
authorize publication, deployment, Git operations, or changes to acceptance.

## 1. Establish The Document Set

Read applicable instructions for the source project and destination, including
ancestor rules and the destination index/naming examples. Identify the requested
audience, source task/specification, authorized output paths, and existing formats.
Use the supplied current destination; historical personal paths are not defaults.

Find existing topic documents before creating new ones. Reuse the established
classification and naming pattern. Ask only when the destination, audience, or
classification would materially change the deliverable. A request for advice or
an outline alone does not authorize saving files elsewhere.

Gate: the authoritative sources, output scope, and storage convention are known.

## 2. Reconcile Evidence Before Writing

Inspect task-owned changes, relevant code/contracts/configuration, test/review
results, and approved decisions. Follow project graph-exploration requirements
where applicable; documentation work does not waive them. Treat historical
conversation as discovery material, not proof that the current implementation
still matches it. Preserve unrelated changes in existing documents.

For each claimed capability, record evidence and status. Tests skipped, missing
runtime data, or an Agent's earlier completion statement are not verification.
State actual deviations from the approved plan. A missing requirement remains
missing: do not rewrite acceptance or mark tasks done just to match existing code.

Gate: implementation facts, planned behavior, deviations, and unknowns are distinct.

## 3. Update Only Applicable Deliverables

Use [delivery-contract.md](references/delivery-contract.md) for content rules.

| Requested outcome | Deliverable |
| --- | --- |
| Update plan/progress | Current phase, completed evidence, open work, risks, next authorized step |
| API change or explicit interface-document request | Code-grounded request/response contract and consumer migration notes |
| Technical handover | Ownership, dependencies, configuration/release steps, verification, troubleshooting, rollback, limits |
| Store a proposal | Clearly labeled proposal and known facts; no implementation/deployment claim |

Do not generate a full document bundle for every task. When both Markdown and
HTML already represent the same topic, synchronize affected facts/statuses while
preserving layout. Do not create a second format or regenerate the whole page
without a concrete need and authorization. Update relevant indexes and links.

Keep one authoritative requirement/task state; delivery documents reference it.
If a material design/behavior decision is unresolved, describe the discrepancy
and seek resolution instead of silently turning the actual behavior into policy.

Gate: requested views agree on facts without expanding task or artifact scope.

## 4. Validate And Hand Off

Check local links/anchors, file existence, encoding, code fences, version/date
consistency, and obsolete phase/next-step statements. Validate API examples
against serialization and actual contract evidence; label illustrative values.
For edited HTML, verify changed navigation/content and preserve the existing
design. Claim visual/browser validation only if actually performed.

Separate document validation from software validation: a clean Markdown diff
does not demonstrate a working API. Formal document/code review follows the
applicable OCR/fallback policy; do not start a separate recursive review chain.

Report exact changed documents, evidence used, unverified items, deviations,
publication/configuration status, and remaining user actions. No automatic
uploads, commits, Nacos publication, or task archive. Existing document dates
represent their actual meaning; do not change a release date to today's date
merely because the document was edited.

Gate: requested documents and indexes are consistent, evidence limitations are
visible, and any required review has actually completed.

For maintenance checks, read
[validation-scenarios.md](references/validation-scenarios.md). These are behavioral
acceptance cases, not an assertion that automatic selection or execution works.
