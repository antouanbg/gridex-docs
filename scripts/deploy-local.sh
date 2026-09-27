#!/bin/sh
# Rebuild the static documentation and rebind its read-only container mount.
set -eu

root=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
cd "$root"
npm ci
npm run typecheck
npm run build

# Docusaurus replaces build/ on each build. The running container retains its
# old bind mount until recreated; restart it immediately after a successful build.
LOCAL_UID=$(id -u) LOCAL_GID=$(id -g) \
  docker-compose -f "$root/compose.yml" --project-directory "$root" \
  up -d --no-deps --force-recreate docs-site

curl --fail --silent --show-error --noproxy '*' \
  --resolve doc.gridex.tech:14443:127.0.0.1 \
  https://doc.gridex.tech:14443/organisations-and-access/ -o /dev/null
curl --fail --silent --show-error --noproxy '*' \
  --resolve doc.gridex.tech:14443:127.0.0.1 \
  https://doc.gridex.tech:14443/en/organisations-and-access/ -o /dev/null

# A 200 HTML response is insufficient: browsers refuse CSS/JS served as
# text/plain when X-Content-Type-Options: nosniff is enabled.
css_asset=$(grep -o 'href="/assets/css/[^"]*"' build/index.html | head -n 1 | cut -d '"' -f 2)
js_asset=$(grep -o 'src="/assets/js/[^"]*"' build/index.html | head -n 1 | cut -d '"' -f 2)
test -n "$css_asset" && test -n "$js_asset"
curl --fail --silent --show-error --noproxy '*' \
  --resolve doc.gridex.tech:14443:127.0.0.1 \
  -I "https://doc.gridex.tech:14443$css_asset" | tr -d '\r' | grep -iq '^content-type: text/css'
curl --fail --silent --show-error --noproxy '*' \
  --resolve doc.gridex.tech:14443:127.0.0.1 \
  -I "https://doc.gridex.tech:14443$js_asset" | tr -d '\r' | grep -Eiq '^content-type: (application|text)/javascript'
echo GRIDEX_DOCS_DEPLOYED
