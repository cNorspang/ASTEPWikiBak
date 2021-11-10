---
title: transportation_network
description: 
published: true
date: 2021-11-10T19:24:52.133Z
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

Apart from following standard notation of DBS, there are these important additions to make a proper presentation of a spatial ER diagram.
- The line in the bottom of each entity describes what type of geometric information it contains.
- The extra square behind road, intersection and segment shows that these are temporal, and that their datapoint change over time.
- Some information is not present (such as the with/against terminology / empty Notes). This is due to the fact that there is data of that kind available on [vejman.dk](http://www.vejman.dk/), but it hasn't yet been needed for extraction.

## Tables

The database contains 5 tables:

- [`municipality`](#municipality)
- [`road`](#road)
- [`intersection`](#intersection)
- [`segment`](#segment)
- [`mileage_post`](#mileage_post)

>Presently, all tables only have the most recent datapoint, but since most have different data at different times, the inclusion of temporal data extension tables such as Rules, Construction, etc. might be beneficial to expand on later if time allows it.
{.is-info}

### base attributes

The `base attributes` are attributes shared between all the different entities, and primarily contains meta data. 

| **Column Name** | **Type** | Explanation                  |
| --------------- | --------  | ---------------------------- |
| <u>id</u>       | INTEGER   | Unique identifier in the database  |
| source          | STRING    | Describes the source of the data   |
| source_id       | INTEGER   | Unique identier in the source      |
| geom            | REFERENCE | Contains the geometry, created by postgis |

The current `sources` are:
[vejman.dk](http://vejman.dk)

The `geom` attribute is created by the `postgis` extension of the `postgresql` database. It saves the 

### municipality

The table `municipality` represents the administrative and regional entity that manages and contains all the road infrastructure.

| **Column Name** | **Type** | Explanation                             |
| --------------- | -------- | ----------------------------             |
| base_attribs    | MULTI    | Read [base attributes](#base-attributes) |
| name            | STRING   | The daily-speak name of the municipality |
| country         | STRING   | The daily-speak name of the country      |

The current municipalities are:
Aalborg

The current countries are:
Denmark

### road

The table `road` represents a single unbroken road inside a municipality. The road contains all the [mileage_posts](#mileage_post) which runs along its path, and is the closest representation of what is present in [vejman.dk](http://vejman.dk).

| **Column Name** | **Type** | Explanation                             |
| --------------- | -------- | ----------------------------             |
| base_attribs    | MULTI    | Read [base attributes](#base-attributes) |
| municipality_id | REFERENCE| ForeignKey to municipality               |
| name            | STRING   | The daily-speak name of the road         |
| description     | STRING   | Describes the general path of the road   |

### intersection

The table `intersection` describes areas where two or more roads intersect. Intersections which have [mileage_posts](#mileage_post) from different municipalities signify the borders between the different municipalities.

| **Column Name** | **Type** | Explanation                             |
| --------------- | -------- | ----------------------------             |
| base_attribs    | MULTI    | Read [base attributes](#base-attributes) |
| type            | STRING   | The type of intersection |
| signal_control  | BOOL     | Whether the intersection has signal control |

The current intersections types are:
TO BE DONE

### segment

The table `segment` describes a segment of a road, which is between two intersections. Attributes described as "with_attribute" designate that the attribute only counts for the side of the road going in the direction From -> To, whereas "against_attribute" designate the opposite direction.

| **Column Name** | **Type** | Explanation                             |
| --------------- | -------- | ----------------------------             |
| base_attribs    | MULTI    | Read [base attributes](#base-attributes) |
| from_id         | REFERENCE| Going from the ForeignKey to mileage_post|
| to_id           | REFERENCE| Going to the ForeignKey to mileage_post  |
| length          | INTEGER  | Length in meters, derived from mileage_posts |
| type            | STRING   | ?     |
| type_max_speed  | INTEGER   | ?     |
| set_max_speed   | INTEGER   | ?     |
| recommended_speed|INTEGER   | ?     |
| one_way         | STRING   | ?     |
| mean_speed      | INTEGER   | ?     |
| daily_year      | INTEGER   | ?     |
| daily_july      | INTEGER   | ?     |
| daily_trucks    | INTEGER   | ?     |
| daily_10_axle   | INTEGER   | ?     |
| max_axle_load   | INTEGER   | Max accepted axle load    |
| max_height      | INTEGER   | ?     |
| max_length      | INTEGER   | ?     |
| max_weight      | INTEGER   | ?     |

### mileage_post

The table `mileage_post` describes the mileage posts ('kilometreringspæle' in danish) which is alongside the road.

| **Column Name** | **Type** | Explanation                             |
| --------------- | -------- | ----------------------------             |
| base_attribs    | MULTI   | Read [base attributes](#base-attributes) |
| road_id         | REFERENCE| ForeignKey to road                      |
| intersection_id | REFERENCE| ForeignKey to intersection               |
| mileage         | INTEGER | How far up the road the mileage post is in meters |

## How to add / change data

In the [TNM Creator Microservice](/services/TNM_Creator_Genesis), a specific folder called `vejman` is responsible for how the database has been setup.
In the folder, a jupyter notebook file called `model_maker` can be run to setup the database from scratch, if any problems are encountered, or data is corrupted.