---
title: Stock Prediction
description: This page describes the use of the stock prediction service
published: true
date: 2020-12-15T14:51:57.479Z
tags: 
editor: undefined
---

# Stock Prediction
This service aims to predict the close price of a stock, based on the previous price history of the given stock. It uses tensorflow with keras to construct a machine learning model aims to calculate the future price value of a chosen stock.
The machine learning model has a variety of settings that can be used to maximize accuracy of the prediction for the specific stock.
The service is divided into three functions, each serving an essential part of the complete service. The three functions can be chosen in the dropdown menu "Select Command".

## Downloading Stock Data
The download stock function is used to get the history of a stock into the aSTEP database, so that it can be used to train on the stock and later predict the future stock.
The stock data is provided by [Alpha Vantage](https://www.alphavantage.co/), a stock data service, which has a wide collection of free to use stock APIs that can fetch many types of stock data including stock time series, fundamental data and technical indicators.
The APIs used in this service are [TIME_SERIES_DAILY_ADJUSTED](https://www.alphavantage.co/documentation/) which returns all available data of the time series stock history for a given ticker and [SYMBOL_SEARCH](https://www.alphavantage.co/documentation/) which is used to get the ticker of a stock, based on the search query the user inputs, to be used in the TIME_SERIES_DAILY_ADJUSTED API.

| Parameter | Description |
| :- | :- |
| Select command | Choose the function to be used |
| Ticker | Choose a ticker name to download to the database |

## Training a Model
The training function creates a sequential machine learning model, based on the values set in the fieldbar, and trains it, based on the historical stock data available in the database.

When the model has been trained, it will be saved in the same directory as the train.py file, which can then be used with the predict function.

It is only possible to train a model if the chosen stock has been downloaded to the database in advance.

| Parameter | Description |
| :- | :- |
| Select command | Choose the function to be used |
| Select stock | Choose a stock to train on from a list of stocks in the database |
| Select algorithm | Choose the algorithm used to build the model (LSTM or GRU) |
| Number of layers | Choose the amount of LSTM/GRU layers in the model |
| Number of neurons in layer # | Choose how many neurons should be in each layer |
| Batch size | Choose the number of days in each batch |
| Number of epochs | Choose the amount of epochs to be trained |
| Learning rate | Controls how quickly the model is adapted to the problem |
| Dropout rate | Controls removal of neurons and synapses during training |
| Number of days to predict | Controls how many days the algorithm has to predict |
| Lookback | Number of recent data points to be used when predicting each future value |

## Predicting
The predict function uses a trained model to predict the future price history of the chosen stock. The prediction will be shown on a "time series line graph".

| Parameter | Description |
| :- | :- |
| Select command | Choose the function to be used |
| Select stock | Choose which stock to predict from a list of stocks in the database |
| Saved models | Choose the model used to predict from a list of saved models |
| Upload new model | Upload a newly trained model to the aSTEP database |
| Prediction start date | Used in combination with prediction end date to determine how many days to predict|
| Prediction end date | Used in combination with prediction start date to determine how many days to predict |

Note: Only one of the fields "Saved models" and "Upload new model" can be filled in.

## Statistics
This command is used to track statistics over every prediction made on the service

| Parameter | Description |
| :- | :- |
| Select command | Choose the function to be used |
| Select stock | Choose which stock to view statistics on |

## Use Case Example
### Step 1
First start of in the "download stock" function.
In the ticker textbox you write "TSLA" followed by pressing "Visualize results". This will download the price history for the electric car company Tesla Inc. and store it in the aSTEP database, followed by showing you the downloaded data in the right panel.

### Step 2
The second part is to use the training function. In this function you set the parameters to the following values and press "Visualize results":

| Parameter | Value |
| :- | :- |
| Select stock | TSLA |
| Select algorithm | LSTM |
| Number of layers | 2 |
| Number of neurons in layer 1 | 128 |
| Number of neurons in layer 2 | 128 |
| Batch size | 256 |
| Number of epochs | 20 |
| Learning rate | 0.6 |
| Dropout rate | 0.2 |
| Number of days to predict | 10 |
| Lookback | 30 |

The service will then prompt the user to download a .zip file which contains the stock price history and the training file, which the user must run manually. When the training is done the trained model named "TSLA14122020.model" will be saved in the same location as the traning file.

### Step 3
The third part is to use the predict function. It will predict future of Tesla Inc. close price, by using the following parameters:

| Parameter | Description |
| :- | :- |
| Select stock | TSLA |
| Choose model | "TSLA1.model" |
| Prediction start date | 2020-10-12 |
| Prediction start date | 2020-12-12 |

By then pressing "Visualize results" the service will calculate the following 10 days from the 30 last days of price history in the database. After the calculation is done you are finished and a "time series line graph" with the prediction results will be shown in the right panel.

> NOTE: Note that the start date and end date may not be too far apart, as the aSTEP service will then timeout
{.is-info}

### Step 4
The fourth part is to use statistics function. After choosing which stock to view statistics on, the service will show model name, startdate, enddate, average MSE, and average MAE for every prediction of the stock.

| Parameter | Description |
| :- | :- |
| Select stock | LOGI |
