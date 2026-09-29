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

A Viewer sees only their permitted data. Customers & contracts and Users &
invitations are hidden from their menu, and a direct URL does not grant access.
If the session check is temporarily unavailable, the portal retries
automatically without signing the user out or substituting demo data.

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
[Customers & contracts → Users & invitations](https://gridex.tech/customers/users/)
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

On a shared computer, use “Sign in with another account” and enter that
person's email. Protected sign-in requires a password again; the portal must
not mix data from the previous profile with the new identity.

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

## Additional services

The approved next step is **Profile → Services**: every verified user,
including a viewer, will see Day-ahead prices, Visualisations, Analysis,
Meteorology and Forecasting. Only the first two will be **independently
requestable**; the other three will say Coming soon. A day-ahead request
selects exactly one country/bidding zone — Bulgaria (BG) only for now. The
request will appear for that organisation's administrator and the platform
administrator under Users & invitations → Service requests.

A request **does not grant access**. The platform administrator enables the
service for an active organisation and separately grants its selected price
zone; that organisation's administrator then enables the specific approved
member. Visualisations do not inherit Day-ahead access: a BG price dashboard
will require both service grants and BG zone scope. Site charts also require
access to that Site. The catalogue/request UI and Site charts are **not
implemented yet**; the guarded BG market dashboard is separate.

The platform administrator can grant a service to an active organisation under
**Customers & contracts → Users & invitations**. This is only an organisation
grant: no member is enabled automatically. The organisation administrator then
explicitly enables each approved member in the same section. Without an
individual grant, the service is hidden from the live menu. Revoking the
organisation grant removes all member grants; they do not return automatically.

See the [Day-ahead guide](/market-prices/) for that service. The full archive
and provider status remain platform-administrator-only. The restricted BG
dashboard in Market requires both individual service grants and organisation
BG scope; real customer-role acceptance testing is still pending.

## OpenRemote Manager administration {#openremote-manager}

Organisation and platform administrators start at the
[GrideX portal](https://gridex.tech/), sign in, then open **Customers & contracts
→ Users & invitations → Organisation administration**. Select **Open OpenRemote
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

Only the verified super administrator can use **Customers & contracts → Users & invitations → New organisation → Approved organisations**. The pilot organisation is protected and is not listed. A recent sign-in is required for changes.

Choose **Suspend organisation**, review the organisation name, then confirm. Access is blocked; existing sessions and streams end. Accounts, roles, Sites and OpenRemote inventory remain intact. Members see “Your organisation is temporarily suspended. Contact the super administrator.”

The verified first administrator receives one BG/EN suspension notice per suspension operation. Queued does not mean delivered. **Check delivery** checks the recipient's provider delivery event without sending again. An unknown or failed result must be investigated; repeating the button never automatically resends an uncertain email. This mandatory access notice is separate from optional event subscriptions.

If a step fails, portal/API access stays blocked and the existing operation remains available for reconciliation. A pending operation is not confirmation that the OpenRemote change has completed. Choose **Complete existing operation** instead of creating another request. Notification problems do not restore access. **Complete notification** can finish a notice that has not yet been attempted.

Choose **Restore access** and confirm to restore the existing permissions after the realm is verified. Members must sign in again; old tokens do not regain access. Restoration sends no new invitation or password email and does not recreate accounts.
