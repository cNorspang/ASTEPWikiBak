---
title: Traveling salesman 
description: Two services used to solve the traveling salveman problem
published: true
date: 2021-12-09T13:00:25.058Z
tags: 
editor: markdown
---

# Traveling salesman problem (TSP)
This section is concerned about solving the traveling salesman problem and will describe two different microservices. The first service creates a model that the second service can use to solve TSP and return to the UI.

## Creating a traveling salesman problem model
As described in [the Creator service](/services/TNM_Creator_Genesis), a full transportation network model (TNM) is saved on the database which is then send to other microservices by the [Controller](/services/TNM_Controller). The TNM is not suitable for working with TSP since nodes that should not be visited are also part of the model. This is why a service is needed that takes the "normal" TNM model as input and returns a TSP model that can be used by other services to solve TSP.

#### Input
An interface for the input of the service can be seen below.

```json
{
	"startNode": <int>,
  "endNodes": [<int>, ...],
  "fuelLevel": <int>
  "model": TNM_Model,
}
```
In the context of TSP, "startNode" and "endNodes" are the id's of  the nodes that are included in the output model of this service. The field "model" represents the entire TNM. Thus, the service removes all nodes from TNM whose id's are not present in the fields "startNode" and "endNodes". 

#### Model creation
The way this service converts the TNM into a TSP model is by using the A* path finding algorithm between all the nodes defined in the input. In each of the new edges created between the nodes information is saved about which nodes this new path represents. This is relevent for when this has to be drawn on the UI. Furthermore the weights of all the edges in the path is combined into a single value that is assigned to the newly created edge.

#### Output
When the service is called with a simple model and "1" as start node and "[2, 4, 6]" as end nodes a snippet of the output can be seen below.
```json
{
    "error_list": [],
    "meta_data": {
        "last_service": "TSP Creator Service",
        "priority": 0
    },
    "vehicle": {
        "id": 0,
        "data": {}
    },
    "nodes": {
        "1": {
            "node_id": 1,
            "node_weight": 0.0,
            "data": {
                "longitude": 41,
                "latitude": 51
            },
            "edges": {
                "0": {
                    "edge_id": 0,
                    "to_node_id": 2,
                    "edge_weight": 4.0,
                    "node_ids_path": {
                        "1": {
                            "node_id": 1,
                            "longtitude": 41,
                            "latitude": 51
                        },
                        "2": {
                            "node_id": 2,
                            "longtitude": 42,
                            "latitude": 52
                        }
                    },
                    "data": {}
                },
                "1": {
                    "edge_id": 1,
                    "to_node_id": 4,
                    "edge_weight": 7.0,
                    "node_ids_path": {
                        "1": {
                            "node_id": 1,
                            "longtitude": 41,
                            "latitude": 51
                        },
                        "3": {
                            "node_id": 3,
                            "longtitude": 43,
                            "latitude": 53
                        },
                        "4": {
                            "node_id": 4,
                            "longtitude": 43,
                            "latitude": 53
                        }
                    },
                    "data": {}
                },
                "2": {
                    "edge_id": 2,
                    "to_node_id": 6,
                    "edge_weight": 8.0,
                    "node_ids_path": {
                        "1": {
                            "node_id": 1,
                            "longtitude": 41,
                            "latitude": 51
                        },
                        "3": {
                            "node_id": 3,
                            "longtitude": 43,
                            "latitude": 53
                        },
                        "6": {
                            "node_id": 6,
                            "longtitude": 43,
                            "latitude": 53
                        }
                    },
                    "data": {}
                }
            }
        },...
    }
}
```
As can be seen in the example, a lot of coordinate data is saved. The reason for this is that it is used by the UI to draw the paths properly.


### Calling the service
The service can be called by sending a **POST** request to **/prune** of this service. Here the contents of the post request should of course match what was described above in the input section.


### Running the service locally
First of you have to download the repository from gitlab[www.google.com]


## Solving the traveling salesman problem
Solving the traveling salesman problem is difficult, so three algorithms using different heuristics to try to solve it have been implemented. These algorithms are all included in this service.

#### Input
The service takes the output of the previous service as input. Thus, the previously described service should be called first to prune the TNM to a suitable graph for the TSP, and then this service can be called with the pruned TNM as input. 

#### Heuristics
Since it is heuristic solutions, the optimal solutions may not be found, but the heuristic algorithms used should be decent. The simplest algorithm is a random one, that just randomly generates a route. This will often not be close to the optimal solution. The second algorithm is nearest neightbor, which works by always going to the closest node. This is better then random, but can still find terrible solutions. Lastly the 2 opt method have been implemented. This again will rarely find the optimal solution, but is often really close.

### Calling the service
The service can be called by sending a **POST** to either **/tsp_random**, **/nearest_neighbor** or **/two_opt**. When the service is called, a route is found using the algorithm specified in the three possible endpoints. Based on what edges are taken in the route, the nodes that are actually visited are saved as a list, and returned. So if an edge consists of 3 nodes, as is the case for edge "1" and "2" in the above JSON, the three nodes will be listed. The output therefore consists of the order and all the nodes that are visited. 