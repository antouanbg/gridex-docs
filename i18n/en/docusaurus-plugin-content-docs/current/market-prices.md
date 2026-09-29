---
id: market-prices
title: Market — day-ahead prices
description: Choosing a country, bidding zone and market product in GrideX.
---

## Where are prices shown?

After signing in, open **Market** (`gridex.tech/market/`). This is the existing section; no new top-level menu is added. Demo mode uses sample values. A live account must show only actually published prices or an explicit unavailable/not-published state.

## How do I choose a market?

1. Select a **country** and **bidding zone**. A country may have more than one zone; browser language or IP location does not silently select the zone.
2. Select the market product. The first release supports **Day-ahead** only. Intraday and balancing products are not shown as available.
3. Select a date. The chart and table use the bidding zone's local time while retaining exact UTC instants. A local hour can repeat at a daylight-saving transition.

Prices come from the **ENTSO-E Transparency Platform**, A44 document, in **EUR/MWh**. These are wholesale prices, not a customer's final purchase or export tariff. Grid fees, taxes and contract markups are excluded. Negative prices are valid; a day without published data is not replaced by zero. A partial day is explicitly labelled and must not be used for automatic planning.

> **Status:** the new live integration is prepared in code. Until the backend service, provider token and public deployment are verified, do not treat the screen as an active price source.

Using these prices for automatic battery control is a separate, not-yet-activated workflow requiring explicit approval and safety limits.
