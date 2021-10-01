---
title: Speed Analysis
description: Created in the spring 2020 semester, the Speed Analysis service is a tool for calculating the speed at which delivery trucks have driven, based on the historical traffic data (GPS readings) from Bring.
published: true
date: 2020-09-06T07:31:04.912Z
tags: 
editor: undefined
---

# Speed Analysis

[comment]: <> "Contains some minor and major differences to the user guide"

**Speed Analysis** is a service dedicated to calculating probable velocities for trajectories and GPS readings stored in tables on the database [DB2/driver_identification_db](/databases/DB2/driver_identification_db).

It was originally made by group *SW601F20* as part of the *routing* story of that semester. The groups of the semester were separated into two: one half working on the *routing* story and the other working on various time-series analyses. The story was composed of three tasks(Henceforth referred to as *Task x*):

1.  Analyze the traffic tendencies (at different hours and days) of road segments based on historical traffic data supplied by the *Bring* delivery company. This data takes the form of lists of GPS readings representing deliveries. Use the results of this analysis to create histograms over travel-time for each road segment.
2.    Categorize edges based on commonalities and the histograms from *Task 1*, as not all edges are completely detailed or have any known traffic tendencies due to lack of data.
2.  Using the results of *Tasks 1* and *2*, find the optimal delivery-route based on historical tendencies.

Additionally, it was mandated that the 3 groups(*SW601F20*,*SW605F20*, and *SW606F20*) worked together to solve *Task 1*. It was therefore split into 3 parts (Henceforth *Task 1.x*) in order to enable independent and parallel development.

1. Calculate the velocity at every GPS reading.
2. Find the road segment to which every GPS reading belong.
3. Calculate histograms for each road segment based on the velocities of the associated GPS readings.

