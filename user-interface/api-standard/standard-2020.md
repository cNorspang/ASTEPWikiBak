---
title: The 2020 Microservice Interface Standard
description: The 2020v1 standard was made to support the Notebook Interface first introduced during Spring 2020.
published: true
date: 2020-08-17T08:44:47.752Z
tags: 
editor: undefined
---

# The 2020 Microservice Interface Standard

In order to support the functionality provided by the [Notebook Interface](/user-interface#notebook-mode) introduced in the Spring 2020 semester, the `2020v1` standard extended the [`y19w20`](/user-interface/api-standard/standard-2019) standard by adding additional information to the `/info` endpoint and defined the new `/data` and `/combined` endpoints. The updated list of endpoints is as such (each item is also a link):

 * [`GET /info`](#info)
 * [`GET /fields`](#fields)
 * [`GET /readme`](#readme)
 * [`POST /render`](#render)
 * [`POST /data`](#data)
 * [`POST /combined`](#combined)

For example outputs for each of the endpoints, refer to the [example service](example-service).

## /info

The `/info` endpoint outputs basic information about the service's identity and functionality. The `/info` endpoint is called with the `GET` method, takes no input, and outputs data with the syntax described below:

```json
GET /info
output: {
    "version": string,
    "name": string,
    "id": string,
    "category": number,
    "input": [list of {
        "name": string,
        "label": string,
        "type": string
    } ],
    "output": [list of {
        "name": string,
        "label": string,
        "type": string
    } ]
}
```

The value of the `version` property tells which version of the Microservice Interface Standard the service implements. Therefore, as of spring 2020, there are only four valid values: `2020v1`, `y19w20`, `19w08` and `2019`.

The value of the `name` property is the label shown in the UI's service-menu and the header displayed when opening a tool in "single-tool mode" and in "notebook mode" (see [this](/user-interface#notebook-mode)).

The value of the `id` property is the service's uniqe identifier and should not be changed once development has moved into later phases, since this identifier is used to find services (used in "notebook mode") that might have been renamed. You should therefore choose a good identifier from the beginning. The format uses lower case letters and dashes for spaces (ie. `my-service`) and should be the same as a valid link to your service on the wiki (so for `my-service` the wiki should have a page with that link in the base).

The value if the `category` property is a number selecting which category the service belongs to and thus which category the service is displayed under in the service-menu. As of the Spring 2020 semester, there are five categories as shown below, however, you should refer to the [UI service wiki-page](/services/user-interface) to see if there are any changes.

- `0`: Path Analytics
- `1`: Trajectory Analytics
- `2`: Time Series Analytics
- `3`: Speech Analytics
- `-1`: Other

The value of the `input` and `output` properties both denote a list of "data channels". The input data channels allow for three kinds of input (the user can choose any one of these methods for each input channel):

- *String input*
- *File upload*
- *The output of another tool (supported in "notebook mode")*

The output channels represent the data outputted by the service and influence the output from the [`/data` endpoint](#data) as explained later. The input/output channels are not intended for settings or the configuration of the service, but rather for raw data, like lists of coordinates or the likes. Configuration is done through the input fields defined by the [`/fields` endpoint](#fields). The types of channels may be arbitrarily chosen, but must have the same meaning accross all services.

The input defined here and the fields defined in `/fields` together define what parameters can be given to the `/data`, `/render` and `/combined` endpoints.

<details>
  <summary>Example</summary>

An example of the output given by the `/info` endpoint when called with a `GET` request:
  
```json
{
    "version": "2020v1",
    "id": "knn-router"
    "name": "kNN Routing Tool",
    "category": 0,
    "input": [ {
        "name": "map-data",
        "label": "Map data for routing on",
        "type": "osm"
    } ],
    "output": [ {
        "name": "routed-map",
        "label": "Map with edges marked if they are in the route",
        "type": "osm-route"
    }, {
        "name": "route",
        "label": "A series of nodes defining a route",
        "type": "route"
    } ]
}
  
```
</details>

## /fields
The `/fields` endpoint outputs a list of the inputs (not the same as those from `/data`) that the service requires from the user. These inputs are represented as "[fields](/user-interface/fields)", of which there are many types. The `/fields` endpoint is called with the `GET` method, takes no input, and outputs data with the syntax described below:

```json
GET /fields
output: {
    "user_fields": [list of [field]],
    "developer_fields": [list of [field]]
}
```

The standard defines both `user_fields` and `developer_fields`, which the user can toggle between in the UI (*user mode* vs. *developer mode*). Do note that the UI does not send the selected mode to the service. In fact, even though the field groups are separate, the names of all fields have to be completely unique, since they are all sent to the service at the same time regardless of the selected mode.

The fields defined here and the input defined in [`/info`](service-interface#info) together define what parameters can be given to `/data`, `/render` and `/combined`.

<details>
  <summary>Example</summary>
  
An example of the output given by the `/fields` endpoint when called with a `GET` request:
  
  ```json
  {
  	"user_fields": [
  		{
  			"name": "street-name",
  			"label": "Street Name",
  			"placeholder": "Ravnsgade",
  			"type": "input"
  		},
  		{
  			"name": "street-zip",
  			"label": "Zip Code",
  			"placeholder": "Input a zip code",
  			"type": "input-number"
  		}
  	],
  	"developer_fields": [
  		{
  			"name": "test-switch",
  			"label": "Select test",
  			"default": "all-tests",
  			"type": "select",
  			"options": [
  				{ "name": "All tests", "value": "all-tests" },
  				{ "name": "Classify Test", "value": "classify-test" },
  				{ "name": "Regression Test", "value": "regress-test" }
  			]
  		}
  	]
  }
  ```
  
</details>

## /readme
The readme endpoint outputs the service's [user documentation](/services/documentation-standard) to the User Interface. This is done by outputting a [Markdown Chart](/user-interface/charts#markdown) containing the markdown-content from the service's `README`-file (which is the user documentation). The `/readme` endpoint is called with the `GET` method, takes no input, and outputs data with the syntax described below:

```json
GET /readme
output: {
	"chart_type": "markdown",
  "content": [readme.md contents]
}
```

<details>
  <summary>Example</summary>

An example of the output given by the `/readme` endpoint when called with a `GET` request:
  
```json
{
    "chart_type": "markdown",
    "content": "# Request for Comments\nTo Manage..."
}
```

</details>

## /render
The `/render` endpoint outputs the results of the service in a [chart](/user-interface/charts); a textual representation which the UI converts into a graphical display. The UI calls the service's `/render` endpoint using the `POST` method and sends the values the user has entered (through input and fields from `/info` and `/fields`) to the service as [form-data](/user-interface/api-standard#input-and-output-formats). In essence, the service receives a list of key-value-pairs, where the key is the name of the input/field and the value is whatever the user entered into that input/field.

```json
POST /render
input: A map from 'field/input name' to 'field/input value'
output: {
    "chart_type": [string],
    "content": [depends on type]
}
```

For an example output, refer to the [example service](example-service#render).

## /data
The `/data` endpoint outputs the results of the service in raw JSON format. This allows the user to browse the raw output in a textual representation or for other services to use this data (supported in "notebook mode"). The UI calls the service's `/data` endpoint using the `POST` method and the same input as with the `/render` endpoint.

The output og `/data` is a JSON object, where the properties/keys are the names of the output channels defined in the `output` property of the `/info` endpoint.

```json
POST /data
input: A map from 'field/input name' to 'field/input value'
output: {
    key1: [any],
    key2: [any],
    ...
    keyN: [any]
}
```

For example, if a service defines two output channels: one with a `name` of `"dank"` and another with a `name` of `"memes"`, the resulting output of `/data` must be structured as such:

```json
{
    "dank": [any],
    "memes": [any]
}
```

For an example output, refer to the [example service](example-service#data).

## /combined
The `/combined` endpoint simply outputs both the `/render` and `/data` outputs in one. This should also be done without doing double computation, so that the server's workload is reduced. The `/combined` endpoint is called with the `POST` method and the same input as `/render` and `/data`.

```json
POST /combined
input: A map from 'field/input name' to 'field/input value'
output: {
    "render": [same output as '/render' given the input],
    "data": [same output as '/data' given the input]
}
```

For an example output, refer to the [example service](example-service#combined).