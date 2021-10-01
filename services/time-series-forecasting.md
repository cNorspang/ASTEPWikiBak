---
title: Time Series Forecasting
description: Time Series Forecasting using TCN, currently the service is comprised of a interface compliant with the aSTEP requirements for 2020v1, a trainer and predictor.
published: true
date: 2020-07-03T13:44:49.107Z
tags: 
editor: undefined
---

# Time Series Forecasting with TCN
Made in the spring semester of 2020 by group SW603F20, the Time Series Forecasting service seeks to fulfill the purpose of doing binary classification on temporal data. The service utilizes a Temporal Convolutional Network for this purpose and is written in Python using Keras and TensorFlow as backend.


> ## Paper 
> The AAU paper for this project can be found [here](https://projekter.aau.dk/projekter/da/studentthesis/classification-of-bacterial-population-growth-with-temporal-convolutional-networks(11393bf0-4be3-4cc8-be69-3bdf8443174e).html). Just remember that you need to be logged in to see it.
{.is-info}

## Problems
> Since we use the [aSTEPFormUtils](https://wiki.astep-dev.cs.aau.dk/en/services/python36-astep-form-utils) libary our service is not compatible with the new [Notebook](https://wiki.astep-dev.cs.aau.dk/Notebook) design. {.is-danger}

> The ground truth field when using an old model is not used, only the "New" ground truth field is read. This means when using a saved model the ground truth field inside of "New" contains the values that are actually being read and as such this field must be filled out if one wishes to utilize the ground truth in conjunction with a saved model. {.is-warning}

> The Force CPU check box dose not work. By not writing out the code necessary for this (This is only a problem if you have all the CUDA things installed, since it would use CPU as standard if not installed). {.is-info}

## Video example
This is a quick video presentaion of the service.

[![Demo](http://img.youtube.com/vi/bBIE5bbyfEA/0.jpg)](http://www.youtube.com/watch?v=bBIE5bbyfEA "Demo")

## Repo information
Time Series Forecasting with TCN, is comprised of an interface compliant with the aSTEP requirements for 2020v1, a trainer and a predictor.

We are using the keras-tcn library found here:
https://github.com/philipperemy/keras-tcn

Also in the repo is class implementations of a few charts described by aSTEP. 
These include:

* Text
* Markdown
* Js Chart
* Generic Time Series
* Geo Cluster
* Composite

Source at: https://daisy-git.cs.aau.dk/astep-2020/time-series-forecasting

## User Guide
### How to use Time-Series Prediction Tool

To use the Time-series prediction tool, the user first have to train a model. To train a model the user has to:

#### Training
![Trainer](https://i.imgur.com/bDSwl3e.png)
- 1: Login to aStep
- 2: Select Time Series Analytics
- 3: Select Time Series Forecasting
- 4: Choose "Train" on the drop down.
- 5: Give some input.
	- 5a: Give the name of the file with the data you want to train with. E.g. "test" or the full name "test.csv".
	- 5b: Or use the input field and the format described in [RFC0016](https://wiki.astep-dev.cs.aau.dk/rfc/0016)
- 6: Input which columns
	- 6a: Input which columns in the csv file the model should use for training.
    The columns can be inserted in the form `1-4`, which means that columns 1, 2, 3 and 4 will be used, or they can just be written like `1, 2, 3, 4`. A comma is needed to separate the columns. E.g `3-5, 7, 9-10` is the columns 3, 4, 5, 7, 9 and 10. The numbering of columns starts at zero. 
    
- 7: Input which columns in the csv file the model should use as labels (aka Ground Truth).
    Columns can be inserted the same way as for training. 
- 8: OPTIONAL: Use advanced mode to select your own hyper parameters.
- 9: Press "Visualise Results".
- 10: Follow the instructions on the page.

- 11: Download the code.
   
- 12: Extract the folder "trainer" from the downloaded zip.

![Trainer2](https://i.imgur.com/1FwF57W.png)
- 13: Put the csv file into the downloaded folder called "trainer".
- 14: Running and installing
	- 14a: If using Linux, run `InstallAndRun.sh`.
	- 14b: If using Windows, run `InstallAndRun.cmd`.

In the folder "trainer" a new folder called "models" is now made, the trained model should be in this when training is done.

##### Advanced mode
Advanced mode allows for more customization of the trainers parameters these include:
* `Lookback Window` - The amount of data we look back.
 
     Default value: `12`
* `nb filters` - The number of filters to use in the convolutional layers.
 
     Default value: `11`
* `Kernel size` - The size of the kernel to use in each convolutional layer.
 
     Default value: `1`
* `nb stacks` - The number of stacks of residual blocks to use.
 
     Default value: `3`
* `Dilations` - A dilation list.
 
     Default value: `[1, 1, 2, 2, 4, 4, 8, 8, 16, 16]`
* `Dropout rate` -  Fraction of the input units to drop. (Between `0` and `1`)
 
     Default value: `0.12`
* `Learning rate` - The learning rate for the model
 
     Default value: `0.01`
* `Validation spilt` - How much of the data we should use for validation (1 is 100%)  
 
     Default value: `0.125`
* `Patience` - What the early stopping patience is (i.e. how many epochs it has to not improve to stop)
 
     Default value: `500`
* `Activation type` - The activation type of the model.
 
     Default value: `sigmoid`
* `Batch size` - The batch size of the model.

     Default value: `1`
#### Prediction
To use the model for prediction: 

![prediction](https://i.imgur.com/rFrTCZS.png)

- 1: Login to aStep
- 2: Select Time Series Analytics
- 3: Select Time Series Forecasting
- 4: Choose "Predict" from the dropdown.
- 5:  Choose "New" to upload the newly trained model.
    Choose "old" to use a model that has already been uploaded and saved. 
- 6: Browse for the new model in the new "models" folder created in the "trainer" folder.
- 7: Input
	- 7a: Browse for the csv file that contains the data you want to predict on. 
	- 7b: Or use the input field and the format described in [RFC0016](https://wiki.astep-dev.cs.aau.dk/rfc/0016)
- 8: OPTIONAL: Input which columns from the csv data file to use for ground truth in the graph. If nothing is input, uses prediction instead for the graph.
- 9: Press "Visualise Results".

#### Uninstall
When you are done with the prediction tool, use the `Clean.cmd` for windows users, and `Clean.sh` for Linux. Clean will uninstall all the files installed with InstallAndRun, the folders will remain. 
And uninstall python and Visual-C if necessary.

#### Input and Output

The service use the input and output defined in [RFC0016](https://wiki.astep-dev.cs.aau.dk/rfc/0016) and input by the fields described above.
Which is supported by the other time-series services from 2020.