---
title: TNM Router ViaFuelStation
description: 
published: true
date: 2021-12-06T08:27:20.591Z
tags: 
editor: markdown
---

# TNM Router ViaFuelStation
The **TNM Router ViaFuelStation** takes as input a single _Transport Network Model_ [(**TNM**)](https://wiki.astep-dev.cs.aau.dk/rfc/0020) with additional information. The additional information is as follows: The ID of the _Node_ where the the route starts, the ID of the _Node_ where the route ends and the amount of available fuel.

The code is available on [Gitlab](https://daisy-git.cs.aau.dk/astep-2021/tnmrouterviafuelstation2021).


## Content 
- [Input Format](#input-format)
- [Output Format](#output-format)
- [End Points](#endpoints)


## Input Format
The accepted _JSON_ input format:

```json
[
    {
        "startNode": <int>,
        "endNode": <int>,
        "fuelLevel": <int>,
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