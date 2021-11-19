---
title: Creator
description: 
published: true
date: 2021-11-19T10:19:48.446Z
tags: tnm
editor: markdown
---

# TNM Creator Service

The Creator Service handles the creation of all data needed for the [Transport Network Model RFC0020](/rfc/0020).

As such, any future user who wants to increase the amount of available data in the Creator should follow the guidelines in [How to insert new data](#how-to-insert-new-data)

Because of this, the Creator service consists primarily of two components.
- [Database connection](#database-connection)
- [The adapter](#the-adapter)

## Database connection
The Creator database is the sole owner of the [transportation_network](/databases/DB2/transportation_network) database.

To gain database access, the service holds a `database.ini` file in the creator src repo. This file holds the credentials to the database and is kept in the gitignore file.

## The adapter
The creator is responsible for serializing the initial data from the database into the TNM model. To be able to do this, it has an Adapter class in the `adapter.py` file which handles two functions.

- from_json(options) takes the options given from the Controller and uses it as input as to which data is needed for the concrete operation.
- to_json(\*\*kwargs) takes four keyword arguments, as can be seen below. Those get converted to a valid TNM model. To make the handling of this conversion easier to change, a `data_model.py` holds the different conversion functions used in the `to_json()` function.
  
### data model file
The data_model.py file contains the initial DataModel with static data, a node_conversion_scheme function, and an edge_conversion_scheme function. The purpose of the DataModel and conversion_scheem functions are to convert the database representation, which is a tuple of data rows, into a TNM representation, which is nodes and edges as specified in [RFC0020](/rfc/0020).

When a microservice introduces new data into the TNM, this file needs to be updated to accomodate the new data. `data_model.py` is used for defining the contents of `nodes` and `edges` and a `conversionScheme function` for each node and edge structure. The conversion functions are injected into the adapter by dependency injection when calling adapter.to_json() within the creator service as shown in the following example:
  ```python
  	adapter.to_json(
                node_conversion_scheme = node_conversion_scheme,
                edge_conversion_scheme = node_conversion_scheme,
                edges=db_handler.get_all('edge'),
                nodes=db_handler.get_all('node')
                )
  ```

## How to insert new data
The [transportation_network](/databases/DB2/transportation_network) database is owned by the Creator Service, and it is therefore the Creator which fetches the data from it and populates the database with data.

The creator, when run, will only fetch data, and haven't been made as a CRUD application, since it only will handle static data.

However, in the /vejman folder, the model_maker.ipync file is a Jupyter Notebook file running python, which holds all the logic and datasets, which create the database.

By dropping all tables, and rerunning the functions, the database will be recreated with any changes made. Local testing with a postgres database having the postgis extension is recommended, since the queries are very slow.

## How relations are made
Due to the complexity of the initial function creating the initial entities and relations, an example is provided to hopefully shed some light on how it is made.

The datasets "municipality_spatial" are structured as rows containing two primary pieces of information. The first is a collection of attributes associated with the primary road at this point in the dataset. The other attributes are associated with the secondary road.
This row then form the meta_information which specify that these two roads intersect at their prescribed mileages.

Each road is, at some point, the primary road in the dataset, but all primary roads are in order. This means the following algorithm was conducted, which specifies the operations being made for each new row of data in the dataset. Each dataset represents a municipality.

- First, a mileage_post id is constructed pointing to the id used in Vejman.dk, so it is possible to update it with future information.
- Then it is checked if there is a "dangling" previous segment, which  will be removed, if the current row is on a new primary road.
- Then the secondary roads mileage_post is checked. If it exists, it means it has been previously visited as a primary road, and the current primary roads mileage_post will then point to the same intersection. If not, the current primary road will create an intersection with the primary road only pointing to this intersection.
- Then, if there is a "dangling" previous segment, it will be updated with a to_id, since the dataset have continued to the next line of the dataset. After this, a new "dangling" segment will be created, with a from_id from the current dataset.

By following this logic, all intersections should be correctly created, together with the relevant entities, which can be seen in the algorithm in model_maker. If errors is found in this reasoning, this description as well as the algorithm should be changed accordingly, and recreate the database.