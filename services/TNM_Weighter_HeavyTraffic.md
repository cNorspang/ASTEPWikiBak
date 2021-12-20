---
title: Weighter Heavy Traffic
description: 
published: true
date: 2021-12-20T11:46:50.326Z
tags: tnm
editor: markdown
---

# TNM Weighter Daily Trucks Count
The purpose of the microservice is to adjust the Weight values of the TNM between 0-1 depending on how many trucks there are on a given road. 

## Content
- [What it does](#what-it-does)
- [How to run it](#how-to-run-it)
- [Input](#input)
- [Output](#output)
- [Endpoints](#endpoints)

## What it does
The service predicts how many trucks can be expected in average on a road. This number is then converted to a weight between 0-1 where 1 corresponds to the maximum trucks count.

The service can be trained to predict how many trucks can be expected on a given road by calling the /train endpoint. The prediction is based on features deduced from TNM data. 
When training a model you should supply the trainer with a complete dataset (no null values) however the trainer will automatically remove edges containing null values. If an edge contains any null data it will be removed from the training set.

The services `data` endpoint uses the model which have been trained through the `train` endpoint.
It has a pretrained model, so it is not necessary to call the `train` endpoint.

The trucks count is predicted based on a decissiontree model and converted to a weight.

## How to run it
### Run local
To run the code locally,first install docker, and then cd into the service folder, and write

- `docker build --tag your_name .`

This command runs the Dockerfile, including running all tests, and builds the container with the name `your_name`.

- `docker run -p 5003:5000 your_name`

The service will then run on `localhost:5003/` in your browser.

The service will respond to regular GET and POST requests, as described in the `endpoints` section.
However, to give an example, this is how the service can be called via postman.

- start postman
- localhost:5003/data 
- insert a TNM file from the `/tnm_example_data` folder as raw json in the body
- send request

There would now be a response, containing the exact same TNM, but with weights on edges being between 0 and 1.

To train a model 
- start postman
- localhost:5003/train 
- insert a TNM file from the `/tnm_example_data` folder as raw json in the body
- send request
 
By calling this endpoint, the model `/src/decision_tree_model.joblib` will be overwritten with a new trained model.
It is that model which is used when calling the `data` endpoint.

### Run on aSTEP
To run the code in aSTEP production on the master branch, you have to be a maintainer on gitlab.
Every developer does however have the ability to run the pipelines on all other branches.

To run the code on the aSTEP servers, go to Gitlab and in your project, find the CI/CD option and go to Pipeline. Then run the pipeline, which will make sure the `Dockerfile` and `.gitlab-ci.yml` file is run, building the image and pushing it to Kubernetes.

When viewing the pipeline (by pressing on the status column), if the build goes through, the review or (production when on master) step will show which url exposes the service.

### Install dependencies
To add new libraries to the `requirements.txt` folder, either just add the libraries following the notation in the `requirements.txt` folder, or create a virtual environment, where you activate the environment, cd into the services root folder and then run
- `pip install -r requirements.txt`
- `pip install your_package1, your_package2, ... your_packageN`
- `pip freeze > requirements.txt`

The old dependencies, as well as the new ones, should be in the new `requirements.txt` file, as well as any needed supplementary dependencies.
Theese denpendencies will by installed by docker when a docker image is build.

### run tests
All tests are run automatically when building the docker image.

- `docker build --tag your_name .`

to bypass the automatic testing comment out this line in the Dockerfile

- `RUN ["pytest", "-vv"]`

To run all tests manually run the command.

- `python3 -m pytest`


All tests will run, which are written in files named `test_some_name.py`
All functions in those files, which have a name `test_your_function()` will run as part of the test.
There are examples in `test_main.py` and `test_adapter.py` in the `src/__pytest__` folder. These give examples of a simple test, how to use parametrization (using the same test suite, testing with different values) and mocking (replacing dependencies, to better isolate implementation code)




## Input
The following json describes an example of data, which could be given to the services endpoints.
Concrete examples are in the `/tnm_example_data` folder.
In the [TNM Service](/rfc/0020), as run from the UI, the [Controller](/services/TNM_Controller) will send the data from the [Creator](/services/TNM_Creator_Genesis) to this service.
No matter what, if the following format is kept, the service can accept it.

```json
{
    "meta_data": {
        "max_length": 3778,
        "min_length": 1,
        "max_slope": 24.527,
        "min_slope": -2.407,
        "max_legal_speed": 80,
        "min_recommended_speed": 0,
        "max_mean_speed": 0,
        "min_mean_speed": 0,
        "max_daily_year": 16138.0,
        "min_daily_year": 57.5,
        "max_daily_july": 14813.0,
        "min_daily_july": 51.5,
        "max_daily_trucks": 2472.0,
        "min_daily_trucks": 87.0
    },
    "vehicle": {
        "id": 1,
        "name": "Fiat multipla",
        "data": {
            "top_speed": 150,
            "mileage": 13204.03,
            "max_fuel": 4.3
        }
    },
    "nodes": {
        "1": {
            "id": 1,
            "weight": 0.0,
            "data": {
                "longitude": 15.9550166585396,
                "latitude": 57.1940874759639,
                "country": "DK",
                "municipality": "Aalborg",
                "is_border": False,
                "type": "null",
                "signal_control": True
            },
            "edges": {
                "1": {
                    "id": 1,
                    "from_node_id": 1,
                    "to_node_id": 3,
                    "weight": 0.0,
                    "data": {
                        "length": 162,
                        "slope": "-1.2",
                        "type": "lokalvej, by",
                        "type_max_speed": "50",
                        "set_max_speed": "50",
                        "recommended_speed": "null",
                        "mean_speed": "null",
                        "daily_year": "3600",
                        "daily_july": "300",
                        "daily_trucks": "20",
                        "daily_10_axle": "30",
                        "fuel_station": False,
                        "max_axle_load": "null",
                        "max_height": "null",
                        "max_length": "null",
                        "max_weight": "null"
                    }
                },
                "2": {
                    "id": 2,
                    "from_node_id": 1,
                    "to_node_id": 3,
                    "weight": 0.0,
                    "data": {
                        "length": 151,
                        "slope": "null",
                        "type": "null",
                        "type_max_speed": "null",
                        "set_max_speed": "null",
                        "recommended_speed": "null",
                        "mean_speed": "null",
                        "daily_year": "null",
                        "daily_july": "null",
                        "daily_trucks": "null",
                        "daily_10_axle": "null",
                        "fuel_station": False,
                        "max_axle_load": "null",
                        "max_height": "null",
                        "max_length": "null",
                        "max_weight": "null"
                    }
                }
            }
        }
	}
}
```

## Output
The exact same TNM as described in [Input](#input) is outputtet except that all edges have been annotated weights being between 0 and 1.

## Endpoints
/info
identifies the microservice to aStep UI

/readme
Returns the readme file for the microservice

/data {TNM}
predicts on TNM dataset

/train {TNM}
trains a new model for the microservice, returns confirmation if the model is successfully trained. 
not implemented: returns an accuracy score. 

/predict {TNM}
predicts on TNM dataset

/test {TNM-test-set}
not implemented: returns model prediction accuracy


## What is missing work
The creator creates a proper TNM model, but has some shortfalls which could be expanded upon.

