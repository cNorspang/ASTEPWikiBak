---
title: Map-Matching
description: A developer-oriented guide for the Map-Matching service
published: true
date: 2020-11-18T10:35:01.780Z
tags: 
editor: undefined
---

# Map Matching
> NOTE: This page reflects the state of the service at the end of the Spring 2020 semester.
> NOTE: This page was not created by the original creators of the service and thus does not follow the Service Documentation Standard.
{.is-info}

**Map Matching** is a service dedicated to matching GPS readings stored on the database [DB2/driver_identification_db](/databases/DB2/driver_identification_db) with edges of the road-network graph stored in the database [mapdata](/databases/DB2/mapdata) (It does NOT use the database, but rather has its own, local copy).

It was originally made by group *SW605F20* as part of the *routing* story of that semester. The groups of the semester were separated into two: one half working on the *routing* story and the other working on various time-series analyses. The story was composed of three tasks(Henceforth referred to as *Task x*):

1.  Analyze the traffic tendencies (at different hours and days) of road segments based on historical traffic data supplied by the *Bring* delivery company. This data takes the form of lists of GPS readings representing deliveries. Use the results of this analysis to create histograms over travel-time for each road segment.
2.    Categorize edges based on commonalities and the histograms from *Task 1*, as not all edges are completely detailed or have any known traffic tendencies due to lack of data.
2.  Using the results of *Tasks 1* and *2*, find the optimal delivery-route based on historical tendencies.

Additionally, it was mandated that the 3 groups(*SW601F20*,*SW605F20*, and *SW606F20*) worked together to solve *Task 1*. It was therefore split into 3 parts (Henceforth *Task 1.x*) in order to enable independent and parallel development.

1. Calculate the velocity at every GPS reading.
2. Find the road segment to which every GPS reading belong.
3. Calculate histograms for each road segment based on the velocities of the associated GPS readings.

*Task 1.2* was fulfilled by this service, which can be found [here](https://astep.cs.aau.dk/tool/astep-2020-mapmatching-microservice.astep-dev.cs.aau.dk), alongside user-documentation. *Task 1.1* is implemented by the *SW601F20*, with the [Speed Analysis](https://wiki.astep-dev.cs.aau.dk/en/services/speed-analysis) service, and *Task 1.3* was was completed by group *SW606F20* with the [Bucketizer](https://wiki.astep-dev.cs.aau.dk/services/bucketizer) and [Historical Road Tool](https://wiki.astep-dev.cs.aau.dk/services/Historic-Road-Tool) services.

## Details
The service makes use of the open-source library [graphhopper](https://github.com/graphhopper/map-matching) in order to map the GPS readings to the edges. This library makes use of a Hidden Markov Model in order to perform the map-matching process. In order to perform map-mathing, the system must receive an entire trajectory (a trajectory is defined as an ordered list of GPS readings which together describe a previous delivery's path), as it is otherwise unable to function.

Additionally, *graphhopper* was also used to make the graph stored in the [mapdata](/databases/DB2/mapdata) database. This was done by downloading the (at the time) latest version of OpenStreetMap's graph of the Danish road-network via [GeoFabrik](https://www.geofabrik.de/), and then using *graphhopper* to parse the file. This local version of the parsed graph is also what this service uses for map matching, not the one stored in [mapdata](/databases/DB2/mapdata).

You can find the service's repository [here](https://daisy-git.cs.aau.dk/astep-2020/mapmatching-microservice).

## Input
The map matching service takes as an input a trajectory, this is defined as an ordered list of GPS readings, which describe a delivery's path.

## Output
The output of the map matching service is a graph showing the trajectory of the delivery route on top of a map of Denmark.

> The input and output parts was not written by the original creators of the service.
{.is-info}
