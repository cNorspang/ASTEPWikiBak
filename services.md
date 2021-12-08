---
title: Services
description: This page lists the documentation pages for the aSTEP services, as well as code libraries used by these services.
published: true
date: 2021-12-08T10:44:32.377Z
tags: 
editor: markdown
---

# Services
> NOTE: This page reflects the state of the system at the end of the Spring 2020 semester.
{.is-info}

The service documentation is split into three sections: "UI and related", "categories in the UI", "utility", and "code libraries" (section titles go by simpler names). Since this wiki was created in 2020, the documentation for 2019 services and back may not be as extensive or even lacking. (Heck, even 2020 may be lacking.) 

Service names are followed by their year of creation enclosed in parentheses. That is: "*Service Name (creation year)*". All service documentation should follow the [Service Documentation Standard](/services/documentation-standard) as much as possible. The [Getting Started](/getting-started) page explains how to make a new service.

## Templates

- [Python Template](/services/python-template) (2021)

## User Interface
- [User Interface](user-interface) (N/A)
- [Notebook](notebook) (2020 Spring)
- [Serice Fetcher](service-fetcher) (2019)
- [Authentication Service](authentication-service) (2019)
- [Socket Service](socket-service) (2019)

## Categories

### Transportation Network (RFC 0020)
- [Creator](/services/TNM_Creator_Genesis) (2021)
- [Controller](/en/services/TNM_Controller) (2021)
- [Combiner - Weights](/services/TNM_Combiner_WeightCombiner) (2021)
- [Combiner - Enhancers](/services/TNM_Combiner_EnhancerCombiner) (2021)
- [Weighter - Heavy Traffic](/services/TNM_Weighter_HeavyTraffic) (2021)
- [Weighter - Naive Length](/services/TNM_Weighter_NaiveLength) (2021)
- [Weighter - Naive Time](/services/naive_time_weighter) (2021)
- [Enhancer - Fill With Mean](/services/TNM_Weighter_FillWithMean) (2021)
- [Router - ViaFuelStations](/services/TNM_Router_ViaFuelStation) (2021)
- [Router - Traveling salesman](/services/Traveling_salesmen) (2021)
- [Router - Dijkstra](/services/Dijkstra_routing) (2021)
- [Router - Naive Greedy search](/services/Greedy_routing) (2021)



### Path Analytics
- [Attribute Prediction](attribute-prediction) (2020 Spring)
- [Graph Attributes](graph-attributes) (2020 Spring)
- [Route Planner](route-planner) (2020 Spring)
- [Attribute Completion](attribute-completion) (2019)

### Trajectory Analytics
- [Historic Road Tool](Historic-Road-Tool) (2020 Spring)
- [Map Matching](map-matching) (2020 Spring)
- [Map Matching Service](/services/map-matching-service-fall-2020) (2020 Fall)
- [Speed Analysis](speed-analysis) (2020 Spring)
- [Weight Completion](Weight_Completion) (2020 Fall)

### Time Series Analytics
- [Exoskeleton Analytics Tool](/services/Exoskeleton_Analytics_Tool) (2019)
- [Exoskeleton Classifier](/services/ExoskeletonClassifier) (2020 Fall)
- [Generic Prediction](Generic_Prediction) (2019)
- [Stock Prediction](stock_prediction) (2020 Fall)
- [Time Series Anomaly Detection](time-series-outlier-detection) (2020 Spring)
- [Time Series Forecasting](time-series-forecasting) (2020 Spring)
- [Outlier Detection](/services/OutlierDetection) (2020 Spring)
- [Streaming Service Connector](/services/StreamingServiceConnector) (2020 Spring)
- [Wind Speed Predictor](/services/WInd_Speed_Predictor) (2021 Fall)
-	[Crude Oil Prediction](/services/CrudeOilPrediction) (2021 Fall)
-	[Electricity Price Predictor](/services/ElectricityPricePredictor) (2021 Fall)

### Speech Analytics
- [Echelon](echelon) (2019)

### Other
- [Bucketizer](bucketizer) (2020 Spring)
- [Legacy Services](legacy-services) (2019)

## Utility
- [DB-resolver](db-resolver) (2019)

## Libraries
- [python36 ASTEP form utils](/services/python36-astep-form-utils) (2020 Spring)

## The 2018 system

The 2018 system split all services into a single UI (the front-end) which requested data from a number of services (the back-end). The project groups programmed all input functionality and graphical output for each of their services into the same UI (the same project), where this UI would simply perform API calls to the respective back-end service depending on the selected project. The backends were referred to as `[project]REST-API` in GitLab.

### The 2018 services

The [Legacy Services](legacy-services) service from 2019 is basically a copy of the 2018 UI, allowing the 2019-2020 UI to still interface with the old back-ends, which are still running on the [Docker host server](/servers#ui-proxy-docker-host). If you ever want to look though the old source code, do note that the 2018 semester groups moved a lot of functionality into libraries, which are separate projects from the back-end projects. The 2018 services are:

- [Logistics](logistics)
- [Ride Sharing](ride-sharing)
- [Hazardous Road](hazardous-road)
- [Driver identification](driver-identification)
- [Map Matching V2](map-matching-v2)
- [Vehicle to Grid](vehicle-to-grid)
- [Energy](energy)
