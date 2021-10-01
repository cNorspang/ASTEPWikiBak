---
title: Request for Comments (RFC)
description: Overview and Guideline
published: true
date: 2021-10-01T15:16:21.137Z
tags: rfc, request, for, comments, change
editor: markdown
---

# Request for Comments
Request for Comments (RFCs) are documents detailing a proposed structure, method or plan for a given aspect of a collectively developed system.

The RFC's present the standard which every student working on aSTEP should follow, to continue developing a uniform aSTEP, or should alernatively reject or revise deprecated standards, and replace with new ones. All the RFC's are split into groupings of the Roles described in [RFC0019](https://wiki.astep-dev.cs.aau.dk/rfc/0019), and all students working on aSTEP should at least be familiar with the RFC's at [Relevant for Everyone](#list-of-rfcs).

***The RFC list of aSTEP serves mainly as a history of the decisions made during the different years of development of aSTEP, to support the decision making of future developers. If they are followed they will lead to a uniform aSTEP website.***

## List of RFCs
<details open>
<summary>Relevant for Everyone</summary>

| RFC Number| Title| Summary | Year |Status
|-------|:-:|:-----|---------|:-----|------
| [RFC0019](/rfc/0019)  | Cooperation | RFC0019 outlines how the current aSTEP groups have chosen to cooperate together | 2021| **Pending**
| [RFC0015](/rfc/0015)  | Interface of Microservices | RFC0015 outlines the addition of 2 endpoints to microservices, `/data` and `/combined`  | 2020 Spring | **Accepted**
| [RFC0014](/rfc/0014)  | Documentation Style				     				 								| RFC0014 outlines the creation of this wiki for documentation | 2020 Spring | **Accepted**
| [RFC0008](/rfc/0008)  | Service Documentation | RFC 0008 outlines how services should return their README documentation | 2019 | **Accepted**
| [RFC0003](/rfc/0003)  | Development Proces | RFC 0003 outlines the use of Gitlab (daisy-git) and the process of creating and accepting merge requests and branches that must exist in repositories | 2019 | **Accepted**
| [RFC0001](/rfc/0001)| The RFC Process | RFC 0001 outlines the use of RFCs for documentation purposes. | 2019 | **Accepted**
</details>

<details open>
<summary>Time Series</summary>

| RFC Number| Title| Summary | Year |Status
|-------|:-:|:-----|---------|:-----|------
| [RFC0016](/rfc/0016)  | Common input/output standard for time-series services | RFC0016 outlines a common data inteface for use with time-series services | 2020 Spring | **Accepted**
| [RFC0013](/rfc/0013)  | Notebook Interface				     				 								| RFC0013 outlines a [Jupyter](https://jupyter.org/)-like interface for aSTEP| 2020 Spring | **Accepted**
</details>


<details open>
<summary>Transportation</summary>

| RFC Number| Title| Summary | Year |Status
|-------|:-:|:-----|---------|:-----|------
| [RFC0020](/rfc/0020)  | Transportation Network Model | RFC0020 outlines a common data model, which transportation microservices can use as their basis | 2021 | **Pending**

</details>

<details open>
<summary>Scrum Masters</summary>

| RFC Number| Title| Summary | Year |Status
|-------|:-:|:-----|---------|:-----|------
|No standards| yet for | scrum masters | | |
</details>

<details open>
<summary>Maintainers</summary>

| RFC Number| Title| Summary | Year |Status
|-------|:-:|:-----|---------|:-----|------
| [RFC0018](/rfc/0018)  | Update HELM | RFC0018 outlines the update of HELM and Kubernetes including admin credentials to Kubernetes |2020 Fall| **Accepted**
| [RFC0012](/rfc/0012) | Server Architecture	| RFC 0012 outlines the servers that exist in the project, and what purpose they serve | 2019| **Accepted**
| [RFC0011](/rfc/0011)  | Authentication Service| RFC 0011 outlines how the authentication service works, and how users can set up tokens and have their services fetch them | 2019 | **Accepted**
| [RFC0010](/rfc/0010)  | Service Fetcher	| RFC 0010 outlines how the service fetcher works, and how services can be made fetch-able by the fetcher | 2019 | **Accepted**
| [RFC0009](/rfc/0009)  | Kubernetes | RFC 0009 outlines how the Kubernetes cluster works and how services can make use of Gitlab's CI/CD with Kubernetes | 2019 | **Accepted**
| [RFC0002](/rfc/0002)  | Database | RFC 0002 outlines the use of a single database entry point (GraphQL) and how to access this entry point from services | 2019 | **Accepted**
</details>

<details open>
<summary>UI</summary>

| RFC Number| Title| Summary | Year |Status
|-------|:-:|:-----|---------|:-----|------
| [RFC0017](/rfc/0017)  | Generic Table | RFC0017 outlines the addtion of a simple generic table to the userinterface | 2020 Fall| **Accepted**
| [RFC0007](/rfc/0007)  | Single Page Application			| RFC 0007 outlines how aSTEP is loaded into a Single-Page Application (SPA), and how to implement this for individual services | 2019 | **Accepted**
| [RFC0006](/rfc/0006)  | Definition of Chart Types		| RFC 0006 outlines the chart types available, as well as examples for how to implement each type     | 2019 | **Accepted**
| [RFC0005](/rfc/0005)  | UI Style Guide | RFC 0005 outlines a standard UI style, along with specific stylings for different elements | 2019 | **Accepted**
| [RFC0004](/rfc/0004)  | Service Interface| RFC 0004 outlines the interfaces/endpoints services must implement to comply to this RFC. This also includes examples of input, output, and communication methods | 2019 | **Accepted**
</details>

## Experience with RFCs
RFCs are used by a number of large online IT communities, for instance the Internet Engineering Task Force. Language development, e.g. the Python language developers, uses RFC in the form of PEPs. RFC as a concept, is applicable in a wide range of domains.

At its core, aSTEP is a multiproject, which means that a significant amount of different study groups will work on it, and the project will be worked on by different people every year.
Because of this, concise and succinct documentation is necessary and a history of the choices made by previous groups, can help future groups make better decisions.
RFCs provide a robust way of documenting the history of decisions made for aSTEP.

All decisions regarding re-development and new functionality are documented in RFCs.
RFCs are based on trust between participants.

All RFC guidelines must be followed by all participating study groups for all benefits of it to be accomplished.
It is difficult to enforce rules in a multi project consisting entirely of students, since all students have the same level of responsibility and therefore it is not possible to force anyone to do anything.

Furthermore, the nature of RFCs dictates some kind of plan driven development.
This is however difficult to accommodate since all participants are students.
Students tends to use agile development frameworks since students in general are not skilled enough to predict the outcome of topics precisely enough to state them formally before they start working on the topic.

In general, RFCs presents a concise and precise way of proposing ideas and functionality, while documenting them at the same time.

## RFC Guidelines

### Creating a new RFC
To create a new RFC, create a new page on this wiki with the path `/rfc/xxxx` where xxxx is the number of the previous RFC + 1. Then edit this page and insert a link to the RFC in the table for the correct year above. The table should also include the title of the RFC, a brief summary as well as the status (which will be **Pending** when first created).

The added row should look like this: 
`| [RFCxxxx](/rfc/xxxx) | Title Here | Summary Here | **Status**`
Resulting in a table which looks like this:
```
| RFC Number 					| Title   				| Summary			 | Status
|:--------------------:|:---------------:|:-----------:|
| [RFCxxxx](/rfc/xxxx) | Title            | Summary      | **Status**
| [RFCxxxx](/rfc/xxxx) | Title 					 | Summary 		 | **Status**
| [RFCxxxx](/rfc/xxxx) | Title 					 | Summary 		 | **Status**
```

All RFCs must follow the [template](#template).

#### Template
All proposed RFCs should follow this template.
```
# 0000 - Name
// *state* is either: "Pending", "Accepted" or "Rejected"
**state** 

*Proposed: 01. Jan. 0000* | *state: 01. Jan. 0000* | *Last Modification: 01. Jan. 0000*

## Summary

Insert one liner here.

## Motivation

Describe why this RFC should be accepted in broad strokes.

## Details

Explain how your RFC is going to function in practice.

## Alternatives

Explain some alternatives which could be considered.

// This part should only be included if the RFC was rejected
## Reason for rejection

Explain why this RFC was rejected.
```
