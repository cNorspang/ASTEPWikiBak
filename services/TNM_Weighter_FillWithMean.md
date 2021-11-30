---
title: Enhancer Fill With Mean
description: 
published: true
date: 2021-11-30T07:54:54.122Z
tags: tnm
editor: markdown
---

# Enhancer Fill With Mean
This service takes a TNM and fills all datapoints with the appropriate mean as calculated from meta_data.

### Acceptance criteria:
**given** TNM containing null values
**when** calling this microservice with the TNM
**then** returns an edited TNM with filled in new values to every null value
