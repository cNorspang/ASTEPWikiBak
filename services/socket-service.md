---
title: Socket Service
description: The Socket Service facilitates the communication between a service and the Socket Chart.
published: true
date: 2020-12-15T02:22:45.745Z
tags: 
editor: undefined
---

# Socket Service

> NOTE: This page reflects the state of the service at the end of the Spring 2020 semester.
> NOTE: This page was not created by the original creators of the service and thus does not follow the Service Documentation Standard.
{.is-info}

Made during the 2019 Spring semester, the Socket Service facilitates the real-time two-way communication between the [Socket Chart](/user-interface/charts#socket-chart) and the service that outputtet that chart to the UI. Due to some requests taking a very long time and in otder to facilitate real time messaging, this service and chart was made. The source code for the Socket Service is found on GitLab here: "https://daisy-git.cs.aau.dk/aSTEP-2019/socketservice".

An example of how a service should set up HTTP endpoints for the Socket Chart is seen on this GitLab page: "https://daisy-git.cs.aau.dk/aSTEP-2019/sw601f19/-/blob/master/flask_service.py". Likewise, the source code of the Socket Chart itself is found on GitLab here: "https://daisy-git.cs.aau.dk/astep-2020/UserInterface/-/blob/master/app/src/app/charts/socketio/socketio.component.ts".

The service, socket chart, and the socket service all work together in a way that we could not quite understand.
