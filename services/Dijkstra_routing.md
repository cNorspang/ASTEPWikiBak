---
title: Dijkstra routing
description: 
published: true
date: 2021-12-06T10:10:37.147Z
tags: 
editor: markdown
---

# Dijkstra Routing
**Dijkstra Routing** is a service for finding the shortest path between two nodes in a weighted graph, using Dijkstra's algorithm. 

# Details
The service uses [Dijkstra's algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm) to navigate the given graph, in an attempt to find the shortest path from the start node to the goal node. The given graph is searched until the shortest path to the goal node is found, after which the path is found by going back through each node's and adding it to a path list until the start node is reached, subsequently the path list is reversed, such that the path starts at the start node and ends at the goal node.

# Input
The service uses the HTTP content-type: *application/json*, followed by the JSON input in the request body as the input data. The different input data used by the service are the following:
- graph
- start_node
- goal_node

[Link to header](#dijkstra_routing)

# Output