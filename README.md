# GrideX public documentation

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
