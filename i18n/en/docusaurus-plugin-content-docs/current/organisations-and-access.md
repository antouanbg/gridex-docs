---
id: organisations-and-access
slug: /organisations-and-access/
title: Organisations, invitations and rights
hide_title: true
description: Who can invite, how invitations are accepted and how Site access is granted.
---

import DocsHero from '@site/src/components/DocsHero';
import GuideNotice from '@site/src/components/GuideNotice';

> The current approved structure and matrices are in [Navigation, services and permissions](./navigation-and-permissions.md#menu-matrix). Section names here follow the new structure; live rollout verification is separate from approval.

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

See the [current menu, role and service matrices](./navigation-and-permissions.md#menu-matrix) and the [approved role-specific screens](./approved-users-screens.md). Paths below are navigation locations; a named section within Users is not a separate menu.

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
   [Settings → Users](https://gridex.tech/settings/users/).
2. Select your organisation, enter your colleague's email, choose a role and
   select only the Sites they need. If there are no Sites yet, the invitation
   can grant membership **without** Site access.
3. Select Send invitation. The portal confirms dispatch. The invitations you
   sent and their statuses remain visible below the form after a page reload.
   If the outcome is unclear, **do not retry blindly** — check the status or
   contact support.
4. Your colleague verifies their email, sets a password on the secure screen
   and signs in to their organisation. The portal accepts the invitation after
   verifying identity; there is no second Accept button. Only
   then verify that they see no more than their permitted Sites.

This form can grant Viewer, Operator, Energy manager or Integrator, but **not**
Organisation administrator. A **Sent** invitation can be revoked or resent by
the same administrator. Resending creates a fresh link for the same user
without duplicating the account or membership. Accepted or revoked invitations
cannot be resent. The email alone does not activate access.

A Viewer sees only their permitted data. Settings → Users are hidden from their menu, and a direct URL does not grant access.
If the session check is temporarily unavailable, the portal retries
automatically without signing the user out or substituting demo data.

After confirmed session expiry or revocation, the portal clears private data
and opens the public [demo](https://gridex.tech/demo/). It does not redirect
you automatically to OpenRemote sign-in. Choose Login in the demo to sign in
again. A temporary connection error is not treated as an expired session.

When you select **Sign out**, the portal ends the identity session and returns
you directly to the public demo, without a blank intermediate page or an
automatic new sign-in. Other open portal tabs leave the private view as well.
Select Sign in from the demo when you want to return.

**Another user on the same computer:** select Sign out, wait for the demo,
then choose Sign in. Enter the new user's email and password. The Switch
account/user option has been removed; accounts are not switched within an
active portal session.

## Steps for the recipient

<div className="gridex-step-grid">
  <div className="gridex-step"><span>01</span><strong>Open the email</strong><p>Verify your address using the received link.</p></div>
  <div className="gridex-step"><span>02</span><strong>Set a password</strong><p>Do this only on the secure sign-in screen.</p></div>
  <div className="gridex-step"><span>03</span><strong>Sign in</strong><p>Select Sign in at gridex.tech, enter the invited email and continue to the correct organisation's protected login.</p></div>
  <div className="gridex-step"><span>04</span><strong>Access confirmed</strong><p>After verified sign-in, the portal completes the invitation without a second action for both the first administrator and invited colleagues.</p></div>
</div>

<GuideNotice label="Never share your password" tone="amber">
  <p>The email alone <strong>does not grant access</strong>. A first administrator does not press a second button: after verified email, password setup and sign-in, the backend checks the invitation and rights. On failure access remains pending. If the link expired or was revoked, request another invitation rather than creating a second account.</p>
</GuideNotice>

### Expired link or forgotten password

If you did not receive the email, enter the **same email address** on the
Sign in page and select “Did not receive the invitation — resend”. The
recipient has one resend attempt per pending invitation. The response does
not reveal whether the address exists. After acceptance, the button cannot
send another invitation. Contact your administrator if delivery still fails;
they can inspect the status and send another link.

An accepted invitation remains **Accepted** in the administrator's list;
the original link expiry is not an account expiry. The last verified sign-in
is shown once recorded. Access remains active until separately revoked or
the organisation is suspended.

If the **first administrator** invitation is still **Sent** but its link has
expired, the platform administrator opens
[Settings → Users](https://gridex.tech/settings/users/)
and selects **Resend invitation** beside **Revoke**. This sends a fresh 24-hour
link to the same email and Keycloak account, without creating another
organisation. The button is unavailable for an accepted or revoked invitation.
If delivery is uncertain, check the invitation status before another attempt.

**Forgot password** on the protected login page of the **correct organisation**
is a separate flow for an existing password. It does not extend an invitation
or activate an organisation. If the login reports invalid credentials, first
check the invited email and organisation. Never send a password to support.

Generic sign-in asks only for an email first. If that address was invited to
multiple organisations, choose the one you want. Enter the password **only**
on the secure Keycloak screen, not in GrideX. The portal does not confirm
whether an account exists for an address without a valid invitation. If sign-in
fails, check the invited email and organisation: a wrong realm can look like
an incorrect username or password.

The email field is near the top of the sign-in page, including on mobile.
If you open Sign in but do not complete authentication, you can immediately
choose another demo section without manually refreshing or seeing customer
data. After sign-in is verified, the portal briefly shows “Sign-in successful”
and opens the Overview home screen.

On a shared computer, open Sign in and enter the next person's email. The
new sign-in page does not silently restore the previous user; the protected
screen asks for a password again. If the identity provider returns the old
account, the portal rejects that session and offers a retry. The previous
user's Site selection is cleared as well. No other profile's data is used
until the new identity has been verified.

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

### Where permissions are checked {#rights-matrix}

**GrideX** checks membership, role and assigned Sites. **OpenRemote** owns
the actual Assets and exact links to the Site, ROCK/ESP and its other child
devices. Access is shown only when both checks succeed.

| GrideX role | Direct OpenRemote Manager | Changes |
| --- | --- | --- |
| Platform administrator | Read-only in their own realm | Verified actions through GrideX |
| Organisation administrator | Read-only for assigned Assets | Manages their organisation through GrideX |
| Viewer | Read-only for explicitly linked Assets | Their administrator assigns Sites |
| Operator, energy manager, integrator | The same restricted read access | Approved actions pass through GrideX |

GrideX uses a **separate service client per organisation** to create Assets
and change links. It is not a human sign-in, and its token never reaches the
browser. `write:assets` is broader than link management; it is confined to
that realm, while the backend checks and audits actions. Removing a Site must
also remove and recheck links to its child Assets. Prices and Visualisations
have separate service permissions.

### One shared administrative design

Under **Settings → Users**, the platform administrator
first selects an approved organisation and manages its five service rows. This is
followed by **New organisation invitation**, **Organisation invitations**, and
**Approved organisations and services**. New invitations require the first
administrator's first name, last name and email. The organisation administrator
has the continuous page described below, scoped to their own organisation.
The member's existing **Services** page remains unchanged in workflow.
All roles use the same GrideX cards, colours, status pills and buttons; actions
remain subject to verified backend permissions. Invitation history includes
accepted entries, filters and pagination. No additional Accept button is added.

### Approved members and their access {#approved-members}

See the [three approved Settings — Users screens](./approved-users-screens.md)
with desktop and mobile references. The organisation administrator sees
**name/email, role, Sites, services and actions** for each member. Open that
person's “Rights and services” to edit access. A service not approved for the
organisation remains visible with an explanation, but cannot be enabled.
Sites and services are saved separately; neither automatically grants the other.

The organisation-administrator screen is one continuous page, without tabs:
**Available services → New member invitation → Member invitations → Approved
members and services**. All five catalogue entries remain visible without
organisation grants; only the two active services can be requested. The approved update replaces the side editor with five columns:
Name/email, Role, Sites, Services, Actions. Details expand below the table;
mobile uses cards. Select
a person by name/email, change their role and Site checkboxes, choose
**Review changes**, then **Save role and Sites**. Services are separate rows
below the permissions. Search and pagination support larger rosters. A
failed service check must not hide the member list. **Retry** checks the
current state again.

**Status on 2 October 2026:** this screen and the protected API are published.
The service clients in GrideX and Novacom were verified separately, and the
existing human roles were verified as restricted to OpenRemote read access.
A real-user test of role and Site editing through the portal remains a separate
check. If the screen warns about an unverified link, do not treat the change
as successful.

Under **Settings → Users**,
the administrator sees all approved members of their organisation, not only
invitations they personally sent. Each entry shows the email address, first
and last name when present, current role, assigned Sites, separate services
and last recorded sign-in. Pending invitations are listed separately and are
not memberships. A new invitation requires a first and last name.

The administrator may change an approved ordinary member among **Viewer**,
**Operator**, **Energy manager** and **Integrator**, and explicitly add or
remove assigned Sites. A change is confirmed only after the corresponding
OpenRemote Site Asset links are verified. The organisation administrator
role cannot be delegated or demoted on this screen. Additional services
are granted separately; a role or Site assignment does not itself enable
an optional service. The platform administrator can inspect each
organisation's members without bypassing its permissions.

If the screen warns that an OpenRemote link is unverified, do not treat a
local record as proof that access works. Contact an administrator before
granting further rights. Larger rosters are paginated.

## Additional services {#additional-services}

### Visible services without approval

All five services **remain visible** when the organisation has no grants.
Day-ahead prices and Charts and visualisations say **Not approved for the
organisation**; Analysis, Meteorology and Forecasting say **Coming soon**.
A disabled button grants no access. A failed check shows an unverified
status, not an assumed permission.

1. The organisation administrator opens **Settings → Users**, in **Available services**,
   and chooses **Request** beside either available service. Prices currently
   request Bulgaria / BG. The request is recorded and the platform
   administrator is notified by email. Only the organisation administrator
   who submitted it may choose **Cancel request** while it awaits a decision.
2. The platform administrator approves or declines the organisation request.
   Approval enables only the organisation, not its members.
3. The organisation administrator opens **Approved members and services**, selects the approved
   person and chooses **Grant and notify**. Access takes effect immediately,
   without another recipient Accept button. **Remove access** revokes it.
4. A member may request a service for themselves under **Services**.
   Their own administrator decides; the member cannot request for the
   organisation, and the platform administrator cannot bypass this level.

```text
Member → personal request → Organisation administrator
                               ↓ if organisation permission is missing
                      organisation request → Platform administrator
                               ↑ organisation-only approval
Member ← individual grant ← Organisation administrator
```

A saved request/change is not proof that email was delivered. Notifications
are processed separately; an uncertain provider outcome is not automatically
resent. Viewing the catalogue never enables permissions. Real-user acceptance
of the revised screen remains a separate check from backend tests.

Under **Services**, every verified member, including a viewer,
sees Day-ahead prices, Visualisations, Analysis, Meteorology and Forecasting.
Only the first two can be requested **independently**; the other three say
Coming soon. Bulgaria (BG) is currently the only price zone. The requester,
organisation administrator and platform administrator can see the request
and its decision history. Repeated submission does not duplicate an open request.

A request **does not grant access**. The platform administrator enables the
service for an active organisation and separately grants its selected price
zone; that organisation's administrator then enables the specific approved
member. Visualisations do not inherit Day-ahead access: a BG price dashboard
requires both service grants and BG zone scope. Site charts also require
access to that Site. Under Settings → Users
→ Service requests each administrator sees their own decision stage. Declining
a request never grants access.

The platform administrator can grant a service to an active organisation under
**Settings → Users**. This is only an organisation
grant: no member is enabled automatically. The organisation administrator then
explicitly enables each approved member in the same section. Without an
individual grant, the service remains visible in the catalogue but its live
screen denies access. Revoking the
organisation grant removes all member grants; they do not return automatically.

### Where services are managed

1. **Services:** every verified member sees the catalogue and their
   own state: enabled service, pending request, available to request or Coming
   soon. Only `day_ahead` and `visualisations` can be requested; requesting
   alone does not grant access.
2. **Settings → Users → approved organisation:**
   the platform administrator sees approved services, available but not yet
   approved services, and future services separately. They may enable a
   requestable service; Day-ahead additionally needs a BG zone grant. Removing
   an organisation grant requires confirmation and deletes member grants.
3. **Settings → Users → Services and member access:** the organisation
   administrator sees approved services and enables approved members one by
   one. Services not approved for the organisation are informational only;
   this administrator cannot enable them at organisation level.
4. **Settings → Users → Service requests:** each administrator sees their
   own decision stage and history. Notifications are queued separately; a saved decision does not confirm email delivery. The other
   three future services cannot be requested or granted yet.

The BG price chart requires individual grants for both Day-ahead prices and
Visualisations, plus both organisation grants and BG zone scope. The full
archive and ENTSO-E provider health remain platform-administrator-only. This
screen does not change OpenRemote inventory or Site permissions.

### Site charts {#site-visualisations}

Open **Sites → selected Site → Visualisations** to see measured values from
the last 24 hours. Data comes from linked OpenRemote Asset history through
the guarded GrideX API; missing measurements are never replaced by demo
values. Configured ROCK Pi measurements can include temperature, load, free
memory/storage and uptime. New sensors appear only after they are
provisioned and linked to this Site.

Access requires the **Visualisations** service for both the organisation and
the individual member, plus that member's current permission for the exact
Site in OpenRemote. Requesting the service alone does not unlock charts.
This is not a shared customer Grafana dashboard or a cross-tenant datasource.

See the [Day-ahead guide](/market-prices/) for that service. The full archive
and provider status remain platform-administrator-only. The restricted BG
dashboard in Services → Day-ahead prices requires both individual service grants and organisation
BG scope; real customer-role acceptance testing is still pending.

## OpenRemote Manager administration {#openremote-manager}

Organisation and platform administrators start at the
[GrideX portal](https://gridex.tech/), sign in, then open **Settings → Users → Organisation administration**. Select **Open OpenRemote
Manager** to create a one-time link valid for one minute and open Manager for
the organisation in the current session. No email or separate setup identity
is involved. The proxy checks access again for the page and its requests;
the direct `auth.gridex.tech/manager/` address is denied without this entry.
Do not share the short-lived, one-time link.

If access is denied, check that you signed in to the correct organisation
and have an active administrator role. If the link expires, return to the
portal and use the button again. Manager is not a bypass for provisioning
unapproved Sites or devices.

This applies to future organisations too: each has its own OpenRemote realm,
and Manager checks the current administrator and exact realm on every request.
A customer administrator cannot open another organisation or the service
`master` realm.

**Status:** the protected entry is deployed. Anonymous denial, blocked service
access and both current OIDC realms have been checked. Real sign-in through
the button with pilot and customer accounts still awaits acceptance by those
users; do not send passwords or one-time links to support if it fails.

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

**Current status:** forms for a new Site and an approved GrideX device are
published. Acceptance with a real customer administrator is still pending;
publication alone does not prove successful provisioning. Do not bypass this
through OpenRemote Manager or a local database.

### How is a new customer Site added?

Under [Sites](https://gridex.tech/sites/), the organisation administrator
enters a **name** and **time zone**, then chooses Create Site. On an empty
list, the form appears on that same page, never under Devices. Other roles do not see this
button. The Site appears only after its OpenRemote asset and administrator
link have been verified in the correct organisation. On failure there is no
locally successful Site; retrying unchanged details cannot duplicate it.

### How is a new GrideX device added?

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

## Suspending and restoring an approved organisation

Prepared for publication; the controls are not yet available in the live portal. Access controls were verified with synthetic organisations; the first real customer suspension and its email delivery remain unverified. This is separate from resending any onboarding invitation.

Only the verified super administrator can use **Settings → Users → New organisation → Approved organisations**. The pilot organisation is protected and is not listed. A recent sign-in is required for changes.

Choose **Suspend organisation**, review the organisation name, then confirm. Access is blocked; existing sessions and streams end. Accounts, roles, Sites and OpenRemote inventory remain intact. Members see “Your organisation is temporarily suspended. Contact the super administrator.”

The verified first administrator receives one BG/EN suspension notice per suspension operation. Queued does not mean delivered. **Check delivery** checks the recipient's provider delivery event without sending again. An unknown or failed result must be investigated; repeating the button never automatically resends an uncertain email. This mandatory access notice is separate from optional event subscriptions.

If a step fails, portal/API access stays blocked and the existing operation remains available for reconciliation. A pending operation is not confirmation that the OpenRemote change has completed. Choose **Complete existing operation** instead of creating another request. Notification problems do not restore access. **Complete notification** can finish a notice that has not yet been attempted.

Choose **Restore access** and confirm to restore the existing permissions after the realm is verified. Members must sign in again; old tokens do not regain access. Restoration sends no new invitation or password email and does not recreate accounts.
