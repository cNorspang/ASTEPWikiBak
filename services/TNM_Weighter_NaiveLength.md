---
title: TNM Weighter Naive Length
description: 
published: true
date: 2021-12-03T08:41:14.691Z
tags: tnm
editor: markdown
---

# TNM Weighter NaiveLength
This service uses the RFC0020 infrastructure, and implements a weighter, which does a naive weighting according to the length of the supplied TNM model.

## What does it do
The flow of the service at the `data endpoint` is as follows
- It receives a `TNM model` from the `controller`.
- The `TNM model` is deserialized in the `adapter` for the `internal representation`.
- This `internal representation` is saved in the `adapter`, for use in the serialization proces at the end of the flow.
- The `internal representation` then goes through all edges, and calculated a normalized weight, such as a small length of an edge gets a weight closer to 0, whereas the longest edge in the whole `TNM model` gets a weight of 1.
- This output then gets put into the `internal representation` of the adapter, which then serializes it and outputs it back to the controller

## How to use
To use this template, simply clone it onto your local computer. Then either remove the (typically hidden) `.git` file, or copy paste the code into a new folder (without the `.git` file), and create a new repository on GitLab to push the code to.

### Run local
To run the code locally,first install docker, and then cd into the service folder, and write
- `docker build --tag naive_length .`
- `docker run -p 5000:5000 naive_length`

The service will then run on `localhost:5000/` in your browser, as a docker container with the name your_name.

### Run aSTEP
To run the code on the aSTEP servers, go to Gitlab and in your project, find the CI/CD option and go to Pipeline. Then run the pipeline, which will make sure the `Dockerfile` and `.gitlab-ci.yml` file is run, building the image and pushing it to Kubernetes.

When viewing the pipeline, if the build goes through, the review step will show which url exposes the service.

### Install dependencies
To add new libraries to the `requirements.txt` folder, either just add the libraries following the notation in the `requirements.txt` folder, or create a virtual environment, where you activate the environment, cd into the service folder and then run
- `pip install -r requirements.txt`
- `pip install your_package1, your_package2, ... your_packageN`
- `pip freeze > requirements.txt`

The old dependencies, as well as the new ones, should be in the new `requirements.txt` file, as well as any needed supplementary dependencies.