# Semantic Comparison Contract

Read when comparing configuration and preparing the preflight report. Apply the
repository's Nacos rule for any later authorized snapshot changes; this reference
defines analysis only and is not a publishing procedure.

## Identify Sources, Not Just Filenames

Match actual endpoint/namespace/group/Data ID/import relationships. Do not blindly
replace a dev filename suffix with test/prod or infer a namespace ID from a display
name. Record service/image version and read time so later changes can invalidate
results. Re-read affected inputs after an environment update; do not reuse a prior
missing-key verdict after the key may have been added.

Determine whether input is a complete Data ID, a partial example, a repository
default, a pasted excerpt, or a live read. A partial file proves only its shown
content, not what is absent elsewhere. Do not treat it as a complete replacement.

## Parse And Preserve Meaning

- Reject malformed YAML/JSON and flag duplicate keys/unsupported documents where
  the parser can detect them. Do not silently compare only the last duplicate.
- Keep scalar types, units, null/empty/absent distinctions, and placeholders.
  A seconds value and a milliseconds value require binding-level interpretation.
- Compare ordered route and filter lists in order. Do not sort every list or
  replace arrays with a lossy set/flattened-key representation.
- Establish actual import order/precedence and environment/argument overrides for
  affected properties. Framework list replacement/merging may differ from map
  merging; an object overlay is not proof of final Spring configuration.
- Relaxed binding can explain aliases only when the real consumer supports it.
  Do not normalize case/dashes universally, especially map keys or named clients.
- Preserve `${ENV_KEY:default}` semantics. A nonempty placeholder is not proof that
  its required environment variable exists or that a safe production value resolves.

If a parser/tool is missing, report the limitation and use only allowed equivalent
evidence. Do not turn a text search into a claimed successful semantic comparison.

## Action Classification

| Finding | Required interpretation |
| --- | --- |
| Key absent from one Data ID | Explicit-source difference; inspect shared imports/overrides/defaults before claiming effective absence |
| Required value absent across confirmed effective sources | Evidenced gap; name consumer, consequence, and release scope |
| Different environment endpoint or secret | Preserve isolation; validate suitability and same-environment caller/receiver agreement |
| Target-only setting | Determine purpose/consumer before recommending deletion |
| Different feature/security setting | Confirm intended behavior and prerequisites; do not copy reference environment blindly |
| Missing configuration for a service outside this release | Report relevance separately; do not call it a universal release blocker |
| Unknown runtime override/version/consumer | Mark unresolved and identify the evidence needed |

For cross-service auth, report only enabled/disabled, value present/absent,
match/mismatch, and whether comparison covered resolved values or only placeholder
expressions. Two matching fallback strings do not prove matching deployed secrets.
Do not print secrets or diagnostic hashes of them.

## Compact Result

Use a table with service/Data ID/key, classification, source/version/time,
consumer/effective-value evidence, release impact, suggested action, and unresolved
checks. Omit sensitive values; examples use obvious placeholders and state whether
they are partial fragments. Prefer reporting keys/actions over a replacement YAML.

Finish with separate statements for repository snapshots, observed runtime
configuration, effective behavior confidence, and publication/deployment status.
Only call configuration preflight clear when all required scoped configuration
checks have evidence and no unresolved blocker remains. Still list unperformed
startup, connectivity, business, and rollout checks; preflight clear is not an
assertion that those separate release gates passed.
