# ConvertKit (Kit) Connector — Preparation

## Product Scope
Build a comprehensive Imperal connector for **Kit (formerly ConvertKit)** under category **C30. Email Marketing & Newsletter**. The integration interfaces directly with the official **Kit REST API v4** (`https://api.kit.com/v4`), providing full coverage across subscribers, email broadcasts, tags/lists, dynamic segments, automation sequences/rules, email templates, and audience health auditing.

## Official API Specifications
- **API Architecture:** RESTful JSON API v4
- **Base URL:** `https://api.kit.com/v4`
- **Core Endpoints:**
  - `GET /account` — verify credentials and retrieve creator identity
  - `GET /subscribers` — list subscribers with status filtering and cursor pagination
  - `GET /subscribers/{subscriber_id}` — detailed subscriber record with tags and custom fields
  - `POST /subscribers` — create or upsert creator audience contact
  - `DELETE /subscribers/{subscriber_id}` — unsubscribe / delete subscriber
  - `GET /broadcasts` — list email broadcast campaigns
  - `GET /broadcasts/{broadcast_id}/stats` — delivery, open, and click performance metrics
  - `GET /tags` — subscriber tags (primary grouping container)
  - `GET /segments` — dynamic audience segments
  - `GET /sequences` — automated multi-step email nurture sequences
  - `GET /email_templates` — email layout templates
- **Authentication Model:** Header-based API Key (`X-Kit-Api-Key: <key>`) or OAuth2 Bearer Token (`Authorization: Bearer <token>`)
- **Mandatory Requirements:**
  - Strict error classification: HTTP 429 rate limits with Retry-After extraction, HTTP 401/403 differentiation (Standard B8/B10).
  - Sanitization of API keys and Bearer tokens in error traces and diagnostic payloads (Standard B8).
  - Multi-tenant connection tracking and isolation via `connection_id` (Standard B9).

## Delivery Gates
1. [x] Official API discovery completed with Kit REST API v4 specifications.
2. [x] Core resource endpoints and authentication methods verified.
3. [x] Five mandatory specification documents authored.
4. [x] Client implemented with B8-B10 compliance, secret redaction, and error categorization.
5. [x] Pydantic schemas and type hints validated without import errors.
6. [x] UI sidebar aligned with `UI_INTERFACE_STANDARD.md` (no duplicate helper text, proper labels, modal help).
7. [x] Synchronized to public GitHub repository and deployed to platform.
8. [ ] Live end-to-end verification with authentic credentials (pending authorized live account).
