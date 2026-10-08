# GrideX documentation handoff

## 2026-10-08 — external audit correction (deployed; external acceptance pending)

Approved role reference now declares UTF-8 and viewport explicitly. Nginx
declares UTF-8 for text responses. BG/EN approved-screen help defines role,
service order, failure-state and mobile acceptance. Preserve canonical layout.
PR #53 merged as 23a120b. Deployed through scripts/deploy-local.sh; BG/EN,
CSS/JS MIME and canonical HTML content-type text/html; charset=utf-8 checks pass
through the local proxy. Browser characterSet UTF-8 and Cyrillic verified.
External VPN/real-account acceptance remains pending; local checks do not prove it.
Build dependency audit reports 47 findings (15 moderate, 16 high, 16 critical).
Runtime serves static output; dependency remediation needs a separately tested
update, not npm audit fix --force. Existing lockfile was preserved.

## 2026-10-04 — public presentation privacy

Owner approved removing personal owner credits and project repository URLs
from BG/EN public portal and help. Open-source/MIT description stays; enquiry
form and permissions remain unchanged. Project-source links removed from
the public device catalogue; third-party references/licences retained.
No account changes, Git history rewriting or repository visibility changes.
Public repositories and previously cached content remain discoverable elsewhere.
Regression: BG/EN About/catalogue browser checks and generated bundle scans.
БГ: премахнати публични лични споменавания и адреси на проектния код.
„Отворен код/MIT“ остава; няма промени на акаунти и права. Историята на Git
и правните бележки не са променяни. Публикуването се проследява в PR.

## 2026-10-04 — approved documentation consistency correction

Owner approved removal of obsolete instructions and visible unambiguous matrices.
Corrected BG/EN organisation and price guides: Services for personal requests,
Settings → Users for administration, Services → Day-ahead for price content.
Settings → Market remains tariff/contract/balancing; collection controls currently
remain in the day-ahead screen. Catalogue visibility is not data access.
Notifications are queued separately; delivery is not implied by a saved decision.
Home links menu/authority/role-action/service matrices and approved role screens.
Historical entries below are retained as dated evidence, not current guidance.
Regression: 8 BG/EN page pairs, required anchors and obsolete-name check added.
Verified: consistency gate 8 BG/EN pairs; TypeScript and both locale builds pass.
Deployed via deploy-local.sh; proxy CSS/JS MIME checks pass. Browser audit:
four guide routes x BG/EN x 390/1440px, no overflow or page errors, all matrix
anchors present. Public-DNS external reachability requires the known VPN route;
the local proxy check is not external acceptance. Git publication is tracked in PR.
Dependency audit reports 31 findings (2 moderate, 29 high); no blind upgrades
were included in this documentation-only correction.
БГ: изчистени са старите менюта и противоречията за уведомленията. Матриците
са видими от началото; права за Обект, услуга и организация остават отделни.
Няма промяна в реални права, API или одобренията. Историята долу не отменя
актуалното ръководство. Не се твърди, че бъдещите услуги са внедрени.

## 2026-10-04 — demo follows database matrix / Демо по базата

Owner explicitly requested every Demo page to follow the approved database
order/matrix. Source: current Phase3 decisions and navigation_catalog revision 1,
27 public metadata rows, read-only checked. No new permissions or backend writes.
app/lib/navigation-catalog.json is a versioned public presentation snapshot:
no users, organisations, grants or inventory. check-navigation-catalog.mjs must
match the database before release; updating the DB alone does not update the
static public demo until the snapshot is reviewed and the frontend republished.
Routes, order, parents and demo landing links share this catalogue.
Separated inverter/charger lists; meters and connectivity stay in Infrastructure;
sample charts move to Services. Sites show sample assets/infrastructure/services.
Users in Demo is explanatory only, never a real invitation or grant form.
BG/EN guide: /demo-navigation/. Verified: 27 DB rows match; 86 browser tests,
29 unit/render tests, TypeScript and lint pass (4 existing image warnings).
Docs BG/EN build and local proxy checks pass. Release pending GitHub checks.
Do not infer completed live modules from this demo work.
Regression discoveries: legacy Demo hid Users while the landing card linked to
it; now shows its explanatory screen. Test JSON imports require type attributes.
First typecheck caught obsolete demo comparisons in the live-only branch; fixed.
Regression coverage: all 27 pages x BG/EN x mobile/desktop, hierarchy/links/help,
no private API calls or page errors. Corrected balancing-card desktop overflow,
duplicate infrastructure catalogue and stale 26-entry mobile test expectation.
The CommonJS render test loader now supports the JSON catalogue import.
БГ: одобрена е корекция на всички демо страници по каталога на базата.
Публичното копие съдържа само структура; няма клиентски данни или права.
Подредбата и адресите са общи, а всяка страница има БГ/EN помощ.
Незавършените реални услуги остават означени, без измислени интеграции.
Промяна в базата изисква сверяване на копието и нова публикация на демото.

