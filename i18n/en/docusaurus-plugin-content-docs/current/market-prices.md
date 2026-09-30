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
  description="A protected native-resolution price archive with explicit rights for each organisation and user."
  imageAlt="Illustrative image of solar panels and energy infrastructure"
  primaryHref="#access"
  primaryLabel="Who has access"
  secondaryHref="https://gridex.tech/market/"
  secondaryLabel="Open Market"
/>

<GuideNotice label="Archive and portal published; acceptance testing pending" tone="amber">
  <p>Live ENTSO-E records have been verified in a separate TimescaleDB. Country controls are published in the portal, but still await acceptance verification with real roles. Demo data are not live prices.</p>
</GuideNotice>

## Who has access? {#access}

**Day-ahead prices** and **Visualisations** are separate services. For now,
only **Bulgaria/BG** can be requested under Profile → Services. A request
does not unlock data. Administrators see its stages under Users & invitations
→ Service requests. A BG price chart requires both individual service grants
and the organisation's BG zone scope.

The platform administrator enables **Day-ahead** for an active organisation. This **does not** enable any of its users automatically. The organisation administrator then enables it individually for approved members. Revoking the organisation grant removes all member grants; restoring the organisation grant does not restore them.

## Which countries are collected?

**Only Bulgaria (BG)** is fetched and stored by default. The platform administrator manages bidding-zone collection in **Market → Price collection by country**. Another zone is fetched and retained only after explicit confirmation there. Disabling collection stops new writes but preserves history. Earlier test records for other zones may remain in the protected archive; they do not mean collection is active.

After enabling the service for an organisation, the platform administrator may separately grant one of the collected zones under **Customers and contracts → Users and invitations → organisation → Day-ahead countries**. This does not enable any of its members or disclose price values. New customers receive no country automatically.

The service is hidden from a member's live menu until they receive an individual grant. Day-ahead permission alone does not disclose price values: BG charts also need Visualisations and an organisation BG grant. Provider status remains restricted to the platform administrator.

The full price archive and direct API remain **platform-administrator-only**. In the live **Market** section (`gridex.tech/market/`), that administrator sees the last API check and the last complete dataset separately. A customer with both individual grants and organisation BG scope may open only the restricted BG charts. Demo data remain separate.

## How are prices retained?

The market worker checks ENTSO-E A44 **once per hour** until the complete next-day dataset is published. One request returns a day's intervals; it does **not** mean a new price is formed every hour. Bulgaria has **15-minute** day-ahead market time units from 1 October 2025: normally 96 values per day, or 92/100 at a daylight-saving change. Native intervals are retained in a separate TimescaleDB without automatic deletion. A mean of four complete consecutive intervals remains available only for hourly compatibility. Older hourly history is not expanded into fabricated quarter-hour values. The archive is per zone, not duplicated per customer.

Prices are in **EUR/MWh**. They are wholesale prices, not a customer's final contracted tariff; grid fees, taxes and markups are excluded. Negative prices are valid, and an unpublished day is never replaced by zero.

Using these prices for automatic battery control is a separate, not-yet-activated workflow requiring explicit approval and safety limits.

## Grafana visualisations

The BG dashboard shows native Bulgarian 15-minute prices; older hourly history remains hourly. Open it inside the portal from **Market → Show selected period** through a short-lived one-time launch. Choose **Today and tomorrow**, the last 48 hours, 7 or 30 days, or **Choose dates** for up to 31 consecutive delivery days. Custom dates run from midnight to midnight in Bulgaria time, including the last selected day and accounting for daylight saving. Changing the chart range does not change stored prices. The backend rechecks session and permissions on every request; there is no standalone public Grafana login. Its separate database role can read BG-only views, not the full archive. Future OpenRemote/Site visualisations need a separate source and organisation/Site isolation. Real customer-role browser acceptance testing is still pending.

### Which day do the prices apply to?

“Day-ahead” means a price for electricity delivered on the indicated date, determined in the previous day's auction. The chart's time axis shows the **delivery date and interval in Bulgaria (Europe/Sofia)**, not when you opened the page. The initial short view covers the past 24 hours and next 36 hours; a future interval appears only if ENTSO-E has published a price for it. **“Last successful refresh”** and **“Latest interval with a price”** identify when data were received and the latest actual BG delivery interval respectively, independently of the chart range.

**“Last check”** is the latest API request; **“Last complete day received”** is the latest complete dataset GrideX obtained. Neither is the delivery date. Before the next day's auction is published, ENTSO-E may return only some intervals. Today's complete prices remain available, but an incomplete next day is not used for planning or filled with zeroes or today's prices. Sources: [ESO — launch of 15-minute day-ahead trading](https://www.eso.bg/doc?news=883), [ENTSO-E Transparency Platform](https://transparency.entsoe.eu/).

The image above is **illustrative**, not a real customer Site.
