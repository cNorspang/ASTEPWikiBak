---
title: Vehicle to Grid (V2G)
description: The Vehicle to Grid project attempts to use electric cars as buffers for the power grid in times of low or high demand compared to the supply of energy, which may depend on the vast renewable energy sources.
published: true
date: 2020-09-30T09:40:34.628Z
tags: 
editor: undefined
---

# Vehicle to Grid

> NOTE: This page reflects the state of the service at the end of the Spring 2020 semester.
> NOTE: This page was not created by the original creators of the service and thus does not follow the Service Documentation Standard.
{.is-info}

> This service broke during the summer 2020 in the proecss of renewing the certificate. Perhaps you can fix it? SSH into the [Docker Host](/servers#ui-proxy-docker-host) server, run `sudo docker restart sw607`, find the output-logs, and observe that `cd` refuses to work during startup for some reason (as if the file system does not exist at that point). Starting the service in a shell and running cd/ls there works fine.
{.is-warning}

Originally created by group SW607F18 (aka. TS2), the Vehicle to Grid service attempts to predict the supply of electricity on and electric vehicles connected to the power grid at any time. This information will be used to utilize the batteries in the cars to serve as buffers when there is high or low demand compared to the electricity supply.

Futhermore, the service also tries to track electricity prices, such that the cars can sell and buy energy in a manner that optimizes charging costs of the car as well as the usage of the power grid.

This service makes use of the [ts2](/databases/DB1/ts2) database from `DB1`. You can find the source code for the service's backend on GitLab here: "https://daisy-git.cs.aau.dk/aSTEP-2018/V2G".
