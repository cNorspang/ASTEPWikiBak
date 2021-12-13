---
title: Creator
description: 
published: true
date: 2021-12-13T08:36:08.979Z
tags: tnm
editor: markdown
---

# TNM Creator Service

The Creator Service handles the creation of all data needed for the [Transport Network Model RFC0020](/rfc/0020).

As such, any future user who wants to increase the amount of available data in the Creator should follow the guidelines in [How to insert new data](#how-to-insert-new-data)

Because of this, the Creator service consists primarily of two components.
- [Database connection](#database-connection)
- [The adapter](#the-adapter)

After this, the more practical questions are answered in
- [How to run it locally](#how-to-run-it-locally)
- [How to insert new data](#how-to-insert-new-data)
- [How relations are made](#how-relations-are-made)
- [What is missing work](#what-is-missing-work)

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
                edge_conversion_scheme = edge_conversion_scheme,
                edges=db_handler.get_all('edge'),
                nodes=db_handler.get_all('node')
                )
  ```

## Input
The Creator accepts an `options` object, which is used to restrict the queries the Creator makes.

```json
{
    "only_filled_data": <bool>,
    "node_limit": <integer> of false
    "municipality": <string> or false
}
```
`only_filled_data` is whether to only get the filled data or not
`node_limit` is how many nodes one wants as a maximum (`false` means everything)
`municipality` is the name of the municipality one wants data from (see in [transportation_network](/DB2/transportation_network) for names). If set to `false` will give all municipalities.

## Output
The Creator outputs a TNM, as described in [RFC0020](/rfc/0020).

```json
{
    "meta_data": {
        "max_length": <int>,
        "min_length": <int>,
        "max_slope": <float>,
        "min_slope": <float>,
        "max_set_max_speed": <int>,
        "min_recommended_speed": <int>,
        "max_mean_speed": <float>,
        "min_mean_speed": <float>,
        "max_daily_year": <float>,
        "min_daily_year": <float>,
        "max_daily_july": <float>,
        "min_daily_july": <float>,
        "max_daily_trucks": <float>,
        "min_daily_trucks": <float>
    },
    "vehicle": {
        "id": <int>,
        "name": <string>,
        "data": {
            "top_speed": <float>,
            "milage": <float>,
            "max_fuel": <float>
        }
    },
    "nodes": {
        "<int>": {
            "id": <int>,
            "weight": <float>,
            "data": {
                "longitude": <float>,
                "latitude": <float>,
                "country": <string>,
                "municipality": <string>,
                "is_border": <bool>,
                "type": <string>,
                "signal_control": <bool>
            },
            "edges": {
                "<int>": {
                    "id": <int>,
                    "to_node_id": <int>,
                    "from_node_id" : <currentNode id>,
                    "weight": <float>,
                    "data": {
                        "length": <int>,
                        "slope": <float>,
                        "type": <string>,
                        "type_max_speed": <int>,
                        "set_max_speed": <int>,
                        "recommended_speed": <int>,
                        "mean_speed": <float>,
                        "daily_year": <float>,
                        "daily_july": <float>,
                        "daily_trucks": <float>,
                        "daily_10_axle": <float>,
                        "fuel_station": <bool>,
                        "max_axle_load": <float>,
                        "max_height": <float>,
                        "max_length": <float>,
                        "max_weight": <float>
                    }
                }
            }
        }
    }
}
```
## Endpoints
All endpoints can be seen in the `service.py` file.

### main
The main endpoint returns a valid TNM model as default, used in the TNM Service (RFC 0020)
The option `only_filled_data` makes it return only edges which have filled data. This does not include `max_weight`, `max_length`, etc. and `mean_speed`, since there sadly isn't any data on those for any of the edges at all in the database.
The option `node_limit` sets a limit for how many nodes can be taken from a query. The reason it is a node limit, is because that road segments gets "split" into a bidirectional graph, making it point in two directions. 


## How to run it locally
To run the creator locally, first you have to create a postgres server on your local computer, where you activate the postgis extension to use spatial  data.
This is done by writing the following query to the database:
- CREATE EXTENSION postgis;

Next, locate the database.ini file in the creator root directory. Change the information in the file to the following

```
	[transportation_network]
  host=host.docker.internal
  database=<your_db_name>
  user=<your_username>
  password=<your_password>
```
The `host.docker.internal` is a way for the docker container to access your local machine, whereas if you write `localhost`, it will instead point to the virtual machine that the container is hosting.
The other data is configured by you when you setup the database.

The final step to run the service locally, is to build and run the container.
In your terminal, go to the directory /your/path/to/tnn-creator-service, and run:
- `docker build --tag creator .`
- `docker run -p 5000:5000 creator`

The `docker run` command runs the commands found in the `Dockerfile`, including a Continious Integration flow, where it runs all the tests written using `pytest`.
Now, when you access `localhost:5000/`, you will go to the root url defined in service.py. If you access `localhost:5000/main`, the main function will be called and should return a full TNM model.

If you have trouble terminating the docker file, you can run:
- `docker container ls`
- `docker rm -f <CONTAINER_ID>`

Inser the container ID found through the ls command, and the docker container will be forced (-f) to terminate.

## How to insert new data
To get new data to the database, it might be possible to get access to vejman.dk by contacting [Institut for By, Byggeri og Miljø](https://vbn.aau.dk/da/organisations/build-institut-for-byggeri-by-og-milj%C3%B8). 

The [transportation_network](/databases/DB2/transportation_network) database is owned by the Creator Service, and it is therefore the Creator which fetches the data from it and populates the database with data.

The creator, when run, will only fetch data, and haven't been made as a CRUD application, since it only will handle static data.

However, in the /vejman folder, the model_maker.ipync file is a Jupyter Notebook file running python, which holds all the logic and datasets, which create the database.

By dropping all tables, and rerunning the functions, the database will be recreated with any changes made. Local testing with a postgres database having the postgis extension is recommended, since the queries are very slow.

### How relations are made
Due to the complexity of the initial function creating the initial entities and relations, an example is provided to hopefully shed some light on how it is made.

The datasets "municipality_spatial" are structured as rows containing two primary pieces of information. The first is a collection of attributes associated with the primary road at this point in the dataset. The other attributes are associated with the secondary road.
This row then form the meta_information which specify that these two roads intersect at their prescribed mileages.

Each road is, at some point, the primary road in the dataset, but all primary roads are in order. This means the following algorithm was conducted, which specifies the operations being made for each new row of data in the dataset. Each dataset represents a municipality.

- First, a mileage_post id is constructed pointing to the id used in Vejman.dk, so it is possible to update it with future information.
- Then it is checked if there is a "dangling" previous segment, which  will be removed, if the current row is on a new primary road.
- Then the secondary roads mileage_post is checked. If it exists, it means it has been previously visited as a primary road, and the current primary roads mileage_post will then point to the same intersection. If not, the current primary road will create an intersection with the primary road only pointing to this intersection.
- Then, if there is a "dangling" previous segment, it will be updated with a to_id, since the dataset have continued to the next line of the dataset. After this, a new "dangling" segment will be created, with a from_id from the current dataset.

By following this logic, all intersections should be correctly created, together with the relevant entities, which can be seen in the algorithm in model_maker. If errors is found in this reasoning, this description as well as the algorithm should be changed accordingly, and recreate the database.

## What is missing work
The creator creates a proper TNM model, but has some shortfalls which could be expanded upon.

- The creator does not fill the geometry of municipality, road and segment entities.
- The creator does not verify that the algorithm described in [how relations are made](#how-relations-are-made) is fully correct. Specifically, it does not verify that a secondary road always will be visited again as a primary road later on in the dataset.
- The creator presently only has data on Aalborg municipality. This means Aalborg and Denmark are static objects.
- Likewise, it does not handle intersections which are bordering other municipalities.
- Vehicle is presently a static object, but could be made into a seperate table.
- Not all mileage_posts have a proper coordinate. An Expector service could be made to "fill out the gaps" of these, by comparing to mileage_posts closeby.
- The database presently has no temporal data tables, which could be created instead of the present use of static information on a road segment and intersections.
- Right now, the Creator returns all the data it can. It could be useful to choose the amount of data retrieved.
- And many more!