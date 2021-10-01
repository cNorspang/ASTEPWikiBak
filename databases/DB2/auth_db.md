---
title: auth_db
description: The auth_db database is used by the Authentication service to store information about the users registered on aSTEP.
published: true
date: 2020-08-26T20:16:32.751Z
tags: 
editor: undefined
---

# auth_db

> NOTE: This page reflects the state of the database at the end of the Spring 2020 semester.
> NOTE: This page was not created by the original creators of the database.
{.is-info}

The `auth_db` database is used by the [Authentication Service](/services/authentication-service), which is also documented in [RFC 0011](/rfc/0011). The database stores information about accounts on the aSTEP website (such as `demo@astep.cs.aau.dk`), user tokens that can be used to grant only certain users acces to your services, and more of which I am not certain.

## Tables

The database contains 11 tables:

- `migrations`
- `oauth_access_tokens`
- `oauth_auth_codes`
- `oauth_clients`
- `oauth_personal_access_clients`
- `oauth_refresh_tokens`
- `password_resets`
- `permission_user`
- `permissions`
- `projects`
- `users`

We will not be documenting these tables any further due to a lack of time, a lack of understanding, and a bit for security reasons.
