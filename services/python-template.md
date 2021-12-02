---
title: aSTEP Python Template
description: 
published: true
date: 2021-12-02T10:34:48.264Z
tags: 
editor: markdown
---

# Python Template Service
This is a template for building a microservice compatible with the aSTEP infrastructure, in which it has implemented the starting points following the RFCs approved by aSTEP.

Currently, many of the RFCs are not properly documented or have confusing explanations. As such, this template tries to be as close to the idea behind the RFCs, but some work would be needed to make them fully compatible.

## How to use
To use this service, simply clone it onto your local computer. Then either remove the (typically hidden) `.git` file, or copy paste the code into a new folder (without the `.git` file), and create a new repository on GitLab to push the code to.

## How to understand the template
The template consist of these:

- A `service.py` file, specifying all the endpoints which the service makes available.
- A `.gitignore` file, preconfigured to ignore standard python files, which should not be on GitLab.
- A `.gitlab-ci.yml` file, which runs all the configuration code for the code to be pushed to Kubernetes.
- A `Dockerfile`, which builds the program image that runs on Kubernetes. Has included a Continious Integration workflow, specifying that all tests should pass for the container to be build.
- A `README.md` file that you read right now
- A `requirements.txt` file, specifying all dependencies which will be installed as part of running the `Dockerfile`
- A `/src` folder having all application code.
- In `/src`, the `__init__.py` file signifies to python that the folder is a python module (making it possible to import/export between files in the folder)
- In `/src`, the `main.py` file has the main function, which run when calling the `/data` endpoint. It should always begin with calling the `adapter.from_json()` method, and returning the `adapter.to_json()` method.
- In `/src`, the `adapter.py` file handles the logic of deserializing the received json to some internal python representation (`from_json()`), and then serializing the internal representation back to some valid json (`to_json()`).
- In `/src`, the `/__pytest__` folder handles all the testing of the microservice, using `pytest` as the framework. 
- In `/src/__pytest__` The `conftest.py` file signifies that `/__pytest__` is a testing folder, similar to `__init__.py` signifying module folders, making it possible to test. It also holds all the fixtures that can be used by all test functions.
- in `/src/__pytest__` The `test_main.py` file holds integration tests for the whole microservice as called on the application level. It initially only tests that the json that comes in, also comes out again.
- In `/src/__pytest__` The `test_adapter.py` file holds all tests for the adapter. For pytest to register tests, all files should be named `test_*.py`. It initially holds some testcode to show pytest functionality.

# Your Service Name
Delete the text above "Your Service Name" and thereafter replace any information which is different from your service and the template in the text below.

Write some introduction, and reference what RFC, product or similar this service supports.

## Content
- [What it does](#what-it-does)
- [How to run it](#how-to-run-it)
- [Input](#input)
- [Output](#output)
- [Endpoints](#endpoints)

## What it does
Describe what it does in such a detail, such that a person who have no context can understand your service (such as the semester coming right after you)

## How to run it
### Run local
To run the code locally,first install docker, and then cd into the service folder, and write
- `docker build --tag your_name .`
- `docker run -p 5000:5000 your_name`

The service will then run on `localhost:5000/` in your browser, as a docker container with the name your_name.

### Run on aSTEP
To run the code on the aSTEP servers, go to Gitlab and in your project, find the CI/CD option and go to Pipeline. Then run the pipeline, which will make sure the `Dockerfile` and `.gitlab-ci.yml` file is run, building the image and pushing it to Kubernetes.

When viewing the pipeline, if the build goes through, the review step will show which url exposes the service.

### Install dependencies
To add new libraries to the `requirements.txt` folder, either just add the libraries following the notation in the `requirements.txt` folder, or create a virtual environment, where you activate the environment, cd into the service folder and then run
- `pip install -r requirements.txt`
- `pip install your_package1, your_package2, ... your_packageN`
- `pip freeze > requirements.txt`

The old dependencies, as well as the new ones, should be in the new `requirements.txt` file, as well as any needed supplementary dependencies.

## Input
Make a presentation of valid input to the service on json format.

```json
{
	"example":{
  	"json": True
  }
}
```

## Output
Make a presentation of valid output to the service on json format.

```json
{
	"example":{
  	"json": True
  }
}
```

## Endpoints
Describe your endpoints