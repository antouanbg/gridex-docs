---
id: market-prices
title: Market — day-ahead prices
hide_title: true
description: Service permissions and ENTSO-E provider status.
---

import DocsHero from '@site/src/components/DocsHero';
import GuideNotice from '@site/src/components/GuideNotice';

<DocsHero
  compact
  eyebrow="GRIDEX · MARKET"
  title="Electricity prices"
  description="A protected hourly price archive with explicit rights for each organisation and user."
  imageAlt="Illustrative image of solar panels and energy infrastructure"
  primaryHref="#access"
  primaryLabel="Who has access"
  secondaryHref="https://gridex.tech/market/"
  secondaryLabel="Open Market"
/>

<GuideNotice label="Archive and portal published; acceptance testing pending" tone="amber">
  <p>Live ENTSO-E hourly records have been verified in a separate TimescaleDB. Country controls are published in the portal, but still await acceptance verification with real roles. Demo data are not live prices.</p>
</GuideNotice>

## Who has access? {#access}

The approved future catalogue treats **Day-ahead prices** and
**Visualisations** as two separate services. A price request selects exactly
one country/bidding zone; **Bulgaria/BG** will be the only initial choice.
Users will request a service under Profile → Services, but a request itself
never unlocks data. Organisation and platform administrators will see its
stages under Users & invitations → Service requests. A BG price chart will
require both individual service grants and BG organisation zone scope. The
**request flow** is not implemented yet; the guarded embedded dashboard is a
separate capability.

The platform administrator enables **Day-ahead** for an active organisation. This **does not** enable any of its users automatically. The organisation administrator then enables it individually for approved members. Revoking the organisation grant removes all member grants; restoring the organisation grant does not restore them.

## Which countries are collected?

**Only Bulgaria (BG)** is fetched and stored by default. The platform administrator manages bidding-zone collection in **Market → Price collection by country**. Another zone is fetched and retained only after explicit confirmation there. Disabling collection stops new writes but preserves history. Earlier test records for other zones may remain in the protected archive; they do not mean collection is active.

After enabling the service for an organisation, the platform administrator may separately grant one of the collected zones under **Customers and contracts → Users and invitations → organisation → Day-ahead countries**. This does not enable any of its members or disclose price values. New customers receive no country automatically.

The service is hidden from a member's live menu until they receive an individual grant. Day-ahead permission alone does not disclose price values: BG charts also need Visualisations and an organisation BG grant. Provider status remains restricted to the platform administrator.

The full price archive and direct API remain **platform-administrator-only**. In the live **Market** section (`gridex.tech/market/`), that administrator also sees ENTSO-E API status and the time of the last successful refresh. A customer with both individual grants and organisation BG scope may open only the restricted BG charts. Demo data remain separate.

## How are prices retained?

The market worker retrieves ENTSO-E A44 and stores complete hourly prices per bidding zone in a separate TimescaleDB with no automatic deletion policy. When the source publishes 15-minute prices, the hourly value is the mean of **four complete consecutive intervals** and is labelled as aggregated; an incomplete hour is not stored as a real price. UTC identifies both local hours during a daylight-saving transition. Each zone/hour is retained once, not copied for every customer.

Prices are in **EUR/MWh**. They are wholesale prices, not a customer's final contracted tariff; grid fees, taxes and markups are excluded. Negative prices are valid, and an unpublished day is never replaced by zero.

Using these prices for automatic battery control is a separate, not-yet-activated workflow requiring explicit approval and safety limits.

## Grafana visualisations

The BG dashboard shows Bulgarian hourly prices in GrideX dark-green and lime chart colours. Open it inside the portal from **Market → Open charts** through a short-lived one-time launch. The backend rechecks session and permissions on every request; there is no standalone public Grafana login. Its separate database role can read BG-only views, not the full archive. Future OpenRemote/Site visualisations need a separate source and organisation/Site isolation. Real customer-role browser acceptance testing is still pending.

The image above is **illustrative**, not a real customer Site.
