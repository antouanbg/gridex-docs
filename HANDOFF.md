# GrideX documentation handoff

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
