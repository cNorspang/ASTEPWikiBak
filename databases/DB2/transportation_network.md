---
title: transportation_network
description: 
published: true
date: 2021-11-10T18:41:28.279Z
tags: tnm, rfc0020
editor: markdown
---

# The transportation_network database

> NOTE: This page reflects the state of the database at the end of the 2021 semester
{.is-info}

The `transportation_network` database contains data derived from [vejman.dk](http://www.vejman.dk/), which describes the road infrastructure and use in Denmark.

The `transportation_network` database is likewise managed by the [TNM Creator Microservice](/services/TNM_Creator_Genesis), and should therefore only be accessed through the endpoints of that service alone, following the microservice infrastructure.

The database stores all the relationsships as a description of a miniworld, containing municipalities, roads, intersections, road segments and mileage posts, as described in the [ER Diagram](#er-diagram).

The database form the data background of the [Transport Network Model RFC0020](/rfc/0020), but the [TNM Creator Microservice](/services/TNM_Creator_Genesis) can be expanded to allow different representations of the data, depending on the needs of other microservices.

## ER diagram

The ER Diagram presented below describes the structure of the different entities in the transportation_network database. The concrete attributes and their meaning are defined in the [Tables](#tables) section.

![finalerdatabase.png](/database/finalerdatabase.png)
*The corresponding draw io file is available [here](/database/finalerdatabase.drawio)*

## Tables

The database contains 5 tables:

- [`municipality`](#municipality)
- [`road`](#road)
- [`intersection`](#intersection)
- [`segment`](#segment)
- [`mileage_post`](#mileage_post)

Presently, all these are modelled as the only tables in the database, but since most of these entities are temporal, and have different data at different times, the inclusion of temporal tables such as Rules, Construction, etc. might be beneficial to expand on later if time allows it.

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
