---
title: sw601f20_routing
description: The sw601f20_routing database is used by the Route Planner service to store the graph it uses. This graph is based on the one contain in mapdata.
published: true
date: 2020-08-27T08:07:37.707Z
tags: 
editor: undefined
---

# sw601f20_routing

> NOTE: This page reflects the state of the database at the end of the Spring 2020 semester.
{.is-info}

Made during the 2020 Spring semester by group SW601F20, the `DB2/sw601f20_routing` database is tied to the [2020 Route Planner](/services/route-planner) service. The service is tasked with making near-optimal parcel delivery plans for the *Bring* company, based on historical GPS data taken from delivery vehicles.



## Tables

This database has 4 tables:

- `destination`
- `address`
- `node`
- `edge`

### destination

The `destination` table contains all of Bring's "static delivery locations". That is: stores, SwipBoxes, etc. at which Bring's delivery personell may leave packages for pick-up. Furthermore, the table also contains Bring's "distribution centers", from which the packages are distributed. Each entry contains the name, address, and geographical coordinates of the delivery location. This is the original set of destinations the 2020 Route Planner could produce delivery routes between (see [address](#address)).

Each entry also has an attribute `Type` of the customly defined data type *destination_type*, which either has the value "*delivery*" or "*distribution*".

| Column name  | Type                             | Explanation                                                  |
| ------------ | -------------------------------- | ------------------------------------------------------------ |
| <u>ID</u>    | INTEGER                          | The primary key and integer identifier of a destination.     |
| Name         | VARCHAR(63)                      | The human readable name of the destination.                  |
| Address      | VARCHAR(63)                      | The address (street name and street number(s)) of the destination. |
| PostalCode   | SMALLINT                         | The postal code of the destination.                          |
| City         | VARCHAR(63)                      | The city name of the destination.                            |
| OpeningHours | VARCHAR(127)                     | The time-intervals in which packages can be delivered to the destination. |
| Latitude     | DOUBLE PRECISION                 | The latitude of the destination on a world map.              |
| Longitude    | DOUBLE PRECISION                 | The longitude of the destination on a world map.             |
| Type         | destination_type *(custom type)* | Is either "Delivery" or "Distribution".                      |

### address

In the summer 2020 (as part of a study job), the 2020 Route Planner was given the ability to produce delivery plans going though any set of addresses. Therefore, the `address` table contains the set of all (we assume) addresses in Denmark, as well as their geographical coordinates. 

| Column name       | Type             | Explanation                                  |
| ----------------- | ---------------- | -------------------------------------------- |
| <u>number</u>     | VARCHAR(10)      | The street number of the address.            |
| <u>street</u>     | VARCHAR(63)      | The street name of the address.              |
| <u>unit</u>       | VARCHAR(63)      | The unit (floor, etc.) of the address.       |
| <u>postalcode</u> | SMALLINT         | The postal code of the address.              |
| lat               | DOUBLE PRECISION | The latitude of the address on a world map.  |
| lon               | DOUBLE PRECISION | The longitude of the address on a world map. |

### node, edge

The tables `node` and `edge` contains the "Largest Strongly Connectec Component" (LSCC) of the graph stored in the [DB2/mapdata](/databases/DB2/mapdata) database. The `node` and `edge` tables of `sw601f20_routing` has the exact same scheme as those from `mapdata` with equivalent names.

The original graph from `mapdata` is *not* strongly connected, resulting in pairs of nodes between which there exist no paths. The 2020 Route Planner wiki-page [describes the problem and solution](/services/route-planner#issues-and-points-of-note) in more depth.
