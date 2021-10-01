---
title: db_stonks
description: 
published: true
date: 2020-12-15T14:48:09.570Z
tags: 
editor: undefined
---

# Stonks-db
Made during the 2020 Fall semester by group SW503E20, the `DB2/db_stonks` database is connected to the [2020 Stock Prediction](/services/stock_prediction) service. The service will download, train, predict and show statistics of a stock based on the price history of the stock.

## Tables

This database has 4 tables:

- `model`
- `statistic`
- `stockdata`
- `stockdata_model`


### Model
The `model` table contains all the models that have been trained by our trainer, which later can be used by the prediction function. We are able to store files on the server via. the BYTEA type. Each model is asociated with at stock via. the modelid.

| Column name       | Type             	| Explanation                                 |
| ----------------- | ---------------- 	| --------------------------------------------|
| modelid     			| INTEGER      			| The id of the stock it belongs to						|
| filename    			| CHARACTER VARYING | The filename										            |
| filedata       		| BYTEA      				| The filedata       													|
| singlemodelid 		| BIGINT[PK]        | The primary key of the model             		|

### Statistic
The `statistic` table contains all the statistics of our predictions. It stores mae and mse values which can help to make better prediction, by tweaking parameters on a given model.

| Column name       | Type             	| Explanation                                 |
| ----------------- | ---------------- 	| --------------------------------------------|
| singlemodelid     | BIGINT      			| The id of the model it belongs to						|
| startdate    			| DATE 							| The startdate of the model			            |
| enddate       		| DATE      				| The enddate of the model										|
| mae 							| NUMERIC        		| The Mean Absolute Error of the model     		|
| mse 							| NUMERIC        		| The Mean Square Error of the model        	|

### Stockdata
The `stockdata` table contains all the stock data for our service. It is possible to access a specific stock by using stockdataid, as this is a reference to a primary key.

| Column name       | Type             	| Explanation                                 |
| ----------------- | ---------------- 	| --------------------------------------------|
| stockdataid     	| INTEGER      			| The id of the stock it belongs to						|
| open    					| NUMERIC 					| The open value of the stock									|
| close       			| NUMERIC      			| The close value of the stock       					|
| high 							| NUMERIC        		| The high value of the stock             		|
| low 							| NUMERIC        		| The low value of the stock             			|
| volume 						| BIGINT        		| The volume value of the stock             	|
| date 							| DATE        			| The date of the stock             					|

### Stockdata_model
The `stockdata_model` table contains all tickers and their primary keys.

| Column name       | Type             	| Explanation                                 |
| ----------------- | ---------------- 	| --------------------------------------------|
| stockid       		| BIGINT[PK]      	| The primary key of the stock  							|
| stockticker 			| CHARACTER VARYING | The ticker of the stock             				|