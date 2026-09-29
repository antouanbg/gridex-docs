# GrideX documentation handoff

## 2026-09-29 — държави за пазарните цени и Grafana

Публичният BG/EN `market-prices` guide вече описва изричното правило: само
BG се събира по подразбиране; супер администраторът разрешава друга зона
за себе си и отделно за активна организация. Услуга, зона и член са различни
права; клиентски ценови стойности засега няма. Старите чужди записи могат
да останат, но не се събират наново без разрешение. Частен операторски
Grafana dashboard е подготвен, не е активиран/публикуван. Backend миграция
018/API са live; frontend PR #70 е слят и Pages deploy мина. Реалният тест
с трите роли още не е потвърден. След source merge задължително
`sh scripts/deploy-local.sh` и проверки на BG/EN страници и
CSS/JS MIME. Реалната приемателна проба с трите роли е отделна.

## 2026-09-29 — права за услуги и пазарен архив

Одобрено: супер администраторът разрешава услуга на организация; нейният
администратор разрешава на всеки одобрен член поотделно. Без лично право
услугата не се вижда в реалното меню. Стойности/история на часовите ENTSO-E
цени са само за супер администратора; в портала засега се показват единствено
API status и последен успешен час. BG/EN страниците `market-prices` и
`organisations-and-access` са синхронизирани. Отделната TimescaleDB реално
съхранява 240 часови реда за 10 зони, без retention. Докато frontend не бъде
публикуван/тестван с истинските роли, страниците изрично го казват.
Typecheck и двуезичен Docusaurus build минават.

## 2026-09-29 — BG/EN помощта е внедрена

PR #15 е слят в `main` като `2c10d73`. От актуалния `main` е изпълнен
`sh scripts/deploy-local.sh`: typecheck, BG/EN build, пресъздаване само на
docs контейнера и локални HTTPS проверки на двата guide адреса плюс
CSS/JavaScript MIME завършиха успешно (`GRIDEX_DOCS_DEPLOYED`).
Външните заявки от този Mac към `doc.gridex.tech` изтичат по публичния
маршрут; достъпността от външна мрежа за тази ревизия остава непотвърдена.
Реалният клиентски тест на вход/покана също остава отделен.

## 2026-09-29 — покани и смяна на акаунт

Одобрените в текущия разговор правила са описани едновременно в BG/EN
`organisations-and-access`: вход с друг акаунт без наследен realm, приемане
на членска покана след проверен вход без втори бутон, еднократно resend от
поканения до същия имейл, приета покана без срок на стария линк и последен
записан вход, нов Обект само в „Обекти“. Локалните typecheck/build минаха.
Още НЕ е публикувано; изчакай backend миграция 016/API и frontend rollout,
после `sh scripts/deploy-local.sh` и провери BG/EN URL и CSS/JS MIME.

## 2026-09-29 — member invitation and session guidance

BG/EN Docusaurus organisation guide now explains send confirmation,
persistent statuses, sent-only resend for the same identity, viewer menu
visibility and automatic transient-session retry. Existing design/components
are unchanged. Typecheck and both locale builds pass. Publication must be
verified separately before calling the guide live.

## 2026-09-29 — customer device guide prepared, not live

BG: Слях двуезичната помощ за нов Обект, ROCK Pi E/OLIMEX ESP32-EVB и до две роли с актуалния вход по имейл и възстановяване на парола. Docusaurus typecheck и BG/EN build минаха. Публикацията чака изрично одобрената backend миграция/API рестарт и проверен frontend deploy; ръководството още отбелязва, че функцията не е live. Без промяна в одобрения дизайн.

EN: Merged the BG/EN Site/device guide with current login and recovery instructions. Typecheck and both locale builds pass. Do not publish it as live until the authorised backend/frontend rollout and real customer acceptance.

## Main and live docs reconciliation — 2026-09-28

Owner-approved PR #9 merged BG/EN organisation-access guidance with the
existing protected Manager guide into `main` (`fcf5500`). The unchanged
approved Docusaurus design was rebuilt and the existing docs container was
recreated from its live checkout. Typecheck, BG/EN builds, HTTPS pages and
CSS/JavaScript MIME checks passed. No real customer suspension has been
performed; the guide marks that limitation. Customer Site/device creation
PR #4 stays open until backend #43 and frontend #55 can be safely deployed.

PR #9 обедини BG/EN помощта за организационен достъп с Manager ръководството
в `main` (`fcf5500`). Публикувано е през съществуващия Docusaurus
контейнер след успешни проверки на типовете, двата езика, HTTPS и MIME за
CSS/JavaScript. Първо реално спиране не е извършено. PR #4 за нови клиентски
Обекти/устройства чака безопасното внедряване на backend #43 и портал #55.

## 2026-09-28 — OpenRemote Manager from the portal

