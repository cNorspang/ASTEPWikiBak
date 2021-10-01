---
title: Bucketizing Tool
description: The "Bucketizing Tool" service was made by the group sw606f20 during the Spring 2020 semester as part of that semester's routing story. The tool is used to create histograms from JSON objects based on some user-specified queries
published: true
date: 2020-09-06T08:52:37.641Z
tags: 
editor: undefined
---

# Bucketizing Tool

> NOTE: This page reflects the state of the service at the end of the Spring 2020 semester.
> NOTE: This page was not created by the original creators of the service, and thus does not follow the Service Documentation Standard.
{.is-info}

**Bucketizing Tool** is a general service dedicated to creating histograms based on user-specified data and quries describing the desired histogram.

It was originally made by group *SW606F20* as part of the *routing* story of that semester. The groups of the semester were separated into two: one half working on the *routing* story and the other working on various time-series analyses. The story was composed of three tasks(Henceforth referred to as *Task x*):

1.  Analyze the traffic tendencies (at different hours and days) of road segments based on historical traffic data supplied by the *Bring* delivery company. This data takes the form of lists of GPS readings representing deliveries. Use the results of this analysis to create histograms over travel-time for each road segment.
2.    Categorize edges based on commonalities and the histograms from *Task 1*, as not all edges are completely detailed or have any known traffic tendencies due to lack of data.
2.  Using the results of *Tasks 1* and *2*, find the optimal delivery-route based on historical tendencies.

Additionally, it was mandated that the 3 groups(*SW601F20*,*SW605F20*, and *SW606F20*) worked together to solve *Task 1*. It was therefore split into 3 parts (Henceforth *Task 1.x*) in order to enable independent and parallel development.

1. Calculate the velocity at every GPS reading.
2. Find the road segment to which every GPS reading belong.
3. Calculate histograms for each road segment based on the velocities of the associated GPS readings.

One part of *Task 1.3* is implemented by this service, specifically creating histograms. When combined with the service [Historic Road Tool](/services/Historic-Road-Tool), they together fulfill the task. *Task 1.1* was fulfilled by group *SW601F20* with the [Speed Analysis](/services/speed-analysis) service, and *Task 1.2* was fulfilled by group *SW605F20* with the [Map Matching](https://wiki.astep-dev.cs.aau.dk/services/map-matching) service.

The service itself can be found [here](https://astep.cs.aau.dk/tool/astep-2020-bucketizer.astep-dev.cs.aau.dk).

## Details
The service is able to take custom data specified as JSON, and run queries over it, which are used to specify what part of the data should be made into histograms, as well as how. This query language is custom-made, and therefore has its own syntax and semantics.

The service is written in Python, and the repository containing its code base can be found [here](https://daisy-git.cs.aau.dk/astep-2020/bucketizer). For more details concerning the query language and the service, see the user documentation on the service or read *SW606F20*'s project report.