*Task 1.1* is implemented by this service, which can be found [here](https://astep.cs.aau.dk/tool/astep-2020-trajectory-analysis.astep-dev.cs.aau.dk). *Task 1.2* was fulfilled by group *SW605F20* with the [Map Matching](https://wiki.astep-dev.cs.aau.dk/services/map-matching) service, and *Task 1.3* was was completed by group *SW606F20* with the [Bucketizer](https://wiki.astep-dev.cs.aau.dk/services/bucketizer) and [Historical Road Tool](https://wiki.astep-dev.cs.aau.dk/services/Historic-Road-Tool) services.

## Current status
The system can analyze specified data stored in the `DB2/driver_identification_db` database. 

The system makes use of two different types of data: Trajectories and GPS readings. A GPS reading contains the latitude and longitude of the reading, as well as a timestamp. A trajectory is an ordered list of GPS readings which together describe the route which a *Bring* delivery truck has taken.

The service can output data in three different formats: As a line-chart, as a JSON object, and as a table written in markdown. The line-chart is only used for analyzed trajectories, and gives a thorough overview of the result, and is interactable (with respect to high-lighting specific readings). The markdown table is only used when analyzing GPS readings. Finally, the JSON object can be used by both types of input. The object contains a list of smaller JSON objects which has fields corresponding to the columns in the `speeds` table described below in **Inner Workings/LocalDB**.

![speedanalysisoutputimage.png](/services/speed_analysis/speedanalysisoutputimage.png)

There are two points to note concerning the service. The service is unable to update the database on its own, which result in it being dependent external updates to the `DB2` database in order to support future trajectories. Lastly, because the service saves its results to a local database, other services are required to directly call **Speed Analysis** for the data, which is an increasingly expensive action to take, as the call-tree expands in depth.
## Inner workings
The service is programmed using C#, with the codebase being available on DAISY-git [here](https://daisy-git.cs.aau.dk/astep-2020/trajectory-analysis).

The service is composed of a 5-part design:

<img src="/services/speed_analysis/speedanalysis3.png" alt="'Speed analysis' Design" style="zoom:40%;" />


#### APIController
For receiving and answering requests, the service uses `ASP.NET CORE` to open the end-points specified by the `2020v1` [Service Interface Standard](/user-interface/api-standard).

The component is primarily responsible for formatting the output of the service. If the service received a *trajectory id* as input, then it will create a `chart.js` chart (As specified [here](/user-interface/charts#chartjs). Likewise, if the system receives a list of GPS IDs as input, it will create a simple table through a markdown table.

Finally, it can create a list of JSON objects containing the results of either type of input.

#### AnalysisManager
The analysis manager is responsible for handling the input received from the `APIController`, calling the various other components, and communication with the `LocalDB` database.

This final task also includes surveying if the input (or some of it in the case of GPS readings) have already been analyzed.

#### AAUDatabaseQuerier
The `AAUDatabaseQuerier` is responsible for handling communication between the service and the `DB2/driver_identification_db`. In order to facilitate this communicaiton, the service makes use of the `Npgsql` NuGet package.

The component has 2 types of queries, who both query from the `DB2/driver_identification_db/alltrajectory` [table]().
- Querying for all GPS readings in a trajectory, given its ID.
- Querying for a trajectory's ID, given the ID of a GPS reading in it.


#### Speed Computation
The speed Computation component is relatively simple. It receives the list of GPS readings for an entire trajectory, and then goes through it, adding velocities to each reading.

>Note that the first reading in any trajectory will always be assigned a velocity of 0 km/h.{.is-info}

To calculate the velocity, the general formula $v = \frac{\Delta s}{\Delta t}$ is used. $\Delta t$ is found by substracting the GPS readings' timestamps with each other. In order to compensate for the curvature of the earth, as well as to translate difference in longitude and latitude, we use the Haversine formula to calculate the distance *d* between two readings:
>$$
a = \sin^2(\frac{\Delta\varphi}{2}) + \cos(\varphi_1) \cdot \cos(\varphi_2) \cdot \sin^2(\frac{\Delta\lambda}{2}) \\
c = 2 \cdot atan2(\sqrt{a}, \sqrt{1-a})\\
d = R \cdot c
$$

Where $\varphi$ is the longitude, $\lambda$ is the longitude, and *R* is the earth's radius in the desired unit (I.e 6371 km).


#### LocalDB

The service has an `SQLite` database which it uses to store previously-computed results, so as to avoid redundant computation. This database has two tables:

###### `analysedTrajectories`:

| Column name            | Type    |
| ---------------------- | ------- |
| *<u>trajectory_id</u>* | INTEGER |

This table is used to store the ID of all already-analyzed trajectories. These are stored in a separate table from the actual results in order to decrease the look-up time.

###### `speeds`:

| Column name     | Type                                      |
| --------------- | ----------------------------------------- |
| *<u>gps_id</u>* | INTEGER                                   |
| *trajectory_id* | INTEGER REFERENCES `analysedTrajectories` |
| *speed*         | REAL                                      |
| *timestamp*     | TEXT                                      |

This table is used to store the results of analyses. *Speed* is measured in km/h, and *timestamp* is the timestamp of the GPS reading, not the computation of the velocity.

#### 

## History

The following subsections describe the change history of the service based on semesters.

### Spring 2020

The **Speed Analysis** service was created by group *SW601F20* in spring 2020, whose report detail the creation in full. 

The service was implemented as a five-component design:

![Speed analysis design as of Spring 2020]()

1. `APIController`: The component which handles I/O by administrating the exposed end-points described by the `2020v1` standard.
2. `AnalysisManager`: The main control component. It is responsible for handling inter-component communication.
3. `AAUDataBaseQuerier`: Component responsible for connecting to `DB2/driver_identification_db` and retrieving the requested GPS readings connected to certain trajectories.
4. `SpeedComputation`: Computation component responsible for calculating the velocities. The component makes use of the basic velocity formula `v = s/t` and the haversine formula to perform these computations.
5. `LocalDB`: A `SQLite` database used to store the analyzed trajectory and GPS readings.

There are a few important points to note:

- The service is dependent on the `DB2/driver_identification_db` tables being up-to-date. It cannot, on its own, update the tables by inserting new trajectories.
- The system speeds up as it is used. As the analysis results don't change over time, the service can instead return previously-analyzed results when prompted.

A potential improvement to the system might be to move `LocalDB` onto `DB2` so that other services aren't required to call this one in a chain (as that is very expensive with respect to time).