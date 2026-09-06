# ConvertKit (Kit) Connector — Auth & Credentials Architecture

## Authentication Lifecycle (Standard B1–B10)
- **Token Protection:** All API keys and OAuth access tokens are stored securely in encrypted tenant vaults.
- **Header Masking:** All outgoing HTTP requests include redacted debugging logs; secrets are scrubbed before emitting diagnostic records.
- **Multi-Tenant Isolation:** All operations enforce `connection_id` isolation.
- **Error Classification:**
  - 401 Unauthorized -> `AUTHENTICATION_FAILED` (Prompt user to refresh key).
  - 403 Forbidden -> `PERMISSION_DENIED` (Explain missing Kit scope).
  - 429 Too Many Requests -> `RATE_LIMIT_EXCEEDED` (Extract `Retry-After` header).
  - 5xx Server Error -> `PROVIDER_ERROR` (Kit upstream issue).
