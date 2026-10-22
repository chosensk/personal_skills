---
name: nacos-release-preflight
description: "Perform read-only Nacos release preflight for IoT-Admin-Cloud: compare requested environments, repository snapshots, and effective configuration sources; classify missing keys, intentional differences, and cross-service blockers. Use before a release or when asked which Nacos settings need attention. Does not apply, publish, or deploy configuration."
---

# Nacos Release Preflight

Identify actionable configuration risks without treating every difference as a
missing setting. Read-only preflight is not configuration implementation or a
release approval. No fixed cluster address, namespace, credential, or historic
snapshot is embedded in this skill.

## Governing Contracts

From the target IoT-Admin-Cloud repository, read applicable
`AGENTS.md`/`project-guide.md` sections and its Nacos synchronization rule at
`.qoder/rules/nacos-config-sync.md`, resolved from that project's root, not this
skill's location or the personal_skills repository.
That rule owns snapshot mapping, authorized cross-environment synchronization,
placeholders, partial-file warnings, and manual publication. Do not duplicate or
relax it. Follow the selected environment directory's own instructions as well.

If a required rule or environment identity cannot be resolved, report the missing
prerequisite. A missing skill/tool follows the host's consent/substitution policy;
it does not authorize installation, configuration mutation, or gate bypass.

## 1. Define Scope And Confirm Identity

Identify the intended release/version, services, target environment, comparison
environment, and current user-authorized access. Inspect existing context/kubeconfig
metadata and approved connection instructions without printing credentials.
Verify the actual cluster/context, service namespace, active Spring Profile,
Nacos endpoint, namespace ID, group, and imported Data IDs where evidence permits.

An environment label such as test does not prove its Nacos namespace is test.
Verify config and discovery namespaces separately when relevant. If a production
call or new access requires approval, obtain it before connecting. Do not switch
contexts globally, create external bindings, or alter workloads to inspect them.

If the target cluster/endpoint cannot be confirmed within authorized scope, stop
live collection; use clearly labeled offline sources or request the missing
identity/access decision. Do not guess a namespace or probe unrelated endpoints
to turn an unresolved target into a runnable comparison.

Gate: identity and authorized scope are confirmed, or the report explicitly
states which identity facts are unresolved and limits its conclusions accordingly.

## 2. Collect Current Sources

Prefer fresh permitted runtime evidence for claims about the deployed environment.
Record source, retrieval time, service/image version, Data ID/group/namespace, and
snapshot completeness. A historical dump remains historical unless revalidated.
If runtime access is unavailable, compare supplied/exported or local sources only
and label the result offline; do not infer online missingness or consistency.

Read only the requested sources. Process sensitive configuration locally; report
secret presence/match status, not values, fragments, low-entropy hashes, tokens,
or private keys. Do not export full live configs to disk or send them to an
external reviewer without separate authorization. Use existing approved access;
temporary tunnels require permitted setup and cleanup of only owned resources.

Gate: each compared source has provenance, freshness, and a declared coverage limit.

## 3. Compare Semantically And Resolve Applicability

Read [comparison-contract.md](references/comparison-contract.md). Parse with an
available YAML/JSON parser and compare structure, not line order or a flattened
map that loses list/override semantics. Report parse problems before conclusions.
Inspect known shared/environment/service imports, runtime overrides, and binding
defaults for affected keys as available; do not assume one universal merge order.
Graph exploration requirements still apply when tracing code bindings/dependencies.

Separate key binding from value resolution. Preserve environment placeholders and
intentional addresses, credentials, pools, and feature choices. Missing explicit
keys/Data IDs are not necessarily missing effective values or startup blockers.
If priority/default behavior is unknown, keep it unresolved instead of asserting
enabled/disabled behavior from a single Nacos document.

Classify each material difference as: missing explicit configuration, effective
gap confirmed, intentional environment difference, behavior difference, target-only
setting, or unresolved. Separately rate urgency/blocking against this release.

Gate: proposed actions distinguish proven effective gaps from mere differences
and explain why each matters to the actual release scope.

## 4. Check Affected Chains

For scoped service calls, verify both ends: auth enablement, signature/secret
agreement without disclosure, timeout units/client identity, discovery/URL/port,
gateway routes and order, and feature activation prerequisites. Configuration
equality alone does not prove endpoint readiness or business success.

Respect independent product-line delivery and credentials. Do not solve a missing
push/auth setting by forwarding through a different product line or copying dev
secrets into test/prod. Consider only evidenced dependencies, not every service.

Gate: affected cross-service configuration gaps and unverified runtime checks are
explicit; no business-health claim is made solely from configuration comparison.

## 5. Report, Then Stop Before Mutation

Report identity/sources/freshness, blockers and evidence, suggested minimal actions,
intentional differences to preserve, unresolved decisions, and a safe validation
order. Use the compact result contract in the comparison reference.

Unless an actual business/release check was performed, say so. Always distinguish
local snapshot state, observed remote state, effective-value confidence, and
publication/rollout status. A clean config comparison is not release approval.

This skill does not edit snapshots, publish Nacos, rotate keys, restart pods,
deploy images, send test messages, or mutate Redis/database state. If the user
also requests changes, finish the preflight and hand its scoped action list to
the separately authorized implementation flow; publication remains manual under
the project rule. Do not generate a publishable full YAML from a partial diff.

For maintenance, use
[validation-scenarios.md](references/validation-scenarios.md), distinguishing manual
scenario review from a real environment or Agent execution test.
