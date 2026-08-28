---
document: Requirements analysis
system: Policy Buddy
status: Baselined for pilot
date: 2026-__-__
---

# Requirements — Policy Buddy

> Worked example. Written before Stage 1. The **out of scope** and
> **constraints** sections are the ones that do real work; requirements
> documents that only list features are the reason scope creep happens.

## Functional requirements

| ID | Requirement | Priority | Verified by |
|---|---|---|---|
| F1 | Answer natural-language questions about published HR and workplace policy | Must | Stage 3 comparison, M2 test set |
| F2 | Cite the source document for every claim in an answer | Must | Manual review; INJ tests |
| F3 | State plainly when the corpus does not cover a question | Must | M6 escalation rate |
| F4 | Escalate unanswerable questions to a human, with the original wording | Must | `escalations.jsonl` |
| F5 | Log every interaction for audit | Must | `agent-audit.jsonl`, Stage 8 |
| F6 | Retrieve semantically, not by keyword | Should | Stage 3 evaluation |
| F7 | Serve multiple concurrent users | Could | Not tested in pilot |

## Non-functional requirements

| ID | Requirement | Target | Verified by |
|---|---|---|---|
| N1 | Answer latency | < 5s typical | Gateway telemetry |
| N2 | Cost per interaction | < $0.02 | `finops-model.md` |
| N3 | Availability | Best effort; no SLA in pilot | — |
| N4 | All interactions attributable to an identity | 100% | Entra + audit log |
| N5 | No provider credentials in application code | Absolute | Stage 4.4, Stage 6.3 |
| N6 | Resistant to prompt injection | See S1–S4 | Stage 5 suite |

## Security requirements

These are stated as requirements rather than left to emerge during
implementation, which is the entire difference between security-by-design and
security-by-retrofit.

| ID | Requirement | Rationale |
|---|---|---|
| S1 | The agent must be able to read `Policies` and nothing else | Least privilege; bounds blast radius on compromise |
| S2 | The agent must never surface content from `HR-Confidential` or `Finance` | Canary controls, INJ-05/06 |
| S3 | Text inside retrieved documents must be treated as data, not instruction | Indirect injection defence |
| S4 | Instruction files (system prompt, skills, AGENTS.md) require PR review | Instruction-file poisoning, R-09 |
| S5 | Every tool invocation must be logged with the calling identity | Incident reconstruction |

**S1 is the load-bearing one.** S3 and the system prompt are mitigations that
degrade gracefully; S1 is a wall. If S1 holds, most of S2 follows for free.
Ranking your controls by which one you would keep if you could only keep one is
a useful exercise, and the answer is rarely the one people spend most time on.

## Explicitly out of scope

The most important section in this document.

| Not doing | Why |
|---|---|
| Answering questions about an individual's own record | Requires personal data access; changes the risk profile entirely |
| Any write action (updating records, sending mail, booking leave) | Read-only bounds the damage from compromise (Stage 4) |
| Determining or recommending employment, disciplinary, or compensation outcomes | Would make this a high-risk system under the EU AI Act; see below |
| Legal advice or interpretation beyond quoting policy | Liability; also outside the corpus |
| Non-English content | Corpus is English-only |
| Replacing the HR service desk | The agent escalates *to* humans; it does not replace them |

**The third row is the one to understand properly.** The technology would not
change at all if this system screened candidates or recommended disciplinary
outcomes — same retrieval, same model, same code. But under the EU AI Act it
would become a high-risk employment system with a completely different
obligation set: conformity assessment, human oversight requirements,
registration, logging duties.

**Risk classification follows use, not architecture.** That is the single most
transferable idea in this document, and writing the boundary down here is what
stops a future feature request from crossing it without anyone noticing.

## Constraints

| Constraint | Impact on design |
|---|---|
| One E5 seat, one Business Standard seat, one guest | Limits multi-user policy testing; shapes Stage 1.2 personas |
| Minimise cost | Serverless only; no provisioned capacity; delete preview resources |
| Single operator, part-time, stop-start | Everything must be resumable; drives `STATUS.md` |
| Tenant has live on-prem AD sync | Synced accounts unusable as test subjects |
| APIM AI Gateway pricing unannounced | Time-box and delete; cannot be a permanent dependency |

## Assumptions, and what happens if they are wrong

Stating these separately from requirements is deliberate. An assumption that
fails is a *replan trigger*, not a bug.

| Assumption | If false |
|---|---|
| The corpus is authoritative and current | Answers are confidently wrong; corpus governance becomes prerequisite work |
| ~60% of questions are findability, not comprehension | Business case section 7 wins; build search instead |
| Employees will trust an AI answer about policy | Adoption fails regardless of technical quality |
| Retrieval scoping is sufficient to protect restricted libraries | S1 fails; the whole security model needs rework |

The third one is the least technical and the most likely to sink the project.
Solution architects consistently under-weight adoption relative to
architecture, because architecture is the part they control.
