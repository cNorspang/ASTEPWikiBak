---
title: solardata
description: Currently, the use of the solardata database is unknown, but it is assumed to contain data related to solar panels
published: true
date: 2020-08-31T11:30:57.646Z
tags: 
editor: undefined
---

# solardata
> NOTE: This page reflects the state of the database at the end of the Spring 2020 semester.
> NOTE: This page was not created by the original creators of the database.
> NOTE: What services (if any) that use the database is currently unknown. Any information on this page is therefore assumed.
{.is-info}

*solardata* is a database stored on DB2. It is currently unknown what services use the database, and therefore, what all the data represents.

The database contains three tables:
- lowry_station
- solartec
- vehicle_testing
## lowry_station

Purpose of table is unknown.

| Column name            | Type                        | Explanation                                                  |
| ---------------------- | --------------------------- | ------------------------------------------------------------ |
| id                     | BIGINT                      | Unique identifier of measurement                             |
| date                   | date                        | Date of measurement                                          |
| mst                    | time without time zone      | Precise time of day                                          |
| global_horizontal      | DOUBLE PRECEISION           | Unknown                                                      |
| direct_normal          | DOUBLE PRECEISION           | Unknown                                                      |
| diffuse_horizontal     | DOUBLE PRECEISION           | Unknown                                                      |
| global_uncorrected     | DOUBLE PRECEISION           | Unknown                                                      |
| direct_uncorrected     | DOUBLE PRECEISION           | Unknown                                                      |
| diffuse_uncorrected    | DOUBLE PRECEISION           | Unknown                                                      |
| direct_bird_estimate   | DOUBLE PRECEISION           | Unknown                                                      |
| avg_wind_speed_10m     | DOUBLE PRECEISION           | Assumed to be the average wind-speed measured in m/s.        |
| peak_wind_speed_10m    | DOUBLE PRECEISION           | Assumed to be highest-measured wind-speed in m/s.            |
| avg_wind_direction_10m | DOUBLE PRECEISION           | Assumed to be direction of the wind in degrees. Zero-state is unknown. |
| mst_timestamp          | timestamp without time zone | Date and time of measurement                                 |

## solartec
Purpose of table is unknown.

| Column name                    | Type                        | Explanation                                                  |
| ------------------------------ | --------------------------- | ------------------------------------------------------------ |
| id                             | BIGINT                      | Entry's unique identifier                                    |
| date                           | date                        | Date of the measurement                                      |
| mst                            | time without time zone      | specific time of the measurement                             |
| global_horiontal_zenith_corr   | DOUBLE PRECISION            | Unknown                                                      |
| global_horizontal              | DOUBLE PRECISION            | Unknown                                                      |
| direct_normal                  | DOUBLE PRECISION            | Unknown                                                      |
| direct_blackphoton_top         | DOUBLE PRECISION            | Unknown                                                      |
| direct_blackphoton_mid         | DOUBLE PRECISION            | Unknown                                                      |
| direct_blackphoton_bot         | DOUBLE PRECISION            | Unknown                                                      |
| diffuse_horrizontal            | DOUBLE PRECISION            | Unknown                                                      |
| avg_wind_speed_10m             | DOUBLE PRECISION            | Assumed to be the average wind speed measured in m/s.        |
| peak_wind_speed_10m            | DOUBLE PRECISION            | Assumed to be the peak wind speed measured in m/s.           |
| avg_wind_speed_std_dev_10m     | DOUBLE PRECISION            | Unknown                                                      |
| avg_wind_direction_10m         | DOUBLE PRECISION            | Assumed to be the average wind direction, measured in degrees. Zero-state is unknown. |
| wind_direction_pk_ws_10m       | DOUBLE PRECISION            | Unknown                                                      |
| avg_wind_direction_std_dev_10m | DOUBLE PRECISION            | Unknown                                                      |
| mst_timestamp                  | timestamp without time zone | Timestamp of measurement.                                    |

## vehicle_testing
Purpose of table is unknown.
| Column name           | Type                        | Explanation                                                  |
| --------------------- | --------------------------- | ------------------------------------------------------------ |
| id                    | BIGINT                      | Unique identifier of measurement                             |
| date                  | date                        | date of the measurement                                      |
| mst                   | time without time zone      | specific time of measurement                                 |
| global_horizontal     | DOUBLE PRECISION            | Unknown                                                      |
| global_secondary      | DOUBLE PRECISION            | Unknown                                                      |
| global_uncorrected    | DOUBLE PRECISION            | Unknown                                                      |
| direct_uncorrected    | DOUBLE PRECISION            | Unknown                                                      |
| diffuse_uncorrected   | DOUBLE PRECISION            | Unknown                                                      |
| avg_wind_speed_3m     | DOUBLE PRECISION            | Average wind-speed measured in m/s                           |
| peak_wind_speed_3m    | DOUBLE PRECISION            | Peak wind-speed measured in m/s                              |
| avg_wind_direction_3m | DOUBLE PRECISION            | Average wind direction measured in degrees. Zero-state is unknown. |
| mst_timestamp         | timestamp without time zone | Time and date of measurement.                                |

