# Maintenance Scenarios

Evaluate with supplied metadata or authorized read-only repositories. No fixture
commits, remote calls, or production actions are needed. Record observed decisions
and evidence separately from these expected outcomes.

| Request / evidence | Expected decision |
| --- | --- |
| Last week; client date 2026-10-22 in Asia/Shanghai | Select [2026-10-12T00:00:00+08:00, 2026-10-19T00:00:00+08:00); state date basis |
| Recent two weeks; no calendar-week context | Use trailing 14 days ending at the captured current time; display exact boundaries |
| Author name contains `.` or `[`; two distinct emails share that name | Use literal matching; resolve attribution rather than broad regex matching |
| Commit authored before the interval but committed inside it | Include on committer-time basis; exclude on author-time basis; do not equate integration with authorship |
| Same change appears as commit, merge, and cherry-pick; feature later reverted | Consolidate outcome; report revert/net state without inflating delivery |
| Shallow repository and no matching author commits | Disclose limited evidence; do not claim no work or fetch automatically |
| Only code commits, no test/deployment evidence | Report implemented changes, not passing tests or successful rollout |
| User asks only for a short report | Answer in chat; no document creation, publication, scheduling, or Git writes |
