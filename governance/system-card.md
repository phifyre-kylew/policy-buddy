# System card — Policy Buddy

Written at Stage 8. This is the document you would hand to a regulator, a
customer, or an internal review board.

## Purpose
[What the system does, who uses it, what decision it supports.]

## Out of scope
[What it must not be used for. Be specific — this section is what stops
scope creep turning a low-risk system into a high-risk one.]

## Data sources
| Source | Contents | Access scope | Provenance |
|---|---|---|---|
| SharePoint `Policies` | Employee handbook content | Read only, one library | Authored internally, synthetic |

## Model
| | |
|---|---|
| Provider | |
| Model | |
| Deployment type | |
| Region | |
| Retention | |
| Used for training? | |

## Known limitations
- Retrieval sometimes returns irrelevant chunks. This does not go away.
- The model can produce fluent text unsupported by retrieved content.
- Prompt injection is mitigated, not solved.

## Risks identified
[Cross-reference risk-register.md]

## Controls applied
| Control | Layer | Stage |
|---|---|---|
| Retrieval scoped to one library | Identity / data | 4 |
| Managed identity, no stored keys | Identity | 4 |
| Content filtering | Application | 5 |
| Output pattern filtering | Application | 5 |
| Gateway rate limits and content safety | Gateway | 6 |
| DLP policies | Data | 7 |
| DSPM monitoring | Visibility | 8 |

## Monitoring
[What is watched, by whom, how often, and what triggers a response.]

## Human oversight
[Who can overturn the system's output, and how.]

## Owner
[A named person. Not a team.]

## Review date
