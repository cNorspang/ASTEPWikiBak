---
title: Service Fetcher
description: The service fetcher is used by the aSTEP UI to find and display services in the UI.
published: true
date: 2020-12-09T13:49:31.387Z
tags: 
editor: undefined
---

# Service Fetcher

> NOTE: This page reflects the state of the service at the end of the Spring 2020 semester.
> NOTE: This page was not created by the original creators of the service and thus does not follow the Service Documentation Standard.
{.is-info}

Originally created during the Spring 2019 semester, the Service Fetcher is responsible for listing all the services available for display and usage in the [User Interface](/services/user-interface). It also lists all the services that cannot be displayed in the UI and the reason. The service is also documented in [RFC 0010](/rfc/0010).

The Service Fetcher repository was forked from *aSTEP 2019* to *aSTEP 2020 (spring)* on GitLab (which became messy, so don't do it), and therefore you'll find the source code in the 2020 repository on here: "https://daisy-git.cs.aau.dk/astep-2020/servicefetcher".

The main page of the Service Fetcher service is found on "https://astep-2020-servicefetcher.astep-dev.cs.aau.dk/" and lists all the available endpoints of the service. Of these, we'll list those we ended up using the most (by my knowledge):

- `/infos/production`: This endpoint lists all the production services that can be displayed and used through the UI.
- `/errors/production`: This endpoint lists all the production services that cannot be displayed/used in the UI as well as the reason.

See: [Production services](/user-interface#support-for-multiple-versions-of-a-service).


## Usage
As mentioned when accessing the service fetcher on the [link](https://astep-2020-servicefetcher.astep-dev.cs.aau.dk/) shown, all of the service fetchers API endpoints are presented.

Lets say a service needed information about all other services currently running on aSTEP, this could be achived by accessing the `info/production` endpoint. You can view the results in the browser in HTML by following the "https://astep-2020-servicefetcher.astep-dev.cs.aau.dk/" and inserting the endpoint `info/production`. This results in the following image:

![output.png](/output.png) 

This could simply be used inside of any given service and manipulate the data.
