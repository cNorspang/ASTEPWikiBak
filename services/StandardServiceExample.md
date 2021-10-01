---
title: Example of Standard
description: This is a page showing an example of how we describe a service
published: true
date: 2020-11-25T08:36:34.996Z
tags: 
editor: undefined
---

# Example of the Exoskeleton timeseries Service
The following document is an idea to how the standard of a service's explanation on the wiki could be like.
# Hand gesture classifying from Biox AAL-Band 2.0
The Gesture classifying service is a service, which use information of a hand gesture from the 8 sensors in the BioX AAL-band 2.0 to classify the hand gesture that was made.

(This part is a description of the service, describe key algorithms and models used)

## Input
This service takes in a stream of data or a CSV file containing datapoints retrieved from the Biox AAL-band 2.0. The data should look like the following in a CSV file:

|Sensor1,| Sensor2, | Sensor3, | Sensor4, | Sensor5, | Sensor6, | Sensor7, | Sensor8|
|---|---|---|---|---|---|---|---|
|Value1, |	Value2, |  Value3, | Value4, | Value5, | Value6, | Value7, | Value8  |

or if it is a stream of data, just in the format of value 1-8 comma separated.

## Output
The output of the Hand Gesture classifying service is a new CSV format that includes the gesture which was recognized by the model.
This is on the following format

|Sensor1,| Sensor2, | Sensor3, | Sensor4, | Sensor5, | Sensor6, | Sensor7, | Sensor8, | Classification |
|---|---|---|---|---|---|---|---|---|
|Value1, |	Value2, |  Value3, | Value4, | Value5, | Value6, | Value7, | Value8, | GestureName|


## Example of use / Tutorial

The following is an example of how to use the service:

First you create your CSV file with datapoints.

CSV inputfile:
|Sensor1,| Sensor2, | Sensor3, | Sensor4, | Sensor5, | Sensor6, | Sensor7, | Sensor8|
|---|---|---|---|---|---|---|---|
|80, |	83, |  82, | 79, | 83, | 80, | 80, | 79  |
|79, |	83, |  82, | 79, | 76, | 82, | 81, | 80  |
|81,|	82,|  83, | 82, | 80, | 79, | 77, | 82  |

Then we save this file on our computer.

Then we press the choose file option on the left hand side of the service. Navigate to the file and accept it.
Then press classify, which then sends the file to the service which uses the trained model to classify each row in the inputfile.

On the screen you should then see the following: \<Picture of output inserted here\> 
Then you press the download button to download the new CSV file, which should contain the following:

CSV output file:
|Sensor1,| Sensor2, | Sensor3, | Sensor4, | Sensor5, | Sensor6, | Sensor7, | Sensor8| Classification|
|---|---|---|---|---|---|---|---|---|
|80, |	83, |  82, | 79, | 83, | 80, | 80, | 79, | Fist |
|79, |	83, |  82, | 79, | 76, | 82, | 81, | 80, | Fist|
|81,|	82,|  83, | 82, | 80, | 79, | 77, | 82, | Fist|