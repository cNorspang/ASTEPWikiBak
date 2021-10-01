---
title: Authentication Service
description: The authentication service is used manage permissions for users and thus restrict access to services.
published: true
date: 2020-08-26T20:26:25.127Z
tags: 
editor: undefined
---

# Authentication service

> NOTE: This page reflects the state of the service at the end of the Spring 2020 semester.
> NOTE: This page was not created by the original creators of the service and thus does not follow the Service Documentation Standard.
{.is-info}

Made during the 2019 Spring semester, the Authentication Service is part of the backend of the [User Interface](/services/user-interface) service, and implements the login-functionality of the aSTEP website. Furthermore, it can also be used to allow only a select range of aSTEP accounts to access certain services displayed in the UI. This process is documented in full in [RFC 0011](/rfc/0011). Finally, this services stores user and access information in the [auth_db](/databases/DB2/auth_db) database.

The service's source code can be found on GitLab here: "https://daisy-git.cs.aau.dk/aSTEP-2019/auth". The service does not seem to be using any libraries stored on GitLab.
