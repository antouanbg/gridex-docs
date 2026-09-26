# GrideX public documentation rules

- Communicate with the owner in Bulgarian. Keep BG and EN guide content in
  parity; do not publish one locale with stale or contradictory instructions.
- This is the public help site for `gridex.tech`, not an independent product.
  Preserve the approved portal's deep-green, lime, card and rounded-control
  visual language. Use typed Docusaurus config, components and theme overrides
  in `src/`; do not replace the portal navigation from this repository.
- Never put credentials, private IPs, client/device identifiers, internal
  runbooks or unaudited operational claims on this public site. Mark generated
  or illustrative imagery as such; never imply it shows a real customer Site.
- A guide is “ready” only after its workflow, roles and screen have been
  checked against the live implementation. Otherwise use the honest
  `coming-soon` destination. Real and demo data must remain distinct.
- For every change run `npm run typecheck` and `npm run build`; verify BG/EN
  routes and mobile/desktop layout. Deploy with `sh scripts/deploy-local.sh`,
  never with a bare build, because the live read-only Docker mount must be
  recreated after Docusaurus replaces `build/`.
- The docs certificate was issued manually with DNS-01 and is not on automatic
  renewal. See README for its expiration and the required follow-up.
