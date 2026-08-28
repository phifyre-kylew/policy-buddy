# Running cost log

Target: buy nothing. Every licence this project needs is already in the tenant.

## Licences

| Date added | Seat | Plan | Commitment | $/month | Date removed |
|---|---|---|---|---|---|
| (existing) | kylew@phifyre.io (admin) | E5 + Copilot Business | — | already owned | — |
| | Barry Allan | Business Standard (idle seat) | already owned | $0 | — |
| | Sam Doyle | guest — no licence | — | $0 | — |
| (existing) | Copilot Studio Viral Trial | trial | **expires: ______** | $0 | — |

**Rule: monthly commitment only, never annual.** Annual locks in twelve months
for a project measured in weeks.

## Azure and services

| Date | Stage | Service | Cost | Note |
|---|---|---|---|---|
| | 4 | Azure AI Foundry | $ | Serverless tokens only — never provisioned |
| | 4 | Key Vault | $ | Per-operation, negligible |
| | 6 | APIM AI Gateway | $ | **PREVIEW, pricing unannounced. Created ____ , DELETE BY ____** |
| | 6 | Application Insights | $ | Telemetry ingestion — also your FinOps Inform-phase data source, see `governance/finops-model.md` |
| | 10 | Defender for Cloud | $0.00 | Paid trial started ____ , **DISABLE BY ____ (day 28)** |

**Running total: $**

## Free tier boundaries I'm relying on
- GitHub Actions: unlimited on public repos
- GitHub Copilot: free tier monthly caps
- Hugging Face: local inference, no cost
- Purview DSPM and DLP: covered by E5 — but **per user**
- Defender for Cloud Foundational CSPM: free indefinitely
- Copilot Studio: viral trial already assigned
- M365 E5 trial: 25 seats / 30 days, held in reserve

## Deletion reminders set
- [ ] APIM gateway resource — Stage 6
- [ ] Defender paid plans — Stage 10, day 28
- [ ] Foundry deployment when project ends

## Near misses
_Log every time you nearly clicked something expensive. This section teaches
you more than the table does._
