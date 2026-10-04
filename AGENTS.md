# GrideX public documentation rules

## Documentation consistency gate — 2026-10-04

Before publication run `node scripts/check-guide-consistency.mjs` and verify
all current BG/EN guides against navigation-and-permissions, not historical
HANDOFF entries. Keep menu, role/action and service-prerequisite matrices
linked from the documentation home. A catalogue entry is not a grant; a saved
notification is not delivered mail. Historical decisions stay dated and must
not override the current matrix. This check supplements, not replaces, review.
БГ: преди публикация провери БГ/EN страниците спрямо актуалната матрица.
Матриците са видими от началото. Старите HANDOFF решения са история, не
действащи указания. Каталогът не дава право; опашката не доказва доставен имейл.

## Approved Users reference — 2026-10-03 / Одобрен визуален шаблон

### Confirmed personal cancellation / Потвърдена лична отмяна

Owner answered “Да, точно този обхват”: pending requests can be cancelled
only by their owner; stopping an active service removes only that person's
member_services grant. Organisation/other members/Site rights remain unchanged.
Re-enabling requires a new organisation-admin approval; no self-enable route.
Buttons: Cancel request versus Stop service, with confirmation before active
access removal. This is the final confirmed scope.
БГ: чакащата заявка се отменя само от собственика; „Спри услугата“ отнема
само неговото лично разрешение. Организация, други хора и Обекти остават
непроменени. Повторно включване изисква ново админско одобрение. Това
е окончателно потвърденият обхват.

The owner approved the three Settings → Users mockups in this conversation.
Canonical reference: gridex-docs static/approved/users-three-roles.html and
docs/approved-users-screens.md, with desktop/mobile images for all three roles.
Preserve the continuous page, five-column member roster, expandable editor,
shared GrideX appearance and role-specific authority. Viewer has no Users menu;
direct navigation is denied. Public reference uses example identities only.
Approval of a visual does not prove backend support. Map every action to an
API and test it before deployment. Owner requires the Cancel/Stop control to
remain and persist its effect within the personal-only scope above.
Do not silently remove the button or broaden permission.

Собственикът одобри трите макета Настройки → Потребители. Водещи са
gridex-docs static/approved/users-three-roles.html и docs/approved-users-screens.md.
Пази общия екран, петте колони, разгъването, GrideX дизайна и отделните роли.
Наблюдател няма административно меню; директен адрес е отказ. Примерните
самоличности не са реални данни. Преди внедряване свържи всяко действие с API
и тест. Собственикът изиска бутонът Отмени/Спри да остане с запис в базата;
обхватът е само личен, с ново админско одобрение за повторно включване.
Не махай бутона и не разширявай права мълчаливо.

## Approved dynamic navigation, access feedback and i18n — 2026-10-03

This owner-approved contract supersedes older navigation names and the matrix
implementation hold ONLY within the approved scope. Follow
`docs/NAVIGATION_CONTRACT_2026_10_03.md` in the frontend repository.

- OpenRemote remains authoritative for identity, inventory and Site access.
  Reuse PostgreSQL service catalogue, organisation/member grants and requests.
  Add versioned navigation metadata and requirement references, not a second
  inventory or independently maintained copy of Site permissions.
- Backend computes navigation for the verified realm + subject + organisation.
  Every API action independently enforces permissions. Visibility is not authority.
  Discard cached access/menu data on logout or identity/organisation change.
- Distinguish missing permission (denied), pending request, coming soon,
  missing infrastructure/inventory, and failed/unavailable verification.
  Explain each to the user in the selected language. Never silently fail,
  show a blank screen, substitute demo data, or label a database/API outage
  as a confirmed missing grant. Only offer request/retry actions already approved.
  No automatic email for every denial is authorised by this instruction.
