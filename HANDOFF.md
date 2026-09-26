# GrideX documentation handoff

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
external browser acceptance of this *new visual revision* remains. The docs
Git repository currently has no remote.

Remaining: publish additional guide topics only after their related portal
screens and permissions are verified. The certificate remains manually
renewed; expiry and procedure are in README.
