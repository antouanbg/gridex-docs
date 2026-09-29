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

<GuideNotice label="The archive works; the portal update is not yet published" tone="amber">
  <p>Live ENTSO-E hourly records have been verified in a separate TimescaleDB. The permissions and new portal screen still await deployment and acceptance testing; demo data are not live data.</p>
</GuideNotice>

## Who has access? {#access}

The platform administrator enables **Day-ahead** for an active organisation. This **does not** enable any of its users automatically. The organisation administrator then enables it individually for approved members. Revoking the organisation grant removes all member grants; restoring the organisation grant does not restore them.

The service is hidden from a member's live menu until they receive an individual grant. Even after that grant, they cannot see price values or provider status at this stage.

For now, **price values and the archive are platform-administrator-only**. Even a member grant does not disclose prices until customer publication is separately approved. In the live **Market** section (`gridex.tech/market/`), the platform administrator sees only ENTSO-E API status and the time of the last successful refresh. Demo data remain separate.

## How are prices retained?

The market worker retrieves ENTSO-E A44 and stores complete hourly prices per bidding zone in a separate TimescaleDB with no automatic deletion policy. When the source publishes 15-minute prices, the hourly value is the mean of **four complete consecutive intervals** and is labelled as aggregated; an incomplete hour is not stored as a real price. UTC identifies both local hours during a daylight-saving transition. Each zone/hour is retained once, not copied for every customer.

Prices are in **EUR/MWh**. They are wholesale prices, not a customer's final contracted tariff; grid fees, taxes and markups are excluded. Negative prices are valid, and an unpublished day is never replaced by zero.

Using these prices for automatic battery control is a separate, not-yet-activated workflow requiring explicit approval and safety limits.

The image above is **illustrative**, not a real customer Site.
