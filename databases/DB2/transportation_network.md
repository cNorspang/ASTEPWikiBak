---
title: transportation_network
description: 
published: true
date: 2021-12-19T20:33:57.204Z
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

As of 2021, the database contains 156525 individual road segments, and 142541 individual intersections.

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
- The MULTI data type references the [base attributes](#base-atributes). Since it is used in all entities, it is described seperatly in its own [section](#base-attributes).
- The ENUM data type is just a simple STRING datatype, with the added caveat that there is a condition as to what values the string can be, described below the given table.

>Presently, no table contain any temporal data. All attributes should be ForeignKeys to their own table, where the data could change at different times (The amount of traffic would be different from 2019 to 2020 for example). This was however not implemented, due to time constraints, and it presently only shows data from 2021.
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

The `geom` attribute is created by the `postgis` extension of the `postgresql` database, and makes it possible to save spatial data. The `geom` column therefore references a seperate table, which is created based on the type of geometry created (ie. a `POINT` type has a table with an X and Y column, whereas `POINTZ` type also has a Z column (in reality it is stored in a single column as a unique hash, but the explanation can be helpful to understand the idea)).
Each `geom` attribute also saves what type of coordinate system is used to interpret the coordinates. The coordinates from vejman are using the UTM 32 system, having SRID 25832. These can then be transformed into SRID 4326, which is the regular longitude/latitude used by most maps.
Bornholm however uses SRID 25833, but Bornholm isn't  presently part of the database.

### municipality

The table `municipality` represents the administrative and regional entity that manages and contains all the road infrastructure. Be aware that roads owned by the state are in fact managed/contained by the administrative entity "Vejdirektoratet" in the real world, but that this information has been omitted due to it being found irrelevant.

| **Column Name** | **Type** | Explanation                             |
| --------------- | -------- | ----------------------------             |
| base_attribs    | MULTI    | Read [base attributes](#base-attributes) |
| name            | ENUM     | The daily-speak name of the municipality |
| country         | ENUM     | The daily-speak name of the country      |

The current `municipality` values are:
Statsbaner (all expresshighways), Aalborg, Aero, Albertslund, Allerod, Ballerup, Billund, Brondby, Bronderslev, Dragor, Egedal, Esbjerg, Faaborg-Midtfyn, Fano, Favrskov, Faxe, Fredensborg, Frederiksberg, Frederikshavn, Frederikssund, Furerso, Gentofte, Gladsaxe, Glostrup, Greve, Gribskov, Guldborgsund, Haderslev, Halsnaes, Herlev, Hillerod, Hjorring, Hoje-Taastrup, Holbaek, Holstebro, Horsens, Horsholm, Hvidovre, Ikast-Brande, Ishoj, Jammerbugt, Kalundborg, Kobenhavn, Koge, Laeso, Langeland, Lejre, Lemvig, Lolland, Mariagerfjord, Morso, Nordfyns, Odder, Odsherred, Rebild, Ringkobing-Skjern, Rodovre, Roskilde, Rudersdal, Samso, Silkeborg, Skanderborg, Skive, Slagelse, Solrod, Sonderborg, Stevns, Struer, Svendborg, Syddjurs, Taarnby, Tonder, Vallensbaek, Varde, Vejle, Vesthimmerlands, Vordingborg

The current `country` values are:
Denmark

### road

The table `road` represents a single unbroken road inside a `municipality`. The `road` contains all the [mileage_posts](#mileage_post) which runs along its path. The distance between two `mileage_posts` are the smallest distance representation of what is present in [vejman.dk](http://vejman.dk).

| **Column Name** | **Type** | Explanation                             |
| --------------- | -------- | ----------------------------             |
| base_attribs    | MULTI    | Read [base attributes](#base-attributes) |
| municipality_id | REFERENCE| ForeignKey to municipality               |
| name            | STRING   | The daily-speak name of the road         |
| description     | STRING   | Describes the general path of the road   |

### intersection

The table `intersection` describes areas where two or more roads intersect. In this database, all `intersections` can be combined with the `segments`, giving a graph representation, where an example of this is the [TNM Service](/rfc/0020).

| **Column Name** | **Type** | Explanation                             |
| --------------- | -------- | ----------------------------             |
| base_attribs    | MULTI    | Read [base attributes](#base-attributes) |
| is_border       | BOOL     | Designates bordering between 2 or more municipalities|
| type            | ENUM     | The functional type of intersection |
| signal_control  | BOOL     | Whether the intersection has signal control |

The current intersections `type` values are:
regular, roundabout, driveway, drivein, other, railway, ramp

### segment

The table `segment` describes a segment of a road, which is between two intersections.
The `segment` holds a `to_id` and `from_id` which are ForeignKeys to a `mileage_post` id, which signifies where the `segment` starts and ends. Each of the `mileage_posts` always hold a reference to an `intersection` and the `road` which the `segment` is part of.
Be aware that since `segment` is purely made by this database, and doesn't exist on [vejman.dk](http://vejman.dk), segments from [vejman.dk](http://vejman.dk) won't have a `source_id`.

| **Column Name** | **Type** | Explanation                             |
| --------------- | -------- | ----------------------------             |
| base_attribs    | MULTI     | Read [base attributes](#base-attributes) |
| from_id         | REFERENCE | Segment starts from the mileage_post id|
| to_id           | REFERENCE | Segment ends at the mileage_post id  |
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

The current segment type values are in quotes:
"expressway", "highway","rural local road, primary", "rural local road, secundary", "rural local road, tertiary", "city road, primary", "city road, secundary", "city local road, primary", "city local road, secundary", "city local road, tertiary", "rural path, primary", "rural path, secundary", "city path, primary", "city path, secundary", "rural green path, primary", "rural green path, secundary", "city green path, primary", "city green path, secundary", "parking facility", "resting facility", "city bicycle path", "rural bicycle path"
Naming follows the order presented in the official documentation in danish, found [here](https://vej08.vd.dk/vis/help/B4831.htm)

The current one_way values are:
"with", "against", "none"

### mileage_post

The table `mileage_post` describes the mileage posts ('kantp??le' in danish) which are those white posts with a yellow marker in the top, which runs alongside any given `road` in Denmark. See [here](http://leverandorportal.vejdirektoratet.dk/Udbuds%20specifikke%20dokumenter/BILAG-LDV-DRI-7-9_Elementbeskrivelse-KANTP%C3%86LE-03042012.pdf) for a formal definition.

| **Column Name** | **Type** | Explanation                             |
| --------------- | -------- | ----------------------------             |
| base_attribs    | MULTI   | Read [base attributes](#base-attributes) |
| road_id         | REFERENCE| ForeignKey to road                      |
| intersection_id | REFERENCE| ForeignKey to intersection               |
| mileage         | INTEGER | How far up the road the mileage post is in meters |

## How to add / change data

In the [TNM Creator Microservice](/services/TNM_Creator_Genesis), a specification for how to add new data has been described.