## Current release — 2026-10-03 / Текущо внедряване

Supersedes earlier “not deployed” notes below. Approved three-role Users screens
merged in energy-os PR #105 (52321e6); Pages deployment 37151980982 succeeded.
Public https://gridex.tech/release.json confirmed the exact merge SHA.
Backend PR #98 (160191f) deployed API-only with backup, healthy; no new migration.
82 browser tests, 29 frontend tests, typecheck/build, and GitHub CI passed.
API: 148 pass/1 skip. Read-only live probe confirms both organisations,
five-service catalogue, member counts 1/2, OpenRemote links and realm denial.
No real grants or emails changed in tests. Real-account acceptance is pending.
Regression: server-render test counted only double-quoted lazy imports and an
obsolete count; corrected to both quote styles and the 22 current modules.
Mobile access error now has icon/text grid cells instead of a narrow text cell.
Canonical BG/EN docs: /approved-users-screens/ and /en/approved-users-screens/.
БГ: одобрените екрани и личното Отмени/Спри са публикувани. Обектите, услугите
и ролите остават отделни права. Публикуването е проверено; тестът с реалните
три акаунта не се представя като вече приключен.
Repository / GitHub: `antouanbg/gridex-docs`

## 2026-10-03 — three Users screens approved / три одобрени екрана

Documentation build regression: inline details/summary markup failed MDX parsing.
Separated tags and Markdown blocks; BG/EN typecheck/build and deployment rerun.
Keep this structure in future screenshot pages. Dependency audit reports 36
findings (2 moderate, 34 high); dependency remediation is separate from this scope.
БГ: поправено е MDX форматирането на разгъваемите мобилни снимки; проверката
и компилацията се повтарят и за двата езика.

Owner approved Settings → Users three-role mockup and requested documentation.
Canonical public reference: gridex-docs /approved-users-screens/ (BG) and
/en/approved-users-screens/ (EN); static/approved/users-three-roles.html retains
the layout with sanitized example identities. Six screenshots cover three
roles at 1024/390px. Backend action mapping: docs/APPROVED_USERS_LAYOUT_API.md
in backend repository. Latest suite: 148 pass, 1 skipped; no new live grants/mail.
Owner confirmed personal-only cancel/stop and new admin approval to re-enable.
Source includes two protected endpoints, five backend regression tests and BG/EN
controls with confirmation. Typecheck, frontend build and four targeted browser
tests passed. New portal layout and endpoints remain undeployed.
БГ: трите екрана са одобрени; публичните копия са с примерни самоличности.
Пазят се desktop/mobile и съответствието с API. Макетът не доказва живо
внедряване. Отмени/Спри записва само личния ефект; ново включване изисква
админско одобрение. Има код и тестове, без промяна на реални права.

## 2026-10-03 — approved migration 023 applied / миграция 023 приложена

