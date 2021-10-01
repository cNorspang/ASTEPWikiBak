---
title: Service Documentation Standard
description: This standard outlines what the documentation (wiki-page) for any aSTEP service should contain.
published: true
date: 2020-08-27T08:57:21.628Z
tags: 
editor: undefined
---

# Service documentation standard

A service's documentation is seperated into two parts: "documentation meant for users" and "documentation meant for developers". We will call these "user documentation" and "developer documentation" for short. The user documentation is displayed directly on the aSTEP website when the corresponding service is opened, whereas the developer documentation belongs on the [aSTEP wiki](https://wiki.astep-dev.cs.aau.dk/). In fact, the wiki should be the goto-place for future developers. 

This document describes the creation, structure, content, and maintenance of the documentation for aSTEP services.

## Creation

The user documentation is a markdown file called `readme.md`, which is stored within the corresponding service. The user documentation is displayed on aSTEP through the service's `/readme` endpoint, which is described [here](https://wiki.astep-dev.cs.aau.dk/user-interface/api-standard/standard-2020#readme). In short, the `/readme` endpoint simply outputs the content of `readme.md`. Whenever a service is updated, a changed (if necessary) `readme.md` file is shipped with the new version of the service.

The developer documentation is a wiki-page located at `https://wiki.astep-dev.cs.aau.dk/services/[service-name]`. To create a new developer documentation page, do the following:

- Go to the [aSTEP wiki](https://wiki.astep-dev.cs.aau.dk).
- Press the "*New Page*" button in the top left corner of the website.
- Enter "`services/[service-name]`" in the input field at the bottom of the pop-up (e.g. "`services/route-planner`"). Should there be a name overlap with another service, just append the year of creation or the creator-group's name at the end.
- Press the "*SELECT*" (or similar) button and choose "*Markdown*" as the editor. (In fact, all pages are to be markdown.)
- Fill in the new documentation page as described in the "**Structure and content**" section below.
- Press "*SAVE*".

When the new page has been created and saved, it should be added to the list of available documentation. To add the new page to the list, do the following:

- Go to the [list of services](https://wiki.astep-dev.cs.aau.dk/services).
- Press the "*Page Actions*" button in the top left corner of the website, followed by "*Edit*" in the drop-down menu.
- Find or add the corresponding service's category as a level 2 header (`## Level 2 header`).
- Add the service to the list within that category by adding the following line sorted alphabetically by the service's name:
  - `- [[Service Name]]([service-name]) ([creation-year])`. 
  - *E.g.: `[Route Planner](route-planner) (2020)`).*
  - Note: the link `[service-name]` is a *relative link*, and is transformed into `https://wiki-link/services/[service-name]`. 
- Press "*SAVE*".

## Structure and content

The user documentation should contain (but is not limited to) the following:

```markdown
# [Service Name]
Introduction to the service. Why was it made (what is the "context" of the service) and what does it do?
Link to developer decumentation.

## How to use the service
This should be a user/consumer oriented guide. 
What does the (user-mode) input fields signify? What kind of data should be inputted and when? What kinds of output is supported and what are these outputs? Show some example inputs.
```

*NOTE: [See here](https://wiki.astep-dev.cs.aau.dk/user-interface/api-standard/standard-2020#fields) for information about `user-mode` and `developer-mode` fields.*

The developer documentation should contain (but is not limited to) the following:

```markdown
# [Service Name]
Introduction to the service. Who made it in the first place and when was it made? Why was it made (what is the "context" of the service) and what does it do? This should be more in-depth than in the user documentation.

## Current status
An overview of the service's capabilities, problems/bugs, future works, status of codebase, etc. How is this service linked to other services? 

What do the user-mode and developer-mode fields signify and how do they relate to the inner workings of the system? 
What kind of data should be inputted and when? 
What kinds of output is supported and what are these outputs? Show some example inputs to the developer fields if necessary.

## Inner workings
This should be a developer oriented guide. Link to the service's GitLab repository.
What programming language, frameworks, and libraries are used?

Mention all the things important to gain an understanding of the system. 
What algorithms are used? What are the core principles? What are the important classes/structures? How does the system architecture look? How does the service communicate with other parties?

## History
The following (level 3) sections should describe the history of and changes made to the service thoughout various semesters. That is, document how different project groups have contributed to the service during different semesters.

NOTE: It does not matter whether the newest or oldest semester is mentioned first. The semesters must be ordered though.

### [semester a]
What project group has created or made changes to the service and which project report documents these changes in full?

What are the (significant) contributions in this semester? Descibe them in a way that gives new developers an overview over the contributions and their workings. Describe system design and if necessary the structure and code of the implementation.

Mention important facts, considerations, circumstances, or topics.

Mention future works, problems, or the sort. Conclude on the semester and contributions.

### [Semester b]
Same structure and content as [semester a].
```

An example of the "**History**" section is as follows:

```markdown
## History

### Semester Spring 2020
Group SW000F20 has made the "Hello world" service. The SW000F20 project report describes the semester in full (context, research, choises, etc.)

Here are some *images* describing the important parts system and a concise description of the design and implementation.

Here are some important facts, considerations, etc.

We can conclude that we have forgotten the comma in the output. Future semesters should fix this.

### Semester Fall 2021
Group SW999E21 has extended and modified the "Hello world" service. The SW999E21 project report describes the semester in full (context, research, choises, etc.)

There is now a comma in the output. The service can output "Hello, world" in any language now. *This component* is now depricated.

Here are some *images* describing the additions to the system and a concise description of the new designs and implementations.

Here are some important facts, considerations, etc.

We can conclude that this is now a perfect piece of software with no flaws. We were never able to produce any errors during use.
```

## Maintenance

Since the users only need the latest version of the user documentation, whenever changes are made to the service, your simply overwrite the old `readme.md` file.

When a new semester has modified the service, they must update the "*Current status*" and the "*Inner workings of service and how to use it*" sections to reflect the latest version of the service. Furthermore, they should add a new semester section called "*Semester [fall/spring+year]*" to the bottom of the "*History*" section. It is strictly forbidden to modify another group's semester section. If anything needs to change, try and contact them instead.