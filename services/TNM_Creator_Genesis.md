---
title: Creator
description: 
published: true
date: 2021-11-11T12:02:43.030Z
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
The [data_model.py](#data-model-file) below shows : line 2 an example of the node data that is recieved from a database request, line 7 a node object `SwNode`, and line 17 a `nodeConversionScheme` translating from datarow to node object. line 30 example of the edge data that is recieved from a database request, line 39 an edge object `SwNode`, and line 51 a `edgeConversionScheme` translating from datarow to edge object. 
  ``` python
    """
      DB: sw601f20_routing, Table: node
      [RealDictRow([('node_id', 1),
                  ('lon', 9.12668762639212),
                  ('lat', 55.7336881175717)]),
  """
  SwNode = {
              "node_id": 0,#int
              "weight": 0.0,#dec
              "data":{
                  "longitude" : 0.0,#dec
                  "latitude" : 0.0000000000000#dec
              },
              "edges": {} #TODO: change list to dictionary
          }

  def SwNodeConversionScheme(row):
      node = {}#SwNode 
      node["node_id"]= row["node_id"]
      node["node_weight"]= 0.0
      node["data"]= {
          "longitude" : row["lon"],
          "latitude" : row["lat"]
      }
      node["edges"]= {} 

      return node

  """
      DB: sw601f20_routing, Table: Edge
      [RealDictRow([('edge_id', 139263),
                  ('edge_basenode', 1),
                  ('distance', 45.83),
                  ('edge_name', 'Åstvej'),
                  ('highway', 'residential'),
                  ('maxspeed', ''),
                  ('edge_adj', 548349)]),
  """
  SwEdge = {
              "edge_id":0,#int  
              "to_node_id": 0,#int
              "weight": 0.0,#dec
              "data":{
                  "distance": 0.00,#dec
                  "road_name": "example road",#string                        
                  "road_type": "example roadtype",#string
                  "maxs_peed": 0#int
              }
          }

  def SwEdgeConversionScheme(row):
      edge = {}#SwEdge
      edge["edge_id"]= row["edge_id"]
      edge["to_node_id"]= row["edge_adj"] 
      edge["edge_weight"]= 0.0

      edge["data"]={
          "distance" : row["distance"],
          "road_name" : row["edge_name"],
          "road_type" : row["highway"],#UNDEFINED 
          "max_speed" : row["maxspeed"],#UNDEFINED
      }
      return edge
  ```
When a microservice introduces new data into the TNM, this file needs to be updated to accomodate the new data. `data_model.py` is used for defining the contents of `nodes` and `edges` and a `conversionScheme function` for each node and edge structure. The conversion functions are injected into the adapter by dependency injection when calling adapter.to_json() within the creator service as shown in the following example:
  ```python
  	adapter.to_json(
                node_conversion_scheme = SwNodeConversionScheme,
                edge_conversion_scheme = SwEdgeConversionScheme,
                edges=sw_handler.get_all('edge'),
                nodes=sw_handler.get_all('node')
                )
  ```
>    **!Note that the variable names in the function calls parameters, on the left side of the equal sign, are used within the to_json function and MUST be identical: 
  *node_conversion_scheme,
  edge_conversion_scheme,
  nodes,
  edges***
{.is-warning}

## How to insert new data
TO DO