- UI labels/help references use stable translation keys; API errors expose
  stable safe reason codes, not raw SQL, internals or another tenant's data.
  BG and EN are mandatory in the same change. Use separate locale resources,
  BCP 47 locale tags and Intl for dates/numbers/units. Add languages through
  locale registration and matching resources, not binary BG/EN conditionals.
  Test key parity, fallback, interpolation, formats and both locales.
  Docusaurus retains its native i18n. Browser machine translation is not a
  substitute. No new localization SaaS or automatic external translation.
- Required hierarchy: Overview; Sites; Energy assets (Battery, Inverter,
  Charging station, Consumer/load); Infrastructure (ONE page); Services
  (Day-ahead, Graphs, Analysis, Meteorology, Forecasting); Mode (Logic, Schedule,
  Alarm); Settings (Users, Plan/subscription, Market [Tariff/settlement,
  Balancing], Profile [Documentation]); About us.
- Users is ONE administrative page. Personal service requests/approvals are
  in Services. Admins can grant without a request. Organisation grant alone
  never grants all members. Super admin has no self-approval requirement.
  Preserve approved five-column member register and mobile detail expansion.
  Do not invent unresolved tariff fields, balancing/alarm write permissions.
- Migrations, seeds, tests and BG/EN documentation are versioned in Git.
  Record source-ready, published, migrated, deployed and verified separately.

Български: това е одобреното правило, не доказателство за внедряване.
Менюто се изчислява от backend за проверения потребител и организация;
OpenRemote остава източник за самоличност, инвентар и достъп до Обекти.
PostgreSQL пази каталога/разрешенията за услуги и версионираната структура
на менюто. Не създавай втори регистър на инвентара или дублирани права.
При липсващо право уведомявай в интерфейса; при непроверим достъп съобщавай
„Не успяхме да проверим достъпа“, не „Нямате права“. Отказ, чакаща заявка,
предстояща услуга и липсваща инфраструктура са различни състояния.
Не добавяй автоматични имейли за всеки отказ. Всички нови текстове са
в общ i18n каталог с BG/EN ключове; нов език се добавя с ресурси и регистрация.
Датите, числата и единиците използват Intl; Docusaurus пази собствената си i18n.
Разделите са точно по одобрения договор: Преглед; Обекти; Енергийни активи;
Инфраструктура; Услуги; Режим; Настройки; За нас. „Настройки → Потребители“
управлява организациите/хората/поканите/Обектите/услугите. Личните заявки са
в „Услуги“. Всяко отклонение по логика/екрани изисква ново одобрение.


## Account changes require logout / Друг акаунт само след изход — 2026-10-02

Owner removed Switch account/user from the portal. Do not restore an
in-session account-switch menu action. Use Sign out → Demo → Sign in with
the new user's email/password. Preserve existing identity mismatch guards,
logout propagation, tenant isolation and all unrelated menu/design decisions.

Собственикът премахна „Смяна на профил/потребител“. Не връщай такава опция
в активната сесия. Друг акаунт: „Изход“ → демо → „Вход“ с новия имейл/парола.
Пази проверката за чужда самоличност, изхода в другите табове и изолацията;
без други промени на менюто/дизайна.

## Ask before resolving contradictions / Питай преди разрешаване на противоречия — 2026-10-02

If an approved template, another approved screen, workflow, permission, API
contract or live state conflicts with the requested implementation, identify
the exact conflicting sources and ask the owner a concrete question before
editing the affected behavior. Recommend an option but do not select it on
the owner's behalf. A pending answer is not approval. Work may continue only
on independent, non-conflicting parts. Do not hide a missing prerequisite,
replace an approved layout, or invent a control/transition to make tests pass.
Record the question, answer and canonical template revision in HANDOFF; tests
must check that approved reference, not a newly invented implementation.
Explicit scope already approved needs no repeated permission.

