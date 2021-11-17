---
title: Creator
description: 
published: true
date: 2021-11-17T11:55:30.042Z
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