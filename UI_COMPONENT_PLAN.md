# ConvertKit (Kit) Connector — UI Component Plan

## Sidebar Form Specifications
- Container: `ui.Stack(direction="v", gap=3, align="stretch")`
- Explicit labels on all inputs:
  - "Connection Label" (placeholder: "e.g. Creator Account")
  - "Kit API Key / Bearer Token" (placeholder: "Paste your Kit v4 API key or token", type="password")
  - "API Endpoint (Optional)" (placeholder: "https://api.kit.com/v4", type="text")
- Action Button: "Connect Kit" (`variant="primary"`)
- Secondary actions:
  - "App settings" (`variant="secondary"`)
  - "How do I set this up?" (`variant="ghost"`, triggers setup modal with step-by-step guidance)
