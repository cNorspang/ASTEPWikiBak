---
title: ts1
description: The ts1 database stores the data needed to predict future electricity prices as well as the predictions
published: true
date: 2020-08-26T12:57:02.451Z
tags: 
editor: undefined
---

# ts1

> NOTE: This page reflects the state of the database at the end of the Spring 2020 semester.
> NOTE: This page was not created by the original creators of the database.
{.is-info}

The `ts1` database is tied to the [2018 Energy](/services/energy) service and stores information about the prices and production of electricity in Denmark.

## Tables

The database contains 3 tables:

- `dk1`
- `forecasts`

### dk1

The `dk1` table contains a history of the hourly electricity production and prices of Denmark. These data were provided by [Nord Pool](https://www.nordpoolgroup.com/). The scheme of the `forecasts` table is seen below.

| Column name                  | Type  | Explanation                                           |
| ---------------------------- | ----- | ----------------------------------------------------- |
| <u>date</u>                  | FLOAT | The time at which this measurement/log was made.      |
| consumption_hourly           | FLOAT | The amount of power used per hour.                    |
| consumption_prognosis_hourly | FLOAT | *Don't know*.                                         |
| price_spot_hourly            | FLOAT | The best electricity price at the time of this entry. |
| production_hourly            | FLOAT | *Probably the current electricity production?*        |
| wind_power_prognosis_hourly  | FLOAT | *Don't know*.                                         |
| wind_power_production_hourly | FLOAT | *Probably the current power production form wind*.    |

### forecasts

The `forecasts` table contains the energy price predictions produced by the [2018 Energy](/services/energy) service. The scheme of the `forecasts` table is seen below.

| Column name | Type                        | Explanation                             |
| ----------- | --------------------------- | --------------------------------------- |
| <u>date</u> | TIMESTAMP WITHOUT TIME ZONE | The time and primary key of a forecast. |
| price       | DOUBLE PRECISION            | The expected electricity price.         |

