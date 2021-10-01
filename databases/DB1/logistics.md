---
title: logistics
description: The logistics database is used by the Logistics (2018) service to store information about delivery locations.
published: true
date: 2020-08-26T07:49:00.386Z
tags: 
editor: undefined
---

# logistics

> NOTE: This page reflects the state of the database at the end of the Spring 2020 semester.
> NOTE: This page was not created by the original creators of the database.
{.is-info}

The `logistics` database is tied to the [2018 Logistics](/services/logistics) service, which is used to find near-optimal package delivery routes for parcel delivery companies. 

## The tables

The database contains 3 tables:

- `Locations`
- `Duration`
- `spacial_ref_sys`

### Locations

The `Locations` table contains information about the "delivery locations" that the Logistics service knows and is able to make routes between. A delivery location can be either a "*Distribution center*" or a "*Delivery point*", which relates to the custom datatype "`location_type`" from the table below.

| Column name          | Type                     | Explanation                                                  |
| -------------------- | ------------------------ | ------------------------------------------------------------ |
| <u>ID</u>            | INTEGER                  | Primary key and integer identifier of a delivery location.   |
| Name                 | VARCHAR(63)             | The name of the physical delivery location.                  |
| Type                 | location_type *(custom)* | Is either "Delivery" or "Distribution"                       |
| Address              | VARCHAR(63)             | The address of the physical delivery location                |
| PostalCode           | SMALLINT                 | The postal code of the area the delivery location is located in. |
| City                 | VARCHAR(63)             | The name of the city the delivery location is located in.    |
| OpeningHours         | VARCHAR(127)            | The time intervals (for each week day) that delivery is possible. |
| Coordinate           | GEOMETRY *(postgis)*     | Special coordinate data that is viewable on a world map.     |
| Latitude             | DOUBLE PRECISION         | The latitude of the physical delivery location.              |
| Longitude            | DOUBLE PRECISION         | The longitude of the physical delivery location.             |
| LinksTo→Locations | INTEGER                  | A foreign key to the distribution center that this location receives packages from. |

### Durations

In order to speed up the routing algorithm, Logistics would pre-compute the "durations" (travel time) between all delivery points, such that this was not necessary when making delivery plans for a collection of packages. These durations are stored in the `Durations` table.

| Name                          | Type             | Explanation                                                  |
| ----------------------------- | ---------------- | ------------------------------------------------------------ |
| <u>FromLocation→Locations</u> | INTEGER          | A primary, foreign key to the location the duration "originates from". |
| <u>ToLocation→Locations</u>   | INTEGER          | A primary, foreign key to the location the duration "goes to". |
| Duration                      | DOUBLE PRECISION | The time it takes in seconds to travel from "from" to "to".  |

### spatial_ref_sys

As for the `spatial_ref_sys` table, we have no idea. Sounds like some kind of spacial data; perhaps some kind of geometry on a world map? Good luck.

| Column name | Type           | Explanation |
| ----------- | -------------- | ----------- |
| <u>srid</u> | INTEGER        | N/A         |
| auth_name   | VARCHAR(256)  | N/A         |
| auth_srid   | INTEGER        | N/A         |
| srtext      | VARCHAR(2048) | N/A         |
| proj4text   | VARCHAR(2048) | N/A         |



