---
title: Graph Attributes
description: The Graph Attributes service was made by the group *SW605F20* during the Spring 2020 semester, as part of that semester's routing story. It, alongside the Attribute Prediction service, are used to append attributes onto edges to allow later algorithms.
published: true
date: 2020-09-06T10:10:08.217Z
tags: 
editor: undefined
---

# Graph Attributes
> NOTE: This page reflects the state of the service at the end of the Spring 2020 semester.
> NOTE: This page was not created by the original creators of the service and thus does not follow the Service Documentation Standard.
{.is-info}

**Graph Attributes** is a service dedicated to filling out missing *attributes* on edges stored in the [mapdata](/databases/DB2/mapdata) database by annotating the road-network graph.

It was originally made by group *SW605F20* as part of the *routing* story of that semester. The groups of the semester were separated into two: one half working on the routing story and the other working on various time-series analyses. The story was composed of three tasks(Henceforth referred to as Task x):

1.  Analyze the traffic tendencies (at different hours and days) of road segments based on historical traffic data supplied by the *Bring* delivery company. This data takes the form of lists of GPS readings representing deliveries. Use the results of this analysis to create histograms over travel-time for each road segment.
2.    Categorize edges based on commonalities and the histograms from *Task 1*, as not all edges are completely detailed or have any known traffic tendencies due to lack of data.
2.  Using the results of *Tasks 1* and *2*, find the optimal delivery-route based on historical tendencies.


*Task 2* is implemented by this service in combination with the [Attribute Prediction](/services/attribute-prediction) service.
*Task 1* was fulfilled by the services [Speed Analysis](/services/speed-analysis), [Map Matching](/services/map-matching), [Bucketizing Tool](/services/bucketizer), and [Historic Road Tool](/services/Historic-Road-Tool), made by the three groups *SW601F20*, *SW605F20*, and *SW606F20*. *Task 3* was implemented group *SW601F20* with the [Route Planner](/services/route-planner) service.

The service (and its user-documentation, written by the service's creators) can be found [here](https://astep.cs.aau.dk/tool/astep-2020-graph-attributes.astep-dev.cs.aau.dk).
## Details
This service serves as the front-end of *Task 2*, and the actual attribute prediction/annotation is performed by the [Attribute Prediction](/services/attribute-prediction) service, which is called by this. The resulting graph is drawn by this service on a world map as a [map-geo chart](/user-interface/charts#geographical-geometry). The graph can also be sent raw in the form of JSON data, so that other services can query this one.

The service is written using Python, and its repository can be found [here](https://daisy-git.cs.aau.dk/astep-2020/graph-attributes) on daisy-git.

For more details, please see *SW605F20*'s project report, which can be found in the project library [here](https://projekter.aau.dk/projekter/en/studentthesis/trajectory-analysis-and-road-network-prediction-on-astep(ff671044-d8dc-4a9a-819f-0ad34d950339).html).