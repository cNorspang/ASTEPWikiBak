---
title: Naive time weighter
description: A simple service weighting an edge based on length and mean speed
published: true
date: 2021-12-06T09:31:03.399Z
tags: 
editor: markdown
---

# Naive time weighter
This simple service was created to make more options available when using the TNM service.
This service simply looks at all edges and divides the length of the edge by the mean speed when driving here. This gives a very naive time estimate for how long it takes to drive this piece of road. The calculated weight is normalised to a number between 0 and 1, where lower is better.

#### How do i use this service?
Send a **POST** request to **/timeWeight** containing the JSON TNM model defined in RFC0020. The service will then return the same model but weighted. 