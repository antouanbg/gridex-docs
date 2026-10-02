# CODEX_STATE

## 2026-10-02 — canonical continuous layout correction

Owner resolved the conflicting templates: use the recommended continuous page,
with one shared GrideX design for all roles. The three-role mockup is canonical
for page order; the member-access mockup applies only inside the approved-member
editor, not as a replacement tabbed page. Organisation admin order: catalogue,
new invitation, invitation history, approved members/editor, pending requests.
Platform order: approved organisation selector, five service rows, new organisation
invitation, invitation history, approved organisation ledger. Member workflow stays
unchanged. No navigation item, permission, grant or second Accept step is added.

Incident: 2026-10-02. The previous release used three assistant-added tabs and a
decorative hero, so services were hidden behind a tab and the approved template
was not followed. Cause: combining older editor design with the newer page
without resolving their conflict; tests checked the resulting implementation
instead of its reference. Correction removes tabs, restores reference styling,
adds order/visibility/style regression checks, and makes first administrator
first/last names required and verified in Keycloak for new invitations only.
Existing identities, devices and grants are untouched. AGENTS now requires an
explicit question before resolving conflicting approved sources.

Source checks: 75 browser tests, 29 frontend unit tests, TypeScript and lint
passed (four existing image warnings); backend 139 passed, one skipped.
Publication/deployment are pending this commit; owner real-account acceptance
remains open. Next: publish paired frontend/backend/BG+EN help, verify the live
read-only membership/catalogue probe, then owner tests request/approval/delivery.

Български: собственикът избра общ непрекъснат екран и един GrideX дизайн за
всички роли. Макетът с трите роли определя реда; старият редактор определя
само вътрешната секция за одобрените потребители. Премахнати са измислените
три таба и декоративният header. Услугите са първи и петте реда са видими,
после следват поканата, историята и хората/правата. Супер администраторът
първо избира одобрена организация. Потребителската логика не се променя.
Новите първи администратори изискват две имена, проверени в Keycloak;
съществуващи акаунти, устройства и права не се променят. Инцидентът е
липса на проверка спрямо водещия макет. Има нови проверки за ред, видимост
и стил, както и правило за въпрос при противоречие. Тестовете: 75 browser,
29 frontend unit, TypeScript/lint и 139 backend (един пропуснат).
Публикуването/внедряването предстоят; реалното приемане от собственика е
отделна отворена проверка.

## 2026-10-02 — publication and verification checkpoint

Merged PR [#43](https://github.com/antouanbg/gridex-docs/pull/43) into main at `765b0cc780ebd88997cbe1d6c5f15e956626aa5b`.
The matching Bulgarian and English organisations-and-access guides are deployed using scripts/deploy-local.sh (GRIDEX_DOCS_DEPLOYED). Typecheck, both locale builds, local HTTPS guide routes and CSS/JS MIME checks passed. Docusaurus and the approved GrideX design remain unchanged.
Paired releases: frontend #100, backend #92, documentation #43.
Status: source tested, published and deployed; owner acceptance remains open.
Next acceptance: signed-in organisation administrator reviews the roster and
all five service rows, requests an unapproved active service, then verifies
the platform decision, individual member grant and actual notification delivery.
Do not fabricate grants or treat test fixtures/mail configuration as delivered mail.

Български: PR #43 е слят в main (765b0cc780ebd88997cbe1d6c5f15e956626aa5b).
Съответстващите BG/EN ръководства organisations-and-access са внедрени чрез scripts/deploy-local.sh (GRIDEX_DOCS_DEPLOYED). Минаха typecheck, двата locale build-а, локалните HTTPS адреси и CSS/JS MIME проверки. Запазени са Docusaurus и одобреният GrideX дизайн.
Кодът е проверен, публикуван и внедрен; приемането от собственика остава отворено.
Следва реален тест: администраторът вижда списъка и петте услуги, заявява
неодобрена активна услуга; проверяват се решението на супер администратора,
личното разрешение и действително полученият мейл. Без примерни права и без
приравняване на тестови данни/мейл настройки с реална доставка.


## 2026-09-30 — Market chart range guide (source gate)

BG/EN Market guides document the protected period control and Bulgarian
delivery-date meaning. Publish only after the matching backend and portal
changes; then verify both locale routes. See HANDOFF.

## 2026-09-30 — account switching documentation (source gate)

The paired BG/EN organisation-access guide documents explicit new-account
login and rejection of a returned previous account. Publish and verify both
locale routes with the matching frontend fix; see HANDOFF. Do not call the
public documentation updated until the deployment gate passes.

## 2026-09-30 — Login guide deployed

BG/EN guide PR #32 is merged and deployed via the approved script. Local
HTTPS routes, updated text and CSS/JS MIME pass. Public hostname verification
from this Mac timed out; external-browser acceptance remains. See HANDOFF.

## 2026-09-30 — sign-in workflow guide

BG and EN organisation/access pages are updated in parity for top-of-page
email, unfinished sign-in returning to Demo, and successful sign-in landing
on Overview. Both locale builds and typecheck pass. Merge/deploy/live route
checks are still distinct gates; see HANDOFF.

## 2026-09-30 — contact enquiry guide (source only)

BG/EN `/contact-inquiries/` explains demo and verified-member enquiries,
the one-use human check, provider-queued versus delivered status and the
pre-filled offer topic. The guide explicitly says deployment/real delivery
are pending. Typecheck and both locale builds pass. Publish only after backend
and portal are reviewed and live; verify both locales and asset MIME.

Ръководството е подготвено на двата езика, но не се представя като работеща
поща преди истински приемателен тест.

## 2026-09-29 — BG-only market country guide

BG/EN market guide describes BG-only default ingestion, explicit platform
collection and separate organisation zone grants, preserved historical rows,
and private/unactivated Grafana preparation. Publish via deploy-local after
backend and portal updates, then verify both locales. See HANDOFF.

## 2026-09-29 — BG/EN service permissions and market archive

Both market-prices and organisations-and-access guides now describe the
owner-approved default-off organisation/member service rights, hidden live
menu and platform-only price archive/status. They state that 240 actual
hourly ENTSO-E prices are in the separate TimescaleDB, but the frontend
permission UI is not yet published or accepted with real roles. Typecheck
and bilingual build passed. See HANDOFF.

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
