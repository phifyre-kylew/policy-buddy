# ADR-000: Build Policy Buddy as a scoped, read-only pilot

**Date:** 2026-__-__
**Stage:** 0
**Status:** Accepted

## 1. What I'm about to do
Build a read-only AI assistant that answers employee questions about published
HR and workplace policy, grounded in a single SharePoint library, as a
time-boxed pilot on Azure AI Foundry.

## 2. Why
People Operations spends significant capacity answering questions already
answered in published documents, employees wait for answers that exist, and
different staff sometimes answer edge cases differently.

Alternatives considered (full analysis in `governance/build-buy-extend.md`):
- **Do nothing:** rejected. Not neutral — employees already use unapproved
  consumer AI for these questions, so this preserves an unmanaged egress path.
- **Better intranet search:** *not rejected on merit.* Probably solves ~60% of
  the problem more cheaply with no fabrication risk. Deferred, with a
  pre-committed condition to revisit (see section 4).
- **M365 Copilot as-is:** rejected for this use case only. It answers from what
  the signed-in user can reach, so answers vary by asker and cannot be scoped
  to the authoritative corpus. Inconsistency is the original problem restated.
- **Buy a vendor assistant:** rejected on cost at pilot scale. Note the hidden
  cost that usually decides these — third-party assessment effort can exceed
  build effort at small scale.
- **Copilot Studio:** deferred, evaluated head-to-head in Stage 9.

## 3. Zero Trust principle served
Least privilege, established at the requirements stage rather than retrofitted.
Requirement S1 (agent reads one library, nothing else) is a design constraint
that predates any code, which is what makes it a wall rather than a mitigation.

## 4. What I expect to go wrong
I expect the model to produce fluent answers unsupported by retrieved text, and
I expect that to be harder to detect than outright errors because it will look
right. I expect adoption, not accuracy, to be the real constraint. I expect to
be tempted to widen the agent's data access the first time it cannot answer a
reasonable question.

**Pre-committed falsification condition:** if M1 (repetitive tickets) improves
by less than 20% at pilot exit, the intranet-search hypothesis was probably
right and should be re-tested before scaling. Recording this *now*, before the
result is known, is what makes it honest rather than rationalisation.

## 5. What actually happened
[Fill in at pilot exit, against M1–M6.]

## Governance note
AIGP Domains I and II — the parts a build-only project otherwise skips
entirely. Problem definition, option analysis, and the risk-classification
boundary in `requirements.md` (this system is low-risk *because of how it is
used*, not because of how it is built) are Domain II reasoning applied to a
concrete system.

NIST AI RMF: **Govern** and **Map**. This ADR and its supporting documents are
the Govern function producing the context that Map depends on. Everything from
Stage 1 onward assumes this work was done; doing it explicitly is what makes
the assumption true.
