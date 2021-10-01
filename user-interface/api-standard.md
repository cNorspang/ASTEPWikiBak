---
title: Microservice Interface Standard
description: The interface standards define protocols used by the aSTEP user interface to integrate services into itself.
published: true
date: 2020-08-20T13:34:32.221Z
tags: 
editor: undefined
---

# Microservice Interface Standard

> NOTE: This page reflects the state of the system at the end of the Spring 2020 semester.
{.is-info}

As is also explained in the [introduction to the aSTEP user interface](https://wiki.astep-dev.cs.aau.dk/en/user-interface#how-the-ui-interacts-with-microservices), for a service to be displayable and usable in the aSTEP user interface, the service has to implement a version of the *Microservice Interface Standard*. All services that seek to implement a standard must:

 1. Listen on port 5000 for HTTP web-traffic (aSTEP handles encryption for you).
 2. Enable [CORS](https://enable-cors.org/) so that the user interface can redirect traffic to the service.
 3. Implement all HTTP endpoints required by the version of the standard.

## CORS
Since the UI is a single page application all services will be called from the browser, and thus CORS *must* be implemented on each service. If it is not, most (probably all) browsers will disallow the webpage from making requests to a given microservice. 

Since the UI is not from the same origin as the microservices, most browsers will disallow requests from the browser to the microservices unless the headers on the microservice explicitly allows it. See [wikipedia](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing) for more information about why and how to implement this. [Enable CORS](https://enable-cors.org/server.html) has a list of libraries for many different languages that can help implement CORS.

Below is a list of what you need to allow:

 - Origins: *any origin*.
 - Methods: `OPTIONS`, `POST`, `GET` (allowing "*any method*" is fine too).
 - Headers: `authorization`, `astep-fields-mode`.

## Input and Output Formats

All endpoints are expected to serve output in `application/json` format and to accept input in both `multipart/form-data` format and `application/x-www-form-urlencoded` format. You can read more about the difference between the two input formats [here](https://dev.to/sidthesloth92/understanding-html-form-encoding-url-encoded-and-multipart-forms-3lpa).

<!-- The 'span' tricks wiki.js to not show "ASP.NET" as a link -->
Input should be handled by whatever library/framework is used to interact with the web. Flask (Python), <span>ASP.</span>NET (C#, etc.), and similar libraries/frameworks have a single way of getting data from the forms that work with both input formats.

## Versions

Currently there are 4 versions of the interface available:

 * [2019, 19w08, y19w20*These are much alike. Made to support the in-UI-rendered charts and fields.*](standard-2019)
 * [2020v1 (spring semester)*Extended the *y19w20* standard to support the Notebook Interface.*](standard-2020)
{.links-list}

All standards made during the same semester are to be documented in the same page. Future versions of the standard are to be named `[year]v[version]` (for example `2020v1`). Since the semester project was moved to the 5th semester (fall semester) in 2020, the names for 2020 spring and 2020 fall standards may seem wierd.

> NOTE: New services are expected to implement the newest version of the standard, whereas older standard-versions are for backwards compatability only.
{.is-info}


## Returning an error

All services should return a 2XX code (see [HTTP status codes](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)) in case of a success, a 4XX code in case the user did something wrong with the input, or a 5XX code in case something went wrong in the service. This is expected for the three 'content' endpoints `/data`, `/render` and `/combined`.

In the case of a 4XX or 5XX status, it can be necessary to show the user a proper error of some kind. The aSTEP User Interface has a built-in utility for doing this in an easy manner. You can return an error either in string format (`text/plaintext`) or in JSON format (`application/json`) containing the fields: `header`, `message`, `code`, and `explanation` (`text/plaintext` and `application/json` are [Content-Types](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Type)).

The error in JSON object is structured as follows:
```json
{
	"header": "A name for the error (for example 'IllegalValue')",
	"message": "A description of what the error means",
	"code": "Accompanying code",
	"explanation": "An explanation of what might be wrong"
}
```
Optional: `header`, `message`, `code`, `explanation`

The `code` field will (when shown in the interface) be rendered as `inline code`. The `header` field will be shown in large text, while the rest of the fields will be shown in normal text size and font.