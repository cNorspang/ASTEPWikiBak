---
title: Attribute Prediction
description: The Attribute Prediction service was made by group SW605F20 during the Spring 2020 semester, as part of that semester's routing story. The service is made to predict missing attributes on edges based on a designated (sub)graph.
published: true
date: 2020-12-15T02:25:08.422Z
tags: 
editor: undefined
---

# Attribute Prediction

> NOTE: This page reflects the state of the service at the end of the Spring 2020 semester.
> NOTE: This page was not created by the original creators of the service and thus does not follow the Service Documentation Standard.
{.is-info}

**Attribute Prediction** is a service dedicated to filling out missing *attributes* on edges of a road-network graph, by predicting what they would be, based on the neighboring edges and what data is available about the edge.

It was originally made by group SW605F20 as part of the routing story of that semester. The groups of the semester were separated into two: one half working on the routing story and the other working on various time-series analysis. The story was composed of three tasks(Henceforth referred to as Task x):

1.  Analyze the traffic tendencies (at different hours and days) of road segments based on historical traffic data supplied by the *Bring* delivery company. This data takes the form of lists of GPS readings representing deliveries. Use the results of this analysis to create histograms over travel-time for each road segment.
2.    Categorize edges based on commonalities and the histograms from *Task 1*, as not all edges are completely detailed or have any known traffic tendencies due to lack of data.
2.  Using the results of *Tasks 1* and *2*, to find the optimal delivery-route based on historical tendencies.


*Task 2* is implemented by this service in combination with the [Graph Attributes](/services/graph-attributes) service.
*Task 1* was fulfilled by the services [Speed Analysis](/services/speed-analysis), [Map Matching](/services/map-matching), [Bucketizing Tool](/services/bucketizer), and [Historic Road Tool](/services/Historic-Road-Tool), made by the three groups *SW601F20*, *SW605F20*, and *SW606F20*. *Task 3* was implemented group *SW601F20* woth the [Route Planner](/services/route-planner) service.

The service (and its user-documentation, written by the service's creators) can be found [here](https://astep.cs.aau.dk/tool/astep-2020-attribute-prediction.astep-dev.cs.aau.dk).
## Details
Currently, the only attribute that the service is able to predict on the speed limit. This was most likely chosen due to the focus of the routing story being what it was. In order to make its predictions, the service makes use of a *Relational Fusion Network* (A machine intelligence technique) and a feature-learning algorithmic framework called *Node2vec*.

Something to note is that this service composes the back-end of the *Task 2* implementation, and it does therefore not expose the `/render` end-point (and subsequently, is only able to return its results raw).

The service is implemented using Python, and its repository can be found [here](https://daisy-git.cs.aau.dk/astep-2020/attribute-prediction) on daisy-git.