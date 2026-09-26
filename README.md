# GrideX public documentation

Separate public Docusaurus site for `https://doc.gridex.tech`. Bulgarian is
the default locale; English pages live under `/en/`. Build with `npm ci &&
npm run build`. The static `build/` output is served by a read-only container
on the existing private Docker ingress network; only the existing HTTPS proxy
may expose it publicly. Do not publish private runbooks, credentials, live
device identifiers or infrastructure addresses in this repository.

The proxy uses a separate trusted certificate for `doc.gridex.tech`; existing
API, auth and Manager TLS routes remain unchanged. `docs/coming-soon.md` is the
honest destination for sections whose user documentation has not been verified
yet. Do not present placeholder chapters as completed guidance.

The first certificate was issued with a manual DNS-01 challenge on 2026-09-26
and expires 2026-12-25. **It is not automatically renewed.** Before expiry,
repeat DNS validation, deploy the replacement using the backend's
`scripts/deploy-public-docs.py`, and verify the live certificate and BG/EN
pages. This is an operational task, not a background renewal promise.
