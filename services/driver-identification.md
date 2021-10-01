---
title: Driver Identification
description: The Driver Identification service attempts to identify drivers based on their driving patterns.
published: true
date: 2020-08-26T10:43:26.601Z
tags: 
editor: undefined
---

# Driver Identification

> NOTE: This page reflects the state of the service at the end of the Spring 2020 semester.
> NOTE: This page was not created by the original creators of the service.
{.is-info}

Originally created by group SW605F18 (aka. TR3) suring the Spting 2018 semester, the *Driver Identification* service attempted to identify the drivers of vehicles based on their driving patterns. These "driving patterns" are extrapolated from the trajectories found in the [driver_identification_db](/databases/DB2/driver_identification_db) database. 

They used "Unsupervised machine learning" to train a categorizer using the labelled trajectories, which should be able to prodict what driver had driven the unlabelled trajectories. However, they did not know what drivers had driven the unlabelled trajectories. Look at their project report if you are interested in more information.

This service is accessible through the [Legacy Services](/services/legacy-services) service. The source code for the service's back-end is found on GitLab at "https://daisy-git.cs.aau.dk/aSTEP-2018/DriverIdentificationREST-API". It also has a library, the source code of which is found here: "https://daisy-git.cs.aau.dk/aSTEP-2018/DriverIdentification".