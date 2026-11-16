# Targeted Runtime Diagnosis

Use current project source, configuration and authorized runtime evidence. These
are diagnostic questions, not assumptions about every framework or deployment.

## Overlays and responsive layout

When a modal or drawer ignores width or looks cramped, identify the actual overlay
component, rendered DOM and mount location, class forwarding, default and computed
styles, CSS scope and cascade. Teleported content may not match a scoped selector;
verify the actual DOM and project component API before choosing a fix. Check the
target desktop and narrow viewports, overflow and interaction in a real browser
when available. Lint and type checks cannot establish visual behavior; report
when browser verification was not performed. Avoid globally styling unrelated
overlays or treating one project's default width as universal.

## BPM visibility and status

When a process is missing or appears both approved and in progress, distinguish
published definition, visibility, start permission, business entry point, process
instance and individual task. Trace the actual page, request, filters, model version
and current user's tenant/permissions. Compare task completion and instance state
using current API and implementation; automatic start-node behavior is project
specific. Do not modify or republish a model during diagnosis without authorization.

## Configuration and service addresses

Identify environment, service version, configuration imports and precedence, then
compare the owning source, repository examples and authorized runtime values.
Distinguish a configuration-center URL override from service-discovery instance
addresses; a reachable mapped port does not establish an application-level call.
Report missing access and redact secrets. A local snapshot is not evidence of a
published configuration, and a config change is not evidence the running service
has loaded it. Follow the target project's rules for any later changes.
