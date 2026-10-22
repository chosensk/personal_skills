# History Selection And Reporting

## Pin Scope

Use the user's repository/ref and author if given. Otherwise use the current
repository/HEAD and resolve the author from available identity evidence; Git
configuration alone is not proof that all matching historical identities belong
to the user. Ask when same-name identities or unclear aliases affect attribution.
Respect `.mailmap`, distinguish author from committer, and record aliases used.
Match selected identities literally after reading metadata; do not interpolate a
user's name as an unescaped Git regex or shell command. Quote filesystem paths.

Use the client's timezone (state its name/offset), not an assumed server zone.
For "last week", select the previous complete Monday-to-Monday calendar week.
For "last two weeks", default to the trailing 14 days ending now unless context
means two calendar weeks; show the exact boundaries and chosen interpretation.
Use half-open intervals [start, end), including start and excluding end.
Default to committer timestamp for a Git-activity report, explicitly distinguishing
this from when code was authored. Honor an explicit author-time request.

## Collect Reliably

Read repository/ref/shallow status and available commit metadata using local
read-only Git. Resolve ref to a commit ID so later ref movement is detectable.
Select commits reachable from that ref and filter numeric `%ct` or `%at` timestamps
against the chosen interval. Ordinary Git date flags use committer dates and may
prune traversal; do not rely on them to implement author-date or exact half-open
selection. Read enough history to support the chosen basis; if volume prevents
that, disclose incomplete coverage rather than silently truncating it.

Useful metadata fields include commit ID, parents, raw and mailmap-resolved author
name/email, and author/committer timestamps. Use unambiguous record separators and
literal identity comparisons. Inspect selected changes and relevant merge parents
as needed; do not copy secrets or sensitive paths into the report.

Avoid `--all` unless explicitly requested. Report shallow boundaries, unavailable
objects, offline/local-only remote refs, and any capped extraction. Do not fetch
or change repository state merely to remove these limitations.

## Interpret Outcomes

- Group by feature/product/module outcome; separate implementation from verified
  testing or deployment. Use actual evidence for every completion claim.
- Avoid counting a merge and its already-included changes as separate outcomes;
  inspect merge-only conflict resolutions when relevant. Do not exclude every
  merge by default if it carries meaningful author-attributed work.
- Identify likely cherry-pick duplicates from content/metadata when material.
  Commit counts alone are not productivity or unique-outcome counts.
- Account for reverts: distinguish activity during the interval from net state
  at its end. A reverted feature is not delivered merely because it was committed.
- Do not attribute another author's changes to a person solely because they
  merged or committed them. State whether the requested report is authorship or
  integration activity if that distinction matters.

## Output Shape

Lead with the requested report, usually 3-6 short Simplified Chinese bullets.
Prioritize delivered capability, meaningful fixes, and governance improvements.
Keep evidence identifiers compact; offer detail only when it adds decision value.
End with scope and genuine limitations. Label inferred intent and unverified
tests/deployment instead of presenting them as facts. An empty result should
explain the selection and possible coverage gaps, without inventing work.
