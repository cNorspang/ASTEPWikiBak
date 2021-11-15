---
title: transportation_network
description: 
published: true
date: 2021-11-15T13:49:45.973Z
tags: tnm, rfc0020
editor: markdown
---

# The transportation_network database

> NOTE: This page reflects the state of the database at the end of the 2021 semester
{.is-info}

The `transportation_network` database contains data derived from [vejman.dk](http://www.vejman.dk/), which describes the road infrastructure and use in Denmark.

The `transportation_network` database is likewise managed by the [TNM Creator Microservice](/services/TNM_Creator_Genesis), and should therefore only be accessed through the endpoints of that service alone, following the microservice infrastructure.

The database stores all the relationsships as a description of a miniworld, containing municipalities, roads, intersections, road segments and mileage posts, as described in the [ER Diagram](#er-diagram).

The database form the data background of the [Transport Network Model RFC0020](/rfc/0020), but the [TNM Creator Microservice](/services/TNM_Creator_Genesis) can be expanded to provide more and different representations of the data, if needed.

## ER diagram

The ER Diagram presented below describes the structure of the different entities in the transportation_network database. The concrete attributes and their meaning are defined in the [Tables](#tables) section.
![tnm_er_diagram.png](/database/tnm_er_diagram.png)
*The corresponding draw io file is available [here](/database/tnm_er_diagram.drawio)*

Apart from following standard notation of DBS, there are these important additions to make a proper presentation of a temporal spatial ER diagram, as well as some clarifications.
- The text in the bottom of each entity describes what type of geometric information it contains as defined by postgis.(Multiline,Point...)
- G denotes Geometric data, T denotes Temporaldata. 
- The extra square behind road, intersection and segment shows that these are temporal (T), and that their datapoint change over time.
- Dotted lines show from which data or relation, a derived attribute can be derived.
- The notes in the bottom of the diagram describe the entities corresponding multi-attribute on either segment or intersection.
- Some of the notes in the bottom are empty. This is due to the fact that there is data of that kind available on [vejman.dk](http://www.vejman.dk/), but it hasn't yet been needed for extraction.

## Tables

The database contains 5 tables:

- [`municipality`](#municipality)
- [`road`](#road)
- [`intersection`](#intersection)
- [`segment`](#segment)
- [`mileage_post`](#mileage_post)

Each table will have a short summary of its semantic meaning, then an overview of its attributes are presented. Names are written as the columns in the database, following its datatype and a short semantic explanation.

The datatypes should be self explanatory, however, there are two exceptions.
- The MULTI data type references the fact that [base attributes](#base-atributes) since it is used in all entities, it is described seperatly in its own [section](#base-attributes).
- The ENUM data type is just a simple STRING datatype, with the added caveat that there is a condition as to what values the string can be, described below the given table.

>Presently, all tables only have the most recent datapoint, but since most have different data at different times, the inclusion of temporal data extension tables might be beneficial to expand on later if time allows it.
{.is-info}

### base attributes

The `base attributes` are attributes shared between all the different entities, and primarily contains meta data. 

| **Column Name** | **Type** | Explanation                  |
| --------------- | --------  | ---------------------------- |
| <u>id</u>       | INTEGER   | Unique identifier in the database  |
| source          | ENUM      | Describes the source of the data   |
| source_id       | INTEGER   | Unique identier in the source      |
| geom            | REFERENCE | Contains the geometry, created by postgis |

The current `source` values are:
[vejman.dk](http://vejman.dk)

The `geom` attribute is created by the `postgis` extension of the `postgresql` database, and makes it possible to save spatial data.

### municipality

The table `municipality` represents the administrative and regional entity that manages and contains all the road infrastructure. Be aware that roads owned by the state are in fact managed/contained by the administrative entity "Vejdirektoratet" in the real world, but that this information has been omitted due to it being found irrelevant.

| **Column Name** | **Type** | Explanation                             |
| --------------- | -------- | ----------------------------             |
| base_attribs    | MULTI    | Read [base attributes](#base-attributes) |
| name            | ENUM     | The daily-speak name of the municipality |
| country         | ENUM     | The daily-speak name of the country      |

The current `municipality` values are:
Aalborg

The current `country` values are:
Denmark

### road

The table `road` represents a single unbroken road inside a `municipality`. The `road` contains all the [mileage_posts](#mileage_post) which runs along its path, and is the closest representation of what is present in [vejman.dk](http://vejman.dk).

| **Column Name** | **Type** | Explanation                             |
| --------------- | -------- | ----------------------------             |
| base_attribs    | MULTI    | Read [base attributes](#base-attributes) |
| municipality_id | REFERENCE| ForeignKey to municipality               |
| name            | STRING   | The daily-speak name of the road         |
| description     | STRING   | Describes the general path of the road   |

### intersection

The table `intersection` describes areas where two or more roads intersect.

| **Column Name** | **Type** | Explanation                             |
| --------------- | -------- | ----------------------------             |
| base_attribs    | MULTI    | Read [base attributes](#base-attributes) |
| is_border       | BOOL     | Designates bordering between 2 or more municipalities|
| type            | ENUM     | The functional type of intersection |
| signal_control  | BOOL     | Whether the intersection has signal control |

The current intersections `type` values are:
TO BE DONE

### segment

The table `segment` describes a segment of a road, which is between two intersections. A segment is likewise always part of a single `road`.
Be aware that since `segment` is purely made by this database, and doesn't exist on [vejman.dk](http://vejman.dk), the segments from that datasource won't have a `source_id`.

| **Column Name** | **Type** | Explanation                             |
| --------------- | -------- | ----------------------------             |
| base_attribs    | MULTI     | Read [base attributes](#base-attributes) |
| from_id         | REFERENCE | Going from the ForeignKey to mileage_post|
| to_id           | REFERENCE | Going to the ForeignKey to mileage_post  |
| length          | INTEGER   | Length of the segment in meters           |
| with_slope			| DECIMAL   | The slope of the segment, going From -> To  |
| type            | ENUM      | Designates the expected usage of the road   |
| type_max_speed  | INTEGER   | Max speed as derived from the road type     |
| set_max_speed   | INTEGER   | Max speed as set by the municipality        |
| recommended_speed|INTEGER   | Recommended speed as set by the municipality|
| one_way         | ENUM      | Designates whether its a one-way street     |
| mean_speed      | INTEGER   | The average mean speed on a day in a year  |
| daily_year      | INTEGER   | The average vehicles on a day in a year     |
| daily_july      | INTEGER   | The average vehicle on a day in july     |
| daily_trucks    | INTEGER   | The average trucks on a day in a year     |
| daily_10_axle   | INTEGER   | The avg. 10-axle vehicles on a day in a year |
| max_axle_load   | DECIMAL   | Max accepted axle load of vehicle in tons    |
| max_height      | DECIMAL   | Max accepted height of vehicle in meters     |
| max_length      | DECIMAL   | Max accepted length of vehicle in meters     |
| max_weight      | DECIMAL   | Max accepted weight of vehicle in tons       |

The current segment type values are:
TO BE DONE

The current one_way values are:
"with", "against", "none"

### mileage_post

The table `mileage_post` describes the mileage posts ('kilometreringspæle' in danish) which is alongside the `road`.

| **Column Name** | **Type** | Explanation                             |
| --------------- | -------- | ----------------------------             |
| base_attribs    | MULTI   | Read [base attributes](#base-attributes) |
| road_id         | REFERENCE| ForeignKey to road                      |
| intersection_id | REFERENCE| ForeignKey to intersection               |
| mileage         | INTEGER | How far up the road the mileage post is in meters |

## How to add / change data

In the [TNM Creator Microservice](/services/TNM_Creator_Genesis), a specific folder called `vejman` is responsible for how the database has been setup.
In the folder, a jupyter notebook file called `model_maker` can be run to setup the database from scratch, if any problems are encountered, or data is corrupted.