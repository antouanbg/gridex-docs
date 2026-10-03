---
title: Approved screens — Users
sidebar_position: 3
---

# Settings — Users: approved design

**Approved by the owner on 2026-10-03.** These three mockups are the binding
reference for the next implementation, not screenshots of an already deployed
new portal. Public copies use example addresses and an example organisation.
Layout, colours, forms and permitted actions must not change without approval.
Images retain the approved Bulgarian source labels; matching English workflows
and verification status are described below.

## Platform administrator

Only the current verified role. Approved organisation selector → five services →
organisation requests → member inspection → new invitation → invitation history →
approved organisation/service ledger. Platform grants organisation services and
zone; it does not bypass organisation admin for personal grants.

![Approved platform administrator desktop reference](/img/approved/users-superadmin-1024.png)

<details>
<summary>Mobile — platform administrator</summary>

![Approved platform administrator mobile reference](/img/approved/users-superadmin-390.png)

</details>

## Organisation administrator

Five services → new invitation → history → approved members in five columns →
expandable editor → member requests. Columns: **Name/email, Role, Sites,
Services, Actions**. Mobile rows become cards. Admin grants services individually,
including to themselves. Site assignments are separate from services and are
verified against OpenRemote.

![Approved organisation administrator desktop reference](/img/approved/users-organisation-admin-1024.png)

<details>
<summary>Mobile — organisation administrator</summary>

![Approved organisation administrator mobile reference](/img/approved/users-organisation-admin-390.png)

</details>

## Member — viewer

Users is **absent from the menu**. A direct URL shows a denial without disclosing
other people or data. Personal requests belong in Services, authorised Sites
in Sites. The lower mockup panels compare these separate personal destinations;
they are not administrative sections available to the viewer.

![Approved viewer desktop reference and administration denial](/img/approved/users-member-1024.png)

<details>
<summary>Mobile — viewer</summary>

![Approved viewer mobile reference](/img/approved/users-member-390.png)

</details>

## Does the backend support it?

Source and test review on 2026-10-03: **148 passing tests, 1 skipped, zero
failures**. This does not establish end-to-end acceptance with three real accounts.

| Mockup action | Status |
| --- | --- |
| Active organisation selection; five-service catalogue | Protected API exists |
| Organisation grant/revoke and BG zone | API exists; member grants never follow automatically |
| Personal grant/revoke, including admin | API exists; requires organisation grant |
| Request, approve, reject | APIs exist with separate levels and checks |
| Admin cancels own organisation request | API exists |
| Member roster, roles, Sites and services | API exists; OpenRemote links verified |
| Invitation, history, resend pending invitation | API exists |
| Email after action | Queue and tests exist; actual receipt not tested in this review |
| Personal request cancellation / personal service stop | New source and tests exist; not deployed live yet |
| New layout on the live portal | **Not deployed yet** |

The initial review found a missing personal cancellation API. Following the
explicit confirmation below, protected actions and tests were added.
The mockup alone is not evidence of a working deployment.

## Confirmed clarification: cancel and stop

The owner confirmed the following, superseding the earlier open note:

- Cancel request changes only the caller's own pending request to Cancelled in the database.
- Stop service, after confirmation, removes only the caller's personal grant.
- Organisation grants, other members and Site assignments remain unchanged.
- Re-enabling requires new approval from the organisation administrator.
- An error never produces local-only success; state must be verified again.

New APIs and controls are implemented in source. Four targeted BG/EN browser
and locale tests passed, alongside typechecking and the frontend build.
**This addition is not deployed live yet.** No additional migration is needed.

## Implementation rules

- Real screen follows this reference, not an older version.
- Role comes from verified identity; there is no role switcher.
- Example names, Sites and statuses must never become live data.
- API failure means Could not verify access, not Permission denied.
- Every write requires backend validation; refresh the row after success.
- Service approval has no second Accept step.
- Test empty, loading, denied and unavailable states separately.
- Acceptance requires three real roles, mobile/desktop, BG/EN, notifications and cross-organisation denial.

See the [final matrix](./navigation-and-permissions.md#menu-matrix) and
[invitations, roles and Sites](./organisations-and-access.md).