The owner approved an immediate, one-time Manager launch button in the
existing GrideX administrator page. Matching BG/EN instructions are published
at `organisations-and-access.md#openremote-manager` in the approved
Docusaurus design (PR #6). Backend migration 014, protected proxy and the
first customer callback are deployed and verified locally. `npm run typecheck`,
BG/EN builds and local HTTPS/CSS/JS MIME checks passed. External positive
browser acceptance with the pilot and customer administrators is still
pending; do not claim that this final step has passed.

Същият раздел на български описва бутона, еднократния линк, организацията
от текущата сесия и отказа на директния адрес. Страницата е публикувана,
backend/proxy са внедрени, но реалният положителен тест от външна мрежа с
двата акаунта още предстои. Дизайнът не е променян.

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

## 2026-09-27 — customer organisation member-invitation help

The owner limited the new how-to to administrators of an **existing customer
organisation**, not the platform/super administrator or first-admin creation.
The BG and EN organisations guides now contain matching member-invitation
steps at `#invite-a-colleague`, including role/Site limits, recipient
acceptance, and the warning not to retry blindly after an ambiguous send.
The first real customer invitation and acceptance remain unverified. The
approved visual design was unchanged. `sh scripts/deploy-local.sh` passed
TypeScript, both locale builds, local HTTPS and CSS/JavaScript MIME checks;
the docs container was recreated. Source was published on `main` as
`c26c676`. An external request from this Mac timed out; the local HTTPS
proxy passed, so external rendering for this revision remains unverified.

## 2026-09-27 — public source repository

The standalone Docusaurus source and its local Git history were published to
the public `antouanbg/gridex-docs` repository on `main`. The owner confirmed
the corrected public mobile rendering and approved the current design.

## 2026-09-27 — approved design and ongoing publication rule

The owner confirmed the corrected public page renders properly and approved
the current GrideX-aligned responsive visual design. Preserve this design for
new and edited pages. Every new or revised user-facing question, workflow,
menu or feature must be documented in its relevant public guide section and
published with the implementation; BG and EN content must remain aligned.
Unverified or not-yet-live behavior must be labeled as such.

## 2026-09-27 — public rendering incident corrected

The owner showed an external mobile screenshot of an unstyled Docusaurus page.
The HTML, image and compiled assets returned 200, but the docs Nginx config
omitted `mime.types`: CSS and JavaScript were served as `text/plain`. Because
`X-Content-Type-Options: nosniff` is enabled, the browser correctly rejected
them. Added `include /etc/nginx/mime.types` and an octet-stream default;
the deploy script now checks the live CSS and JS MIME types, not only HTML.
This supersedes the earlier visual acceptance claim below.

After redeployment, the local production HTTPS proxy returned 200 with
`text/css`, `application/javascript`, and `image/jpeg` for the expected assets;
a 390px Chromium session through that proxy rendered the correct H1, loaded
the hero image, applied the body font, and logged no failed HTTP responses.
The owner subsequently confirmed the external mobile page renders correctly.

## 2026-09-27 — portal-aligned redesign

Owner reported that the original Docusaurus site looked unformatted and had no
visual material. The site remains Docusaurus, but now uses a typed
`docusaurus.config.ts`, `src/components/*` and TypeScript theme overrides for
the global footer and document CTA. Its BG and EN pages have a responsive
photographic hero, guide cards, clear invitation steps, status notices and
portal links. The original generated solar-site image is explicitly labeled
illustrative and stored at `static/img/solar-hero.jpg`; it is not a customer
Site. Styling follows the approved GrideX green/lime portal shell.

Acceptance evidence: `npm run typecheck` and
`npm run build` passed; BG and EN home/guide plus BG pending page rendered on
1440px and 390px without horizontal overflow, with one H1 and loaded image.
Both locale-specific home → guide → steps links worked in Chromium.
`sh scripts/deploy-local.sh` was run successfully. Through the live local HTTPS
proxy, BG and EN guide pages returned 200 with trusted TLS, the hero image
returned 200, and the API's unauthenticated `/api/v1/me` still returned 401.
The owner previously confirmed the public docs address works from outside;
the owner has now also accepted the corrected visual revision from outside.

Remaining: publish additional guide topics only after their related portal
screens and permissions are verified. The certificate remains manually
renewed; expiry and procedure are in README.
# Email-first sign-in help / Вход по имейл — 2026-09-28

Потвърденото решение за общия вход е описано двуезично на страницата
„Организации, покани и права“: имейл от поканата → правилен Keycloak realm →
парола само там. При няколко организации има избор. Това не заменя проверките
за членство/Обекти и не обявява още непубликуван frontend за продукционен.

EN: The BG/EN access guide now documents email-first realm routing and
Keycloak-only passwords. Publish together with the frontend/backend change;
do not claim a live rollout from this docs commit alone.
# 2026-09-29 — „Пазар“ / Market day-ahead guide

BG/EN `/market-prices/` guide was added for the owner-approved existing
`/market/` view and ENTSO-E A44 day-ahead product. It explicitly says the
integration is prepared but not yet publicly verified. TypeScript and both
locale builds pass. Do not publish a false live claim; after backend token,
real A44 and portal browser acceptance, update the status line and deploy
with `scripts/deploy-local.sh`, verifying HTML/CSS/JS in BG and EN.
