---
title: Map Matching Service (Fall 2020)
description: The Map Matching Service allows users to map match raw GPS points to an OSM map.
published: true
date: 2020-12-16T13:19:12.166Z
tags: 
editor: undefined
---

# Map Matching Service

The Map Matching Service is an aSTEP service that was developed in fall 2020 through the collaboration between groups **SW502E20** and **SW505E20**. The service was developed because both groups needed map matched data for their respective services also developed during the course of that semester.

---

The purpose of this service is to match trips consisting of raw GPS data to a road network defined by OpenStreetMap (**OSM**). For more details on what map matching entails it is recommended that the reader looks at the project reports written by either Group SW502E20 or Group SW505E20.

As the service was to be developed collaboratively, it was necessary to define subtasks for each group to complete. As such it was decided that
- Group SW505E20 would develop the **user interface** and **database** for the service. This meant that the group was responsible for presenting map matched trips on a map, as well as storing map matched data in a database. As such, a **Map Matching UI repository** was made containing the presentation and data access logic.
- Group SW502E20 would develop the underlying **map matching logic**. This resulted in the group creating a Map Matching API that would handle the actual map matching operations, offering an endpoint that the UI made by Group SW505E20 could simply POST an http request to. The **Map Matching API repository** was made to encapsulate this logic. For the actual map matching, the [GraphHopper library](https://www.graphhopper.com/) was utilized.

The service can be used through the UI on the aSTEP platform [here](https://astep.cs.aau.dk/tool/astep-2020-fall-sw505-test-service.astep-dev.cs.aau.dk).

The expected input and output for the service, as well as the two repositories, can be found below.

## Input

If using the Map Matching Service through the UI, the input is in the form of a GPX file uploaded to the service. It is also possible to batch match several trips using a different file format. More information about the format of these files can be found in the readme of the Map Matching UI repository below.

If using the Map Matching Service directly through http requests to the API, the input is in the form of a JSON object containing the same information as the aforementioned GPX file. The exact format of the JSON input can be found in the readme of the Map Matching API repository below. When sending a map match request to the API, the following endpoint is used:

[https://astep-2020-fall-mapmatching.astep-dev.cs.aau.dk/mapmatch](https://astep-2020-fall-mapmatching.astep-dev.cs.aau.dk/mapmatch)

## Output

When used through the UI, the Map Matching Service will present a visualization of the map matched trip on an embedded OSM map. Both the matched route as well as the raw points will be visualized. Using the batch map matching function will store the matched trips in **DB2** as well.

If an http request is sent directly to the API, the output will be in the form of a JSON object containing information about the distance traveled, the average speed as well as which edges on the OSM map are traveled on. More concrete information about this output can be explored in the readme of the Map Matching API repository below.

## Repositories

The repository for the Map Matching API can be found [here](https://daisy-git.cs.aau.dk/astep-2020-fall/mapmatching).

The repository for the Map Matching UI can be found [here](https://daisy-git.cs.aau.dk/astep-2020-fall/sw505-test-service).