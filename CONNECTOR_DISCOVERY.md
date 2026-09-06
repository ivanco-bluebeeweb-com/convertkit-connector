# ConvertKit (Kit) Connector — Connector Discovery

## Primary Source Documentation
- Official Developer Portal: `https://developers.kit.com/`
- API Reference: `https://api.kit.com/v4`
- Authentication Guide: `https://developers.kit.com/v4/reference/authentication`

## Verified Endpoints & Capabilities
| Resource | Method | Path | Description |
|---|---|---|---|
| Account | GET | `/account` | Identity verification & primary email |
| Subscribers | GET | `/subscribers` | List audience contacts with pagination |
| Subscribers | GET | `/subscribers/{id}` | Detailed subscriber record |
| Subscribers | POST | `/subscribers` | Upsert subscriber |
| Broadcasts | GET | `/broadcasts` | List newsletter broadcasts |
| Broadcasts | GET | `/broadcasts/{id}/stats` | Performance stats & click analytics |
| Tags | GET | `/tags` | Audience interest tags |
| Segments | GET | `/segments` | Dynamic condition filters |
| Sequences | GET | `/sequences` | Automated multi-step drip campaigns |
| Templates | GET | `/email_templates` | Email layout templates |

## Authentication Discovery
- Primary: API Key via `X-Kit-Api-Key` header or `Authorization: Bearer <api_key>`
- OAuth 2.0 Authorization Code flow for third-party marketplace apps.
