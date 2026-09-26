# GrideX public documentation

Separate public Docusaurus site for `https://doc.gridex.tech`. Bulgarian is
the default locale; English pages live under `/en/`. Build with `npm ci &&
npm run build`. The static `build/` output is served by a read-only container
on the existing private Docker ingress network; only the existing HTTPS proxy
may expose it publicly. Do not publish private runbooks, credentials, live
device identifiers or infrastructure addresses in this repository.

For subsequent content deployments run `sh scripts/deploy-local.sh` on the Mac.
Do not run `npm run build` alone against the live container: Docusaurus replaces
the `build/` directory and Docker retains the old bind mount, resulting in 404
until the docs service is recreated. The script rebuilds, recreates only the
docs service and checks both locales through local HTTPS.

The proxy uses a separate trusted certificate for `doc.gridex.tech`; existing
API, auth and Manager TLS routes remain unchanged. `docs/coming-soon.md` is the
honest destination for sections whose user documentation has not been verified
yet. Do not present placeholder chapters as completed guidance.

The first certificate was issued with a manual DNS-01 challenge on 2026-09-26
and expires 2026-12-25. **It is not automatically renewed.** Before expiry,
repeat DNS validation, deploy the replacement using the backend's
`scripts/deploy-public-docs.py`, and verify the live certificate and BG/EN
pages. This is an operational task, not a background renewal promise.
