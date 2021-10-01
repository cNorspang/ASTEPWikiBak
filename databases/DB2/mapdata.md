---
title: mapdata
description: Created in spring 2020, the mapdata database contains the danish road network in the form of a graph, as supplied by OpenStreetMap.
published: true
date: 2020-08-26T07:24:44.904Z
tags: 
editor: undefined
---

# The mapdata database

> NOTE: This page reflects the state of the database at the end of the Spring 2020 semester.
> NOTE: This page was not created by the original creators of the database (though we used it).
{.is-info}

The `mapdata` database was created during the spring 2020 semester by the routing supergroup in order to store a graph (vertices+edges) of the danish road-network.

Specifically, group SW605F20 used the [GraphHopper](https://www.graphhopper.com/) java library to parse the graph stored in the latest danish OpenStreetMap file from [Geofabrik](https://download.geofabrik.de/), and then uploaded the data to the new database.

A point to node about this graph is that it is not strongly connected. That means that there are some sections of the graph where it is either not possible to enter them or leave them. As a result of this, certain routing efforts might be negatively affected, since there exist pairs of nodes with no path between them. The database [sw601f20_routing](/databases/DB2/sw601f20_routing) contains the largest, stronly connected component of this graph in the `edge` and `node` tables (these tables may have been better off placed in the `mapdata` database).

## Tables

The database contains 3 tables:

- `node`
- `edge`
- `edge-geometry`

### node

The table `node` contains the nodes of the graph. These nodes represent intersections between roads in the road network.

| **Column Name** | **Type** | Explanation                  |
| --------------- | -------- | ---------------------------- |
| <u>node_id</u>  | INTEGER  | The node's unique identifier |
| lon             | REAL     | The node's longitude         |
| lat             | REAL     | The node's latitude          |

### edge

The table `edge` contains the edges of the graph. These edges represent "road segments" which are streaches of road with no branches. That is, the roads between intesections.

| **Column Name** | **Type**     | Explanation                                                  |
| --------------- | ------------ | ------------------------------------------------------------ |
| <u>edge_id</u>         | INTEGER      | The edge's unique identifier                                 |
| edge_basenode→node   | INTEGER      | The node of the graph at which the edge starts.              |
| distance        | REAL         | The length of the edge, measured in meters.                  |
| edge_name       | VARCHAR(100) | Name of the road that the edge is a part of.                 |
| highway         | VARCHAR(20)  | The type of road it is.                                      |
| maxspeed        | VARCHAR(20)  | The registered maximum speed one is allowed to drive at on this edge. |
| edge_adj→node        | INTEGER      | The node of the graph at which the edge ends.                |

### edge_geometry

The table `edge_geometry` contains additional nodes describing how an edge should be drawn on a world map (more specifically, the [map-geo chart](/user-interface/charts#geographical-geometry)). Since only few road segments are completely straight, we use these elements to draw the edge so that it mimics the road's curvature. The database is currently (As of August 2020) sorted, so that the order of entries for each edge describe the order in which the points should be drawn and connected.

| **Column Name** | **Type** | Explanation                                    |
| --------------- | -------- | ---------------------------------------------- |
| edge_id         | INTEGER  | The edge which the geometry-element belongs to |
| lon             | REAL     | The element's longitude                        |
| lat             | REAL     | The element's latitude                         |

An example would be the edge with `edge_id = 960998`. It has the following 3 entries:

|      | edge_id | lon              | lat              |
| ---- | ------- | ---------------- | ---------------- |
| 1    | 960998  | 11.1821853261184 | 55.600091008844  |
| 2    | 960998  | 11.17775576959   | 55.600378787526  |
| 3    | 960998  | 11.1774609128563 | 55.6003955513327 |

This edge would be drawn as 1-2-3 on a world map, where the integers represent elements and the dashes represent the line-segements drawn between the element-coordinates.

> NOTE: It is correct that this table has no primary or foreign keys.
{.is-info}
