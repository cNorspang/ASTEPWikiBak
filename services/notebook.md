---
title: Notebook
description: The notebook service is the backend that supports the functionality of the Notebook Interface first introduced to the aSTEP UI in 2020.
published: true
date: 2020-09-04T21:45:31.388Z
tags: 
editor: undefined
---

# Notebook

> NOTE: This page reflects the state of the service at the end of the Spring 2020 semester.
> NOTE: This page was not created by the original creators of the service and thus does not follow the Service Documentation Standard.
{.is-info}

Originally made in Spring 2020, the Notebook service stores the list of notebooks for all aSTEP users (see the [Notebook interface](/user-interface#notebook-mode)). The source code of this service is found on GitLab here: "https://daisy-git.cs.aau.dk/astep-2020/notebook".

It is a really simple python app that simply stores all the services open in each notebook for each user. Of cource, some users may not have any notebooks. 

> Currently, the notebooks are stored only in memory, so they are lost if the service is restarted.
{.is-warning}
