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
  <div className="gridex-step"><span>03</span><strong>Sign in</strong><p>Use the organisation named in your invitation.</p></div>
  <div className="gridex-step"><span>04</span><strong>Access confirmed</strong><p>For a first administrator, the portal completes the invitation after sign-in. An invited colleague still accepts in Profile.</p></div>
</div>

<GuideNotice label="Never share your password" tone="amber">
  <p>The email alone <strong>does not grant access</strong>. A first administrator does not press a second button: after verified email, password setup and sign-in, the backend checks the invitation and rights. On failure access remains pending. If the link expired or was revoked, request another invitation rather than creating a second account.</p>
</GuideNotice>

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

## Status of the first live test

The owner reports that the first customer received the email and signed in.
Automatic invitation completion and tenant isolation have **not yet been
verified on the published portal**. Do not confuse email dispatch or sign-in
with proven active access.

The photograph is illustrative, not a customer Site. Content last reviewed:
27 September 2026.
