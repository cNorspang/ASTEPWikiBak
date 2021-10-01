---
title: driver_identification_db
description: The driver_identification_db contains data related to trajectories provided to the aSTEP project by Bring.
published: true
date: 2020-08-26T07:11:52.441Z
tags: 
editor: undefined
---

# driver_identification_db

> NOTE: This page reflects the state of the database at the end of the Spring 2020 semester.
> NOTE: This page was not created by the original creators of the database.
{.is-info}

The `driver_identification_db` database containins data which describe the various trajectories provided by the parcel-delivery company *Bring*. A trajectory is defined as the list of GPS readings taken during a delivery from some location *A* to another location *B*.

The database contains one month worth of trajectories for 101 cars, where one GPS point is sampled every second.

The trajectories from this database is used by the services [2018 Driver Identification](/services/driver-identification), [2020 Map Matching](/services/map-matching) and [2020 Speed Analysis](/services/speed-analysis). As a side note, this data was initially given to a semester before 2018.

## Tables

The database contains 7 tables:

- `driver`
- `gpspoints` (Spring 2020)
- `mapmatchedpoints` (Spring 2020)
- `rawtrajectory`
- `rawtrajectorynodriver`
- `trajectorypoint`
- `trajectorypointnodriver`

The tables above are presented in aplhabetical order, where as below they're in "logical" order to ease understanding.

### driver

The `driver` database contains the unique, valid identifiers of all drivers, and nothing more. Some of the trajectories have a driver (of the delivery vehicle) associated with it, and some of the trajectories do not. The 2018 Driver Identification service tried to identify which driver had driven what unlabelled trajectories, based on a set of trajectories in which the driver was known.

| Column name | Type    | Explanation                                     |
| ----------- | ------- | ----------------------------------------------- |
| <u>id</u>   | INTEGER | Primary key and integer identifier of a driver. |

### rawtrajectory and rawtrajectorynodriver

The tables `rawtrajectory ` and `rawtrajectorynodriver` describe the trajectories that exist in the database. They are not the trajectories (or rather GPS readings) themselves.

The table `rawtrajectory` has the following schema:

| **Column Name** | **Type** | Explanation                                                  |
| --------------- | -------- | ------------------------------------------------------------ |
| driver→driver          | INTEGER  | A foreign key to the identifier of the driver who drove the delivery represented by the trajectory. |
| name            | REAL     | Purpose of this column is currently unknown.                 |
| <u>id</u>              | REAL     | The trajectory's unique identifier.                          |
| size            | INTEGER  | The number of GPS readings that compose the trajectory.      |

The table `rawtrajectorynodriver` has a nearly identical schema, but lacks the `driver` column.

### trajectorypoint and trajectorypointnodriver

The tables `trajectorypoint` and `trajectorypointnodriver` contains the data describing the various GPS readings stored in the database. The have the same schema, with the difference being which table they are partnered with. `trajectorypoint` contains the GPS readings belonging to the trajectories in `rawtrajectory` , while `trajectorypointnodriver` contains the GPS readings belonging to the trajectories stored in `rawtrajectorynodriver`.

| **Column Name** | **Type**  | Explanation                                                  |
| --------------- | --------- | ------------------------------------------------------------ |
| <u>id</u>              | INTEGER   | The GPS reading's unique identifier.                         |
| time            | timestamp | The specific time at which the reading was taken.            |
| lon             | REAL      | The measured longitude of the reading.                       |
| lat             | REAL      | The measured latitude of the reading.                         |
| direction       | INTEGER   | What direction is the vehicle is facing at the time of the reading. The direction is measured in degrees, though precisely which way 0 degrees refer to is unknown. |
| trajectory→(*)      | INTEGER   | The id of the trajectory to which the reading belongs.       |

(`*`) The table `trajectorypointnodriver` has a foreign key to `rawtrajectorynodriver`, whereas `trajectorypoint` has a foreign key to `rawtrajectory`.

> NOTE: The `trajectorypoint` table originally had a `driver` attribute, but someone deleted it at some point during Spring 2020. The information is luckily still present through the `rawtrajectory` table, so the attribute can be restored if need be.
{.is-info}

### gpspoints

Is the union of the `trajectorypoint` and `trajectorypointnodriver` tables over all their common columns. The explanation/description of the `gpspoints` table is the same as [above](#trajectorypoint-and-trajectorypointnodriver).

> NOTE: The `trajectory` attribute of the `gpspoints` table is *not* a foreign key.
{.is-info}

### mapmatchedpoints

Created in Spring 2020, the table `mapmatchedpoints` associates each GPS reading in this database with an "edge" from the road-network-graph defined in the [mapdata](/databases/DB2/mapdata) database (it might have been better to place this table there). This association is made using the [2020 Map Matching](/services/map-matching) service, which tries to find the edge in the road-network-graph representing the specific road the GPS reading was measured on.

| **Column Name** | **Type** | Explanation                                                  |
| --------------- | -------- | ------------------------------------------------------------ |
| <u>id→gpspoints</u>       | INTEGER  | The primary key as well as the foreign key to the correposning GPS reading.                         |
| lon             | REAL     | The longitude of the edge which the GPS reading has been matched to. |
| lat             | REAL     | The latitude of the edge which the GPS reading has been matched to. |
| edge_id         | INTEGER  | The id of the edge which the GPS reading has been matched to. |

Please note that there is redundant data in the form of the latitude and longitude, which are also stored elsewhere. 

> NOTE: The `edge_id` attribute of the `mapmatchedpoints` table is *not* a foreign key (since the edge objects are located in another database).
{.is-info}
  
## Views

The database contains 1 view:

- `alltrajectory` (Spring 2020)

### alltrajectory

The structure/definition of `alltrajectory` is identical to that of [gpspoints](#gpspoints). The difference is that the view is recomputed everytime, whereas `gpspoints` is not. Refer to the description of the `gpspoints` table for a description of the `alltrajectory` view.

The reason for this seemingly double definition is that two groups had different ideas as to how we should combine all GPS readings into one (this is why you should learn about "coordination").