При противоречие между одобрен шаблон, друг одобрен екран, логика, права,
API договор или реално състояние посочи точните източници и задай конкретен
въпрос ПРЕДИ редакция на засегнатото поведение. Предложи вариант, но не
решавай вместо собственика. Чакащ отговор не е одобрение. Продължи само
независимите непротиворечиви части. Не скривай липсваща предпоставка,
не заменяй одобрен дизайн и не измисляй контрола/преход за успешен тест.
Запиши въпроса, отговора и водещата версия на шаблона в HANDOFF; тестовете
проверяват нея, а не самостоятелно измислената реализация. Не искай повторно
разрешение за вече изрично одобрения обхват.


- For each new feature or changed workflow, require an owner-reviewed complete
  logic diagram and frontend desktop/mobile page mockup before implementation.
  Identify roles, states, notifications, errors/retries, revocation and exact
  existing menu placement; state explicitly if no UI changes. Record the
  owner's approval and exact scope in the implementation repositories first.
  Do not publish a partial or assistant-invented process as approved or live.
- Every owner-approved form/screen must be stored with its approved visual and
  a BG/EN description of placement, fields, validations, actions, role access,
  status/error/empty states and outcome. Keep proposal and live guide distinct;
  publish and link the guide from the corresponding live frontend page only
  after implementation is verified.
- За всяка нова функция/променен процес изисквай предварително прегледани от
  собственика пълна диаграма на логиката и desktop/mobile макет на страницата.
  Посочи роли, състояния, уведомления, отказ/повторен опит, отнемане и място
  в менюто; ако UI не се променя, отбележи го. Първо се записват одобрението
  и точният обхват в хранилищата за реализация. Не публикувай частичен или
  измислен от асистента процес като одобрен или работещ.
- За всяка одобрена форма/екран запази одобрения вид и BG/EN описание на
  мястото, полетата, валидациите, действията, правата, статусите/грешките и
  резултата. Разграничи предложение от работещо ръководство; публикувай и
  свържи помощта от реалния екран след проверено внедряване.

- First place each new feature's full process, role-specific desktop/mobile
  screens and form description in Git as clearly marked DRAFT documentation.
  Present that exact version to the owner. Implementation starts only after
  explicit owner approval of both the documented logic and screens. Keep draft
  specifications out of live help navigation until the implementation is
  verified; revise and re-approve changed scope.
- Първо качи пълния процес, отделните desktop/mobile екрани по роли и
  описанието на формите като ясно означена ЧЕРНОВА в Git документацията.
  Представи точно тази версия на собственика. Реализацията започва само
  след изрично одобрение на документираната логика и екраните. Не включвай
  чернова в публичната помощ преди проверено внедряване; променен обхват
  иска ново одобрение.

- Owner-approved project display name (2026-09-30): use **Antouan** in both
  Bulgarian and English project credits and new documentation. Do not invent
  titles or restore a former full name. Preserve historical Git metadata,
  existing legal notices and accurate bibliographic citations.
- Одобрено име на собственика в проекта: **Antouan** на български и английски.
  Не връщай старото пълно име или титли. Запазвай историята на Git,
  съществуващите правни бележки и точните библиографски цитати.

- Approved target (2026-09-29): all verified members see five service catalog
  entries. Only day-ahead (one selected country/zone, BG initially) and
  visualisations are independently requestable; analysis, meteorology and
  forecasting are Coming soon. Platform admin grants organisation and zone;
  organisation admin grants individual member. Requests grant nothing. A BG
  Grafana price dashboard needs **both** services and BG scope. Document
  target versus currently deployed features separately in BG and EN; never
  state that customer prices or embedded Grafana are live until verified.
- Одобрената цел: каталог с пет услуги, но само „Ден напред“ (един избор,
  първоначално BG) и „Графики“ са отделно заявяеми. Заявката не дава достъп;
  супер администраторът разрешава организация/зона, после нейният администратор
  конкретен член. BG ценов график изисква и двете услуги и BG зона. Ясно
  различавай одобрения процес от реално публикуваните функции на BG и EN.

