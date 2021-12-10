---
title: Naive time weighter
description: A simple service weighting an edge based on length and mean speed
published: true
date: 2021-12-10T12:27:28.874Z
tags: 
editor: markdown
---

# Naive time weighter
This simple service was created to make more options available when using the TNM service.
This service simply looks at all edges and divides the length of the edge by the mean speed when driving here. This gives a very naive time estimate for how long it takes to drive this piece of road. The calculated weight is normalised to a number between 0 and 1, where lower is better.

#### How do i use this service?
Send a **POST** request to **/timeWeight** containing the JSON TNM model defined in RFC0020. The service will then return the same model but weighted. 

## Running the service locally
First of you have to download the repository from [Gitlab](https://daisy-git.cs.aau.dk/astep-2021/group-11/TimeWeighter) and have docker installed on your system. You can also run the service without docker, but do yourself a service and start using docker. After downloading the repository enter it and write the following command:
- `docker build --tag name .`

**name = filename of built image, so change it to whatever suits your needs**
This will build an image according to the specifications of the "Dockerfile" inside the folder. When the image has been build succesfully, it is time to run it with the following command:
- `docker run -p 5001:5000 name`

The "-p" option tells docker to map port 5001 on your computer to port 5000 inside the docker image. This is relevant since the code of this service is specified to listen to port 5000. This also means that we can see our service if we visit:
- `localhost:5001/`

To use the service send a post request to `localhost:5001/timeWeight` containing data that satisfies the input defined higher up on this page. We would recommend the tool `postman` for this process, and if the input was correct, the service will produce a weighted TNM model.