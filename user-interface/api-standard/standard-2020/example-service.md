---
title: Microservice Example
description: A brief example of a microservice and what contents are passed through each endpoint
published: true
date: 2020-08-07T20:18:07.357Z
tags: 
editor: undefined
---

# Microservice Example

Every microservice within aSTEP must expose certain [endpoints](/user-interface/api-standard) to be usable in the aSTEP UI. Seen below is a mock example of a microservice that implements the [`2020v1`](/user-interface/api-standard/standard-2020) Microservice Interface Standard. This example service takes one or more gps coordinates and tell which city they are located in. 

## /info

The `/info` endpoint output below declares that the display name of the service is `micro-service-example` and that it is placed under category `1 = Trajectory Analytics` (as of spring 2020). The service's identifier (used in "[notebook mode](/user-interface#notebook-mode)") is `example-id` and the service implements the `2020v1` Microservice Interface Standard.

The `/info` endpoint defines one input channel named `gps-coordinates` of type `gps`, and one output channel named `gps-map` of type `gps-map`. This means the service at least requires a list of GPS coordinates as input and definately will output a map with GPS points on it. The types of channels may be arbitrarily chosen, but must have the same meaning accross all services.

```json
{
    "id":"example-id",
    "name":"micro-service-example",
    "version":"2020v1",
    "category":1,
    "input":[
        {
            "name":"gps-coordinats",
            "label":"insert GPS coordinates here",
            "type":"gps"
        }
    ],
    "output":[
        {
            "name":"gps-map",
            "label":"GPS point on map",
            "type":"gps-map"
        }
    ]
}
```

## /fields

The `/fields` endpoint here defines one *user field* and one *developer field*. The user field is of the type `select` (drop-down menu) with the name `matching-area`, in which the user can select wether to match GPS coordinates to Danish cities only or to all cities in the world. The developer field is of type `select` with the name `test-select`, in which the user can select one of a series of tests.

```json
{
    "user_fields":[
        {
            "name":"matching-area",
            "label":"Matching area",
            "default":"only-denmark-area",
            "type":"select",
            "options":[
                {
                    "name":"Only denmark",
                    "value":"only-denmark-area"
                },
                {
                    "name":"Entire world",
                    "value":"entire-world-area"
                }
            ]
        }
    ],
    "developer_fields":[
        {
            "name":"test-select",
            "label":"Select a test",
            "default":"none-test",
            "type":"select",
            "options":[
                {
                    "name":"None",
                    "value":"none-test"
                },
                {
                    "name":"All tests",
                    "value":"all-test"
                },
                {
                    "name":"Location test",
                    "value":"location-test"
                },
                {
                    "name":"Matching test",
                    "value":"matching-test"
                }
            ]
        }
    ]
}
```

## /readme

The `/readme` endpoint simply outputs the service's user documentation (the `README.MD` file) in a markdown chart.

```json
{
    "chart_type":"markdown",
    "content":"# Example \n\nThis service matches GPS coordinates to cities.
}
```

## /render

Upon clicking "*Visualize Results*", the UI could send the following input to the service along with the `POST` request to `/render`. We match a single coordinate [57.11,9.82] to a city that can only be in Denmark, and we don't perform any tests.

```http
gps-coordinats = 57.11,9.82
matching-area  = only-denmark-area
test-select    = none-test
```

The service processes the input and could produce the following output. It outputs a chart of type `map-cluster` and centers the initial map-camera-position to exactly above the entered coordinate. The coordinate itself is added to the chart's list of points to display.

```json
{
    "chart_type":"map-cluster",
    "content":{
        "view":{
            "center":{
                "lat":57.11,
                "lon":9.82
            },
            "zoom":7.5
        },
        "points":[
            [57.11, 9.82]
        ]
    }
}
```

## /data

Upon clicking "*Print Raw Results*", the UI could send the following input to the service along with the `POST` request to `/data`. We again match a single coordinate [57.11,9.82] to a city that can only be in Denmark, and we don't perform any tests.

```http
gps-coordinats = 57.11,9.82
matching-area  = only-denmark-area
test-select    = none-test
```

The service processes the input and could produce the following output. The output says that the first (and only) GPS coordinate maps to Aalborg in Denmark. Do notice that the output of `/data` has a property named after the output channel defined in `/info`. All output channels should show up in the output of `/data` like this.

```json
{
	  "gps-map":[
        "Aalborg, Denmark"
    ]
}
```

## /combined

Lastly, the `/combined` endpoint simply outputs both the results for `/render` and `/data` at the same time. Given the same input as with `/render` and `/data`, the `/combined` endpoint will produce the following output.

```json
{
    "render":{
        "chart_type":"map-cluster",
        "content":{
            "view":{
                "center":{
                    "lat":57.11,
                    "lon":9.82
                },
                "zoom":7.5
            },
            "points":[
                [57.11, 9.82]
            ]
        }
    },
    "data":{
	      "gps-map":[
             "Aalborg, Denmark"
        ]
    }
}
```