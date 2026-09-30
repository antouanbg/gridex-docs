---
id: contact-inquiries
slug: /contact-inquiries/
title: Contacting GrideX
description: How a visitor or signed-in member can send an enquiry to the team.
---

> The form and API are published. A test enquiry on 30 September 2026 was accepted by the email provider (`queued`), and its receipt in the mailbox was confirmed. Testing the form from an external network is still pending.

## Who can send an enquiry?

- A visitor without an account uses **About → Enquiry from the demo** and enters a name, reply email, topic and message.
- A signed-in member with a verified email uses **About → Send an enquiry** and chooses any topic. The sender address comes from the verified session, not a browser-supplied address.
- **Request an offer** in About pre-fills the topic for SunStorage Pro 261 but does not send anything by itself. Only **Send enquiry** submits the form.

## Check and confirmation

The form uses a short one-time human check, a hidden autofill trap and server-side frequency limits. Do not include passwords, keys or other sensitive information. A success message means the email provider accepted the message for sending; it does **not** guarantee mailbox delivery. If the result is uncertain, do not retry immediately.
