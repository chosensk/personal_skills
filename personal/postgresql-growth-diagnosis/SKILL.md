---
name: postgresql-growth-diagnosis
description: Diagnose PostgreSQL table or disk growth with cost-aware read-only evidence, including retention behavior, heap, indexes and TOAST. Use when investigating growing tables, cleanup effectiveness or space reclamation; does not perform maintenance or data changes.
---

# PostgreSQL Growth Diagnosis

Explain what is growing, why, and what the evidence can establish. Follow the
project's database and access rules; this skill grants no connection or mutation
permission. Confirm the requested environment, database, schema, table and time
range before querying. Do not print credentials, payloads or personal data.

1. Establish the metric and observation period: row count, logical payload,
   relation size or host disk. Identify writers, sync frequency, retention rules,
   protected records, batch limits and actual scheduling from current source and
   authorized runtime evidence. A configured job is not proof it ran.
2. Check PostgreSQL version, access, table scale and query cost first. Start with
   catalog/statistics and bounded aggregates; estimates and cumulative statistics
   are not exact counts or growth rates. Avoid unbounded scans of large tables;
   inspect the plan or use existing metrics, sampling and timeouts when appropriate.
   If evidence is insufficient, say so rather than running a costly query by default.
3. Separate main heap, indexes, TOAST and auxiliary storage using version-appropriate
   official PostgreSQL documentation. Do not add overlapping size functions or
   label an estimated count as exact. Compare timestamps and multiple observations
   before asserting a rate; an old snapshot alone cannot prove current growth.
4. Relate eligible data and job execution evidence to retention semantics: deletion,
   payload clearing and metadata retention affect row counts differently. Check
   live/dead tuple estimates and vacuum/analyze timestamps as clues, not exact bloat
   measurements. Ordinary vacuum makes space reusable and may truncate tail pages;
   do not promise immediate shrinkage or claim it never returns space to the OS.
5. Report observed facts, likely causes, alternatives, missing evidence and the
   scope/time of each observation. Describe candidate retention or reclamation
   approaches with locking, disk and operational tradeoffs for a DBA to assess.
   DELETE, UPDATE, DDL, VACUUM, VACUUM FULL, repack, job/config changes and
   scheduling require separate applicable authorization; do not execute them as
   part of diagnosis. Do not infer production state from another environment.

When validating this skill, use [scenarios.md](references/scenarios.md); expected
decisions are not evidence of a database query or actual operational validation.
