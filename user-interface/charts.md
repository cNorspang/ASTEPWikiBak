---
title: Chart types
description: A list of all the charts available in the aSTEP user interface.
published: true
date: 2021-11-15T12:03:32.722Z
tags: user_interface, ui, chart
editor: markdown
---

# Chart Types
> NOTE: This page assumes you've read and understood [how the UI interacts with microservices](/user-interface#how-the-ui-interacts-with-microservices) in order to render and display graphical results.
{.is-info}

> NOTE: This page documents only the charts we could find documentation on. There are some undocumented charts which can be found by looking at the [UI source code](https://daisy-git.cs.aau.dk/astep-2020/UserInterface/-/blob/master/app/src/app/chart-view/chart-view.component.html).
{.is-info}

To display visual results, services output textual definitions of "charts", which are standardized visual elements rendered by the [user interface](/user-interface) itself, and not the service. This is done to make all aSTEP services look alike. In the following you'll find descriptions of all available charts as well as a [guide to create new charts](#how-to-create-new-chart-types).

Services output charts in [JSON](https://en.wikipedia.org/wiki/JSON) format as described in each chart's "syntax" section, which shows templates for each respective chart. These templates will make use of wildcards for you to fill out, the details of which are as follows:

| **type** | **definition** |
|:---:|---|
|**[string]**|Any string|
|**[number]**|Any real number (decimal or integer) |
|**[coordinate]**|A dictionary, given as `{"lat":[number],"lon":[number]}` |
|**[geo-view]**|A dictionary, given as `{"center":[coordinate],"zoom":[number]}` |
|**[color]**|An HTML color (`#fff`, `#2a2a2a`, `rgb(255,255,255,1)`, `white`) |
|**[any]**| Dependent on the chart. See footnotes for the specific chart |

## Text chart 
The 'Text' chart simply renders its content as any other HTML renderer. The purpose for this chart is to show documentation or similar text-based information (for example a datadump), however, it can also be used to create a custom output, not supported by any other chart type.

> A problem that might need fixing: Relative links to images in your project folder etc. will not simply work, as the HTML is shown "as-is". Relative links will - when parsed by the client browser - point at the UI server and not the microservice from which they are returned. Keep in mind that this is problematic when you intend to show images from a /static folder in your Flask app, or similar.
> It is preferable, when possible, to use the Markdown chart type instead when referring to your static assets, as it enforces a standardized design, but also supports relative links. Some applications on the platform currently save their static resources on this wiki in the [Page_for_permanent_pictures](/Page_for_permanent_pictures) folder when HTML is needed, and use absolute links instead. The behavior of the text chart described above is an area of possible improvement.
{.is-warning}

### Syntax
```json
{
    "chart_type": "text"
    "content": [HTML string]
}
```

### Output
The given HTML string, as-is.

## Markdown
The 'Markdown' chart converts its Markdown content into HTML and renders this. This type is preferred over raw HTML, since it is sure to conform to set style standards. See [this basic syntax guide](https://www.markdownguide.org/basic-syntax/) for more information about Markdown and the possibilities within it.

The purpose of this chart type is to show README files, but it can be utilized to show any form of data. Another advantage is that relative links are rewritten when converting the Markdown to HTML. This makes it possible to self-host images, but also link to other endpoints. For example if the output contains a download link or likewise.

To make use of the relative paths, you must expose them in the API of your service. For example, if your Markdown includes an image, say `![](my_image.jpg)`, the service will need an endpoint for `my_image.jpg`, which returns JPG data and has the content-type `image/jpg`. Similarly, if the markdown includes a link as `[click here to download](statics/our_report.pdf)` you should have an endpoint called `statics/our_report.pdf`, which returns PDF data and has the content type `application/pdf`. It is recommended you read up on "serving static files" within the framework you're using for your service, in order to make the endpoints to the files.

From a technical perspective, the conversion from a relative path to an absolute path is done by prepending the URL of the microservice to the relative path if the following regex, when tested on the relative path, finds zero matches: `/^https?:\/\/|^\/\//i`. 

### Syntax
```json
{
    "chart_type": "markdown"
    "content": [markdown string]
}
```

### Output
The Markdown content converted into HTML.


## Simple-table
The 'simple-table' chart adds the ability to represent data in a easy-to-read format.
This chart is a generic table, where the developer can define their own columns where each column can be sortable.

This chart is implemented from [Hjalmers Angular-Generic-Table](https://github.com/hjalmers/angular-generic-table). The module is installed in the app and a part of the component is implemented. A bit of customization is done to make compatible with the aSTEP platform.

The simple-table was implemented in 2020-fall and is used by the [exoskeleton-classifier](/services/ExoskeletonClassifier) service.

### Syntax
```json
{
	"chart_type": "simple-table",
	"content": {
		"settings":[ settings ],
		"fields":[ fields ],
		"data":[ data ]
	}
}
```


### Configuration
> The configuration settings below are just the basics to get the table working, if you want to know more, visit hjalmers [wiki](https://github.com/hjalmers/angular-generic-table/wiki/Configuration).
{.is-info}


#### Settings: 

The settings array defines how each column behaves. Here we define in which order the columns should be displayed, and if the user should be able to sort the table with this column, or how a column should be sorted as default. The "objectKey" is used as a unique identifier to the specific column. More settings can be found [here](https://github.com/hjalmers/angular-generic-table/wiki/Configuration#settings-array)

```json 
"settings": [ 
	{
    "objectKey": [ string ],
    "sort": [ enable, asc, desc or disable ],
  	"columnOrder": [ int ]
 	}
]
```

#### Fields: 

In the fields array, the "name" property is printed as the column header, of the column with the corresponding objectKey. It can be used to much more, which is documented in hjalmers [wiki](https://github.com/hjalmers/angular-generic-table/wiki/Configuration#fields-array).   

```json 
"fields": [
	{
  	"name": [ string ],
    "objectKey": [ string ]
 	}
]
```

#### Data: 

The data array is where all the data that has to be displayed in the table, goes. Each entry is a row in the table. The properties has to be a objectKey defined earlier, which defines which data goes into which column.

```json 
"data": [
	{
  	"first column": "first row",
    "second column": 1,
	},{
  	"first column": "second row",
    "second column": 2,
	}
]
```

### Example syntax
```json
{
	"chart_type": "simple-table",
	"content": {
  	"settings": [ 
      {
        "objectKey":'id',
        "sort":'asc',
        "columnOrder":0
      },{
        "objectKey":'name',
        "sort":'enable',
        "columnOrder":1
      }
  	],
    "fields": [
      {
        "name":'ID',
        "objectKey":'id'
      },
      {
        "name":'Name',
        "objectKey":'name'
      }
    ],
    "data": [
      {
        "id": 1,
        "name": "Anna",
      }, {
        "id": 2,
        "name": "Julie",
      }
    ]
  }
}
```

### Example output
![simple-table-output.png](/chart_examples/simple-table-output.png)

## Geographical Clustering
This chart creates clusters on a geographical map. This chart was originally created for a service made by a 2018 group that used clustering to display traffic collision and risk zones. This chart can be used to display clustering based on different geographical point. The clusters will merge and split according to the zoom-level.

### Syntax
```json
{
   "chart_type": "map-cluster"
   "content": {
      "view": [geo-view]
      "points": [list of [coordinate]]
   }
}
```

### Example Output
![cluster-output.png](/chart_examples/cluster-output.png)

## Geographical Geometry
The 'Geographical Geometry' chart should be able to create any geometric shape on a geographical map (given enough fiddling). The chart uses [OpenLayers](https://openlayers.org/)' javascript library to take a GeoJSON object, interpret it, and draw it on a world map. This chart was originally made by a 2018 group that used the geometry to draw routes on the map.

You can play around with GeoJSON at this website: https://geojson.io. A more technical demonstration is found [here](https://openlayers.org/en/latest/examples/geojson.html). Do note that this chart (as of the Spring 2020) does not implement all geometries (there are more geometries available than those on the website) and is a bit restrictive in regards to the styling of features. It is possible to add the missing functionality if you do the necessary programming. The guide to [creating new chart](#how-to-create-new-chart-types) explains where charts are located.

### Syntax
```json
{
    "chart_type": "map-geo"
    "content": {
       "view": [geo-view]
       "featureData": {
           "type": "FeatureCollection"
           "features": [list of [feature]]
       }
    }
}
```

The basic syntax for this chart is as above. The value of `view` defines the initial position and zoom on the map, as the chart is loaded. The value of `featureData` is the same object as on the https://geojson.io website. The `[feature]` objects inside the `features` list/array is structured almost exactly like the features on the https://geojson.io website. Note that `properties` here and on the website are *completely different things* (sorry). Below you see the syntax for a feature. 

```json
// [feature]
{
    "type": "Feature",
    "style": [style],
    "geometry": [geometry],
    "properties": {
        "name": [string]
    }
}
```
Optional: `properties`, `name`.

The value of `type` is a constant, which is required by the GeoJSON standard. If the value of `name` inside the optional member `properties` is provided, the chart will display that name along with the color of the feature. The syntax for `[geometry]` are shown below and `[style]` further below.

```json
// [geometry]
{
    "type": [string],
    "coordinates": ['type'-dependent*]
}
```

The chart supports 4 geometry-types: *Point*, *MultiPoint*, *LineString*, and *MultiLineString*. The value-type of `coordinates` depends on the value of `type` as depicted below. Note, here a coordinate is just a list consisting of longitude and latitude, e.g. [5.5, 6.6], and not a dictionary, as was mentioned earlier (at least in Python). 

```json
[coordinate]                     // "type": "Point"
[list of [coordinate]]           // "type": "MultiPoint"
[list of [coordinate]]           // "type": "LineString"
[list of [list of [coordinate]]] // "type": "MultiLineString"
```

Lastly, `[style]` is structured according to the syntax below. However, not all geometry types make use of all style options. Unused options may be omitted. The comments show what geometry-types use what style options. (as of fall 2020 this is not correct and all styleoptions must be included)

```json
// [style]
{
    "fill": {
        "color": [color]  // Point, MultiPoint, LineString, MultiLineString
    },
    "stroke": {
        "color": [color], // LineString, MultiLineString
        "width": [number] // LineString, MultiLineString
    }
}
```

### Example Output
![geo-lines-output.png](/chart_examples/geo-lines-output.png)

## Chart.js
Chart.js is a powerful javascript framework for rendering different linecharts, barcharts, and others. These types can be used for temporal data.

### Syntax
```json
{
    "chart_type":"chart-js"
    "content": {
        "data": [list of 
            { 
                "data": [list* of [number]], // Values on the y-axis
                "label": [string]            // The name of the data series
            }
    	  ],
    	  "labels": [list* of [string]],       // The labels on the x-axis
  		  "colors": [list of
    	      { 
                "backgroundColor": [color],
      	        "borderColor": [color],
      	        "pointBackgroundColor": [color],
      	        "pointBorderColor": [color],
      	        "pointHoverBackgroundColor": [color],
      	        "pointHoverBorderColor": [color]
    	      }
  	    ],
  	    "type": [string*]
    }
}
```

`[list*]` elements all have to be the same length.

`[string*]` can be any of the following:

- line
- bar
- radar
- doughnut
- pie
- polarArea
- bubble
- scatter

### Example Output
![chartjs-output.png](/chart_examples/chartjs-output.png)

## Composite
Sometimes it is relevant to display multiple different types of data. For example a graph and a datadump and an explanation of the values. 

Instead of making a custom chart type with all these values, it is possible to use the composite chart to display them in multiple tabs. Each tab displays its own chart, making it easy to navigate between them, without making new backend requests.

### Syntax
```json
{
    "chart_type": "composite",
    "content": [list of 
        {
            "name": [string]
            "chart_type": [string*]
            "content": [any*]
        }
    ]
}
```

`[string*]` must be a chart\_type defined on this page.

`[any*]` must	be the content of the given chart type.

### Example Output
![composite-output.png](/chart_examples/composite-output.png)

## Composite Scroll
The 'Scroll' chart appends charts after each other in a scrollable window.

### Syntax
```json
{
    "chart_type": "composite-scroll",
    "content": [list of 
        {
            "chart_type": [string*]
            "content": [any*]
        }
    ]
}
```

`[string*]` must be a chart\_type defined on this page.

`[any*]` must	be the content of the given chart type.

### Example output
The example contains a 'Geographical Geometry' chart and a 'Chart.js' chart.
![scroll-chart-1-min.png](/chart_examples/scroll-chart-1-min.png)

## Generic Timeseries Chart
This chart type is based on the chart framework [ChartJS](https://www.chartjs.org/).
The front-end uses ChartJS 2.7.3. To check if this has been updated go [here](https://daisy-git.cs.aau.dk/astep-2021/userinterface-21/-/blob/master/app/package.json). 
The source code implementation can be found [here](https://daisy-git.cs.aau.dk/astep-2021/userinterface-21/-/tree/master/app%2Fsrc%2Fapp%2Fcharts%2Fgeneric-timeseries).


### Syntax
The syntax of the `generic-time-series` chart type is detailed below. Starting with the entire overview of JSON properties, which are described in more detail afterward.
```json
{
    "chart_type": "generic-time-series",
    "content": {
        "chartData": { 
        		<Dictionary of [string]: {
                    "data": [List of [float]],
                    "inputSize": [integer],
                    "predictions": [
                    		List of {
                            "data": [List of [float]],
                            "error": <Dictionary of [string]: [float]>,
                            "classifications": <Dictionary of [string]: [float]>
                    		}
                		]
            }
        },
        "labels": <Either [List of [string]] or <NoneType>>
    }
}
```

```json
//chartData
{
    "chart_type": "generic-time-series",
    "content": {
        "chartData": { 
        		<Dictionary of [string]: [List of [dataset]]
        },
        "labels": <Either [List of [string]] or <NoneType>>
    }
}
```
*Note that `dataset` is not a JSON property for the chart type, however it is used as an abstraction above to ease the understanding of the different JSON components of the chart type. The `dataset` property is simply replaced by wrapping the contents in curly brackets, see the example provided further below.*

`labels` corresponds to the values shown on the x-axis of the rendered chart. Default is simply the integer range from 1 to input length of the data.

```json
//dataset
"chartData": {
		<Dictionary of [string]: {
    		"data": [List of  [float] or [integer]],
        "inputSize": [integer],
        "predictions": [List of [prediction]]
    }
}
```
`data` corresponds to the input data, i.e the solid part of the function when rendered.
`inputSize` corresponds to the amount of elements from `data` to use for the next prediction step.

```json
//prediction
"predictions" : {
		"data": [List of [float] or [integer]],
    "error": <Dictionary of [string]: [float]>,
		"classifications": <Dictionary of [string]: [float]>
}
```
`data` corresponds to the y-values of the prediction based on the input data. Providing one element for `data` corresponds to predicting 1 timestep ahead, providing *n*-elements corresponds to prediction the next *n*-timesteps ahead.
`error` is a dictionary mapping a `string` to a `float`, corresponding to providing a name of an error function to the output of said error function. i.e using Mean Average Error (MAE) one can pass:
```json
error: {
		"mae": 66.3
}
```
`error` is optional.

`classifications` is a dictionary mapping a `string` to a `float`, corresponding to providing a name of a class to the confidence of the data belonging to said class. For example provided data is examined to determine if it is an outlier:
```json
classifications: {
		"outlier": 90
}
```
`classifications` is optional.

### Example of `generic-time-series` use
```json
  {
    'chart_type': 'generic-time-series',
    'content': {
        'chartData': {
            'My Function': {
                'data': [
                     0,
                     100,
                     200,
                     8300,
                     8400
                ],
                'inputSize': 3,
                'predictions': [
                     {
                        'data': [
                             300,
                             300,
                             300,
                             300,
                             300
                        ],
                        'error': {
                            'mae': 60.0,
                            'smape': 17.320508075688775
                        }
                    },
                     {
                        'data': [
                             400,
                             400,
                             400,
                             400,
                             400
                        ],
                        'error': {
                            'mae': 80.0,
                            'smape': 20.0
                        }
                    },
                     {
                        'data': [
                             8700,
                             8700,
                             8700,
                             8700,
                             8700
                        ],
                        'error': {
                            'mae': 1740.0,
                            'smape': 93.27379053088815
                        }
                    },
                     {
                        'data': [
                             8800,
                             8800,
                             8800,
                             8800,
                             8800
                        ],
                        'error': {
                            'mae': 1760.0,
                            'smape': 93.8083151964686
                        }
                    },
                     {
                        'data': [
                             8900,
                             8900,
                             8900,
                             8900,
                             8900
                        ],
                        'error': {
                            'mae': 1780.0,
                            'smape': 94.33981132056604
                        }
                    }
                ]
            }
        }
    }
} 

```

The JSON example provided above define the `generic-time-series` graph for some arbitrary data.
First of all in line 2 the `chart_type` to use is defined as `generic-time-series`, while the 
the function or line to render is defined in line 5, and called *My Function*.
The input `data` of the function is defined in lines 6 through 12 as 5 data points and the `inputSize` is 3. This signify that the first `data` property within the `predictions` object predict 5 timesteps ahead based on the first 3 input `data` points. In essence, the data points [0, 100, 200] (lines 7-9) is used to predict [300, 300, 300, 300, 300] (lines 16-22) with a `mae` of 60.0 and `smape` of 17.320508075688775 for timesteps 4 through 8, based on timesteps 1 through 3.


The graph use timesteps to move over the predictions at a predefined tickrate.
For timestep 2 the input data points [100, 200, 8300] (lines 8-10) is used to predict another 5 timesteps ahead resulting in the [400, 400, 400, 400, 400] (lines 29-35) prediction with a `mae` of 80.0 and `smape` of 20.0.
This process is carried out until all of the input data has been used or there is no more predictions to render.

A static image of the rendered graph can be seen below, and a working implementation can be generated by visting the [Generic Time Series Prediction Service](https://www.astep.cs.aau.dk/tool/astep-2019-sw601f19.astep-dev.cs.aau.dk?example=3&prediction_steps=10&input_steps=32&data=&gpu=false&model=&gen_input_steps=&gen_prediction_steps=&hyper_config=&tune_config=&train_data=&train_gpu=false&kernel_width=%5B32,32,32,32,32%5D&n_filters=%5B16,16,16,16,16%5D&dilation_rate=8&latent_dim_lstm=50&dropout_lstm=0.2&latent_dim_gru=50&dropout_gru=0.2&latent_dim_reg_lstm=50&dropout_reg_lstm=0.2&train_model=&train_input_steps=32&train_prediction_steps=10&epochs=50&use_bias=false&bias_initializer=1&weight_initializer=1&batch_size=32&val_split=0.2&loss_function=1&optimizer=1&activation_function=1&learning_rate=0.01&clip_value=2&clip_norm=1&host=&image=&model_data=&prediction_data=&command=1) and pressing *Visualise Results*.

![genereic-time-series-prediction-example.png](/generic_prediction/genereic-time-series-prediction-example.png)

## Socket Chart
*NOTE: The documentation here is very vague. Sorry.*

Socket is for two-way – or delayed – textual communication back and forth with the server. This was initially created to make it possible to build Docker images on the GenericPrediction service of 2019, where the process would take some time, so intermediate information was needed, ending with the result being the name of the service.

The value of `sendOnConnect` is a message the socket I/O server *(probably the microservice from which this chart was returned)* will receive upon connection, however the socket I/O server needs logic to handle what ever message it receives (example [here](https://daisy-git.cs.aau.dk/aSTEP-2019/sw601f19/-/blob/master/flask_service.py) starting on lines 268 and 296).

The Socket chart uses another service - the [Socket Service](/services/socket-service) - which works as an intermediate broker for REST-based two way communication. 


### Syntax
```json
{
		"chart_type": "socket",
    "content": {
        "sendOnConnect": <Dictionary of [string]: [any]>,
        "url": [string]
    }
} 
```

### Example
```json
{
    "chart_type": "socket"
    "content": {
        "sendOnConnect": {
            "msg": "hello"
            "times": 5
        },
        "url": "@service"
    }
} 
```

## Undocumented chart types
There are some chart types for which we cannot (or don't have time to) find any documentation nor usage, however, since they exist they are left mentioned but undocumented here:

- `robotics-classification`
- `exoskeleton`
- `driver-identification`
- `pdf`
- `time-series-data`

# How to create new chart types
The current implementation of the architecture is developed in Angular. To add new chart types, these have to be written as TypeScript code in Angular.

It should be possible to implement simple chart types without a deeper understanding of Angular, but more complex behaviour will be easier after reading the [Angular documentation](https://angular.io/docs). 

To add a new chart type, you first need to add a new component-folder to `app/src/app/charts`, which can easily be done by copying one of the existing chart types. Note that the file names and variables have to be changed accordingly. You can find this folder in the [User Interface 2020 Fall](https://daisy-git.cs.aau.dk/astep-2020-fall/UserInterfaceF20/-/tree/master/app%2Fsrc%2Fapp%2Fcharts) on GitLab.

An example could be adding a folder `helloworld-chart` with files:

- `hello-world.component.ts`
- `hello-world.component.css`
- `hello-world.component.html`
- `hello-world.component.spec.ts`

where the `css` file is the stylesheet for the component, the `html` is the template of the component, `ts` is the behavior and `spec` are the specification tests for the component.

The `hello-world.component.ts` file should contain something like:

```typescript
import { ChangeDetectionStrategy, Component } from "@angular/core";
import { ChartComponent } from "../chart-component";

@Component({
    selector: "app-hello-world",
    templateUrl: "./hello-world.component.html",
    styleUrls: ["./hello-world.component.css"],
    changeDetection: ChangeDetectionStrategy.OnPush
})

export class HelloWorldComponent extends ChartComponent<string> {
}
```

It is important to change the `@Component` to have the correct `templateUrl` and `styleUrls` and also to make a relevant `selector`. The selector is the name of the component when used in HTML code, so to use this chart you should write `<app-hello-world [content]="content"></app-hello-world>`, where content has to be a string due to passing a string to the ChartType interface in `ChartComponent<string>`. The code `[content]="content"` should not be changed and is already correct. The name of the class also has to be changed. To see examples of actual behaviour and usage, please see the implementation of existing chart types.

Lastly, you must register the chart. This is done as so:

1. In the file `app/src/app/app.module.ts` ([link](https://daisy-git.cs.aau.dk/astep-2020/UserInterface/-/blob/master/app/src/app/app.module.ts)), the component has to be imported like this:
`import { HelloWorldComponent } from "./charts/helloworld-chart/hello-world.component";`
2. In the file `app/src/app/app.module.ts` ([link](https://daisy-git.cs.aau.dk/astep-2020/UserInterface/-/blob/master/app/src/app/app.module.ts)), the component's name (`HelloWorldComponent`) is added to the `declarations` list.
3. In the file `app/src/app/chart-view/chart-view.component.html`   ([link](https://daisy-git.cs.aau.dk/astep-2020/UserInterface/-/blob/master/app/src/app/chart-view/chart-view.component.html)), the component is added to the switch case handling the chart types like this:
```html
<app-hello-world *ngSwitchCase="'hello-world'" [content]="content"></app-hello-world>
```

Where the name `app-hello-world` needs to be changed to the selector you defined in the `*.component.ts` file, and the switch-case needs to be the label passed from the microservice. That is, if you write `"'my-chart'"` in the switch case, you make the UI use the chart by having your micro-service output the following data to the UI:

```json
{
    "chart_type": "my-chart",
    "content": [your-choice]
}
```

Now the chart type should work as expected. You can test this by [running the UI locally](/services/user-interface#how-to-run-the-ui-locally) and [use a locally running microservice](/user-interface#support-for-multiple-versions-of-a-service) to output the new chart to the UI.

However it is worth discussing with other groups whether the behaviour already exists or if others are working on it. Ideally you should add a section to this page before you start implementing the chart type, to make sure the design make sense and is generalized. This has the side effect that the idea and design of the chart type will be peer-reviewed. Alternatively, you could propose the new chart in an [RFC](/rfc) and have it evaluated at the next steering committee meeting.