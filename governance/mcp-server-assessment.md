# Third-party MCP server assessment

Complete at Stage 5.5 against a real published server. Do not install it —
assess it.

Installing an MCP server is not like installing a library. A library runs code
you invoked deliberately; an MCP server hands an autonomous system the ability to
act on your behalf, guided by text descriptions you probably skimmed. The trust
decision is larger and the review is usually smaller.

**Server assessed:**
**Publisher:**
**Version / pinned:**

## Identity and authorization
- [ ] Accepts only tokens scoped to its own endpoint
- [ ] Actions run under the calling user's permissions
- [ ] A low-privilege user cannot reach data they couldn't reach directly
- [ ] No token passthrough to downstream services
- [ ] Conditional access or equivalent can be applied

## Scope and least privilege
- [ ] Every exposed tool is needed
- [ ] Read and write capabilities are separable
- [ ] Blast radius on full compromise is understood and acceptable
- [ ] Access can be revoked quickly, and revocation takes effect

## Tool descriptions as untrusted input
- [ ] Every tool description read in full
- [ ] No imperative language aimed at the model
- [ ] Descriptions cannot change post-install without notice
- [ ] Version pinned rather than auto-updating

## Provenance and supply chain
- [ ] Publisher identified, source public and readable
- [ ] Recently maintained; maintainer responsive to security reports
- [ ] Dependencies reviewed
- [ ] Signed or otherwise verifiable
- [ ] Security contact and disclosure policy exist

## Data handling
- [ ] Data it sees, and where that data goes, is documented
- [ ] Server-side retention and logging understood
- [ ] External calls and their jurisdictions known
- [ ] Transport encrypted and authenticated

## Observability
- [ ] All tool invocations logged with calling identity
- [ ] An incident could be reconstructed from the logs
- [ ] Logs reach a place someone actually looks

## Decision
> **Verdict:** Approve / Approve with conditions / Reject
>
> **Conditions required:**
>
> **Residual risk after conditions:**
>
> **Accepted by:**            **Review date:**

## Would you approve this for organisational use, and what would you require first?
