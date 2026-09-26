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
echo GRIDEX_DOCS_DEPLOYED