Verification update: Docusaurus BG/EN deployed with scripts/deploy-local.sh;
typecheck/build and live proxy HTML/CSS/JS MIME checks passed. Both
/navigation-and-permissions/ and /en/navigation-and-permissions/ contain
menu-matrix and authority-matrix. Normal-DNS auth request timed out (000);
forced local proxy returned issuer 200 and admin denial 404. External web
probe could not access the docs URLs. Public-network acceptance is not proven
by these local checks; do not diagnose a site outage without VPN/route evidence.
Docs npm ci reported 36 dependency advisories (2 moderate, 34 high); no blind
audit fix applied. Follow-up: assess dependency tree and static-build exposure.
БГ: BG/EN помощта е внедрена; локалният жив proxy обслужва матриците и правилни
CSS/JS типове. Външната проверка остава мрежово непотвърдена. npm отчете
36 предупреждения за зависимости (34 high); необходим е отделен анализ,
без автоматично обновяване на несъвместими версии.

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

## 2026-10-03 implementation checkpoint / проверка на реализацията

Navigation migration 023 seeds 27 approved entries; authenticated
GET /api/v1/me/navigation returns identity-bound presentation states, no-store.
Existing resource authorization remains mandatory. Frontend consumes catalogue
order/visibility; known route/component mapping remains in source. Asset presence
still comes from authorised inventory requests, not new local inventory records.
Keyed BG/EN navigation resources and the five-column member register are implemented.
Database migration dry-run succeeded with ROLLBACK (27 rows); not yet applied.
Backend suite: 144 tests, 143 pass, 1 skip, zero failures. All four navigation
unit/HTTP tests pass. Frontend TypeScript/build pass, eight invitation/member
tests pass; demo checks pass at 360/390/430, new route tests at 390/1440 pass.
Full browser regression rerun: 79 passed, zero failures.
Docusaurus BG/EN typecheck/build pass. Live migration/API/frontend acceptance
still pending. Older inline translations and remaining view integration are
NOT claimed fully migrated. Do not call this a completed production rollout.

БГ: има работещ локален каталог/API и петколонна таблица; тестовете по-горе
са проверени. Пробата на миграцията е върната назад. Всички 79 браузърни теста
минават; живото внедряване и приемането остават отделни стъпки. Не разширявай права
и не представяй неприключените екрани/преводи като готови.

Follow-up regression evidence: initial full browser run 57/79, next 74/79.
Failures exposed a real navigation-shell regression when catalogue verification
failed and stale test expectations for renamed routes/collapsed member details.
Fixed safe shell links and anonymous-only demo navigation; last nine targeted
tests pass, including all five remaining failures. Full rerun passed all 79 tests.
БГ: отстранено е скриване на основните връзки при непроверим каталог и показване
на демо навигация след неуспешна проверка на вход. Пълният набор е успешен.

Publication: frontend PR #105, backend PR #96, documentation PR #48.
Live deployment is blocked pending explicit owner approval for migration 023
and gridex-api restart. The execution reviewer rejected the combined merge/live
operation before execution; no live migration or restart occurred. Keep frontend
deployment behind the backend schema/API rollout. Browser fixtures are not proof
of production role acceptance; some screenshots intentionally show unavailable
dependencies. Full legacy i18n conversion remains outstanding.
БГ: чака се изрично одобрение за миграция 023 и рестарт само на gridex-api.
Не представяй Git публикацията и локалните тестове като живо внедряване.

## 2026-10-03 — approved dynamic navigation / динамична навигация

Owner approved PostgreSQL navigation metadata with existing service grants;
OpenRemote remains inventory/identity/Site authority. AGENTS contains the
binding hierarchy, user feedback for denied versus unverifiable access,
BG/EN locale resources and future-language extension rule. No blanket email
notification on denial, new rights or fallback demo data is authorised.
Status: LOCAL / implementation ongoing, not migrated or deployed.
Frontend navigation labels now use keyed BG/EN resources; legacy inline
translations still need migration. Full effective-navigation API, database
seed/migration, access feedback wiring and end-to-end role/tenant tests remain.
Test incident: localhost preview initially blocked by sandbox (EPERM), not a
website outage. JSON imports in Node tests required type:json attributes;
source corrected. Re-run localization suite and TypeScript before publication.

