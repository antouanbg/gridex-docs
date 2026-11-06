# GrideX public documentation

## Customer PDF specification / Клиентска PDF спецификация

Edition 4.0, 6 November 2026: two separate 35-page documents with a linked
contents page and approved example screens for the three account roles.

- [Български PDF](static/downloads/GrideX_Full_Product_Specification_BG_2026-11_v4.pdf)
- [English PDF](static/downloads/GrideX_Full_Product_Specification_EN_2026-11_v4.pdf)

Пълен продуктов обхват: Обекти, активи, инфраструктура, услуги и права,
стратегии, пазарни цени, икономика, прогнозиране и проектни разширения.
Изображенията са одобрените примерни макети от тази документация,
с примерни самоличности, а не нови снимки от клиентски акаунти.
Английската версия има английски текст и пояснения; референтните екрани
запазват оригиналния български интерфейс. Активираните модули се определят
от клиентската конфигурация и договора.

Full product scope covers Sites, assets, infrastructure, services/access,
strategies, market prices, economics, forecasting and project extensions.
Screens are the approved reference mockups with example identities, not
new captures of customer accounts. The English edition has English prose
and captions; screenshots retain the original Bulgarian interface.
Activated modules depend on customer configuration and contract.

Authoring sources: `scripts/customer-pdf/`. Install Python packages
`reportlab` and `Pillow`, and DejaVu Sans regular/bold fonts. Set
`GRIDEX_PDF_FONT_DIR` if fonts are not under `/usr/share/fonts/truetype/dejavu`,
then run `python3 scripts/customer-pdf/build_full_spec.py` from the repository.
Output goes to `static/downloads/`. Render and inspect both PDFs after edits;
keep both locales in the same release. Git publication is separate from
deploying the documentation website.

Separate public Docusaurus site for `https://doc.gridex.tech`. Bulgarian is
the default locale; English pages live under `/en/`. Build with `npm ci &&
npm run build`. The static `build/` output is served by a read-only container
on the existing private Docker ingress network; only the existing HTTPS proxy
may expose it publicly. Do not publish private runbooks, credentials, live
device identifiers or infrastructure addresses in this repository.
The source repository is `https://github.com/antouanbg/gridex-docs`.

The BG/EN Market guide documents the current country collection policy:
only BG is enabled by default; additional zones and organisation rights need
explicit platform-administrator action. The BG-only Grafana price dashboard
is embedded from the live Market screen through a guarded one-time launch;
there is no standalone Grafana login. Customer access needs both individual
Day-ahead and Visualisations grants plus organisation BG scope. The direct
price archive API remains platform-administrator-only. The service-request
screen and Site charts are not implemented yet.

For subsequent content deployments run `sh scripts/deploy-local.sh` on the Mac.
Do not run `npm run build` alone against the live container: Docusaurus replaces
the `build/` directory and Docker retains the old bind mount, resulting in 404
until the docs service is recreated. The script rebuilds, recreates only the
docs service and checks both locales through local HTTPS.

The public-facing design follows the GrideX portal's deep green, lime accent,
card and rounded-control language. `docusaurus.config.ts`, `src/components/`
and `src/theme/` contain typed configuration, content and theme components;
run `npm run typecheck` before publication. The solar-site hero image is an
original generated illustration, **not a photograph of a customer Site**.
The final prompt was: “an original editorial photograph of a modern solar
energy site with panels, a distant control building, deep forest-green and
sage palette, early morning light, negative space for a heading, no people,
logos, text or watermark.” It was generated with the built-in image tool and
saved as `static/img/solar-hero.jpg`.

The proxy uses a separate trusted certificate for `doc.gridex.tech`; existing
API, auth and Manager TLS routes remain unchanged. `docs/coming-soon.md` is the
honest destination for sections whose user documentation has not been verified
yet. Do not present placeholder chapters as completed guidance.

The first certificate was issued with a manual DNS-01 challenge on 2026-09-26
and expires 2026-12-25. **It is not automatically renewed.** Before expiry,
repeat DNS validation, deploy the replacement using the backend's
`scripts/deploy-public-docs.py`, and verify the live certificate and BG/EN
pages. This is an operational task, not a background renewal promise.
