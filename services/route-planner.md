---
title: Route Planner
description: Created in the spring 2020 semester, the Route Planner service is a tool for creating delivery plans for efficiently distributing parcels from a distribution center to a set of delivery points.
published: true
date: 2020-12-09T12:47:03.456Z
tags: 
editor: undefined
---

# Route Planner

**Route Planner** is a service dedicated to using various algorithms and graph-options to calculate delivery routes for parcels. It was originally made by group *SW601F20* as a part of the *routing* story of that semester. 

The groups of the semester were divided into 2 super-groups: One working on various time-series analytics and the other working on the *routing* story. The story was composed of three tasks (Henceforth referred to as *Task x*):

1. Analyze the traffic tendencies (At different hours and days) of road segments based on historical traffic data supplied by the *Bring* delivery company. This data takes the form of a list of GPS readings representing deliveries. Use the results of this analysis to create histograms over travel-time for each road segment.
2. Categorize edges based on commonalities and the histograms from *Task 1*, as not all edges are completely detailed or have any known traffic tendencies due to a lack of data.
3. Using the results of *Tasks 1* and *2*, find the optimal delivery-route based on historical tendencies.

It was mandated that the entire routing super-group (*SW601F20, SW605F20*, and *SW606F20*) worked together to solve *Task 1*. The solution can be read about [here](/services/speed-analysis). *Task 2* was solved by group *SW605F20* with the [Attribute Prediction](/services/attribute-prediction) and [Graph Attributes](/services/graph-attributes) services. *Task 3* is implemented by this service, which can be found on the aSTEP website [here](https://astep.cs.aau.dk/tool/astep-2020-sw601f20-routing.astep-dev.cs.aau.dk).

## Using the service
A detailed explanation on how to use the service, as well as the input and output can be found in the readme on the services GitLab repository [here](https://daisy-git.cs.aau.dk/astep-2020/sw601f20-routing/).



## Current status

Currently, the service can compute delivery routes of various lengths originating from any number of distribution centers using two different algorithms and two different cost models. All routes are restricted to the graph of the Danish road-network stored in the [`sw601f20_routing`](/databases/DB2/sw601f20_routing) database.

In the following, a "*delivery plan*" consists of one or more "*delivery routes*", where a delivery route originates in a parcel distribution center, travels through a number of delivery locations, and returns to that distribution center.

The two algorithms that the service implements are:

- An **N**on-dominated **S**orting **G**enetic **A**lgorithm (NSGA-II), which is specified to solve the multiple traveling salesman problem (MTSP). This genetic algorithm will, over a series of generations/iterations, create new populations that are then compared with their surviving cousins and ancestors. A new population equal to the initial one in size are picked, and the rest are then discarded. The algorithm compares routes first on total length of delivery plans, and then on which has the lowest difference between the longest and shortest route in the delivery plan. The algorithm has a few additional input fields, which specify the number of trucks available at each distribution center, the number of generations that the algorithm will run for, the size of the population that is kept between generations, and the mutation rate of solutions generated (which is used to discourage stagnation due to inbreeding).
- A greedy algorithm created by *SW601F20*. This algorithm solves the travelling salesman problem (TSP) by using the greedy algorithm concept. The algorithm will always try to choose the cheapest unvisited destination as its next stop. However, because computing what is the nearest (the one with the cheapest path) destination can become very expensive if there are many unvisited locations to check, the algorithm prunes a lot of location that it deems improbable as the optimal next choice. Since computing distances is cheaper than computing paths, the algorithm first finds the nearest unvisited node using the haversine distance, and then computes paths only to the nodes that are at most double that distance away from the current node. It then chooses the one with the shortest path. With this, the algorithm assumes that the optimal path can be found by only ever taking a path within this distance of the current node.

The two cost models implemented by the service are:

- The **static** edge information loader. This cost model uses the *expected traversal time in seconds* as its cost, and is based on the speed limits of the road segments.
- The **dynamic** edge information loader. This cost model uses the *expected traversal time in seconds* as its cost, and is based on traffic tendencies extrapolated from historical traffic data. The loader get these tendencies by communicating with the services [Historic-Road-Tool](/services/historic-road-tool) and [Attribute Prediction](/services/attribute-prediction).

For a how-to guide, see the user-documentation [here](https://astep.cs.aau.dk/tool/astep-2020-sw601f20-routing.astep-dev.cs.aau.dk).

##### Developer-mode

The developer-mode of the service allows the user to input a distribution center and a list of destinations to deliver to manually. It is only possible to specify a single distribution center. Additionally, one must specify the starting time of the route. Edge information source and algorithm choice is still specified by the user-mode menu. In order to make the system use this mode, you must not have uploaded a workload file.

##### Issues and points of note

The graph of the Danish road-network that was supplied by OpenStreetMap was not strongly connected, which means that there are pockets of nodes that it is either not possible to enter, leave or both. In order to ensure that the algorithm does not, as a result, break, we created a graph containing only the largest, strongly connected component (LSCC) of the original graph, which can be found in the database [`DB2/sw601f20_routing`](/databases/DB2/sw601f20_routing). As a result of this, then any route made  by this service will be guaranteed to not crash, but they will look broken due to some roads being inaccessible.

The script used to produce the LSCC can be found [here](lscc-script).

###### The new UI

The current user-interface was taken from the [Logistics](/services/logistics) service, and modified thereafter. There is therefore a significant overlap between the two.

The current user-interface can be see below in the 3 images. For a description of this, see the user-documentation.

![maps_tab.png](/services/route-planner/maps_tab.png)
![error_tab.png](/services/route-planner/error_tab.png)

###### Future works

Route Planner has the following future works and improvements:

- Improve the service's general efficiency and execution speed. This could be done by:
  - Improving the dynamic edge information loader, so that it is practical to use. This mostly involves increasing the execution speed of it.
    - One part of the inefficiency most likely stem from the height of the call-stack to other services. These become exponentially more expensive, and both services directly called each call other services themselves.
    - Another part is the sheer number of calls to other services, whoose results each then have to be parsed before use.
  - Having a database of pre-computed results for often-used road- and route-segments.
- Fix the graph so that the entire Danish road-network can be used, rather than just the largest, strongly connected component.
- Implement routing algorithms using machine learning.  This will require much more historical traffic data, than what is currently stored in [`DB2/driver_identification_db`](/databases/DB2/driver_identification_db). 
- Transferring the functionality of the [Logistics](/services/logistics) legacy service into this one. This primarily takes the form of implementing a routing algorithm that can solve the capacitated vehicle routing problem.
  - The group behind `Logistics` also had a list of future works that were not implemented by *SW601F20*, and could be looked at.
  - One possibility would be to update all algorithms to take weight and volume of parcels into account.
- Implement a smarter chunk manager. This includes using a *memory* limit rather than a chunk limit, as chunks are to broad a category. Additionally, it should be possible for the user do disable the limit, so as to trade space for time.
	- Currently, there can only exist a single request at once, as they all use the same chunk database. This should clearly be fixed.
- Implement a new output format which would be able to be uploaded to a GPS, so as to make the delivery plans usable for drivers.



## Inner workings

The service's back-end is programmed using C# with the UI being programmed using JavaScript, HTML and CSS. The implementation makes use of one framework and two libraries: 

- The `ASP.NET CORE` framework, which is used to handle HTTP communication,  CORS, and other web-related functionality.
- The `SQLite Core` library, which is used to operate locally-stored databases.
- The `Npgsql`library, which is used to communicate with databases stored on the aSTEP server system.

The codebase can be found on Daisy-git [here](https://daisy-git.cs.aau.dk/astep-2020/sw601f20-routing).

##### Design

The service's design makes use of many interfaces, so that it is easy to extend the functionality later on. The service structure, as it is currently, makes use of 7 interfaces, the higher one is in the chain, the more functionality will have to be re-implemented unless components are reused.

The design can be seen in the image below. The green ovals represent databases, the orange/brown curved rectangles represent interfaces, and the blue squares represent classes.
![task3design.png](/services/route-planner/task3design.png)

###### IRouter

The `IRouter` interface is used to represent routing algorithms. The primary responsibility of any implementation of this interface is therefore, given a distribution center and a list of destinations to visit, to create a delivery plan which fulfills some criteria specified by the chosen algorithm. A delivery plan can countain multple delivery routes, where a delivery route is defined as a precise list of nodes which together describe the route's entire path in detail.

A few specific implementations are described [further down below](#algorithms).

###### IPathFinder
The `IPathFinder` interface is used to represent *pathfinding* algorithms. For the service, a pathfinding algorithm is defined as one which finds the best path (according to some criteria) between two nodes in a graph.

Examples of such algorithms are *Dijkstra's* and *A**.

###### IRoadMap
The `IRoadMap` interface is used to represent a graph of a road-network. How this representation functions is up to the implementation. It must simply allow the programmer various means of getting nodes and edges, as well as the possibility of dropping/clearing properties set by the pathfinding algorithm. An example of two properties would be Dijkstra setting a cost and parent.

###### IChunkManager
The `IRoadMap` implementation currently being used by the service makes use of a *chunking* principle. The road-network is divided into a set of *chunks* which can be loaded, saved, and re-loaded as neccessary throughout the routing process. In order to facilitate intelligent use of chunks, we therefore have the `IChunkManager` interface, implementatios of which are capable of making these decisions.

###### IEdgeInformationLoader
Because a large part of *Task 3* involved using traffic tendencies as a cost model, we use the interface `IEdgeInformationLoader` to represent various forms of cost models. Any implementation of the interface have the responsibility that, given any edge in the graph, they return a cost for traversing that edge.

Currently, the service has two implementations:
- The `static edge information loader` which uses the speed limits stored on the edges. Defaults to 40 km/h if no speed limit is known.
- The `dynamic edge information loader` which uses the [Historic-Road-Tool](/services/Historic-Road-Tool) and [Attribute Preciction](/services/attribute-prediction) services to compute its results.

###### IMapDataQuerier & IMapGeometryQuerier
The interface `IMapDataQuerier` is used to query any and all external sources for graph data. It is immaterial whether that source is a local database made using `SQLite` or one stored on the aSTEP cluster.

Any implementation of `IMapDataQuerier` must also implement the `IMapGeometryQuerier`. This interface is used when drawing the resulting delivery plans on a map. Because roads are not straight, but are often quite liberal in their shape, we need precise descriptions of a road segment's form. This description will therefore have to be queried from an external source as well.


##### Algorithms
The service currently implements three algorithms:
- A classic *A** for pathfinding.
- A custom-made greedy routing algorithm, which solves the traveling salesman problem.
- A specialized **N**on-dominated **S**orting **G**enetic **A**lgorithm (NSGA-II), which solves the multiple traveling salesman problem.

For some more details than what is provided below concerning the various algorithms, see *SW601F20*'s project report.

###### Custom greedy algorithm
The greedy algorithm is priamrily based on the greedy principle, which means that the algorithm will always make the short-term best choice, and hope that this will produce a near-optimal final result. 

An image of how the algorithm works can be seen below.
![greedy.png](/services/route-planner/greedy.png)
The algorithm finds the clostest-unvisited destination. Closeness is computed using haversine formula. The algorithm then finds all destinations that are at most twice the closest distance from the current node. A path is computed to each of these destinations, and the fastest path is chosen. The process then repeats itself until there are no more unvisited destinations, upon which the algorithm returns back to the starting node.

The algorithm's pseudo-code can be seen below.
![greedyrouter.png](/services/route-planner/greedyrouter.png)
###### NSGA-II
 The algorithm is based on [this paper](https://www.tandfonline.com/doi/full/10.1080/21642583.2019.1674220).
 
 The NSGA-II algorithm is a multi-objective evolutionary algorithm. Being multi-objective means that the algorithm is capable of pursuing and optimizing for an abitrary number of objectives, such as path length, fuel expenses, and departure time. Being evolutionary means that the algorithm generates a random *population* of solutions which then compete against each other and mutate over a set number of generations, where only the best solutions survive a generational culling.
 
 Any solution made by the algorithm is encoded as a *chromosome*. Using this encoding, it is possible to represent any possible solution as a list of integers, by mapping each destination to an integer value (called a *gene*), and then ordering them in order to deliminate the solution. In the case of this algorithm, the ordering is the order in which destinations are visited. Additionally, because there are multiple vehicles which a chromosome code for, there is a section of genes on the chromosome dedicated to describing which route starts and ends where.
 ![chromosomeexplainer.png](/services/route-planner/chromosomeexplainer.png)
 This image shows an encoded chromosome. *Part 1* describe the visit order and *Part 2* describe which vehicle's route is described where. This chromosome uses 4 vehicles, and a decoded version can also be seen. Here, Part 2 is removed, and there is instead inserted '0's to signify the start of a new vehicle route.
 
 There are 5 additional functions to understand, which the NSGA-II algorithm makes use of:
 - `crossover`
 	- This function pairs two solutions and creates a child out of them.
 - `mutationReverse`
 	- This mutation function takes a segment of Part 1 of the encoded chromosome, and reverses the ordering of it. It is used to promote varied solutions and combat inbreeding.
 - `mutationTranspose`
 	- This mutation function divides Part 1 of the encoded chromosome into three parts, and reorders them as 2-3-1.
 - `fastNonDominatedSorting`
 	- This function divides solutions into what is called *fronts*. What characterizes a front is: For any solution in front *n*, then there exists in front *n-1* a solution which dominates that solution, and for any solution in front *n+1*, there is a solution in front *n* which dominates that solution. A solution is placed in a front if, at the time of insertion, there is no solutions which dominate it in the front. Domination is determined by objectives, and it is possible to be dominated by solutions sharing the same front due to how insertion works.
 - `crowdingDistanceAssignment`
 	- This function assigns a value based on chosen objectives, where higher values are assigned to more *unique* (but not necessarily better) solutions. This is only done to solutions that are inside the same front, and is used to pick solutions out when adding the entire front to the surviving population would be choosing too many solutions to survive.
 
 ![nsga-ii_1.png](/services/route-planner/nsga-ii_1.png)
 ![nsga-ii_2.png](/services/route-planner/nsga-ii_2.png)
 
## History

### Summer 2020

During the summer of 2020, two members of group *SW601F20* were hired to maintain the aSTEP project until the next semester started in Autumn 2020. As a part of this maintenance, they were also asked to modify certain parts of the *Route Planner* service. These modifications were:

- A new UI taken directly from the [Logistics](/services/logistics) service.
- A parsing functionality for `.csv` workload files and route-planning back-end to make use of workload files.
	- This allows the user to write a .csv file containing the delivery data, where they can make use of addresses and postal codes rather than IDs.

As a part of implementing these, the following was also added to the service:

- Implement an error-window.
- An address database.
	- A database containing (we assume) every address in Denmark.
- An address-parsing functionality.

The design of the service went unchanged from Spring 2020, and the new functionalities were instead simply added onto existing components. For a design diagram, see the Spring 2020 history section.
##### Result
While the system's UI and HCI has been significantly improved (and the system also future-proofed, somewhat), the inefficiency of the dynamic edge information loader is still holding the service back from being properly functional. Now, though, a normal user can use the service (hopefully) without major issues, as long as they are using the *static* cost model.

The future works are the same as those from Spring 2020, but the point below has been fulfilled.
-  Implement a better input format for destinations. This should take the form of a `.csv` uploader, which contains to and from addresses that can be parsed.
### Spring 2020
The **Route Planner** service was first created during the Spring 2020 semster by group *SW601F20*.

The system was able to use two algorithms:
- a custom greedy algorithm, which could be used to solve the travelling salesman problem.
- NSGA-II, a multi-objective, evolutionary algorithm, which could be used to solve the multiple travelling salesman problem.

Both of these algorithms made use of the same *A** algorithm to facilitate pathfinding. 

The primary task of the service was to grant aSTEP a service capable of creating routes based on traffic tendencies extrapolated from historical traffic data. In order to use this, as well as other cost models, an interface was created to represent these models. The interface had two implementations:
- The `static edge information loader` cost model, which uses the *expected travel-time in seconds* as its cost. This expectation is based on the speed limits of road segments. This model was primarily used for testing the rest of the system.
- The `dynamic edge information loader` cost model, which uses the *expected travel-time in seconds* as its cost. This expectation is based on traffic tendencies and speed limits of the road-network, as provided by the [Historic-Road-Tool](/services/Historic-Road-Tool) and [Attribute Prediction](/services/attribute-prediction) services, respectively.

Currently, the system is unable to route to the entirety of the danish road-network as the graph that is used is not strongly connected. This means that there are numerous pockets spread through-out the graph where you can't enter, leave or both. In order to ensure that there exists a path between any two nodes in the graph, the service instead uses a road-network graph that is the largest, strongly connected component of the original one.

##### Design
The design was primarily based around using interfaces for any components, so that extensions were easy to make in the future. A diagram showing the design can be seen below:
![task3design.png](/services/route-planner/task3design.png)
A total of 7 interfaces were used:
- `IRouter`
	- A representation of routing algorithms. Any algorithm which solves a problem derived from the *vehicle routing problem* belongs here.
- `IPathFinder`
	- A representation of pathfinding algorithms such as *Dijkstra's* and *A**
- `IRoadMap`
	- A representation of a road-network.
- `IChunkManager`
	- A representation of the control logic handling the loading and saving of chunks of the road-network. Obviously, this assumes that the `IRoadMap` implementation has divided the road-network into chunks.
- `IEdgeInformationSource`
	- A representation of cost models used for the road-network.
- `IMapDataQuerier`
	- A representation of any component that connects to external sources, such as databases.
- `IMapGeometryQuerier`
	- Any implementation of `IMapDataQuerier` must also implement this. It represents any component capable of acurrately illustrating various roads' curvature on a world map. The reason is that such data is stored externally as well.
##### Result
While the primary result of the semester was achieved - that is, enabling aSTEP to have a service capable of routing with traffic tendencies - a lot of secondary goals went unfilfillled. The combination of these result in the service being, pardon my french, functionally unusable with respect to its primary focus. Firstly, the lack of a practical input method for destinations makes the service tedius for advanced users and impossible for newcomers.

![oldui.png](/services/route-planner/oldui.png)

Having to manually insert specific destination IDs is a chore, require that any and all destinations are already registered in a database, and require that the user knows the specific IDs.

Secondly, the computation speed of the *dynamic* cost model makes the service functionally useless due to how long even the shortest of routes take to compute.

The future works of the service are therefore:
- Implement a better input format for destinations. This should take the form of a `.csv` uploader, which contains to and from addresses that can be parsed.
- Improve the service's general efficiency and execution speed. This could be done by:
  - Improving the dynamic edge information loader, so that it is practical to use. This mostly involves increasing the execution speed of it.
    - One part of the inefficiency most likely stem from the height of the call-stack to other services. These become exponentially more expensive, and both services directly called each call other services themselves.
    - Another part is the sheer number of calls to other services, whoose results each then have to be parsed before use.
  - Having a database of pre-computed results for often-used road- and route-segments.
- Fix the graph so that the entire Danish road-network can be used, rather than just the largest, strongly connected component.
- Implement routing algorithms using machine learning.  This will require much more historical traffic data, than what is currently stored in [`DB2/driver_identification_db`](/databases/DB2/driver_identification_db). 
- Transferring the functionality of the [Logistics](/services/logistics) legacy service into this one. This primarily takes the form of implementing a routing algorithm that can solve the capacitated vehicle routing problem.
  - The group behind `Logistics` also had a list of future works that were not implemented by *SW601F20*, and could be looked at.
  - One possibility would be to update all algorithms to take weight and volume of parcels into account.
- Implement a smarter chunk manager. This includes using a *memory* limit rather than a chunk limit, as chunks are to broad a category. Additionally, it should be possible for the user do disable the limit, so as to trade space for time.
	- Currently, there can only exist a single request at once, as they all use the same chunk database. This should clearly be fixed.
- Implement a new output format which would be able to be uploaded to a GPS, so as to make the delivery plans usable for drivers.