---
title: Wind Speed Predictor
description: This micro service predicts the wind speed on an hourly basis for a set number of time steps ahead in time.
published: true
date: 2021-12-09T08:31:10.042Z
tags: service, microservice, time-series, timeseries, time series, 2021, f21
editor: markdown
---

# Wind Speed Predictor
The goal of implementing a wind speed predictor was to assist other groups using wind speed as a parameter in their models. This semester(fall 2021) two other groups want to use the data for prediction of [electricity pricing](url) and [fuel pricing](url) however, other groups in the Intellegent Transportation cluster also saw a use in this, as one group predicts the best bicycle route dependending on the wind.
The service predicts the wind speed on an hourly basis based on data from either a user provided CSV file or data from the aSTEP database. The data in the database origins from DMI.
The library model allows the user to add more data than only wind, such that multiple parameters are considered.

It was initially created by the group 5 of the fall 2021 semester.

## Current status
The service is fully running, but the models are not accurate to a satisfiable degree. Therefore, furture semesters could focus on increasing the accuracy of the current model.
Another improvement would be to add more models to the service, such that the user can decide and compare what models fit their use the best.
For now the ARMA model can take any amount of parameters into account using the `exog` parameter, however the accuracy of the model still leaves room for improvement. Future developers should play around with different parameters and find the best fit.
The output of the model should be improved such that it fits the other time-series and maybe intellegent transport groups better. Future developers might even wanna make it an option to model the data structure of the output to the users need

## Inner workings

The code of this project is found at [GitLab](https://daisy-git.cs.aau.dk/astep-2021/group-5). It includes 4 repositories, but only 2 that are active. The active repositories are the [WheatherDataPredictor](https://daisy-git.cs.aau.dk/astep-2021/group-5/weatherdatapredictor), which contains the service, and the [FormattingWheatherData](https://daisy-git.cs.aau.dk/astep-2021/group-5/formattingweatherdata), which is responsible for fetching data from the [DMI API](https://dmiapi.govcloud.dk/#!/) and ingesting it to the aSTEP database. As of now the database contains data from november 2020 - october 2021, but new data is easily inserted by adding files from the API to the "WeatherData" folder found at [GitLab repository](https://daisy-git.cs.aau.dk/astep-2021/group-5/formattingweatherdata/-/tree/master/WeatherDataFormatter) and changing the property of the file to `Copy Always` in the editor. Hereafter you run the solution file and data is ingested to the database.
NOTE: that the `DatabaseContext.cs` file should use a `appsettings.Production.json` file containing access information instead of `appsettings.Development.json`. Ask serverdudes for an ingestion key.

The weather data is taken from the [DMI API](https://dmiapi.govcloud.dk/#!/) and ingested to the aSTEP database. The service uses `Pandas` to model data and `Statsmodels` for predictive models.

**Languages:**
Python (service)
C# (database ingestion)
GraphQL (database queries)

## History
### Group 5 (fall 2021)
The service is fully running, but the models are not accurate to a satisfiable degree. Therefore, furture semesters could focus on increasing the accuracy of the current model.
Another improvement would be to add more models to the service, such that the user can decide and compare what models fits their use the best.
**The initial authors of the service is:**
Alexander Nesheim
Christopher C. Jensen
Jacob T. Rasmussen
Lasse D. Skaalum
Laurits C. B. Mumberg
Philip C. Greve