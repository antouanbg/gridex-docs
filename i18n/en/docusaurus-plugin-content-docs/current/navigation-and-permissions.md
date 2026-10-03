---
title: Navigation, services and permissions
sidebar_position: 2
---

# Navigation, services and permissions

> Approved structure, implementation in progress. This describes the contract,
> not confirmation that every screen has already been deployed.

## Sections

| Section | Subsections |
| --- | --- |
| Overview | Home screen |
| Sites | Your accessible Sites and related data |
| Energy assets | Battery; Inverter; Charging station; Consumer and load |
| Infrastructure | One screen, no submenus |
| Services | Day-ahead prices; Graphs and visualisations; Analysis; Meteorology; Forecasting |
| Mode | Logic; Schedule; Alarm |
| Settings | Users; Plan and subscription; Market; Profile |
| Settings — Market | Tariff and settlement; Balancing |
| Settings — Profile | Documentation |
| About us | Information and enquiries |

## Services {#services}

Everyone can see the catalogue. Only day-ahead prices and graphs are requestable.
The other three services are coming soon. The platform administrator enables a
service for an organisation; its administrator enables it individually for each
member, including themselves. Administrators may grant without a prior request.
A request itself grants no access. A price graph requires prices, graphs and an
authorised price zone.

Personal requests and grants belong in Services. Administrative decisions belong
in Settings — Users. The platform administrator does not request their own access.

## Administration {#administration}

One Users page contains organisations/people within the administrator's authority,
invitations, roles, Site assignments and services. The table has five columns:
Name/email, Role, Sites, Services, Actions. Details expand; mobile rows become cards.
A menu selection does not grant authority.

Tariffs and the electricity distribution contract are entered by the platform
administrator or the relevant organisation administrator. Moving a section does
not imply approval of new fields or write permissions.

## Inventory {#inventory}

OpenRemote remains authoritative for Sites, assets and infrastructure. ROCK Pi,
ESP, meters, routers, controllers, gateways, sensors and cloud connectors are
infrastructure, not energy assets. A catalogue does not prove compatibility or
an operational driver.

Asset subsections appear when accessible assets of that type are registered.
Temporarily offline assets remain visible. Demo shows all four types using sample
data. A Site with energy assets requires at least one infrastructure component.

## Access feedback

- **Not permitted:** verification succeeded but access has not been granted.
- **Awaiting approval:** a request exists; it does not yet grant access.
- **Coming soon:** the feature is not active yet.
- **Infrastructure missing:** the required prerequisite is not registered.
- **Could not verify access:** a temporary failure, not proof of revoked access.

Navigation is loaded for the current identity. Every action is independently
authorised on the server. No other user's data or demo substitute is shown.

## Languages

Bulgarian and English use matching translation keys. Menu labels are not
permission identifiers. A new language requires a complete catalogue,
registration and tests; geolocation is not proof of language preference.
Documentation uses Docusaurus i18n.
