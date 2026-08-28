# Infrastructure

Azure resources defined as code, so the environment can be destroyed when you
stop working and rebuilt in a couple of minutes.

This also gives Stage 10 something to scan — Defender for Cloud checks IaC files
for misconfiguration before deployment, which is "shift left" made concrete.

```
az deployment group create --resource-group policy-buddy-rg --template-file main.bicep
az group delete --name policy-buddy-rg     # tear down
```

Resources: Foundry project, Key Vault, Application Insights, and — Stage 6 only,
delete afterwards — the API Management AI gateway.
