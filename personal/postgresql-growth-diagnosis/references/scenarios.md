# Maintenance Scenarios

| Evidence or request | Expected decision |
| --- | --- |
| Row count rises while old response bodies are cleared | Separate retained metadata from payload retention; do not infer cleanup failed solely from row count |
| A scheduled job exists in source | Seek authorized execution evidence and eligibility; leave runtime status unknown without it |
| Relation size stays high after deletion | Explain reusable space and assess heap, indexes, TOAST and vacuum evidence; do not assert exact bloat from dead tuple estimates |
| One estimated count and a single size snapshot | Do not claim an exact count or growth rate; request or obtain a comparable second observation |
| Exact count on a very large live table | Assess cost and privileges first; prefer existing estimates or bounded evidence and disclose uncertainty |
| User requests diagnosis only | No cleanup, maintenance, DDL, job changes or configuration writes |
| Ordinary vacuum is observed | Do not promise immediate disk shrinkage; tail truncation may return some space depending on conditions |
