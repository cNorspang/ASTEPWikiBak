---
title: Generic Prediction
description: What the Generic Prediction does
published: true
date: 2020-11-19T09:22:45.604Z
tags: 
editor: undefined
---

# Generic prediction
The Generic prediction service takes any dataset on the csv format, uses machine learning models to create a model for predictions. Then it can make a prediction of future data based on the input data.

## Input
The input data must be given in the csv format: with the first line being the names of the variables, and the following lines being the data itself. This could look like so in excel:

<style>
        table, th, td {border: 3px solid  #000;}
        table {   border-collapse: collapse; }
</style>

<table overflow-x="auto" class="a"> 
  <tr>
  	<th> Element type x</th>
    <th> Element type y</th>
  </tr>
  <tr>
    <th> x1</th>
    <th> y1</th>
  </tr>
  <tr>
    <th> x2</th>
    <th> y2</th>
  </tr>
  <tr>
    <th> ...</th>
    <th> ...</th>
  </tr>
  <tr>
    <th> x_n</th>
    <th> y_n</th>
  </tr>
</table>

Furthermore it needs a trained model, this can be aquired by following the documentation guide under the service. (https://astep.cs.aau.dk/tool/astep-2019-sw601f19.astep-dev.cs.aau.dk)
Lastly it takes 2 input parameters: the amount of steps to predict, and how many steps to use for each input.

## Output
The output of the service, is a model that canbe used to predict future data points for the dataset. Furthermore if you upload the model to the service (or run one of the examples on the service) you will be able to see the following:

![generic_prediction_picture.png](/generic_prediction/generic_prediction_picture.png)

> This page was not written by the original creators and is purely based on the documentation on the service's readme file.
{.is-info}