- Market country policy (owner, 2026-09-29): BG is the sole default collected
  zone. Platform administrator explicitly enables any other collection zone
  and separately grants collected zones to organisations. Service, zone and
  member permissions are distinct. Historical foreign rows may remain; no
  new foreign collection is allowed by default. The later owner decision
  permits only a guarded embedded BG price dashboard, not a standalone public
  Grafana login or unrestricted tenant datasource. State current verification
  status accurately in BG/EN.
- За пазара само BG се събира по подразбиране. Други зони и организационни
  права се включват поотделно от супер администратора. Старите чужди записи
  не се трият автоматично. По-късното решение допуска само защитен вграден
  BG ценови dashboard, но не и публичен самостоятелен Grafana вход или
  неограничен източник на клиентски данни.

- Before documenting or publishing a new feature, control, role, device choice
  or automatic workflow, verify the owner's exact approval. If it is not
  explicitly approved, ask a concrete question and wait for confirmation;
  do not turn an assistant suggestion into product behavior. Device selection
  belongs in GrideX frontend and authoritative inventory in OpenRemote.
- Преди описание или публикуване на нова функция, контрола, роля, избор на
  устройство или автоматичен процес провери изричното одобрение на собственика.
  Ако липсва, задай конкретен въпрос и изчакай потвърждение. Изборът е в
  GrideX frontend, а единственият основен инвентар е OpenRemote.
- Communicate with the owner in Bulgarian. Keep BG and EN guide content in
  parity; do not publish one locale with stale or contradictory instructions.
- Every new or edited public guide, help answer, menu explanation and workflow
  MUST have an English version in the same change, not as a later task. Update
  both `docs/` (BG) and its matching
  `i18n/en/docusaurus-plugin-content-docs/current/` page (EN), including
  labels, links and current availability. If either locale is missing or stale,
  the documentation is unfinished: do not merge, deploy or mark the task done.
  Verify both public URLs after publication.
- Всяка нова или редактирана публична страница, отговор в помощта, обяснение
  на меню и процес ЗАДЪЛЖИТЕЛНО има английска версия в същата промяна. Ако
  BG или EN липсва или е остарял, не сливай, не публикувай и не обявявай
  задачата за завършена; след публикация провери и двата адреса.
- This is the public help site for `gridex.tech`, not an independent product.
  Preserve the approved portal's deep-green, lime, card and rounded-control
  visual language. Use typed Docusaurus config, components and theme overrides
  in `src/`; do not replace the portal navigation from this repository.
- The owner approved the current responsive documentation design on
  2026-09-27. Treat it as the baseline for every new or revised page; do not
  replace its visual system without the owner's approval.
- For every new or revised user-facing question, workflow, menu or feature,
  update the corresponding section of this documentation in the same work and
  publish the guide with the implementation. Keep Bulgarian and English in
  sync. If the feature is not live or cannot be verified, say so explicitly in
  that section; do not present planned behavior as operational.
- Never put credentials, private IPs, client/device identifiers, internal
  runbooks or unaudited operational claims on this public site. Mark generated
  or illustrative imagery as such; never imply it shows a real customer Site.
- A guide is “ready” only after its workflow, roles and screen have been
  checked against the live implementation. Otherwise use the honest
  `coming-soon` destination. Real and demo data must remain distinct.
- For every change run `npm run typecheck` and `npm run build`; verify BG/EN
  routes and mobile/desktop layout. Deploy with `sh scripts/deploy-local.sh`,
  never with a bare build, because the live read-only Docker mount must be
  recreated after Docusaurus replaces `build/`. Verify that the live proxy
  serves CSS as `text/css` and JavaScript as a JavaScript MIME type; HTML 200
  alone does not prove the site renders with `nosniff` enabled.
- The docs certificate was issued manually with DNS-01 and is not on automatic
  renewal. See README for its expiration and the required follow-up.
