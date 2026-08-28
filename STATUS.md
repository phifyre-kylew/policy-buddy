# Where I left off

**The only file you need to open when you come back.** Update it before you stop
for the day — thirty seconds then saves fifteen minutes of re-orientation later.

---

## Right now

**Current stage:** 0 — Requirements and business case
**Last worked:** 2026-__-__
**Next action:** _One sentence, specific enough that you could start without thinking._

> Good: "Run `pip install sentence-transformers chromadb python-docx`, then create
> src/ingest.py from the guide."
> Useless: "Continue Stage 3."

**Anything half-finished?**
_Unmerged branch, resource created but not configured, policy sitting in
simulation mode, document uploaded but not labelled._

**Anything I was confused about?**
_Write it down while it's fresh. Future-you will not remember the question, only
the vague feeling that something was unresolved._

---

## Billing — check every single time you sit down

| Thing | State | Started | Must stop by | Checked |
|---|---|---|---|---|
| APIM AI Gateway (Stage 6) | not created | | delete when stage ends | |
| Defender paid plans (Stage 10) | off | | day 28 | |
| Copilot Studio viral trial | assigned | | expires: ______ | |
| Azure spend this month | $ | | budget $10 | |

**Away more than 60 days?** Purview pauses processing for inactive tenants and
resumes when you reopen the solution. Open DSPM early in the session so it starts
catching up while you work on something else.

**If you are pausing mid-Stage-6 or mid-Stage-10, delete the resource first.**
Both rebuild in minutes. Neither is worth paying for while you are not looking at
it. Record the deletion here and pick the stage up cleanly later.

---

## Stage progress

- [ ] **0 — Requirements and business case** (writing only, $0)
  - [ ] Problem stated in one paragraph, no technology named
  - [ ] Business case read/adapted, metrics M1-M6 defined
  - [ ] Requirements written, incl. out-of-scope and constraints
  - [ ] Build/buy/extend analysis done
  - [ ] Stakeholder map, conflicts named
  - [ ] ADR-000 committed with a falsification condition
- [ ] **1 — Tenant preparation**
  - [ ] Audit logging enabled (verified with a search 24h later)
  - [ ] Barry Allan licensed, mailbox provisioned
  - [ ] Sam Doyle invited, shows as Guest
  - [ ] Copilot Studio trial expiry recorded above
  - [ ] Three libraries created
  - [ ] 18 documents uploaded
  - [ ] ADR-001 committed
- [ ] **2 — GitHub, VS Code, Copilot**
  - [ ] Repo public, branch protection on `main`
  - [ ] Keyword search working
  - [ ] At least one merged PR
  - [ ] GitHub Action green
  - [ ] MCP server running, tools visible in Agent mode
  - [ ] ADR-002 committed
- [ ] **3 — Hugging Face local RAG**
  - [ ] Libraries installed
  - [ ] Corpus downloaded into `corpus/`
  - [ ] `ingest.py` run, vectordb built
  - [ ] `retrieve.py` returning sensible results
  - [ ] Ten-question comparison written
  - [ ] ADR-003 committed
- [ ] **4 — Foundry and the agent**
  - [ ] Budget alert set BEFORE creating anything
  - [ ] Serverless deployment (NOT provisioned)
  - [ ] App registered in Entra, client and tenant IDs saved
  - [ ] Scoped to `Policies` library only
  - [ ] Key Vault holding secrets, none in repo
  - [ ] Agent calling tools
  - [ ] Tools exposed as MCP server
  - [ ] IaC that builds and destroys
  - [ ] Vendor assessment written
  - [ ] ADR-004 committed
- [ ] **5 — Securing the agent**
  - [ ] Baseline run of all 20 cases, recorded honestly
  - [ ] Four mitigations applied one at a time
  - [ ] MCP-01 to MCP-05 run
  - [ ] Third-party MCP server assessed
  - [ ] Injection suite in CI
  - [ ] Risk register populated with named owners
  - [ ] ADR-005 committed
- [ ] **6 — AI gateway** ⚠️ bills while it exists
  - [ ] Gateway created — DATE: ______
  - [ ] Model published, credentials out of app
  - [ ] MCP server published behind gateway
  - [ ] Four policy types applied and tested
  - [ ] Telemetry to App Insights
  - [ ] Resources tagged (project/stage/owner/environment)
  - [ ] Cost-per-interaction calculated in finops-model.md
  - [ ] Naive forecast written, with its flaws explained
  - [ ] **Resource DELETED, $0 confirmed**
  - [ ] ADR-006 committed
- [ ] **7 — Purview DLP**
  - [ ] Content Explorer reviewed, accuracy noted
  - [ ] Three labels published
  - [ ] Auto-labelling run in simulation first
  - [ ] Three DLP policies enforced
  - [ ] Bypasses documented
  - [ ] Sam's permissions corrected
  - [ ] ADR-007 committed
- [ ] **8 — Purview DSPM**
  - [ ] Risk assessments run
  - [ ] Two collection policies (custom app + Copilot)
  - [ ] Traffic generated across all three AI systems
  - [ ] Screenshots in `evidence/`
  - [ ] One finding closed end to end
  - [ ] System card written
  - [ ] ADR-008 committed
- [ ] **9 — Copilot Studio** ⚠️ trial clock
  - [ ] Trial status confirmed
  - [ ] Agent built, build time recorded
  - [ ] Injection suite re-run
  - [ ] Connection permissions compared
  - [ ] Same MCP server connected
  - [ ] Build comparison written
  - [ ] ADR-009 committed
- [ ] **10 — Defender for Cloud** ⚠️ bills after day 30
  - [ ] Foundational CSPM confirmed on and free
  - [ ] Free recommendations addressed
  - [ ] IaC scanning connected
  - [ ] Paid trial started — DATE: ______
  - [ ] **Paid plans DISABLED by day 28**
  - [ ] Final assessment written
  - [ ] ADR-010 committed

---

## Open questions

_Things you hit and moved past. Revisit when you have energy._

| Date | Question | Resolved? |
|---|---|---|
| | | |
