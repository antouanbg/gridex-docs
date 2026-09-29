# CODEX_STATE

## 2026-09-29 — BG/EN access guide correction

Both locale guides include approved account-switch, automatic member
acceptance, one-time same-email resend, accepted status/last login and
Sites-only creation. Built locally; live publication depends on backend
migration 016 and frontend deployment. See HANDOFF.

## 2026-09-29 — invitation/session/viewer guide

The existing BG/EN Docusaurus organisation guide documents the corrected
member invitation, scoped sent status/resend, viewer-only navigation and
automatic session retry. Preserve the accepted visual design. Typecheck and
both locale builds pass; publish and verify HTTPS assets before marking live.

## 2026-09-28 publication checkpoint

PR #9 merged as fcf5500 and deployed through the existing Docusaurus
container. BG/EN builds and public local HTTPS/CSS/JS checks passed.
Customer Site/device guide PR #4 remains pending on backend #43 and
frontend #55. See HANDOFF.

## Organisation suspension / Спиране на организация — 2026-09-27

EN: Implemented suspension/restoration in the existing super-admin panel, strict verified pilot-subject permission, pilot protection, revision-locked durable operations, audit and one Mailgun attempt per suspension with recipient-specific delivery verification. API responses/SSE and patched OpenRemote HTTP/WebSocket sessions enforce denial; old JWTs stay revoked after restoration. Accounts, roles and inventory are preserved. Request source: delegated owner task `01a0cea9-3cd0-7430-b309-95795bf293a6`; history reader returned empty items, so the explicit request and repository decisions were used.

BG: Реализирани са спиране/възстановяване в съществуващия супер-админ панел, право само за проверения pilot subject, защита на пилотната организация, устойчиви операции/ревизии, audit и един Mailgun опит за всяко спиране с проверка на доставката до получателя. API/SSE и поправеният OpenRemote HTTP/WebSocket налагат отказ; старите JWT остават невалидни след възстановяване. Акаунтите, ролите и инвентарът се пазят. Източник е делегираното искане от посочената задача; history инструментът върна празни записи и са използвани изричното искане и repository решенията.

Evidence / Доказателства:
- Backend: 68 passing tests, including isolated PostgreSQL transactions, concurrency, multi-realm identity, idempotency, mail ambiguity and active SSE denial. Manager image `1.30.0-organisation-access-v2` compiled with the original issuer test plus access-guard tests.
- Isolated real OpenRemote/Keycloak: populated synthetic Asset inventory preserved, other realm unchanged, cross-realm denial, existing WebSocket closed, BG/EN disabled login, restore, old-token denial and fresh-token access. Test containers/volumes were removed afterward; no real customer data or email was used.
- Frontend: 23 unit/render tests, 52 Chromium tests after integrating main's realm-isolation PR #51, including BG/EN two-tab suspension, null battery/SOC/SOH, empty/denied/unavailable states. Lint has only two existing image warnings.
- Docs: typecheck and both locale builds; BG/EN 390/1440px layout reviewed without overflow.

Runtime / Внедряване: Manager v2 and API with migration 013 are healthy; source hashes match this branch. Private backup `organisation-access-vzUVs1`; organisation/membership/Site counts unchanged. Read-only verified platform identity, feature flag and unauthenticated 401 passed; access-operation count is zero. Local master discovery/admin/login and forced-local trusted-TLS public issuer/Manager/ingress denials passed. Normal-DNS public auth probes time out from this Mac; external real-owner acceptance remains unverified. Няма спряна реална организация, изтрити акаунти, повторна покана или изпратен имейл. Реалната първа доставка остава непроверена; Mailgun acceptance не се представя като delivered.

Publication / Публикуване: backend PR https://github.com/antouanbg/gridex-openremote-backend/pull/40 targets `feat/live-organisation-invitations`, since deployed setup-client/docs-proxy dependencies are not in main. Frontend PR https://github.com/antouanbg/gridex-energy-os/pull/52 and docs PR https://github.com/antouanbg/gridex-docs/pull/1 target main; neither is merged or publicly deployed by this task. Automatic approval review rejected the docs merge, citing trusted AGENTS review/no-automatic-merge rules. No workaround was used. Автоматичната проверка отказа docs merge по правилото за review и забрана за автоматично сливане; frontend/docs остават за изрично одобрение.

Exact next action / Точно следващо действие: obtain owner approval to merge and publish frontend #52 and docs #1 after their checks; update the publication-status note, deploy docs with `scripts/deploy-local.sh`, verify live Pages and BG/EN CSS/JS MIME, then record the actual first owner-triggered suspension/delivery. Keep backend #40's separate base dependency for review. Do not resend the onboarding email here. Изчакай одобрение за frontend #52 и docs #1; след проверките публикувай, смени статуса в ръководството, провери Pages/MIME и запиши първото реално спиране/доставка. Backend #40 пази отделната dependency основа. Не изпращай повторна покана от тази задача.
