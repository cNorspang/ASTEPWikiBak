---
title: Ride Sharing
description: The Ride Sharing service 
published: true
date: 2020-08-26T11:35:00.905Z
tags: 
editor: undefined
---

# Ride Sharing

> NOTE: This page reflects the state of the service at the end of the Spring 2020 semester.
> NOTE: This page was not created by the original creators of the service.
{.is-info}

This service made by what we assume to be group SW604F18 (aka. PA2), since the SW604F18 project report cannot agree with itself on the year. Ride Sharing attemps to effectively satisfy a collection of "passenger transport demands", based on a collection of "available vehicles", while also adhering to a collection of constarints such as "wait time" and "travel delay".

This service makes use of the [DB1/postgres](/databases/DB1/postgres) database and the [OSRM_service](/servers#db1-and-db2) to find paths between the pickup and dropoff locations of the passengers. 

This service is accessible through the [Legacy Services](/services/legacy-services) service. You can find the source code for the service's backend on GitLab here: "https://daisy-git.cs.aau.dk/aSTEP-2018/Mobility-as-a-ServiceREST-API". We are unsure as to what libraries it uses.

See the project report for more information.
