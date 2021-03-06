---
title: TNM Combiner WeightCombiner
description: 
published: true
date: 2021-11-19T13:14:40.868Z
tags: tnm
editor: markdown
---

# The TNM Combiner
The **TNM combiner** takes a list of "_Microservices_", each containing information about the microservice, how the user prioritise the service and a _Transport Network Model_ [(**TNM**)]() as input. The WeightCombiner combines the received models into a single model, accounting for the users preferences.

The code is available on [Gitlab](https://daisy-git.cs.aau.dk/astep-2021/astep-6).

**Combined Weight Equation**

The combined weight of each _node_ and _edge_ is calculated using the following equation: 
  
  $$W_{r} = \sum_{i=1}^{n}W_{i}P_{i}$$
  
  Where:
  - $W_{r}$ is the combined weight of the _node_ or _edge_.
  - $W_i$ is the weight on the current _node_ or _edge_.
  	- Where $0 \le W_i \le 1$
  - $P_i$ is the priority of the current model, given by the user.
  	- Where $0 \le P_x \le 1$ and $\sum_{i = 1}^{n} P_i = 1$
  - $n$ is the number of models
  

## Content 
- [Input Format](#input-format)
- [Output Format](#output-format)
- [End Points](#endpoints)


## Input Format
The accepted _JSON_ input format:

```json
[
    {
        "name": <string>,
        "url": <string>,
        "userPref": <float>,
        "model": {
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
    }
]
```
**Attributes**
- **"name"** : _The name of the last microservice, which altered the model._
- **"url"** : _The url of the last microservice._
- **"userpref"** : _The priority (chosen by the user) for the model._


## Output Format
The generated _JSON_ output generated by the weightCombiner:
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
        "max_daily_year": <int>,
        "min_daily_year": <int>,
        "max_daily_july": <int>,
        "min_daily_july": <int>,
        "max_daily_trucks": <int>,
        "min_daily_trucks": <int>
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
                        "daily_year": <int>,
                        "daily_july": <int>,
                        "daily_trucks": <int>,
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
The microservice has three endpoints:
- [Status](#Status)
- [Combine](#Combine)
- [Info](#Info)

### Status
_Request type_:  **GET**

_Path_: ???/???

##### Usage
Used to see if the server is running. Only used for debugging. 

If the server is running the result will be as follows:
```
The WeightCombiner is online!
```

### Combine
_Request type_:  **POST**

_Path_: ???/combine???

##### Usage
The endpoint for combination expects a list of *microservice* (**MS**) objects within the request body. 

The accepted input format can be seen [here](#input-format).

The generated **TNM** output can be seen [here](#output-format).

 _In case of any errors, an error message will be returned (status code 400)._


### Info
_Request type_: **GET**
_Path_: "/info"

##### Usage
Used to get information about the service.

The information is in the form of a redirect to the readme which is present on [GitLab](https://daisy-git.cs.aau.dk/astep-2021/astep-6/-/blob/master/README.md).