БГ: одобрено е динамично меню от PostgreSQL с текущите разрешения за услуги;
OpenRemote остава единствен източник за инвентар и Обекти. Липсващо право,
чакаща заявка и непроверим достъп се съобщават различно. AGENTS е актуализиран.
Само локална подготовка: няма приложена миграция/жив release. Менютата вече
ползват BG/EN ключове; останалите inline преводи, API и цялостните тестове
предстоят. Не представяй подготовката като завършено внедряване.

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


## 2026-09-30 — изход към демото

BG/EN указанията за организации и достъп вече описват директното връщане
към публичното демо след „Изход“ и поведението на другите табове. Публикувай
след съответната backend callback и frontend поправка; реален потребителски
тест след внедряване остава отделно потвърждение.

## 2026-09-30 — Market chart range guide (source gate)

Paired BG/EN Market pages now describe the new short initial range, presets,
custom Bulgaria-local delivery dates (up to 31 days), and the two status Stats.
Do not publish before the protected backend proxy/range and portal controls
are live. Typecheck/build must pass, then deploy with the Docusaurus script
and verify both locales and asset MIME. Real mobile owner acceptance is open.

## 2026-09-30 — account switch guide (source gate)

The BG/EN organisation-access guide now explains that choosing a new email
starts a new explicit login, an old identity is rejected, and the previous
Site choice does not carry into the new account. No customer credentials are
included. Source typecheck/build pass. Merge and redeploy the guide with the
frontend account-switch correction, then verify both locale routes and asset
MIME. External mobile acceptance remains with the owner.

## 2026-09-30 — Login guide deployment checkpoint

PR #32 is merged as `1667b62`. The approved `sh scripts/deploy-local.sh`
completed with `GRIDEX_DOCS_DEPLOYED`; both BG/EN routes and CSS/JS MIME
passed. The running container serves the new BG and EN sign-in paragraphs.
The public `doc.gridex.tech` address timed out from this Mac, so external
browser acceptance is still open; this is not evidence that the container
failed. Next: open both locale URLs from an external network and confirm
normal rendering. No credentials are needed for this guide.

## 2026-09-30 — Login and Demo guide update

The paired BG/EN organisation/access guide now explains that email entry is
near the top of Login, an unfinished sign-in returns directly to the chosen
Demo section, and verified sign-in briefly confirms success before Overview.
No credentials or customer data are documented. Typecheck and both locale
builds pass. This is source-ready, not yet a verified public deployment.
Next: merge with the frontend correction, run `sh scripts/deploy-local.sh`,
check BG/EN routes and CSS/JS MIME, then record external browser acceptance.

Двуезичните указания за прекъснат и успешен вход са подготвени. Следва
публикуване и проверка на живите страници, без предварително да се обявяват
за достъпни.

## 2026-09-30 — contact guide publication gate

BG/EN contact guides are built but not deployed. Dependency: backend support
mail API, private recipient config and portal About form must be live first.
Acceptance: publish with `sh scripts/deploy-local.sh`, verify BG/EN routes,
CSS/JS MIME and the About help link after real visitor/member inbox tests.
Exact next action: review docs PR and wait for the backend/frontend release;
only then publish and mark the About help destination ready.

Двуезичният текст е подготвен; живото публикуване и проверките предстоят.

## 2026-09-29 — дата на доставка в „Пазар“

BG/EN ръководството „Пазар — цени ден напред“ описва отделно деня/часа
на доставка, последния реално наличен BG час и часа на ENTSO-E обновяване.
Обяснението не смесва непубликуван утрешен ден с нула или стара цена.

## 2026-09-29 — Site графиките са публикувани в документацията

PR #21 е в `main` (`cc61e33`); `sh scripts/deploy-local.sh` завърши с
`GRIDEX_DOCS_DEPLOYED`. BG/EN Docusaurus build и локалните HTTPS/MIME
проверки минаха. Външният `doc.gridex.tech` от този Mac не е потвърден
заради мрежовия път. Реалният вход и графика с клиентски акаунт остават
за приемателен тест след ръчните org/member одобрения.

## 2026-09-29 — BG/EN ръководство за графиките на Обект

