---
title: Wind Speed Predictor
description: This micro service predicts the wind speed on an hourly basis for a set number of time steps ahead in time.
published: true
date: 2021-12-02T09:43:42.367Z
tags: service, microservice, time-series, timeseries, time series, 2021, f21
editor: markdown
---

# Wind Speed Predictor
The goal of implementing a windspeed predictor was to assist other groups using wind speed as a parameter in their models. This semester two other groups wants to use the data for prediction of [electricity pricing](url) and [fuel pricing](url) however, other groups in the Intellegent Transportation cluster also saw use in this, as one group predicts the best bicycle route dependent on the wind.
The service predicts the wind speed on an hourly basis based on data from either a user provided CSV file or data from the aSTEP database.


Introduction to the service. Who made it in the first place and when was it made? Why was it made (what is the "context" of the service) and what does it do? This should be more in-depth than in the user documentation.

## Current status
The service is fully running, but the models are not accurate to a satisfiable degree. Therefore, furture semesters could focus on increasing the accuracy of the current model.
Another improvement would be to add more models to the service, such that the user can decide and compare what models fits their use the best.
For now the ARMA model only takes 2 parameters into account; wind speed and humidity. This should be expanded upon such that all varying factors are taken into account.
An overview of the service's capabilities, problems/bugs, future works, status of codebase, etc. How is this service linked to other services?


What do the user-mode and developer-mode fields signify and how do they relate to the inner workings of the system?
What kind of data should be inputted and when?
What kinds of output is supported and what are these outputs? Show some example inputs to the developer fields if necessary.

## Inner workings

The code of this project is found at [GitLab](https://daisy-git.cs.aau.dk/astep-2021/group-5). It includes 4 repositories, but only 2 that is active. The active repositories is the [WheatherDataPredictor](https://daisy-git.cs.aau.dk/astep-2021/group-5/weatherdatapredictor), which contains the service, and the [FormattingWheatherData](https://daisy-git.cs.aau.dk/astep-2021/group-5/formattingweatherdata), which is responsible for fetching data from the [DMI API](https://dmiapi.govcloud.dk/#!/) and ingesting it to the aSTEP database. As of now the database contains data from november 2020 - october 2021, but new data is easily inserted by adding files from the API to the "WeatherData" folder found at [GitLab repository](https://daisy-git.cs.aau.dk/astep-2021/group-5/formattingweatherdata/-/tree/master/WeatherDataFormatter) and changing the property of the file to `Copy Always` in the editor. Hereafter you run the solution file and data is ingested to the database.
NOTE: that the `DatabaseContext.cs` file should use a `appsettings.Production.json` file containing access information instead of `appsettings.Development.json`. Ask serverdudes for an ingestion key.

The weather data is taken from the [DMI API](https://dmiapi.govcloud.dk/#!/) and ingested to the aSTEP database. The service uses `Pandas` to model data and `Statsmodels` for predictive models.

**Languages:**
Python (service)
C# (database ingestion)

This should be a developer oriented guide. Link to the service's GitLab repository.
What programming language, frameworks, and libraries are used?

Mention all the things important to gain an understanding of the system.
What algorithms are used? What are the core principles? What are the important classes/structures? How does the system architecture look? How does the service communicate with other parties?

## History
The following (level 3) sections should describe the history of and changes made to the service thoughout various semesters. That is, document how different project groups have contributed to the service during different semesters.

NOTE: It does not matter whether the newest or oldest semester is mentioned first. The semesters must be ordered though.

### Group 5 (fall 2021)
The initial creation of the service. The service is fully running, but the models are not accurate to a satisfiable degree. Therefore, furture semesters could focus on increasing the accuracy of the current model.
Another improvement would be to add more models to the service, such that the user can decide and compare what models fits their use the best.
For now the ARMA model only takes 2 parameters into account; wind speed and humidity. This should be expanded upon such that all varying factors are taken into account.
**The initial authors of the service is:**
Alexander Nesheim
Christopher C. Jensen
Jacob T. Rasmussen
Lasse D. Skaalum
Laurits C. B. Mumberg
Philip C. Greve