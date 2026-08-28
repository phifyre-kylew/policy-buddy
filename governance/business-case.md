---
document: Business case
system: Policy Buddy
status: Approved for pilot
author: [You]
date: 2026-__-__
review: At pilot exit, or on any material change to scope
---

# Business case — Policy Buddy

> **How to read this.** This is a *worked example*, not a template to fill in.
> It is written as though a real architect wrote it before building anything.
> Read it critically: at least three of the numbers below are estimates
> presented with more confidence than they deserve, and the document says so
> where that is true. Learning to spot that in your own writing is the point.

## 1. The problem, stated without reference to any solution

People Operations at Contoso receives a high volume of repetitive questions
that are already answered in published policy documents: leave entitlement,
expense thresholds, remote-work rules, equipment provisioning.

Three costs follow from this:

- **People Operations time.** Answering the same questions repeatedly is the
  single largest consumer of the HR service desk's capacity.
- **Employee delay.** Employees wait for an answer that already exists in a
  document they could not find or did not know existed.
- **Inconsistency.** Different HR staff sometimes give different answers,
  particularly on edge cases, because they interpret the policy rather than
  quoting it.

**Note the framing.** This section deliberately does not mention AI, agents, or
Copilot. If the problem cannot be stated without naming the technology, the
project is a solution looking for a problem — which is the most common failure
mode in enterprise AI, and the reason this document exists before Stage 1.

## 2. Why now

- The policy corpus was consolidated into a single SharePoint structure this
  year, so for the first time there is one authoritative source to point at.
- Employees are already using unapproved consumer AI tools for work questions
  (see risk R-12, shadow AI). Doing nothing is not a neutral option; it is a
  choice to let that continue unmanaged.
- Microsoft 365 Copilot licences already exist in the tenant, so some
  capability is available without new spend.

## 3. Options considered

Summarised here; the full analysis is in `build-buy-extend.md`.

| Option | Verdict |
|---|---|
| Do nothing | Rejected — shadow AI use continues unmanaged |
| Improve search / intranet IA | **Not rejected outright.** See section 7 |
| Use M365 Copilot as-is | Rejected for this use case — see `build-buy-extend.md` |
| Buy a vendor HR assistant | Rejected — cost and data-residency review burden |
| Build on Azure AI Foundry | **Selected** for the pilot |
| Build in Copilot Studio | Deferred — evaluated as a comparison in Stage 9 |

## 4. Success metrics

Defined *before* building, so the evaluation cannot be retrofitted to whatever
the system turns out to be good at.

| # | Metric | Baseline | Target | How measured |
|---|---|---|---|---|
| M1 | Repetitive questions reaching HR service desk | ~120/month (estimate) | −40% | Service desk ticket categories |
| M2 | Answer accuracy on a fixed 30-question test set | n/a | ≥90% correct, 0 fabricated | Manual review each release |
| M3 | Fabrication rate (answers not supported by retrieved text) | n/a | 0 tolerated in test set | `evaluation/` records |
| M4 | Sensitive data disclosure incidents | 0 | 0 | DSPM + DLP alerts |
| M5 | Cost per interaction | n/a | < $0.02 | `finops-model.md` |
| M6 | Escalation rate (agent hands off to human) | n/a | 5–20% | `evidence/escalations.jsonl` |

**M6 has no "good" direction, deliberately.** Too low means the agent is
guessing at things it should hand off; too high means it is not useful. A
metric where both extremes are bad forces a judgement call rather than
letting anyone optimise a number. Most metric sets lack one of these and are
worse for it.

**M1's baseline is the weakest number here.** It is an estimate, not a
measurement, because ticket categories do not currently separate "policy
lookup" from other HR queries. Fixing that measurement *is itself work* that
should happen before the pilot ends, or M1 cannot honestly be reported. Flagged
rather than quietly relied on.

## 5. Costs

| Item | Estimate | Confidence |
|---|---|---|
| Azure AI Foundry (serverless tokens) | $5–15/month at pilot scale | Medium |
| Key Vault, App Insights | < $5/month | High |
| API Management AI Gateway | **Unknown** — preview, pricing unannounced | None |
| Licences | $0 — existing E5 and Copilot seats | High |
| Build effort | ~80 hours | Low |

The gateway line is genuinely unknown and is shown that way rather than
guessed. A cost table with no "unknown" rows in it is usually hiding one.

## 6. Benefits, and the honest limits of claiming them

The efficiency case is real but modest and hard to attribute: time saved by
People Operations does not automatically become value unless that capacity is
redeployed. This document does **not** claim a dollar ROI, because the honest
answer is that it cannot be calculated reliably at this scale.

The stronger benefits are ones that resist quantification:

- **Consistency** — every answer traces to a cited source document.
- **Governance visibility** — an approved, monitored path reduces unmanaged
  shadow AI use.
- **Organisational capability** — the controls, patterns, and assessments built
  here are reusable for the AI systems that follow.

Stating that ROI cannot be reliably calculated is more defensible than
producing a confident number from soft assumptions. Architects who fabricate
precision here lose credibility the first time someone checks.

## 7. The strongest argument against this project

**A better intranet search might solve most of the problem for less money and
less risk.** Roughly 60% of the repetitive questions are probably "I could not
find the document," not "I read it and did not understand it." AI is a
comparatively expensive fix for a findability problem, and it introduces
fabrication risk that a search box does not have.

This section exists because a business case with no counter-argument is
advocacy, not analysis. Reviewers should be more suspicious of a document that
argues only one way.

**Why the pilot proceeds anyway:** the shadow-AI exposure is already present
and unmanaged, the licences are already paid for, and the capability built here
transfers to future systems. If M1 improves by less than 20%, the search
hypothesis should be re-tested before scaling.

That last sentence is the important one — it is a **pre-committed falsification
condition**. Written before the result is known, it is honest. Written
afterwards, it would be rationalisation.

## 8. Recommendation

Proceed with a time-boxed pilot on the terms above. Re-evaluate at pilot exit
against M1–M6. Do not scale to additional domains (IT, Finance) until the HR
pilot has cleared M2, M3, and M4.
