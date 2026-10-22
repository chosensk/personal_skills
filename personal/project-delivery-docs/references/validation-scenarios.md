# Behavioral Acceptance Scenarios

Use during maintenance. Exercise with authorized isolated fixtures; no automatic
external publication, Agent delegation, dependency installation, or real project
mutation. A manual instruction walkthrough is not an independent execution test.

| Input situation | Expected behavior |
| --- | --- |
| User supplies a destination with existing topic/index rules | Inspect and reuse those rules before choosing files |
| A previous conversation used a different absolute directory | Use the current authorized destination, not the historical path |
| Only a progress update is requested | Update relevant existing progress views, not a full new documentation bundle |
| Markdown and HTML coexist with different current-phase claims | Synchronize affected facts and indexes; preserve existing layout/history |
| Implementation differs from approved acceptance | Record the discrepancy/open requirement; do not silently approve or rewrite it away |
| Interface annotations omit gateway/auth/serialization behavior | Inspect actual contracts and record unresolved fields; do not invent them |
| Local tests pass but no environment was read | Report verified local behavior, not deployed/published success |
| Snapshot was updated but Nacos was not published | State repository-only change and pending runtime/publication status |
| No test results exist for a claimed completed behavior | Label the behavior implemented/unverified as supported, not tested |
| User asks for a proposal without implementation | Produce only authorized proposal documents with proposed/pending status |
| Existing document includes unrelated edits or historical release dates | Preserve them; scope changes and update dates according to their meaning |
| A cross-directory link or HTML view cannot be checked | Fix within scope or disclose the validation gap; do not claim complete validation |
| User asks only how to organize documents | Answer without creating destination files or task records |
| Documentation is complete but no upload/commit was requested | Hand off local documents without publication, Git writes, or archive |

Record actual tools/results and limits in the current task evidence. These cases
do not by themselves establish host discovery, visual rendering, or runtime API
correctness. Do not store live credentials or copied conversation transcripts.
