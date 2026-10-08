---
title: Navigation, services and permissions
sidebar_position: 2
---

# Navigation, services and permissions

Binding visual reference: [the three approved Users screens](./approved-users-screens.md).

> Current approved matrix. Navigation and the Users screens are published; the demo follows the 27 catalogue entries. This does not mean that future services and operational forms are implemented. Limitations are stated below.

Quick links: [menus](#menu-matrix) · [roles and actions](#role-actions) · [service requirements](#service-access) · [authoritative sources](#authority-matrix).

## Overview {#overview}

The landing screen summarises the selected authorised Site. Demo uses sample
data; after sign-in missing measurements remain unverified, never zero or demo.
Invalid quality means No valid data. With no Site, ask the administrator for
access; connected infrastructure is under Infrastructure.

## Profile {#profile}

Settings → Profile displays verified identity, role and email notification
preference. Notification consent covers supported events and is not a service
grant. A saved preference does not prove delivered mail. Sign out returns to Demo;
another account signs in after logout. Never enter passwords in an enquiry form.

## Plan and subscription {#plans}

Settings → Plan and subscription is an administrative section. The current live
screen has no complete billing or plan editor and explains the missing integration.
Demo content is not an active contract. Grant services in Settings → Users;
personal requests belong in Services.

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

Site cards list registered assets and infrastructure from verified OpenRemote
inventory and personal service grants for the same organisation. Failed
verification is distinct from a confirmed empty list. A service grants no extra
Site or measurement access. Platform administrators need no self-approval,
but customer data is not automatically accessible.
Repeated records for one source/metric show the latest valid measurement.
Different sources are never merged; repeated metric labels identify their source.
Memory uses MiB and uptime uses hours.

OpenRemote may show browser registrations such as Chrome or Opera Mobile.
These are console resources, not energy assets or GrideX infrastructure.
They are not automatically deleted; their presence alone does not prove foreign access.

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

## Final navigation matrix {#menu-matrix}

Approved target matrix, 2026-10-03. Visibility is not write authority.
Demo contains sample data without real actions. Member includes Viewer,
Operator, Energy manager and Integrator. Every action needs its role,
authorised Site and service; menu visibility alone is insufficient.

| Section — subsection | Role / condition | Account type | Data and description |
| --- | --- | --- | --- |
| Overview | Authorised data only | All + demo | Home after sign-in |
| Sites | Admin creates; members see linked Sites | All + demo | Sites, available assets and authorised services; no separate Site Visualisations menu |
| Energy assets | Site access and registered assets | All + demo | Registered inventory; offline does not mean absent |
| Energy assets — Battery | Registered accessible battery | All + demo | Storage |
| Energy assets — Inverter | Registered accessible inverter | All + demo | Production |
| Energy assets — Charging station | Registered accessible station | All + demo | Charging |
| Energy assets — Consumer and load | Registered accessible load | All + demo | Consumption; catalogue does not prove a working driver |
| Infrastructure | Authorised Site; writes require existing permission | All + demo | One page: ROCK Pi, ESP, meter, router, controller, gateway, sensor, cloud connector |
| Services | Everyone sees catalogue | All + demo | Personal requests/grants; administration in Settings — Users |
| Services — Day-ahead prices | Platform admin or organisation + member grant + zone | Authorised live accounts; demo sample | BG only by default; full archive API remains platform-only |
| Services — Graphs and visualisations | Platform admin or organisation + member grant; always an authorised source | Authorised live accounts; demo sample | Platform admin sees only already-authorised Sites. Customer price graphs need Prices + Graphs + zone |
| Services — Analysis | Coming soon, not requestable | All | Does not activate unfinished features |
| Services — Meteorology | Coming soon, not requestable | All | Future service |
| Services — Forecasting | Coming soon, not requestable | All | Future service |
| Mode | Authorised Site and existing action permission | By permissions; demo | Does not automatically permit physical commands |
| Mode — Logic | Existing role/Site checks | By permissions; demo | No new rights inferred from menu |
| Mode — Schedule | Existing role/Site checks | By permissions; demo | Physical safeguards preserved |
| Mode — Alarm | Authorised data only | By permissions; demo | New editing permissions remain unresolved |
| Settings | Children filtered by permission | All + demo | Container, not general administrative authority |
| Settings — Users | Platform / organisation admin | Admins; demo mockup | One page for organisations, people, invitations, roles, Sites and services |
| Settings — Plan and subscription | Administrative scope | Admins; demo | Plan never auto-grants personal services |
| Settings — Market | Platform / organisation admin | Admins; demo | Market configuration, not personal price service |
| Settings — Market — Tariff and settlement | Platform / own organisation admin | Admins; demo | Tariff and distribution contract; full fields/validation pending |
| Settings — Market — Balancing | Administrative section | Admins; demo | New operational permissions are not approved |
| Settings — Profile | Current user only | All + demo | Personal data and preferences |
| Settings — Profile — Documentation | Everyone | All | Contextual BG/EN help |
| About us | Everyone | All | Information and protected enquiry |

Live asset categories require registered accessible assets. Demo shows all four.
PV installation and Thermal system are not destinations. At least one
infrastructure component is required for a Site with energy assets.

## Responsibility and OpenRemote matrix {#authority-matrix}

| Resource / decision | Managed by | Authoritative source |
| --- | --- | --- |
| Organisation / separate realm | Platform admin through GrideX | OpenRemote / Keycloak; business state and binding in GrideX |
| User / first and last name / identity | Invitation and verified registration | Keycloak; never invent missing names |
| Role / membership | Admin within authorised scope | GrideX permissions checked against realm/membership |
| Site | Administrator creates, not ordinary member | OpenRemote Site/Asset |
| Member — Site | Admin links specific person and Site | OpenRemote links; GrideX orchestrates and verifies |
| Asset / infrastructure | Authorised GrideX operations | OpenRemote Assets, parents, attributes and relationships |
| Device commissioning | Currently organisation admin; verified platform actions separately | GrideX orchestration, OpenRemote inventory, Edge safeguards |
| Organisation service / price zone | Platform admin | GrideX PostgreSQL catalogue and grants |
| Personal service, including admin | Organisation admin | Separate personal grant in GrideX PostgreSQL |
| Menu / order / prerequisite / translation key | Versioned approved matrix | PostgreSQL catalogue; known pages and BG/EN resources remain in code |
| Human OpenRemote Manager | Read-only, including administrators | OpenRemote permissions and protected GrideX entry |
| Backend service client | Separate per organisation, its realm only | Backend-only identity, not human login |

## Roles and actions {#role-actions}

This table describes scope; it grants no new rights. Each operation independently checks identity, organisation and Site on the server.

| Action | Platform administrator | Organisation administrator | Member |
| --- | --- | --- | --- |
| Organisations | Approve, invite, suspend within global scope | Own organisation only; cannot create another | No administrative access |
| People, roles and Sites | View within global administrative scope | Manage own people and link permitted Sites | View linked Sites only; cannot create a Site |
| Organisation service and price zone | Grant/revoke for a selected active organisation | Request from platform admin; cancel own pending request | Cannot request for the organisation |
| Individual service grant | No self-approval; does not replace the organisation level for individual grants | Grant/revoke per approved person, including self | Request from own admin; cancel own request or stop own service |
| Device commissioning | Explicitly supported global actions only | Organisation administrator | Not by default, including Integrator |
| OpenRemote Manager | Protected entry, read-only human account | Same, limited to own realm | No administrative launch from this screen |

Member includes Viewer, Operator, Energy manager and Integrator. Viewer is
read-only. Other roles do not automatically receive every action, service or
Site: separate server checks apply. Undefined operational rights are not granted.

## Service requirements {#service-access}

| What I want to view | Required rights / state |
| --- | --- |
| Catalogue and personal requests | Verified member; prior service approval is not required |
| BG price chart | Organisation: Prices + Charts + BG zone; person: individual Prices + individual Charts |
| Site measurements and charts | Platform admin without a personal grant, or organisation and person: Graphs; always access to the exact OpenRemote Site and measurements |
| Full price archive and ENTSO-E status | Platform administrator only; customer chart permission does not provide this |
| Analysis, Meteorology, Forecasting | Coming soon; not requestable or enabled as live services |

**Location:** catalogue and personal requests belong in **Services**; decisions
for organisations and people belong in **Settings → Users**. **Settings → Market**
holds tariff/contract and balancing settings, not personal wholesale prices.
The platform administrator finds country-collection controls under
**Services → Day-ahead prices**; collection and customer permissions are separate.

## Approval and revocation {#approval-flow}

1. Platform admin selects an approved active organisation and grants a service, including the price zone.
2. Organisation admin also sees unapproved services and requests/cancels their request to platform admin.
3. Organisation admin grants an available service to an approved member, including themselves, even without a prior request.
4. Member requests their admin. The request is visible at the appropriate administrative level and a notification is sent; admin approves or rejects.
5. Access takes effect after the administrative action — no second service Accept step.
6. Organisation revocation removes personal grants; re-enabling does not restore them automatically.

Platform admin does not request personal services; this does not automatically
open foreign inventory in Manager. Registration invitations are separate from
services. Accepted membership does not expire with its old email link. Member
table has five columns: Name/email, Role, Sites, Services, Actions, with
expandable details/mobile cards.
See [Organisations, invitations and permissions](./organisations-and-access.md).

## Verification boundary

This matrix records final structural decisions, not a claim that every future
service, driver or financial form is implemented. Unresolved permissions are
not broadened. Full migration of legacy text to i18n and live-screen acceptance
with real roles remain separate checks.

## Languages

Bulgarian and English use matching translation keys. Menu labels are not
permission identifiers. A new language requires a complete catalogue,
registration and tests; geolocation is not proof of language preference.
Documentation uses Docusaurus i18n.
