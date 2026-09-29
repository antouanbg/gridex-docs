# GrideX public documentation rules

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
