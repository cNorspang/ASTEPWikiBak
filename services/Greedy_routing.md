---
title: Greedy Routing
description: Naive "shortest" path routing service
published: true
date: 2021-12-10T07:51:10.242Z
tags: routing, tnm
editor: markdown
---

# Greedy Routing
**Greedy Routing** is a service for finding a path between two nodes in a weighted graph based on the model presented in [RFC0020](https://wiki.astep-dev.cs.aau.dk/rfc/0020), using a greedy approach for searching through the graph. 

# Details
The service uses a naive greedy search algorithm to navigate the given graph, in an attempt to find a short path from the start node to the goal node. The given graph is searched by always following the lowest cost edge in the frontier until the goal node is found, after which the path is found by iteratively going back through the node's parent nodes and adding it to a path list until the start node is reached, subsequently the path list is reversed, such that the path starts at the start node and ends at the goal node.

# Input
The service uses the HTTP content-type: ***application/json***, followed by the JSON input in the request body as the input data. The input data should be posted to the ***/data*** endpoint to use the service. The different input data used by the service are the following:
- [model](#model)
- [start_node](#start_node)
- [goal_nodes](#goal_nodes)

The input JSON should encompass these three fields as such:
``` json
{
	"model": <graph model>,
	"start_node": <integer>,
  "goal_nodes": [<integer>]
}
```

### model {#model}
The field '*model*' encompasses the weighted search graph in the field '*nodes*', along with some other fields such as '*meta_data*' or '*vehicle*'. The field should follow the format stated in [RFC0020](https://wiki.astep-dev.cs.aau.dk/rfc/0020). An example of what the field '*model*' could look like can be seen below.
``` JSON
{
	"model": {
  	"nodes": {
    	"1": {
      	"from_node_id": 1,
        "weight": 0.0,
        "data": {
        	"longitude": 42.1,
          "latitude": 32.3
        },
        "edges":{
        	"52": {
          	"id": 52,
            "from_node_id": 1,
            "to_node_id": 2,
            "weight": 0.4,
            "data": {
            	"length": 104,
              "mean_speed": 65
          	}
        	},
          "53": {
          	...
          }
       	}
     	},
      "2": {
  			...
     	}
  	}
 	}
}
```

### start_node {#start_node}
The field '*start_node*' contains the ID of the node which should be the starting node of the search. An example of the field can be seen below.
``` JSON
{
	"start_node": 1
}
```

### goal_nodes {#goal_nodes}
The field 'goal_nodes' contains an array of the IDs of the nodes which should be the goal nodes of the search, though the router only finds the path to the first element in the array, so more than one goal node is not possible. An example of the field can be seen below.
``` JSON
{
	"goal_nodes": [3]
}
```

# Output
The service outputs a modified version of the content received in the *model*' field. When the path has been found, the service modifies the received model such that the field '*nodes*' originally containing the search graph, not only contains the nodes and edges used in the path, from start to goal, ordered from start to goal. If the received '*model*' field contains a *'meta_data*' field, where the field *'last_service*' field exists, the service also updates it's value with the name of this service. An example of what the output of the service could look like can be seen below.
The field '*start_node*' contains the ID of the node which should be the starting node of the search. An example of the field can be seen below.
``` JSON
{
	"model": {
  	"meta_data": {
    	"last_service": "Dijkstra Routing"
    },
    "nodes": {
    	"1": {
      	"from_node_id": 1,
        "weight": 0.0,
        "data": {...},
        "edges": {
        	"3": {
          	"id": 3,
            "from_node_id": 1,
            "to_node_id": 2,
            "weight": 0.3,
            "data": {...}
          }
        }
      },
      "2": {
      	"from_node_id": 2,
        "weight": 0.0,
        "data": {...},
        "edges": {
        	"7": {
          	"id": 7,
            "from_node_id": 2,
            "to_node_id": 3,
            "weight": 0.2,
            "data": {...}
          }
        }
      },
      "3": {
      	"from_node_id": 3,
        "weight": 0.0,
        "data": {...},
        "edges": {}
      }
    }
  }
}
```

As can be seen in the example, the field '*nodes*' contains the nodes and edges used in the path. In this example the starting node is node 1, and the goal node is node 3, here node 1, goes to node 2 using edge 3 and node 2 goes to node 3 using edge 7, and because node 3 is the goal, no edge is used to move further, hence it's '*edges*' field is empty.