---
title: Notebook Documentation
description: A starting guide for using the notebook interface
published: true
date: 2020-12-09T14:06:36.437Z
tags: 
editor: undefined
---

# Notebook Interface User Guide

You can take a deeper look at the Notebook Interface's source code at the Gitlab repository [here](https://daisy-git.cs.aau.dk/astep-2020-fall/UserInterfaceF20).

## Creating a New Notebook
When you accesss the notebook interface you will be prompted with a list of all the existing notebooks. From here you are able to access your already existing notebooks, delete a notebook (red box) or create a new notebook (blue box).
![notebookcreatedelete.png](/notebookcreatedelete.png)

Creation works by inputting a name for a notebook in the textfield and clicking the blue plus icon. To delete a notebook press the red trashcan icon.

## Adding a New Service
When entering a notebook, the option to add a service to the notebook will be displayed at each supported service in the sidebar. To add the service simply press the icon located on the right (blue box). 
![notebookadd.png](/notebookadd.png)

When a new service is selected, it will be added at the bottom of the notebook. It will be given a default name (red box) that you can change as you want, it is recommended that your service name is either in a form of lowerCamelCase or snake_case.

## Using Stream Processing
To use the stream processing feature, the notebook gives you have to have at least 2 services in the notebook. Please note that it is importan, that you run the service, you wish to get data from or else the system will not have the data available.

We will now show an example where we use the speed analysis service to acquire some data about a specific trajectory and the bucketizer service to group it into more managable pieces.

![notebookserial1.png](/notebookserial1.png)
We start by creating the speed analyser and inputting the trajectory ID that we want to analyse. We then run the service by using the green play button in the top right corner of the service. When the service is done it will show you the data as either the raw JSON data or as a visual render. This can be chosen at the bottom of the service.

![notebookserial2.png](/notebookserial2.png)
For this example we will choose to show the data in raw JSON form, since this allows us to see the available data channels (highlighted in red). These data channels are used to specify what data we want to use in the other services.

![notebookserial3.png](/notebookserial3.png)
When we want to use the data from the speed analysiser in our bucketizer, we specify the ID of the service we what to use. In this case it is "speed", it is important to prefix the ID with @. We then postfix with a dot and the data channel that we want the data from, in this case it is the ".gpsSpeed" data channel.
![notebookresult.png](/notebookresult.png)