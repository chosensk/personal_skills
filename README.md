# Personal Skills

Source collection for personal Codex skills. Repository:
https://github.com/chosensk/personal_skills. Check Git status and the remote for
current publication state; local files alone do not establish what is published.

## Inventory

| Skill | Purpose | Source location in this collection |
| --- | --- | --- |
| Engineering Workflow | Risk-scaled development orchestration and review gates | [personal/engineering-workflow](personal/engineering-workflow/SKILL.md) |
| Project Delivery Docs | Evidence-grounded progress, API and handoff documents | [personal/project-delivery-docs](personal/project-delivery-docs/SKILL.md) |
| Git Work Report | Concise author/period reports from local Git history | [personal/git-work-report](personal/git-work-report/SKILL.md) |
| Behavior Contract Audit | Before/after business behavior and caller compatibility | [personal/behavior-contract-audit](personal/behavior-contract-audit/SKILL.md) |
| Word SOP Swimlane | Editable business flowcharts and SOP diagrams, with optional source screenshots | [personal/word-sop-swimlane](personal/word-sop-swimlane/SKILL.md) |
| PostgreSQL Growth Diagnosis | Cost-aware read-only table growth and retention diagnosis | [personal/postgresql-growth-diagnosis](personal/postgresql-growth-diagnosis/SKILL.md) |
| Nacos Release Preflight | Read-only configuration preflight for IoT-Admin-Cloud | [projects/iot-admin-cloud/nacos-release-preflight](projects/iot-admin-cloud/nacos-release-preflight/SKILL.md) |

Each skill directory includes an entrypoint and resources suited to its scope.
Scenario descriptions are not evidence of executed tests.
Original authoring assessments describe their stated historical versions only.

Third-party skills, plugin caches, conversation histories, configuration exports,
credentials and project business source code are not included. References to
external skills/tools are optional routes or explicit prerequisites, not bundled
dependencies or permission to install anything.

## Use In Codex

This is a source collection, not an automatically activated Codex skill directory.
Copy a selected complete skill directory into an approved discovery location:

- Personal skills: `$CODEX_HOME/skills/<skill-name>`, or
  `~/.codex/skills/<skill-name>` when `CODEX_HOME` is unset.
- IoT-Admin-Cloud skill: `<target-project>/.agents/skills/nacos-release-preflight`,
  following that project's instructions and the host's supported discovery rules.

Before copying, inspect any existing destination and compare differences. Do not
overwrite, delete or replace an installed copy implicitly. Keep a recoverable copy
of local changes when an approved update requires replacement. Confirm the host
exposes the skill after refresh or in a new conversation; files on disk alone do
not prove activation.

Example requests after discovery:

```text
Use $engineering-workflow for this cross-module implementation.
Use $project-delivery-docs to update the requested technical handover.
Use $git-work-report to summarize the specified author's work last week.
Use $behavior-contract-audit to compare this change with the agreed baseline.
Use $postgresql-growth-diagnosis to investigate PostgreSQL table growth.
Use $word-sop-swimlane to turn the supplied Word SOP into an editable swimlane diagram.
Use $nacos-release-preflight for an authorized read-only configuration comparison.
```

## Project And Tool Prerequisites

Word SOP Swimlane includes a Python-standard-library DOCX extraction helper.
Diagram generation/rendering and optional VSDX/WPS validation still require the
capabilities described in its format reference; they are not bundled generators.
The extractor covers the main document body and tables, not headers, footers or
chart rendering. Its current implementation requires the DOCX relationship part
`word/_rels/document.xml.rels`; documents without it are not supported by this
helper. The repository copy uses the user's requested output directory, falling
back to `outputs/` in the current workspace when none is specified. Its original
client-specific archive name and fixed local path have been removed; the installed
source copy was not modified. No business documents,
screenshots or generated diagrams are included in this repository.

Nacos preflight remains project-specific. It reads
`.qoder/rules/nacos-config-sync.md` from the target IoT-Admin-Cloud project root,
plus applicable project instructions and authorized environment evidence. Those
rules and live configuration are intentionally not copied here. Missing required
rules or target identity block the dependent checks; never guess them.

Engineering Workflow uses **CodeGraph** for routine source/relationship retrieval
and pre-edit impact, plus **Understand Anything** for on-demand architecture and
business navigation. Known-file edits do not require both tools. Freshness,
scoped fallback, cross-boundary evidence, and analysis permissions are defined in
[the retrieval rules](personal/engineering-workflow/references/skill-routing.md#understand-anything--codegraph-retrieval).
This is a workflow convention, not bundled tools or a guarantee of complete graphs.

Other skills defer to effective host/project policy. This collection does not
install CodeGraph, Understand Anything, OCR, Codex CLI, gstack, parsers or any
other tool. Missing selected skills follow the workflow's consent/substitution
protocol. Mandatory evidence and review gates remain mandatory; no automatic
agents, commits or publication.

## Keep One Maintained Source

Maintain
the skill instructions here and deploy approved updates to discovery locations.
Installed directories are runtime copies, not a second independent source.
If an installed copy was edited, compare and bring the intended changes back here
before deployment; do not blindly sync either direction. Verify the actual
installation and discovery state for each target rather than inferring it.

## Connect To GitHub Safely

This directory is already a clone of the intended repository. Before staging,
check the remote again if time has passed or someone else may have added content.
Reconcile new remote history and instructions rather than overwriting them.
Confirm repository visibility before publication; do not assume it is private.

Review the exact diff and private/project-specific material before committing.
Committing requires explicit applicable authorization; remote push remains a
manual user action under the current collaboration rules. Do not force-push or
upload local runtime histories. Consider a private repository until the
project-specific contents have been approved for public distribution.

## Validation

For updates, validate skill frontmatter and UI YAML, relative links, UTF-8 without
BOM, unfinished placeholders, exact file scope, and sensitive content. Exercise
relevant maintenance scenarios separately from structural checks. Follow the
effective formal-review toolchain, preserving authorization and evidence limits.

The official skill validator requires PyYAML; do not install it implicitly if
unavailable. An available YAML parser can validate structure but does not prove
skill selection, agent compliance, tool availability or live environment behavior.
