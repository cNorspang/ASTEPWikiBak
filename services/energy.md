---
title: Energy
description: The Energy service from 2018 attempts to forecast the electricity prices of Denmark for the next 24 hours.
published: true
date: 2020-08-26T12:46:23.725Z
tags: 
editor: undefined
---

# Energy

> NOTE: This page reflects the state of the service at the end of the Spring 2020 semester.
> NOTE: This page was not created by the original creators of the service.
{.is-info}

Made by group SW603F18 (aka. TS1) in 2018, the Energy service tries to predict the energy prices of Denmark for the next 24 hours. It uses deep learning (likely supervised) to analyse the historical electricity prices provided by [Nord Pool](https://www.nordpoolgroup.com/) and thus make the predictions.

The electricity prices analysed and the forecasts produced by the service are all stored in the [ts1](/databases/DB1/ts1) database. 

This service is accessible through the [Legacy Services](/services/legacy-services) service. You can find the source code for the service's backend on GitLab here: "https://daisy-git.cs.aau.dk/aSTEP-2018/Energy-Mangement". We are unsure of what libraries the service uses.
