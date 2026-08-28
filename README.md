# Policy Buddy

A staged learning project: build an AI agent, then govern it.

An HR policy Q&A agent built twice — once pro-code (Python, Azure AI Foundry, MCP)
and once low-code (Copilot Studio) — with Microsoft Purview, Defender for Cloud,
and an Azure API Management AI gateway wrapped around both.

Everything in this repository is synthetic. Contoso Ltd is fictional. All names,
identifiers, card numbers, and account details are invented.

## Layout

| Folder | Contents |
|---|---|
| `src/` | The pro-code agent |
| `mcp-server/` | Tools exposed over Model Context Protocol |
| `tests/injection/` | Prompt injection and MCP attack suite |
| `evaluation/` | Honest records of what worked and what didn't |
| `governance/` | Business case, requirements, assessments, risk register, system card, FinOps model |
| `decisions/` | One ADR per stage, written before building |
| `evidence/` | Dashboard screenshots as audit evidence |
| `infra/` | Bicep / Terraform so the environment can be destroyed and rebuilt |

## Running

```
pip install -r requirements.txt
python src/ingest.py      # chunk and embed the corpus
python src/retrieve.py    # semantic search
python src/agent.py       # the agent
```

## Status

- [ ] Stage 0 — Requirements, business case, decision to build
- [ ] Stage 1 — Tenant preparation
- [ ] Stage 2 — GitHub, VS Code, Copilot
- [ ] Stage 3 — Hugging Face local RAG
- [ ] Stage 4 — Azure AI Foundry and the agent
- [ ] Stage 5 — Securing the agent
- [ ] Stage 6 — The AI gateway
- [ ] Stage 7 — Purview DLP
- [ ] Stage 8 — Purview DSPM
- [ ] Stage 9 — Copilot Studio
- [ ] Stage 10 — Defender for Cloud
