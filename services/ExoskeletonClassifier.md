---
title: Exoskeleton classifier
description: This page describes the use of the Exoskeleton Classifier service
published: true
date: 2020-12-17T10:15:39.784Z
tags: 
editor: undefined
---

# Exoskeleton Classifier
The Exoskeleton Classifier service uses information of a hand gesture from the 21 sensors in a BioX AAL-band 2.0 to classify the hand gesture that was made.
The gestures it can recognize are motorcycle hand gestures. These include:
Left turn, Right turn, Stop, Follow me, Single file, Double file, Refreshment stop, Hazard in roadway and Fuel.

For doing the classifications a few models were trained using machine learning. Among a total of 11 models, these include Random Forest and FCN.

The service has the option for using prerecorded datasets. These are saved in the  [ExoskeletonClassification2020Fall](https://wiki.astep-dev.cs.aau.dk/databases/DB2/ExoskeletonClassification2020Fall) database.

> Technical things about the models and preprocessing is described below, can be skipped if you just want to know how the service works.
{.is-info}

Tutorials on how to use the service can be found at the end of this document. <a href="#Tutorials">Go to tutorials</a>


### Models
An assortment of models were trained on a dataset collected using the data collection software which can be <a href="https://daisy-git.cs.aau.dk/astep-2020-fall/exoskeleton-classifier/-/blob/master/Data%20collection%20program.zip" target="_blank">downloaded here</a>.

Two of these models trained, are an FCN (Fully Convolutional Network) and a Random Forest.

The FCN consist of 3 layers, each containing 48 filters with the padding set to 'same' which means the output will have the same size as the input. For example given a 32x32 table as input the output would also be a 32x32 table.

The Random Forest model consists of a forest of 50 decision trees which are used to classify the gestures.

### Preprocessing
The service takes as input a CSV file, and data is preprocessed in several steps before classification. 
* First, the single data points (each being a time series consisting of ***n*** steps) are extracted from the dataset by using the *GroupBy()* function from Pandas, along with corresponding true labels, if included. Euler angles are also feature engineered at this point, using a sine transformation, to avoid confusing the model about large numerical distances that really represent spatially small distances. Irrelevant features, such as TIME after sorting each time series after this column, are also dropped at this point.
* Secondly, the time steps of each time series are aggregated as much as possible by averaging feature values, while making sure that the final number of time steps align with the chosen model. Using the average like this works under the assumption, that each feature value is static over time with a static gesture (i.e.: not involving any meaningful movement). But please note that the data defies this assumption to some degree.
* As a final step, each time series is normalized, using constants fitted to the original training set. These constants are saved in the same folder as the model trained with the data. 
 

<style>
        table, th, td {border: 4px solid  #000;}
        table {   border-collapse: collapse; }
  			html {   scroll-behavior: smooth; }
</style>


## Input
This service's input is a CSV file containing datapoints retrieved from the Biox AAL-band 2.0 (max 50mb). The columns should look like the following in the CSV file:
<div style="overflow-x:auto;">
<table border="4px solid #000" overflow-x:="auto" class="a">
  <tr>
    <th>FSR_1</th>
    <th>FSR_2</th>
    <th>FSR_3</th>
    <th>FSR_4</th>
    <th>FSR_5</th>
    <th>FSR_6</th>
    <th>FSR_7</th>
    <th>FSR_8</th>
    <th>Gravity_X</th>
    <th>Gravity_Y</th>
    <th>Gravity_Z</th>
    <th>ANGULAR_VELOCITY_X</th>
    <th>ANGULAR_VELOCITY_y</th>
    <th>ANGULAR_VELOCITY_Z</th>
    <th>LINEAR_ACCELERATION_X</th>
    <th>LINEAR_ACCELERATION_Y</th>
    <th>LINEAR_ACCELERATION_Z</th>
    <th>EULER_ANGLE_X</th>
    <th>EULER_ANGLE_Y</th>
    <th>EULER_ANGLE_Z</th>
    <th>TIME</th>
    <th>SUBJECTID</th>
    <th>REPID</th>
    <th>GESTURE</th>
  </tr>
  <tr>
    <th>Sensor1 Value</th>
    <th>Sensor2 Value</th>
    <th>Sensor3 Value</th>
    <th>Sensor4 Value</th>
    <th>Sensor5 Value</th>
    <th>Sensor6 Value</th>
    <th>Sensor7 Value</th>
    <th>Sensor8 Value</th>
    <th>GravX Value</th>
    <th>GravY Value</th>
    <th>GravZ Value</th>
    <th>AngX Value</th>
    <th>AngY Value</th>
    <th>AngZ Value</th>
    <th>LinearX Value</th>
    <th>LinearY Value</th>
    <th>LinearZ Value</th>
    <th>EulerX Value</th>
    <th>EulerY Value</th>
    <th>EulerZ Value</th>
    <th>Time Value</th>
    <th>Subject Value</th>
    <th>Repetition Value</th>
    <th>Gesture Name</th>
  </tr>
</table>
</div>

It is also possible to give a version without the GESTURE column, however this results in not getting a confusion matrix and metrics.

To record your own data, please use the Python script called "BioX_Collect_Data.py" which can be found <a href="https://daisy-git.cs.aau.dk/astep-2020-fall/exoskeleton-classifier/-/blob/master/Data%20collection%20program.zip" target="_blank">here</a> in the zip file "Data collection program" which also contains a guide alongside a library by BioX needed to use the armband.

Otherwise, if you don't have your own data it is possible to use the dropdown menu and choose a data sample from the Exoskeleton 2020 Fall database.

## Output
When "visualise result" (sic) is pressed, the service takes in the data from the uploaded file or from the chosen dataset. 
Firstly, at the top a label showing the options chosen is presented.
The data from the file is then classified and after processing it shows a confusion matrix like the following:  

![exoskeleton_classification_wiki_output_confusion_matrix.png](https://wiki.astep-dev.cs.aau.dk/exoskeleton_classifier/confusionmatrix.png)

To the right of the matrix, some statistics are shown, and they are the following 4 values:

![exoskeleton_classification_accuracy_image.png](https://wiki.astep-dev.cs.aau.dk/exoskeleton_classifier/exoskeleton_classifier_statistics.png)

- **Accuracy** is how precise the predictions are compared to the actual classification. The prediction is compared to the "GESTURE" field in the data. Correct predictions divided by total predictions.
- **Precision** is how many true positives divided by how many false positives is predicted. This can lead to division by zero if there are no false positives.
- **Recall** is how many classifications that are correctly predicted divided by how many there were in total. For example how many "Left turn" predicted correct divided by how many "Left turn" there were to predict. The final value is then the weighted average of the values for each gesture.
- **F1 score** is a measure that combined Precision and Recall. It uses the following formula: F1 = 2 * (Precision * Recall) / (Precision + Recall). 
After these metrics is a table showing the classifications as well as outliers in percentage shown.

![exoskeleton_classification_table_examplepng.png](https://wiki.astep-dev.cs.aau.dk/exoskeleton_classifier/exoskeletonclassifiertableexample.png)


Furthermore, it is possible to mouse over the labels and classifications to see an image of how the gesture looks alongside its name.

![LeftTurnGestureExample.png](https://wiki.astep-dev.cs.aau.dk/exoskeleton_classifier/gestureshowing.png)

## Example of use / Tutorial
<div class="main" id="Tutorials"></div>
The following is an example of how to use the Exoskeleton Classification service:

First you either record some data using the following program combined with a BIOX AAL 2.0 armband to create your csv file with datapoints or use previously recorded data from a dropdown menu.


<a href="#UploadingDataset">Upload dataset guide</a>
<a href="#UseExistingDataset">Use existing dataset guide</a>
<a href="#VideoTurtorials">Video guides</a>

### Uploading dataset
<div class="main" id="UploadingDataset">
</div>
This section describes how to use the service if you choose to upload your own dataset.

First, you start by pressing the "Browse" button or the textfield next to it to open a navigation window. In this window you navigate to your CSV file containing the data and confirm the choice.

![upload_file_exoskeleton_classification_example.png](https://wiki.astep-dev.cs.aau.dk/exoskeleton_classifier/exoskeleton_upload_file_example.png)

Next, you use the dropdown menu under the label "Choose a model" to choose which classication model you want to use.

If you wish to have outlier detection on the data you provide the service, mark the "Use outlier detection" which will add a new column in the output table describing the percentage of outliers for each repetition of data.

> Using outlier detection will increase load times dramatically.
{.is-warning}

If your file does not contain labels, you uncheck the checkbox labeled "File includes labels". Otherwise, let it be checked.

If you wish to use outlier detection on the data, press the checkmark box with the label "Use outlier detection".

Finally, press the "Visualise Results" (sic) button.


### Using existing datasets
<div class="main" id="UseExistingDataset"></div>
This section describes how to use the service using an existing dataset.

First step is to choose the dataset you want to classify. This is chosen from the dropdown menu with the label "Use existing dataset".

As a friendly reminder, remember to uncheck the checkbox "File includes labels" if you pick the premade dataset without labels.

If you wish to have outlier detection on the data, mark the "Use outlier detection" checkbox which will add a new column in the output describing the percentage of outliers for each repetition of data. The value "Failed" indicates that something went wrong during outlier detection (Usually happens due to network limitations).

Finally, click the "Visualise Results" (sic) button.


### Checking the output
At the top of the page you will be able to see which options were chosen for the classification followed by a confusion matrix if the input data contains labels, like the following:

![exoskeleton_classification_wiki_output_confusion_matrix.png](https://wiki.astep-dev.cs.aau.dk/exoskeleton_classifier/confusionmatrix.png)

This matrix shows how many time series have been predicted to be a specific label and the true label of that prediction.
To the right of this you will see the metrics of Accuracy, Precision, Recall and F1 score.
Finally, you can see a table showing each prediction compared to its true label and the percentage of outliers, if the outlier option is selected.

If there were labels and outlier detection:

![exoskeletonclassifieroutputwithlabel.png](https://wiki.astep-dev.cs.aau.dk/exoskeleton_classifier/exoskeleton_classifier_with_everything.png)

If there were labels and no outlier detection:

![exoskeletonclassifieroutputwithlabelnooutliers.png](https://wiki.astep-dev.cs.aau.dk/exoskeleton_classifier/exoskeleton_classifier_with_everything_but_outlier.png)

If there were no labels in the dataset the label column will be removed and look like so:

![exoskeletonclassifieroutputnolabel.png](https://wiki.astep-dev.cs.aau.dk/exoskeleton_classifier/exoskeleton_classifier_no_label.png)

And if there were no labels in the dataset and no outlier detection like so:

![exoskeletonclassifieroutputnolabel.png](https://wiki.astep-dev.cs.aau.dk/exoskeleton_classifier/exoskeleton_classifier_no_label_no_outlier.png)

Likewise, if no labels were in the file the metrics won't be showed either since they can't be calculated.

Finally, if you hover your cursor over a true or predicted label, a little image displaying the gesture alongside its name. This looks like so:

![LeftTurnGestureExample.png](https://wiki.astep-dev.cs.aau.dk/exoskeleton_classifier/gestureshowing.png)

# Video tutorials
Two videos showing the use of the service were recorded and can be seen here:
Uploading your own dataset:

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/dLaxTuR0xHM/0.jpg)](https://www.youtube.com/embed/dLaxTuR0xHM)

Using an existing dataset:

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/E4IH1gFZ0Q4/0.jpg)](https://youtu.be/E4IH1gFZ0Q4)

