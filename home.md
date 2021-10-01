---
title: The aSTEP Wiki
description: The main documentation for "aau's Spatio-TEmporal data analytics Platform"
published: true
date: 2020-12-16T20:09:35.434Z
tags: 
editor: undefined
---

# Welcome to the aSTEP wiki

Initially made in Spring 2020, this wiki intends to serve as a common, centralized documentation for the aSTEP system, oriented towards developers and administrators, new and old. The wiki is to be maintained by the (at the time of reading this) current aSTEP semester, such that the coming semesters have easy access to descriptions of the current state and history of aSTEP.

You'll find links to the wiki's content in the blue sidebar located to the left (you may have to open it first). If you don't know what to read first, take a look at the "Where to start" guide located after the following introduction to aSTEP.

> NOTE: There is an old [aSTEP Google Drive](https://drive.google.com/drive/folders/0B-3gK8jdmmY5MFBlVkQtejZnTGM) with some documentation from 2019 and back. However, since Spring 2020 wasn't aware of its existence before near the semester's end, this has not been integrated into the wiki.
{.is-info}

## Introduction to aSTEP

**The aSTEP platform:**
The "***aSTEP***" (***a**au's **S**patio-**TE**mporal data analytics **P**latform*) project is a web-based platform that aims to become a solid foundation on which application developers can build their own services, by providing them with a wide range of data analytics functionality for (but not limited to): spatial data, temporal data, and spatio-temporal data. Respectively, this is data such as: floor plans (space), bacterial growth over a period (time), and trajectories (changes in space over time).

The aSTEP platform serves both as a research and learning environment, on which one can study data-heavy data analytics applications such as machine learning, data mining, data prediction, and much more.

**The aSTEP system:**
Fundamentally, 10 server computers together host all functionality on aSTEP. The servers can roughly be split into: "those that host the website and data" and "those that host development and deployment". The following paragraphs explains these very broadly.

The [aSTEP website](https://astep.cs.aau.dk) follows the *microservice architecture*, meaning that all its functionality is split between various web-based processes called *microservices*. Each microservice may be implemented in their own programming language. A *Kubernetes Cluster* consisting of three server-computers hosts all these microservices, and two database servers each hosting a *PostgreSQL Database Manager* stores all the data used by the microservices.

One server computer hosts the *GitLab* installation used to manage and provide *Git-style version control* for all aSTEP source code. Another server host a *GitLab Runner* which GitLab uses to automatically build, test, and compile microservices. Finally, GitLab integrates with Kubernetes, allowing for automated deployment of microservices to aSTEP as well.

**The aSTEP semester project:**
Apart from maintaining the wiki, servers, website, and microservices, the purpose of the aSTEP semester project is to acquire the skills needed to work towards a larger common goal across groups (as well as super groups). As for the main contact person, they'll also acquire the skills to oversee and steer a collaborative effort, to plan and organize cross-group steering meetings, and to ensure that all work is seen to an end.

You'll learn the importance of proper communication, documentation, and expectations agreement, as well as the importance of upholding inter-group deadlines and being ready to adapt to changes in plans.

## Where to start

If you are a new aSTEP semester, trying to understand the aSTEP system and this wiki, take a look at the [Getting started](/getting-started) guide. The guide explains the process of: getting to know the system, getting your semester set up, adding functionality to aSTEP, and maintaining aSTEP. 

If you're interested in the details of the aSTEP system, take a look at the pages listed under "System documentation" in the blue sidebar to the left.  If you run into problems with the servers you can take a look at the offending server's documentation or visit the [Server Help Guide](/servers/server-help-guide).

If you're interested in project/wiki guidelines and a history of the project's management, take a look at the pages listed under "History and guidelines" in the blue sidebar to the left.

## System documentation

The six links under the "System documentation" section of the blue sidebar document everything about the aSTEP system and platform. This includes anything from the inner workings and usage of the server computers, to the workings and usage of the aSTEP website and the development of microservices.
<!-- This long comment is made, as the following belongs to the route planner service
## How to use the service

The following sections describe how to use the service, as well as the purpose of the service's input fields, some example values to use as input, and how to get the various forms of output.

### How to run the service

Upload a `.csv` workload file containing information about the parcels to be delivered.  Select an *edge information source*. This specifies what cost model to use for the routing. Then choose a routing algorithm to use. Some algorithms have additional input that must be specified. Finally, press the blue button `Visualise results` (As `Print Raw Results` does not work), and wait for the service to compute a route for you. The result will be displayed in the frame showing this guide.

### The input fields

The Route Planner has the following three user-mode input fields:

- **`Workload file`:**  The service takes a `.csv` file as input. This file should contain information about all potential deliveries for a specific day. It must have eleven columns. Some are unused, but the `.csv`-structure is specified by a third party. The columns are:
  - *Random number*: Unknown and unused.
  - *Delivery date*: Date of delivery.
  - *Product* : Unknown and unused.
  - *Destination Address*: Road name and number of the delivery's destination.
  - *Delivery postal code:* Postal code of the delivery's destination.
  - *From address:* Road name and number corresponding to the distribution center that the package is stored at prior to its delivery.
  - *From postal code:* Postal code of the distribution center.
  - *Weight*: Weight of the parcel, measured in kilograms (kg). Currently unused.
  - *Volume*: Volume of the parcel, measured in cubic meters (m^3). Currently unused.
  - *Delivery day*: Day of delivery. Unused.
  - *Delivery time interval*: At what time of day can the parcel be delivered. Is it the entire day or a specific interval. Is relevant when the destination is a package shop with its own working hours. Currently unused.
- **`Edge information source`:** This option specifies the cost model used by the service when computing routes. Currently, the service have two different cost models:
  - *Static*: The cost model used for road segments is the *expected traversal time in seconds* and is based on the speed limits of the road segments.
  - *Dynamic*: The cost model of road segments is the *expected traversal time in seconds* and is based on the traffic tendencies extrapolated from historical traffic data. This option *massively* increases computation time, and is therefore not yet advisable as an option.
- **`Routing algorithm`:** Currently, the service implements two different routing algorithms:
  - *Greedy Router*: A greedy algorithm designed by ourselves (Group *SW601F20*), which takes no additional input.
    - Note that this algorithm cannot take into account multiple vehicles being used. It assumes one vehicle per distribution center.
  - *NSGA-II Router*: An evolutionary and genetic algorithm (based on the NSGA-II algorithm), which takes 4 additional input:
    - *Number of salesmen*: The maximal number of delivery trucks that are available to use for a distribution center.
      - This option is currently global, so all distribution centers will have the same number of trucks specified here.
    - *Number of generations*: A higher number of generations gives a higher potential for a good result, but increases computation time. 
    - *Number of solutions per generation*: A higher number of solutions per generation gives a higher potential for a good result, but increases computation time. This parameter has a lower bound of 4. For efficiency's sake, this value should always be a multiplicative of 4. 
    - *Mutation rate*: A percentage written as a decimal number between 0 and 1, which describes how quickly or extremely the algorithm makes changes to its current solutions. A higher rate increases the computation time with a minor amount.

### Example input

##### Workload file

An example of the content of a workload file is:

| Random number | Delivery date | Product | Destination address                 | Delivery postal code | From address      | From postal code | Weight | Volume   | Delivery day | Delivery time interval |
| ------------- | ------------- | ------- | ----------------------------------- | -------------------- | ----------------- | ---------------- | ------ | -------- | ------------ | ---------------------- |
| 123           | 23.01.2019    | 349     | Kapelvej 13                         | 9400                 | Amalienborgvej 57 | 9400             | 0,22   | 0        | 23.01.2019   | 9-17                   |
| 123           | 23.01.2019    | 349     | Kapelvej 13                         | 9400                 | Amalienborgvej 57 | 9400             | 0,22   | 0        | 23.01.2019   | 9-17                   |
| 123           | 23.01.2019    | 349     | Rolighedsvej 21                     | 9400                 | Amalienborgvej 57 | 9400             | 0,22   | 0        | 23.01.2019   | 9-17                   |
| 123           | 23.01.2019    | 349     | AC Jacobsensvej 19                  | 9400                 | Amalienborgvej 57 | 9400             | 0,22   | 0        | 23.01.2019   | 9-17                   |
| 123           | 21.01.2019    | 342     | SwipBOX Føtex Nørresu Vestergade 30 | 9400                 | Amalienborgvej 57 | 9400             | 0,9    | 0,015225 | 21.01.2019   | 9-17                   |
| 123           | 23.01.2019    | 349     | DoesNotExist 1337                   | 9400                 | Amalienborgvej 57 | 9400             | 0,22   | 0        | 23.01.2019   | 9-17                   |
| 123           | 21.01.2019    | 342     | SwipBOX Føtex Venusvej F Venusvej 8 | 7000                 | Birkedam 18       | 6000             | 0,9    | 0,00396  | 21.01.2019   | 9-17                   |
| 499970        | 21.01.2019    | 340     | Østergade 54                        | 5000                 | Birkedam 18       | 6000             | 1      | 0        | 21.01.2019   | 9-17                   |

Note that the fourth and last rows will intentionally result in errors when used, so as to demonstrate that functionality.

##### Edge information source

As for the edge information source, we recommend you use `Static`. With `Dynamic`, routing between the distribution center and 2 delivery points takes more than an hour. With `Static`, it takes around 12 seconds.

##### Algorithm inputs

###### Greedy

N/A

###### NSGA-II

If you choose the *NSGA-II* algorithm, then we recommend starting with the following value for the additional parameters:

- *Number of salesmen*: `3`
  - Any positive  integer number will work. The service is able to optimize the number it will actually use.
- *Number of generations*: ` 10` or `20`
  - Any positive integer number will work.
- *Number of solutions per generation*: `4` or `8`
  - Should be a multiplicative of 4, but any integer over 3 will work.
- *Mutation rate*: `0.05`
  - Any decimal number between 0 and 1 will work.

### The output

The service can output results in only one format by pressing the button `Visualize Results`, as `Print Raw Results` is not supported.

The output has three sections to describe:

- The computed routes will be displayed on a world map. Here, squares represent distribution centers, circles represent stops, and each route has its own unique color showing its path. The map has 4 interactable components:
  - You can drag the map around to change what you look at. It is also possible to zoom in and out with using your scroll wheel or touchpad.
  - You can change the zoom level using the `+` and `-` buttons in the upper-left corner of the map.
  - You can press the blue home-button to return to the initial view.
  - You can click on the `Choose a route` drop-down menu to see a list of all routes, grouped by their distribution center. This also shows the route's expected cost in time (HH:mm). Choosing a route will move the view to show the entire route. 
  - You can click on a route segment to highlight it, and highlight information about it in the table described below.
- Below the map, there is a table. This table is able to display information about a specific route. In order to see this data, the route must be chosen on one of the ways described above. This table lists each stop of the route as a separate row. If you click on a row, it will move the map to show the route towards the stop, and highlight both the route and the row. The table has the following columns:
  - *Arrival / Departure*: a pair of timestamps (HH:mm), describing the arrival and departure times for the stop.
    - It is assumed that a stop will always, no matter the number of packages that are delivered there, take 5 minutes exactly.
    - The arrival time of the first row is left blank as it is not applicable. The same is the case of the last row's departure time.
  - *Address*: The address of the stop. Does not contain the postal code.
  - *Name*: The name (if any can be found) of the stop.
    - An example would be `SwipBOX Føtex Nørresundby`.
    -  If it is a private address, it will say `(private)`.
  - *Packages*:
    - The number of packages that are delivered at the stop.
    - The first row shows the total number of packages to deliver here.
    - The last row always displays 0.
- Above the map, there is two tabs. It will be by default set to `Map`, which shows the above two components. The other tab `Errors` will show information about any parcels in the workload file that could not be included. The parenthesis show the number of failed parcels. The tab shows the information in the form of a table, with three columns:
  - *Error type*: What type of error is it. 
  - *Description*: A description of the error.
  - *Origin*: Where did the error occur. If it was a parsing error of any row in the workload, it will say at which row the erroneous item can be found. 
-->

## History and guidelines

The three links under the "History and guidelines" section of the blue sidebar document the history of decisions made during steering meetings (meetings between representatives from all groups), as well as the guidelines for documenting decisions and meetings, and guidelines for maintaining the wiki.

The [RFC](/rfc)s document the evolution of aSTEP and is considered the single source of truth regarding decisions made in the steering meetings. The [Summaries](/summaries) section contains summaries from steering meetings where (among many other things) the RFC's are either accepted or rejected.
