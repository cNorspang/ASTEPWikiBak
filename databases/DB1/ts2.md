---
title: ts2
description: The ts2 database stores data related to the "Vehicle to Grid" service from 2018
published: true
date: 2020-08-26T13:29:56.976Z
tags: 
editor: undefined
---

# ts2

> NOTE: This page reflects the state of the database at the end of the Spring 2020 semester.
> NOTE: This page was not created by the original creators of the database.
{.is-info}

The `ts2` database is tied to the [2018 Vehicle to Grid](/services/vehicle-to-grid) service. The information it stores is used by the service to "make some calculations" (I'm not really sure, sorry) related to how the Danish power grid can use electric car batteries as power buffers.

## Tables

The database contains 3 tables:

- `configurations`
- `chargingschedules`
- `bookings`

### configurations

Since the service tries to model the charging and discarging of car batteries, the `configurations` table contains various states or conditions under which such a battery can exist and charge. Basically, it models various different cars. We are unsure about the units of the values. The scheme of the `configurations` table is shown below. 

| Column name     | Type             | Explanation                                                  |
| --------------- | ---------------- | ------------------------------------------------------------ |
| <u>cid</u>      | INTEGER          | The primary key and integer identifier of a configuration.   |
| batterycapacity | DOUBLE PRECISION | The current max capacity of the battery in the configuration. (presumeably kWh) |
| batterylevel    | INTEGER          | The current energy level of the battery in the configuration. (presumeably percentage) |
| chargepower     | DOUBLE PRECISION | The current energy charge rate of the battery in the configuration. (presumeably kW) |
| dischargepower  | DOUBLE PRECISION | The current energy discharge rate of the battery in the configuration. (presumeably kW) |
| minuteinterval  | INTEGER          | *Not exactly sure.*                                          |

### chargingschedules

The entries in the `chargingschedules` table represent when a car is connected to the grid or not. We are unsure about the details of this table. The scheme of the `chargingschedules` table is shown below. All entries must satisfy `start_time < end_time`.

| Column name       | Type        | Explanation                                                  |
| ----------------- | ----------- | ------------------------------------------------------------ |
| <u>start_time</u> | TIMESTAMP   | The start time of s schedule, and part of the primary key.   |
| <u>end_time</u>   | TIMESTAMP   | The end time of s schedule, and part of the primary key.     |
| energy_amounts    | FLOAT[]     | *Not exactly sure.*                                          |
| prices            | FLOAT[]     | *Not exactly sure.*                                          |
| timestamps        | TIMESTAMP[] | *Not exactly sure.*                                          |
| <u>vehicle_id→configurations</u> | INTEGER     | The configuration or car linked to a schedule, and part of the primary key. |
| force_chargecost  | FLOAT       | *Not exactly sure.*                                          |

### bookings

The charging schedules from `chargingschedules` are based on the times at which the vehicles are not driving, and thus connected to the grid. The entries from the `bookings` table represents the time at which the cars are driving and thus not charging. The scheme of the `bookings` table is shown below.

| Column name      | Type                        | Explanation                                                  |
| ---------------- | --------------------------- | ------------------------------------------------------------ |
| <u>vehicleid</u> | INTEGER                     | The primary key and integer identifier of a booking. While it is not a foreign key, it is most likely connected to the attribute `configurations.cid`. |
| starttime        | TIMESTAMP WITHOUT TIME ZONE | The time at which the car starts driving, i.e. is disconnected from the grid. |
| endtime          | TIMESTAMP WITHOUT TIME ZONE | The time at which the car stops driving, i.e. is re-connected to the grid. |
| tripmilage       | DOUBLE PRECISION            | The number of miles the car has driven while disconnected from the grid.                      |
