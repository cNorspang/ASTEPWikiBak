---
title: Outlier Detection Service
description: The Outlier Detection Service is an anomaly detector, implemented with the algorithm Half-Space-Trees
published: true
date: 2020-12-15T05:38:42.720Z
tags: 
editor: undefined
---

# Outlier Detection Service
The Outlier Detection Service is an anomaly detector. It works on windows of a specified size, always comparing data in the current window to data in the last. In each window, it will give a score for each row based on how the data matches against the last window. Using the z-score algorithm, the score is converted to a boolean indicating outlier or not. It is applicable in a streaming context and has therefore been made accessible through the Streaming Service Connector API. 
It is also available through the UI.

The Outlier Detection Service
- Streaming Service Connector API
- The UI.



### Streaming Service Connector
**Files:**
The outlier detection service ONLY works with CSV files.

**CSV variant:**
The first row is used to set the names of the columns. Names can be any string. For all other rows, strings are not accepted and if there is one string in a column, the entire row is ignored.
CSV Example:
```
data1,data2,int3,float4
55,0,81,0,6.5
56,0,96,0,5.2
50,1,89,7,5.0
```

##### Endpoints:

**/open**
Creates a network with the specified 'key' argument and saves it in a map list till it's /close is called

**/close**
Deletes network with specified 'key' argument from list of networks.

**/sendrow**
The outlier detection service must have recieved X(not yet determined) amount of rows before it can begin determining outliers.
For those rows, it will return below json string with 'ready' set to false:

                    'ready': False,
                    'message': "",
                    'rowcount': X,
                    'learnfromfuture': False,
                    'rowStr': X,X,X
X is determined by the window size, which is set by default but can also be set through the /open request with the parameter 'windowssize'. Once X amount of rows has been retrieved, the outlier detection will start returning values for each row:

			'ready': True,
                    'message': "",
                    'rowcount': X,
                    'learnfromfuture': False,
                    'anomalyscore': X,
                    'outlier': True or False,
                    'rowStr': X,X,X
The json in both cases will also include the variables 'analyzedrowscount' and 'ignoredrows' which will be appended to the json when rows are finished being analyzed.

**Parameters:**
These parameters can be set in a request to the /open endpoint. They are used to initialize the HSTree
- 'verbose': Bool - Setting for verbosity of output
- 'windowssize': int - window size for trees algorithm. 
- 'numberoftrees': int - number of trees in the algorithm
- 'sizelimit': int - size limit of trees in algorithm
- 'maxdepth': int - max depth of trees  in algorithm

If none are set, they are set to default values.

**/sendfile**
Divides the file into rows and treats them like /sendRow. Json is the result of /sendRow on all rows in file

**Example**
Here is a python file that shows how to make requests to the API. Swap the sent file with your own and run the python file.
- [proof_of_concept.py](/proof_of_concept.py)

## The UI
The service is controlled by using the fields to select datasets and actions.

**Upload file**
The first field in the side bar is used to upload a csv file. The csv file is only uploaded when the insert action is selected and visualise result to pressed. The dataset will then be uploaded into a database server (DB2 currently).

If no errors occurred then the message `Dataset: {dataset} inserted!` is displayed.

**Action**
The available options are:
- insert
	- inserts a csv file into database
- delete
	- deletes a dataset from database
- show
	- prints the first 10 rows from the selected dataset
- analyze
	- runs outlier detection on the selected dataset

**Dataset**
This dropdown shows all datasets uploaded to the service. Use this option in combination with the action dropdown or upload file.
