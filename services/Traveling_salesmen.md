---
title: Traveling salesman 
description: Two services used to solve the traveling salveman problem
published: true
date: 2021-12-06T08:39:24.959Z
tags: 
editor: markdown
---

# Traveling salesman problem (TSP)
This section is concerned about solving the traveling salesman problem and will describe two different microservices. The first service creates a model that the second service can use to solve TSP and return to the UI.

## Creating a traveling salesman problem model
As described in the other service of TNM, a full transportation network is saved on the database and used by the service in TNM. This road network is not suitable for working with TSP since nodes that sound not be visited are also part of the model. This is why a service is needed that takes the "normal" TNM model as input and returns a TSP model that can be used by other services to solve TSP.

#### Input
A interface for the input of the service can be seen below.

```json
{
	"startNode": <int>,
  "endNodes": [<int>],
  "fuelLevel": <int>
  "model": TNM_Model,
}


```

#### Output

### Calling the service





## Solving the traveling salesman problem

### Heuristics

### Calling the service