Към ръководството за организации е добавен `#site-visualisations` и на двата
езика: точен OpenRemote Обект, отделни права за услугата, последни 24 часа,
без демо данни и без общ Grafana клиентски източник. Docusaurus BG/EN build
мина. Live deploy и проверка на връзките се отразяват отделно.

## 2026-09-29 — BG/EN описват заявките за услуги

Обновени са ръководствата за организации и „Пазар“ и на двата езика.
„Профил → Услуги“ показва заявяемите `day_ahead` (само BG) и
`visualisations`; заявката не дава достъп. Описани са отделните одобрения
и историята. Графики за OpenRemote Обекти все още не са внедрени.
Docusaurus BG/EN build мина; live публикацията се записва отделно след
backend миграция 020 и frontend rollout.

## 2026-09-29 — BG/EN Grafana guide е публикуван

PR #18 е слят в `main` (`12fbc9d`) и от този commit е изпълнен
`sh scripts/deploy-local.sh` до `GRIDEX_DOCS_DEPLOYED`. BG/EN guides,
CSS/JS MIME и локалният HTTPS маршрут са проверени. Публичният маршрут
от този Mac изтича по мрежовия път, затова външно отваряне на docs и
пълният iframe тест с човешки акаунт не се твърдят като проверени.
Екранът за заявки за услуги и графиките за Обекти остават за следваща
реализация; не ги представяй като налични.

## 2026-09-29 — защитен BG пазарен dashboard

BG/EN ръководствата `market-prices` и `organisations-and-access` вече описват
отделните права за „Цени ден напред“ и „Графики“, BG зона, вградения бутон
в „Пазар“ и еднократния защитен вход. Пълният архив/API остава само за супер
администратора; Grafana чете единствено BG read-only изгледи. Екранът за
заявки и графиките за Обекти не са внедрени. Реален браузърен приемателен
тест с клиентско разрешение предстои; старите записи по-долу отразяват
състоянието преди тази публикация. Двуезичният build и typecheck минават.

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

# 2026-09-30 — Услуги и права по организация / Organisation service rights

BG/EN страницата „Организации, покани и права“ вече описва целия одобрен
път: каталог в „Профил → Услуги“, заявка без автоматично право, разрешение
за активна организация от супер администратор, после индивидуално
разрешение от организационен администратор. Уточнени са петте услуги,
двете активни за заявки, BG зоната и нужните две права за ценовата
визуализация. Неразрешените услуги остават видими като каталог, но не
отварят защитено съдържание. Тази промяна е само в изходния код на
документацията; публичният сайт още не е проверен след ново внедряване.

EN: The BG/EN organisations-and-access guide now documents the complete
platform-admin → organisation-admin → member service grant flow and the
five-item catalogue. Source is updated; public deployment/verification is
still pending.

Publication update: PR #37 merged into `main` at `a1268df`. The approved
`sh scripts/deploy-local.sh` recreated the read-only docs container and
returned `GRIDEX_DOCS_DEPLOYED`; BG and EN guide routes served the new headings
over the local HTTPS proxy, with CSS and JavaScript MIME checks passing. Direct
public-hostname checks from this Mac timed out because the external route/VPN
was unavailable; verify both URLs from an external network. This is an open
verification item, not evidence that the docs service failed.
## 2026-10-02 — approved access model in BG and EN help

`organisations-and-access` now has parallel `#rights-matrix` and
`#approved-members` sections in Bulgarian and English. The matrix explains
human read-only OpenRemote Manager, realm-local backend Asset clients,
GrideX role/Site checks and separate service entitlements. The member page
links to these anchors. Docusaurus build and TypeScript pass. Keep the
production-status note until backend role migration, portal deployment and
real-account acceptance are verified; source documentation alone is not a
live entitlement.

Live checkpoint: after backend role migration and portal Pages deployment,
`sh scripts/deploy-local.sh` returned `GRIDEX_DOCS_DEPLOYED` following BG/EN
typecheck/build and local HTTPS/CSS/JS checks. BG/EN status was updated in
PR #41. Signed-in real-user acceptance remains pending.
