# CODEX_STATE

## 2026-10-03 — confirmed personal cancel/stop

Owner confirmed: cancel only own pending request; stop only own active grant.
Organisation, other members and Site assignments unchanged. Re-enable requires
new organisation-admin approval. Source implemented; API 148 pass/1 skip,
four targeted BG/EN browser/locale tests pass, frontend typecheck/build pass.
No new live permission changes. New API/portal controls are not deployed yet.
Approved three-role reference is in gridex-docs /approved-users-screens/ and EN.
БГ: обхватът е окончателно одобрен, само личен. Има код и тестове;
не се твърди живо внедряване на новите бутони и API.

## 2026-10-03 — approved migration 023 applied / миграция 023 приложена

Owner explicitly approved migration 023 and restart of gridex-api in this chat.
Backup created in the private runtime backup directory; no credentials published.
Deployment returned NAVIGATION_API_HEALTHY. Read-only verification: 27 rows,
revision 1; API healthy, anonymous navigation request returns 401. API started
2026-10-03T18:54:45Z. Existing environment and other containers preserved.
Backend PR #96 merged to main (4649ce1). Frontend PR #105 is not deployed yet;
do not claim the new menu is live merely because its API is ready.
The full BG/EN menu-role-account-data matrix and OpenRemote responsibility
matrix are in docs navigation-and-permissions, with approvals/revocation,
infrastructure prerequisites, five-column member design and unresolved items.
Previous pending-approval notes below are historical and superseded here.

БГ: изрично одобрената миграция 023 е приложена след частен backup.
Потвърдени са 27 записа, revision 1, здрав API и отказ 401 без вход.
Рестартиран е само gridex-api; другите контейнери и настройки са запазени.
Backend #96 е в main. Frontend #105 още не е внедрен. Пълната матрица BG/EN
и отговорностите на OpenRemote са описани; бъдещи услуги/драйвери,
неуточнени права и целият стар i18n не се обявяват за готови.

## 2026-10-02 — remove in-session account switching

Owner explicitly removed Switch account/user. The account menu now retains
Profile, Documentation and Sign out only. Another person must Sign out →
Demo → Sign in with their own email/password. No identity, permission,
backend, logout or OIDC policy is changed; existing mismatch guards remain.
BG/EN inline help and Docusaurus guide updated; AGENTS prohibits restoring
the switch action. Regression covers both languages, desktop/mobile,
logout clearing private data, new same/cross-realm login and stale/callback
failures. All 11 targeted browser tests passed; Pages build, TypeScript
and lint passed (four existing image warnings). The initial mobile test
attempt omitted opening Menu; corrected the test, not the production layout.
Source ready; merge/publication tracked by this release PR. Docs deployment
uses deploy-local.sh; owner/real-Keycloak logout/login acceptance remains
separate from browser fixtures. No backend restart needed.

Български: по изрично искане е премахната „Смяна на профил/потребител“.
Остават Профил, Документация и Изход. Друг акаунт се ползва само с
„Изход“ → демо → „Вход“ с новите имейл/парола. Няма промени на права,
backend, организации, OIDC или текущата защита за несъвпадаща самоличност.
Помощта е обновена на BG/EN; AGENTS забранява връщането на опцията.
11 целеви browser теста минаха, с Pages build, TypeScript и lint.
Първият mobile тест не отваряше Меню — поправен е тестът, не дизайнът.
Кодът е готов; публикацията се проследява в PR. Реалният Keycloak тест
от собственика остава отделен от симулираните сценарии. Без рестарт на API.

## 2026-10-02 — continuous layout publication checkpoint

Published and merged: frontend PR #102 (main 07a792147820d3e26db775493bc89bffdde4e0f4),
backend PR #94 (df78df72991125d9bdcb5c1e15576f22e22e5da1), docs PR #45
(6aa1f92ec24ad76b82a7a9f49b2dce3924f52487). Frontend Pages run 37029349030
succeeded. API-only rollout is healthy; backup service-admin-t11cFC is in the
existing private-backups directory. Read-only live probe verifies pilot 1,
customer 2 members; each catalogue has five services and zero grants; tenant
and viewer guards and OpenRemote links/profile recipients verified. No mail
sent and no grant changed by the probe.

BG+EN Docusaurus deployed through scripts/deploy-local.sh; both locale builds,
typecheck and proxy asset checks passed. 75 browser/29 frontend unit tests,
139 backend tests (one skipped) and final 10 role/layout regressions passed.
Four existing image lint warnings and 17 existing moderate docs dependency
audit findings remain outside this layout correction.

Auth gate: local master discovery/console/login passed; the public proxy on
loopback 14443 returns customer discovery 200 and admin/master/health/metrics
404. Normal-DNS public auth timed out (HTTP 000) from this Mac; no configured
VPN connection was shown. This is a network-blocked external check, not proof
of an auth outage or external security acceptance. Owner real-account screen
acceptance, request/approval and notification delivery remain open.
Next: signed-in organisation administrator checks services first, invitations
and both approved members, then tests an explicit service request and decision.
The member's existing workflow and all unrelated navigation remain unchanged.

Български: frontend #102, backend #94 и docs #45 са слети в main.
Pages публикацията е успешна; внедряването само на API е здраво с частно
резервно копие. Живата проба само с четене потвърждава един пилотен и двама
клиентски членове, пет услуги без права, OpenRemote връзки и изолация.
Не изпраща писма и не променя права. BG/EN помощта е внедрена с успешни
build/typecheck/asset проверки. Минаха 75 browser, 29 frontend unit, 139
backend (един пропуснат) и последните 10 регресионни проверки по роли.
Локалните auth проверки са успешни; публичният proxy връща 200 за клиентски
issuer и 404 за master/admin/health/metrics. Публичният auth през нормален
DNS от Mac е блокиран от маршрут (timeout/000), без видима VPN връзка.
Това не доказва срив или външно приемане на защитата. Остават реалното
приемане на екрана с акаунт, заявка/одобрение и полученото уведомление.
Следва тест от администратора: услуги най-горе, покани и двамата одобрени
членове, след това изрична заявка и решение. Няма друга промяна на менюто.

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
