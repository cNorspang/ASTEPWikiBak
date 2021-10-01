---
title: The 2019 Microservice Interface Standards
description: Throughout 2019 three revisions of the standard was made with the primary focus of supporting the dynamically rendered UI elements (fields and charts).
published: true
date: 2020-08-07T19:11:56.344Z
tags: 
editor: undefined
---

# The 2019 Microservice Interface Standards

The 2019 Microservice Interface Standard was made in order to support the dynamically generated [fields](/user-interface/fields) and [charts](/user-interface/charts) in the then new 2019 User Interface. This was subsequently extended twice, resulting in the `19w08` and `y19w20` standards, which added the distinction between *user fields* and *developer fields*. The UI can toggle between two modes displaying either *user-* or *developer fields*, called *user mode* and *developer mode*.

> NOTE: The following is taken from [RFC-0004](/rfc/0004) verbatim.
{.is-info}

#### Info

The UI requires the name of the service, what version of the interface is utilized (to create backward and forward capabilities), and a category to index these correctly in the navbar.
It is quite important that a given microservice does not return a version number which is not actually enforced, as the UI will render data from the service incorrectly. 
If the info-endpoint is not created, the service fetcher will simply ignore the service, making it possible for non-UI relevant microservices to run on the production cluster without interfering with the UI.

interface:
```json
GET /info
return: {
  "name": string,
  "version": string,
  "category": number
}
```
The value of `category` has to be in `[-1,0,1,2]` where they represent "Other", "Path Analytics", "Trajectory Analytics", "Time-Series Analytics", respectively.

`version` has to be in the set of accepted version (see versioning).

Example:
```json
{
  "name": "My Routing Tool",
  "version": "2019",
  "category": 0
}
```

### Readme
*required from version `y19w20`*

This is returned on the index page of a given project, and upon pressing the `documentation` button.

Interface:
```json
GET /readme
return: {
  "chart_type": string,
  "content": <aditional data as expected by the specific chart type - see chart types>
}
```
Example:
```json
{
  "chart_type": "markdown",
  "content": "### This is my readme file!"
}
```


#### Fields

This endpoint is used to generate the form area.
The fields supplied here should reflect the values expected at the `render` endpoint.

Depending on the version returned at the `info` endpoint, differences will be expected

these will return lists of `Field`, which has the following structure:

```json
interface Field {
  "type": string,
  "name": string,
  "label": string,
  "options"?: [ { name: string, value: string } ],
  "default": string
}
```

##### Allowed field types


This is the exhaustive list of field types.
The values mean the following, and map to their HTML counterparts:
* `name` is the name of the fields and will be used as key when sending data to `/render`  
* `label` is the text just above the field in the form  
* `options` is optional, but required when type is "select".  
* `default` is the default value set in the field or the default option chosen for type "select".
* `placeholder` is the default value set in the field or the default option chosen for type "select".
* `fields` is a list of subfields (so it"s recursive)

The following list is examples, but should be deducible:

###### Input
Single line text input

```json
{
  "name": "variable_name",
  "label": "My Label",
  "default": "hello world",
  "placeholder": "Input some text",
  "type": "input"
  
}
```
Optional: `default`, `placeholder`

###### File
File upload field

```json
{
  "name": "variable_name",
  "label": "My Label",
  "placeholder": "Input some text",
  "type": "file"
}
```
Optional: `placeholder`


###### Checkbox
A boolean checkbox field.

```json
{
  "name": "variable_name",
  "label": "My Label",  
  "default": "true", 
  "placeholder": "Input some text",
  "type": "checkbox"
}
```
Optional: `default`, `placeholder`
###### Numeric
Numerical input value.

```json
{
  "name": "variable_name",
  "label": "My Label",
  "default": 1234,
  "placeholder": "Input some text",
  "type": "input-number"
}
```
optional: `default`, `placeholder`

###### Select Field
Select dropdown field.

```json
{
  "name": "variable_name",
  "label": "My Label",
  "default": "encoder_decoder",
  "type": "select",
  "options": [ 
    {
      "name": "Encoder Decoder",
      "value": "encoder_decoder"
    },
    {

      "name": "CNN",
      "value": "cnn"
    } 
  ]
}
```
optional: `default`

###### Select Field (with sub elements)

Select dropdown field.
Depending on the selected value different fields are shown.

```json
{
  "name": "variable_name",
  "label": "My Label",
  "default": "encoder_decoder",
  "type": "formset-select",
  "options": [ 
    {
      "name": "Encoder Decoder",
      "value": "encoder_decoder",
      "fields": []
    },
    {
      "name": "CNN",
      "value": "cnn",
      "fields": [
        {
          "name": "variable_name",
          "label": "My Label",
          "default": 1234,
          "placeholder": "Input some text",
          "type": "input-number"
          
        }
      ]
    } 
  ]
}
```
Optional: `default`
###### Button

??? 

##### Version `2018` & `2019`
*deprecated*
interface:
```text
GET /fields
return: [Field]
```
example:
```text
GET /fields
return: [
    {
        "name": "model_name", 
        "label": "Name of Model", 
        "type": "select", 
        "options": [
            {"name": "My Cool Model", "value": "cool_model"}, 
            {"name": "Ugly Model", "value": "ugly_model"}
        ]
    },
    {
        "name": "data_size", 
        "label": "Size of test badge", 
        "type": "num", 
    }
]
```
##### Version `19w08`

interface:
```text
GET /fields
return: {
    "user_fields": Field[],
    "developer_fields": Field[],
}
```
example:
```text
GET /fields
return: {
    "user_fields": [
        {
            "name": "model_name", 
            "label": "Name of Model", 
            "type": "select", 
            "options": [
                {"name": "My Cool Model", "value": "cool_model"}, 
                {"name": "Ugly Model", "value": "ugly_model"}
            ]
        },
        {
            "name": "data_size", 
            "label": "Size of test badge", 
            "type": "num", 
        }
    ],
    "developer_fields": []
}
```

#### Render

The endpoint used to render a specific chart, be it a topological map, a linechart or something else.

It **must** allow POST requests. It may optionally support GET requests.

The input required here depends on the fields expressed through the `field` endpoint, as the fields generate a form that sends a request to this endpoint.

**Important note**: the input is form data(on the form `key1=value1&key2=value2`), which is what the UI will send.

Interface:
```json
POST /render
input: list of fields as formdata
return: {
  "chart_type": string,
  "content": <aditional data as expected by the specific chart type - see chart types>
}
```
Example:
```json
POST /render
input: "model_name=cool_model&data_size=5"
return: {
  "chart_type": "text",
  "content": "this is a data dump of your cool model."
}
```