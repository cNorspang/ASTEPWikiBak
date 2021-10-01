---
title: Time Series Anomaly Detection
description: Anomaly Detection on Time Series Data
published: true
date: 2020-11-19T08:34:24.334Z
tags: 
editor: undefined
---

# Time Series Anomaly Detection
Made in the spring semester of 2020, by group SW604F20, the purpose of the service is to detect anomalies on time series data, through the use of recurrent variational autoencoders.
Recurrent variational autoencoders are a form of neural network, that combines variational autoencoder with recurrent neural networks.
The neural network detects anomalies by learning the normal pattern of training data. It reconstructs inputs and determines which points in the input data, that it cannot reconstruct well. These points are marked as anomalies.

## Current status
The neural network is able to capture anomalies in synthetic univariate time series data with high accuracy. Less so in real univariate time series data, and even less in multivariate. The webservice is able to show the results of the anomaly detection.

The service uses the input and output defined in [RFC0016](https://wiki.astep-dev.cs.aau.dk/rfc/0016), and thus is supported by the other time-series services from 2020.

> The accuracy of the model is low, when predicting on datasets with large clusters of anomalies. This is probably because of a problem with KL-Divergence and thus large clusters are recognized as part of the normal partterns and are recreated faithfully.

> Because of the way the model is saved after training, to use the aSTEP User Interface for Prediction (through the "provide" method"), the model must be trained using exactly Python 3.6 on a Linux system. A solution to this could be to switch out `model.save` with `model.save_weights` (See [this](https://www.tensorflow.org/tutorials/keras/save_and_load#manually_save_weights)). {.is-warning}

## Implementation Details
The neural network is created in TensorFlow 2, using the included Keras library. This allows for ease of programming and readability, by allowing us to code the neural network in "layers".

The webservice is implemented in Python Flask.
## Usage
There are two ways to use this service.

### Example
To use an example, choose Example from the drop-down menu, and choose an example. The examples are neural networks trained on a specific dataset, and run on the same dataset.
When using examples, F1-score, precision and recall will be provided, such that the accuracy of models trained on different datasets can be observed.

### Provide
It is also possible to provide a model and dataset to visualize the use of that model on that dataset.
To do this, choose Provide from the drop-down menu, and in the Modelfile field, upload a model. This model should be trained using the [provided training script](#training).
In the TSD field, upload a CSV file, or provide input in the time series data format. A percentile must also be chosen. 
Percentile refers to the number of anomalies expected to be present in the dataset. For example, if 1% anomalies is expected, 0.01 percentile should be chosen.

#### Training
To train a model, use the provided training script found [here](https://daisy-git.cs.aau.dk/astep-2020/time-series-anomaly-detection).
To install, follow these steps:
##### Requirements
- Python 3.6
- Ubuntu or other Linux OS
##### Installation
- Clone the repository
- Navigate to `time-series-anomaly-detection/`
- Create a python virtual environment using `python -m venv venv`
- Activate virtual environment using `source venv/bin/activate`
- Install requirements using `pip install -r requirements.txt`
- Run script `training.py`

##### Usage
To run the script use `python training.py ARGS`

###### The following arguments are available:
**Positional arguments, these must always be set, and must appear in this order:**
- `input` The input training set.
- `output` The path to save the model at.
- `columns` A comma separated string of columns to use from the input. For example if columns 1 and 2 wish to be used, `1,2` or `1-2` must be input as `columns`
- `epochs` The number of epochs to train.

**Optional arguments. These may be set if needed, most have recommended defaults:**
- `-b, --batch-size` Batch size to use when training. Default is `256`
- `-w, --window-size` Window size for sliding windows algorithm during preprocessing. Default is `64`
- `-g, --gru` Number of GRU units in the model. Default is `32`
- `-d, --dense` Number of Dense units in the model. Default is `32`
- `-lr, --learning-rate` Learning rate when training. Default is `1e-3`
- `-loss {mse, binary_crossentropy}` Which type of loss function to use. Possible options `mse` and `binary_crossentropy`. Default is `binary_crossentropy`
- `--checkpoints` Checkpoints. First argument is path, the path where the checkpoint will be saved. Second argument is frequency, how many epochs between checkpoints. Default is `output_latest_checkpoint.hdf5` and `10`
- `--early-stopping` Early stopping. First argument is epsilon, how muych the loss must change for it to be registered. Second argument is patience, how long to wait for a change in loss before early stopping. Default is `1e-7` and `100`
- `--lr-decay` Learning rate decay. First argument is rate, a factor which will be applied to the learning rate. Second argument is the frequency, the number of epochs between this factor is applied. Default is `0.8` and `10`
- `--factor` A factor that will be applied to KL-Divergence when training. Should be higher for smaller datasets, and lower for higher datasets. Default is `0.001`
- `--plot-loss` Path to plot loss after training. Default is `output_loss.png`
- `--visualise-frequency` How often to visualise reconstruction during training. Default is `-1`/off
- `--resume` Path to checkpoint to resume from. This argument should only be used if resuming from a checkpoint.
- `-v, --verbosity` Increase output verbosity. Example `-vv` for verbosity of 2. Default is `1`

***For arguments `--checkpoints`, `--early-stopping` and `--lr-decay`, these may be disabled by providing arguments `-1, -1`.***

## Output of the service
After running this training program on the dataset you will have a model which is able to detect and mark anomalies in the dataset. This model and a dataset can be uploaded to the service to observe how well it works on the data.
> This output part was not written by the orginial authors of the service.
{.is-info}


## History
### Semester Spring 2020
Group SW604F20 created this service by designing and implementing the neural network, and exposing it to aSTEP's User Interface via a Python Flask webservice.

The neural network is a recurrent variational autoencoder, a variation of auto encoders with some recurrent parts. 
Good accuracy was achieved on datasets with small clusters of anomalies.
On datasets with large clusters of anomalies, accuracy was less than expected.








