---
title: postgres (DB1)
description: The postgres database from DB1 stores a graph (vertices+edges) of the danish road network.
published: true
date: 2020-08-26T11:44:42.295Z
tags: 
editor: undefined
---

# postgres (DB1)

> NOTE: This page reflects the state of the database at the end of the Spring 2020 semester.
> NOTE: This page was not created by the original creators of the database.
{.is-info}

The `postgres` database from `DB1` stores a graph of (at least) the danish road network. This information has been extracted from the latest danish OpenStreetMap file from [Geofabrik](https://download.geofabrik.de/) using the command line tool *osm2pgrouting*. 

The database is used by the [2018 Losistics](/services/logistics) service (more specifically, the service uses the [OSRM_service](/servers#db1-and-db2) which uses the database). The database is also used by the [2018 Ride Sharing](/services/ride-sharing) service.

> NOTE: We believe this database has the *postgis* extension installed, which adds the `GEOMETRY` data type. Geometries can be visualized using *pgAdmin*.
> NOTE: This database has the *pgRouting* extension installed, which allows for "on-database-server routing" based on the road-network graph stores on the database. This appears to be separate from the [OSRM_service](/servers#db1-and-db2).
{.is-info}

## Tables

This database contains 14 tables (listed in a somewhat logically grouped order):

- `users`

- `nodes`

- `ways`
- `way_nodes`
- `way_adjacencies`

- `edges`
- `edge_nodes`

- `relations`
- `relation_members`

- `logs`
- `schema_info`
- `spatial_ref_sys`

- `NY_network`
- `requests`

Since the information about these tables are vast and uncertain, they'll be explained in groupes in the sections below. We do not present the schemes of all tables.

> It is correct that none of these tables use any foreign keys.
{.is-info}

### users

Geofabrik keeps track of the users who contribute information to Open Street Maps. The `users` table contains the IDs and names of the users.

### nodes

The `nodes` table contains all the nodes of the road-network graph. The nodes represent intersections and likely also intermideate points on road segments which represent the road's curvature.

| Column name  | Type                           | Explanation                                                  |
| ------------ | ------------------------------ | ------------------------------------------------------------ |
| <u>id</u>    | BIGINT                         | Primary key and integer identifier of a user.                |
| version      | INTEGER                        | *Probably the number of revisions of this information*.                                        |
| user_id      | INTEGER                        | *Probably the latest contributor*.                           |
| tstamp       | TIMESTAMP WITHOUT TIME ZONE    | *Probably the time this information was latest updated*.     |
| changeset_id | BIGINT                         | *Probably where this info came from*.                        |
| tags         | HSTORE                         | Labels describing the road conditions at the node.           |
| geom         | GEOMETRY *(postgis extension)* | A string representation of the node's coordinates. |

### ways, way_nodes, way_adjacencies

The entries of the `ways` table represent streaches of roads spanning multiple nodes. We believe that these "ways" only represent movement in one direction on a given streach of road given the attributes of the `way_adjacencies` table. The scheme of `ways` is seen below.

| Column name  | Type                           | Explanation                                                  |
| ------------ | ------------------------------ | ------------------------------------------------------------ |
| <u>id</u>    | BIGINT                         | Primary key and integer identifier of a way.                |
| version      | INTEGER                        | *Probably the number of revisions of this information*.                                        |
| user_id      | INTEGER                        | *Probably the latest contributor*.                           |
| tstamp       | TIMESTAMP WITHOUT TIME ZONE    | *Probably the time this information was latest updated*.     |
| changeset_id | BIGINT                         | *Probably where this info came from*.                        |
| tags         | HSTORE                         | Labels describing the type of road this way represents.      |
| nodes          | BIGINT[]                       | An array of the nodes along the road this way represents.    |
| linestring   | GEOMETRY *(postgis extension)* | A string representation of the the drawable line on a world map representing the road. |

The `way_nodes` table contains a list representation of the attribute `ways.nodes` for all entries in `ways`, but additionally, it also lists the sequence number of each node. The scheme of `way_nodes` is seen below.

| Column name        | Type    | Explanation                                                  |
| ------------------ | ------- | ------------------------------------------------------------ |
| <u>way_id</u>      | BIGINT  | The way this entry belongs to.                               |
| node_id            | BIGINT  | The node in the way in question.                             |
| <u>sequence_id</u> | INTEGER | The index of the node in the sequence of nodes defining the "way". |

The `way_adjacencies` table represents what "ways" are connected to each other. More specifically, what "ways" you can travel onto from what other "ways". The scheme of `way_nodes` is seen below.

| Column name | Type   | Explanation                            |
| ----------- | ------ | -------------------------------------- |
| town        | TEXT   | The town in which these to ways touch. |
| from        | BIGINT | The way from which you can travel.     |
| to          | BIGINT | The way to which you can travel.       |

### edges, edge_nodes

The entries of the `edges` table represent streaches of roads spanning multiple nodes, but only between intersections. So where a "way" can span many intersections, en "edge" only spans the space between intersections. In fact, "ways" are split into one or more "edges". Just as with "ways" we believe that "edges" only represent movement in one direction on a given streach of road. The scheme of `edges` is seen below.

| Column name | Type                           | Explanation                                                  |
| ----------- | ------------------------------ | ------------------------------------------------------------ |
| <u>id</u>   | VARCHAR(25)                    | Primary key and identifier of an edge. The id also shows in what sequect the "edge" appear on a "way". |
| way_id      | BIGINT                         | The id of the "way" this edge is part of.                    |
| node_ids    | BININT[]                       | An array of the nodes along the road segment this edge describes. |
| tags        | HSTORE                         | Labels describing the type of road this edge represents.     |
| linestring  | GEOMETRY *(postgis extension)* | A string representation of the the drawable line on a world map representing the road this edge is a part of. |

The principle of `edge_nodes` is the same as with `way_nodes`.

### relations, relation_members

The tables `relations` and `relation_members` seem to relate to geographical structures such as lakes, rivers, or other landmarks that a map could be interested in showning. However, we don't under stand the tables, nor do we believe they are used by any of the services. The schemes of these tables have been omitted.

### logs, schema_info, spatial_ref

We have no clue about the tables `logs`, `schema_info`, and `spatial_ref`. The schemes of these tables have been omitted.

### NY_network, requests

We are not certain about the `NY_network` table (which is *not* related to New York as far as we can see), but the `requests` table is related to the [2018 Ride Sharing](/services/ride-sharing) service. The scheme of `requests` is seen below.

| Column name       | Type                        | Explanation                                                  |
| ----------------- | --------------------------- | ------------------------------------------------------------ |
| pickup_datetime   | TIMESTAMP WITHOUT TIME ZONE | Time of pickup.                                              |
| dropoff_datetime  | TIMESTAMP WITHOUT TIME ZONE | Time of dropoff.                                             |
| paggenger_count   | INTEGER                     | Number of passengers.                                        |
| trip_distance     | DOUBLE PRECISION            | The distance between pickup and dropoff (probably in kilometers, in a straight line). |
| pickup_longitude  | DOUBLE PRECISION            | The longitude of pickup.                                     |
| pickup_latitude   | DOUBLE PRECISION            | The latitude of pickup.                                      |
| dropoff_longitude | DOUBLE PRECISION            | The longitude of dropoff.                                    |
| dropoff_latitude  | DOUBLE PRECISION            | The latitude of dropoff.                                     |
| <u>request_id</u> | INTEGER                     | The primary key and integer identifier of a request.         |

## Views

The database has 4 views:

- `geography_columns`
- `geometry_columns`
- `raster_columns`
- `raster_overview`

But we don't know what these are used for.
