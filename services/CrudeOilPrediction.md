---
title: Crude Oil Prediction
description: A microservice that predict the price of crude oil based on previous data.
published: true
date: 2021-12-02T23:46:18.440Z
tags: 
editor: markdown
---

# Crude Oil Forecasting

## The Microservice
This microservice aims to predict the price of crude oil based on previous data. The model is made using PyTorch utilizing the Graph WaveNet algorithm. The microservice contains multiple models trained on different data where the difference between the data is the time between each data entry. The user selects what model they want to use by selecting it in a dropdown menu. The microservice will output a graph that includes the data points and the new predicted price as well as a table of the data points and the new predicted price. 

## User Interactions
The users of the microservice have two different ways of using the service. They can either type the input into the input fields or upload a CSV file where the first column contains the crude oil price and the second column contains the dollar index.

The user should aim to use the model closest to their data which means that if the time between each data entry is one hour the user should use the model with one hour between each data entry. 

## The Data
The microservice takes as input a list that needs to have a certain data structure. There is a list that contains the oil prices and a list that contains the dollar indexes. These lists are combined so that: data = [oilPricesList, dollarIndexesList]. The list is then made into a tensor and used on the model to predict. 
