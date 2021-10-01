---
title: Historic Road Tool
description: 
published: true
date: 2020-11-18T10:22:31.267Z
tags: 
editor: undefined
---

# Historic Road Tool
The Historic Road Tool is a tool made by several groups during the spring semester of 2020. It was made on the request of Prof. Bin Yang, as a way for the students of the groups to familiarize themselves with the workings of aSTEP.

It is tool for getting historical speed data for certain trajectories. The tool takes as input a list of trajectory ID's, coordinates, or edge ID's, along with a query.

## Current status
As the Historic Tool is mostly a stitching of three other tools (see explanation below), most bugs and problems will arise either from those tools specifically, or from miscommunication between the tools. For example, if the input or output format in one tool is changed, it will lead to the Historic Tool failing, if the data is not massaged into proper form in the Historic Tool, when needed.

The Historic Road Tool is connected to the Map Matching tool, Speed Analysis tool, and the Bucketizer tool.

## Inner workings of service
In essence, the Historic Tool is a streamlined process of taking some input, running it on the Map Matching tool, running some of *that* output through the Speed Analysis tool, combining the two, then finally running the combined data through the Bucketizer tool.

More formally, the historic tool will take the input, find GPS points in a database that may match (based on the result of the Map Matching service), and add speeds to these points (based on the result of the Speed Analysis service). Finally, these data points are bucketized, based on the query given. Documentation for the queries can be found in the [bucketizer documentation](https://wiki.astep-dev.cs.aau.dk/services/Bucketizer).

Trajectory ID's are based on route data provided by Bring, while Edge ID's are based on edge data from [OpenStreetMap](https://www.openstreetmap.org/). In general, it is recommended to stick to trajectory ID's, as these are more easily found than the other two types.

Below, the result of running the historic tool can be seen.

![historic-tool-example-1.png](/historic-tool-example-1.png)

![historic-tool-example-2.png](/historic-tool-example-2.png)

## Output
The output of this service is the result of a query request (written in their own [Query language](/services/Bucketizer)), put into a bar chart or can be viewed as a JSON format. In the picture above the x-axis shows the value of a speed, and the y-axis shows how many times this speed has been given to a point on the trajectory.

> This output part was not written by the creators of this service.
{.is-info}

## History

### Spring 2020
Intitial creation.  
The service is largely complete, though not without problems. Most notably is the slow runtime. It has been found, through experimentation, that the culprit is likely to be the final call to the bucketizer with all the data. For a singular point (for example, trajectory 1285), the URL header ended up being ~90.000 characters, which takes a long time to encode in an HTTP request.

Some solutions could be to hash the data in some way to cut down on the raw amount of characters to send. Alternatively, the Historic Tool could have a local version of the Bucketizer contained inside it, although this would likely become problematic if the two versions then diverge.