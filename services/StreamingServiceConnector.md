---
title: Streaming Service Connector
description: Streaming Service Connector is an API on the aSTEP platform that allows access to services which work with streams
published: true
date: 2020-12-14T12:15:59.727Z
tags: 
editor: undefined
---

# Streaming Service Connector
Streaming Service Connector Documentation
The Streaming Service Connector (SSC) has the responsibility to redirect the request to the desired service. If a service can work with streams it can be set up to use the SSC to allow one API for all streaming services. 

To configure the SSC to redirect to a service, just extend the if-controlstructure as shown below in the Streaming Service Connector service.


def GetURLFromService(service):
    URL = ""
    # add to this for new services
    if service == "-o":
        URL = "https://astep-2020-fall-outlieronstreams.astep-dev.cs.aau.dk"
    return URL

To add parameter for a specific service, add them to the AppendParamsBasedOnService function below. 

def AppendParamsBasedOnService(PARAMS, service, request):
    if service == "-o":
        PARAMS = AppendIfExist(PARAMS, "verbose", request.args.get("verbose", None))
        PARAMS = AppendIfExist(PARAMS, "windowssize", request.args.get("windowssize", None))
        PARAMS = AppendIfExist(PARAMS, "numberoftrees", request.args.get("numberoftrees", None))
        PARAMS = AppendIfExist(PARAMS, "sizelimit", request.args.get("sizelimit", None))
        PARAMS = AppendIfExist(PARAMS, "maxdepth", request.args.get("maxdepth", None))
   return PARAMS

As for other needs, we expect future groups to refactor and extend the code accordingly.

-	SW504E20
