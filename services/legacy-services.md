---
title: Legacy Services
description: "Legacy Services" is a service from 2019 used to access the services from 2018.
published: true
date: 2020-11-18T10:03:34.068Z
tags: 
editor: undefined
---

# Legacy Services

> NOTE: This page reflects the state of the service at the end of the Fall 2020 semester.
> NOTE: This page was not created by the original creators of the service and thus does not follow the Service Documentation Standard.
{.is-info}

Made during the 2019 Spring semester, the Legacy Services service allows for the usage of the services developed during the 2018 Spring semester, despite the UI from 2018 having been closed down. Except for the [2018 Vehicle To Grid](/services/vehicle-to-grid) service which broke and now won't start again. The 2018 UI code was simply copied into Legacy Services. 

Do note that the name "Legacy Services" can be very misleading, since the services are in no way out of order or otherwise outdated. They are still working and their back-end services are running on the [Docker Host](/servers#ui-proxy-docker-host) server.

The legacy services include the following services:
[driver-identification](/services/driver-identification)
[energy](/services/energy)
[logistics](/services/logistics)
[ride-sharing](/services/ride-sharing)
[vehicle-to-grid](/services/vehicle-to-grid)
It also includes:
Hazardous roads
Map matching V2
However these two haven't had a wiki page written yet. And their readme files are either non existing or doesn't say anything useful.

The source code for this service is found on GitLab here: "https://daisy-git.cs.aau.dk/aSTEP-2019/legacyservices". We don't think it uses any libraries stored elsewhere on GitLab.
