---
id: organisations-and-access
slug: /organisations-and-access/
title: Organisations, invitations and rights
hide_title: true
description: Who can invite, how invitations are accepted and how Site access is granted.
---

import DocsHero from '@site/src/components/DocsHero';
import GuideNotice from '@site/src/components/GuideNotice';

<DocsHero
  compact
  eyebrow="GRIDEX · ACCESS AND ORGANISATIONS"
  title="Organisations, invitations and rights"
  description="A clear path from the first invitation to the right permissions for each person and Site."
  imageAlt="Illustrative image of solar panels and energy infrastructure"
  primaryHref="#steps-for-the-recipient"
  primaryLabel="See the steps"
  secondaryHref="https://gridex.tech/"
  secondaryLabel="Open the portal"
/>

<GuideNotice label="Live access is by invitation only">
  <p>The demo is open, but it contains sample values. Sign in does not create an account or grant permissions for customer Sites.</p>
</GuideNotice>

## Who sends the invitation?

The platform administrator invites the **first administrator** of a new
organisation. Once accepted, that administrator can invite colleagues only
within their organisation, selecting each person's role and permitted Sites.

If you already belong to an organisation, ask its administrator for an
invitation. If you are the first person from a new organisation, contact the
GrideX team.

## Invite a colleague — for organisation administrators {#invite-a-colleague}

These steps are only for an administrator of an **existing customer
organisation**. They do not create a new organisation and are not instructions
for the platform administrator.

1. Sign in to your organisation and open
   [Customers & contracts → Users & invitations](https://gridex.tech/customers/users/).
2. Select your organisation, enter your colleague's email, choose a role and
   select only the Sites they need. If there are no Sites yet, the invitation
   can grant membership **without** Site access.
3. Select Send invitation. After confirmed dispatch, wait for your colleague
   to receive the message. If there is an error or the outcome is unclear,
   **do not assume the email was sent or retry blindly** — check the state or
   contact support.
4. Your colleague verifies their email, sets a password on the secure screen,
   signs in to their organisation and accepts the invitation in Profile. Only
   then verify that they see no more than their permitted Sites.

This form can grant Viewer, Operator, Energy manager or Integrator, but **not**
Organisation administrator. A sent invitation can be revoked in the same
session; the email alone does not activate access.

## Steps for the recipient

<div className="gridex-step-grid">
  <div className="gridex-step"><span>01</span><strong>Open the email</strong><p>Verify your address using the received link.</p></div>
  <div className="gridex-step"><span>02</span><strong>Set a password</strong><p>Do this only on the secure sign-in screen.</p></div>
  <div className="gridex-step"><span>03</span><strong>Sign in</strong><p>Choose Sign in at gridex.tech, enter the invited email and the portal will route you to the right organisation.</p></div>
  <div className="gridex-step"><span>04</span><strong>Access confirmed</strong><p>For a first administrator, the portal completes the invitation after sign-in. An invited colleague still accepts in Profile.</p></div>
</div>

<GuideNotice label="Never share your password" tone="amber">
  <p>The email alone <strong>does not grant access</strong>. A first administrator does not press a second button: after verified email, password setup and sign-in, the backend checks the invitation and rights. On failure access remains pending. If the link expired or was revoked, request another invitation rather than creating a second account.</p>
</GuideNotice>

Generic sign-in asks only for an email first. If that address was invited to
multiple organisations, choose the one you want. Enter the password **only**
on the secure Keycloak screen, not in GrideX. The portal does not confirm
whether an account exists for an address without a valid invitation. If sign-in
fails, check the invited email and organisation: a wrong realm can look like
an incorrect username or password.

## Roles and Sites

| Role | Scope |
| --- | --- |
| Platform administrator | Invites the first administrator of a new organisation. |
| Organisation administrator | Manages people and permitted Sites within their own organisation. |
| Viewer | Reads authorised data. |
| Operator | Performs authorised operational actions. |
| Energy manager | Works with authorised strategies and settings. |
| Integrator | Works with authorised device settings. |

Each customer organisation has a separate OpenRemote space. Site access is
explicit: membership without a Site grant does not expose another customer's
data. The current member invitation flow cannot delegate the organisation
administrator role.

## Sites, devices and commissioning {#sites-and-devices}

1. **Only an organisation administrator creates Sites** in GrideX. Each Site
   belongs to that organisation's separate OpenRemote realm. The platform
   administrator can see users and rights across organisations; that does not
   move customer devices between them.
2. The administrator grants Site access to invited and approved members.
   They see only explicitly permitted Sites. A member with the **Integrator**
   role, as well as the organisation administrator, can prepare device settings.
   A Viewer only reads them.
3. Under **Sites → Devices**, choose only confirmed GrideX hardware:
   **ROCK Pi E** as controller/backend link and **OLIMEX ESP32-EVB** as
   communication node. Define at most two roles and a communication peer per
   device. Selection and draft settings neither send commands nor prove
   connectivity. External protocol references are not GrideX production drivers.
4. **Only the organisation administrator commissions and activates equipment
   for now.** Ownership and OpenRemote links, configuration, ROCK Pi
   acknowledgement and real heartbeats must be checked first. ESP32 is
   configured through ROCK Pi; battery commands remain locked until separately
   approved commissioning.

**Current status:** already registered ROCK Pi/ESP32 units can be viewed and
their roles drafted. Forms for a new customer Site and device have been
prepared but are **not yet published or accepted with a real customer account**.
Do not bypass this through OpenRemote Manager or a local database.

### How will a new customer Site be added?

Under [Sites](https://gridex.tech/sites/), the organisation administrator
enters a **name** and **time zone**, then chooses Create Site. On an empty
list, the form will appear on that same page. Other roles will not see this
button. The Site appears only after its OpenRemote asset and administrator
link have been verified in the correct organisation. On failure there is no
locally successful Site; retrying unchanged details cannot duplicate it.

### How will a new GrideX device be added?

After selecting a Site, the administrator opens
[Devices](https://gridex.tech/devices/), chooses an approved **ROCK Pi E** or
**OLIMEX ESP32-EVB** variant and enters a name. For an ESP32, they select the
already registered ROCK Pi E as its parent. A Site can have only one ROCK Pi E
controller. The new asset appears in the list after verification. Device roles
and communication settings remain a separate draft; merely adding inventory
does not alter Ethernet, send OTA/Modbus commands or prove a heartbeat. If
OpenRemote is unavailable, the screen reports an error, not demo values.

## Status of the first live test

The owner reports that the first customer received the email and signed in.
Automatic invitation completion and tenant isolation have **not yet been
verified on the published portal**. Do not confuse email dispatch or sign-in
with proven active access.

The photograph is illustrative, not a customer Site. Content last reviewed:
27 September 2026.
