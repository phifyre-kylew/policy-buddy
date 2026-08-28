# Risk register

Residual risk is almost never "none". If you write "none", think harder.
Every row needs a named human who accepts what remains.

| ID | Risk | Likelihood | Impact | Mitigation | Residual | Accepted by | Review |
|---|---|---|---|---|---|---|---|
| R-01 | Agent retrieves and discloses confidential HR data | Low | High | Managed identity scoped to Policies library only; DLP policy; output filter | Low | | Quarterly |
| R-02 | Indirect prompt injection via poisoned document | Medium | High | Content filters; output filtering; restricted write access to corpus | Medium | | Monthly |
| R-03 | Model fabricates policy detail not present in retrieved text | High | Medium | Citations required in output; disclaimer; human escalation path | Medium | | Monthly |
| R-04 | Sensitive data appears in user prompts | Medium | Medium | DSPM collection policies; user guidance; DLP | Low | | Quarterly |
| R-05 | Over-permissioned identity through low-code connection | Medium | High | Connection review; avoid maker-context connections | Medium | | Per change |
| R-06 | Unexpected cloud spend | Medium | Low | Budget alerts; serverless only; deletion reminders | Low | | Monthly |
| R-07 | Tool poisoning via malicious MCP tool description | Medium | High | Pinned server versions; description review; no unvetted servers | Medium | | Per change |
| R-08 | Confused deputy — agent acts with higher privilege than caller | Low | High | Actions run under calling user's RBAC; scoped Entra tokens | Low | | Quarterly |
| R-09 | Instruction-file poisoning — unreviewed edit to system prompt, a SKILL.md, or AGENTS.md changes agent behaviour | Medium | High | PR review required on all four file types; MCP-06 in CI; retrieval scoping holds regardless of instruction text | Low | | Per change |
| R-10 | Copilot surfaces oversharing in HR-Confidential to licensed users | | | | | | |
| R-11 | Synthetic sensitive data persists in audit/eDiscovery indefinitely | | | | | | |

Add rows as you find them. You will find them, especially in Stages 5 and 7.
