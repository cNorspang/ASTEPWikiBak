---
title: User Interface
description: The "User Interface" is the service for the entire aSTEP website.
published: true
date: 2020-12-07T11:32:41.503Z
tags: 
editor: undefined
---

# User Interface
> NOTE: Since the aSTEP wiki was made in spring 2020, anything regarding previous semesters is mearly our interpretation of the documentation/knowledge we have. The Spring 2020 and back documentation is not written by someone affiliated with the UI development.
{.is-info}

> NOTE: Since the UI group of Spring 2020 wanted to call "aSTEP services" for "aSTEP tools" instead (due to the Notebook and since "tool" is a more dicerning name than "service") there may be some confusion around this. The terms will be used interchangeably. The term "service" is used on this wiki to avoid confusion with the documentaion from previous semesters.
{.is-info}

We don't exactly know when the first version of the User Interface was made. The User Interface is the implementation of the actual aSTEP website, and was made in order to collect all services on the same platform. This page is oriented towards those who wish to continue development of the UI. See the [User Interface user documention](/user-interface) for a guide for how to use the UI together with your own service.

## Current status

The User Interface service in it's current state was made during the Spring 2019 semester and further expanded upon during the Spring 2020 semester. Small adjustments were made in the summer 2020. 

The UI service is implemented in TypeScript using the Angular framework as well as the Redux framework for maintaining the internal state in the UI (Google it). The source code of the UI is found on GitLab here: "https://daisy-git.cs.aau.dk/astep-2020-fall/UserInterfaceF20". There are probably better editors, but you can use "VS Code" with the Angular and TypeScript extensions installed to open and edit the UI project's source code. The UI makes use of the [Notebook](/services/notebook) service, the [Service Fetcher](/services/service-fetcher) service, the [Authentication](/services/authentication-service) service, and the [Socket Service](/services/socket-service).

### Main pages and service displays

There are currently 5 main pages of aSTEP:

- *About*: The main page and introduction to the aSTEP project.
- *Contact*: Shows the contact persons for each semester as well as the latest system administrators.
- *Education*: Shows a list of old projects.
- *Research*: Probably the list of use-cases for aSTEP or the research in which aSTEP has been used.
- *Wiki*: Shows this wiki embedded in the aSTEP website.

Apart from the 5 main pages, there are 2 different modes of accessing services from the [service list](#list-of-services):

- *Notebook*: Enters the [Notebook Interface](/user-interface#notebook-mode) which is facilitated by the [Notebook](/services/notebook) service.
- *Single service*: Entered by pressing a service in the left-hand-side service menu.

Lastly, there is the *Login* page, which uses the [Authentication](/services/authentication-service) service to manage aSTEP users.

### List of services

The left-hand side of the aSTEP UI displays a list of all active aSTEP services separated into the following categories:

- Path Analytics
- Trajectory Analytics
- Time Series Analytics
- Speech Analytics
- Other

You press a category's label to expand or collapse its contents. The [Service Fetcher](/services/service-fetcher) service is used to populate this list. The UI lists all production (see [this](/gitlab#one-version-per-branch) and [this](/user-interface#support-for-multiple-versions-of-a-service)) services that implement a [Microservice Interface Standard](/user-interface/api-standard).

### Fields and Charts

This wiki already documents the [fields](/user-interface/fields) and some of the [charts](/user-interface/charts) of aSTEP. In short, fields are the UIs way of taking input to an aSTEP service and the charts are its way of displaying output from an aSTEP service.

The current [field](/user-interface/fields) types are:

- file
- checkbox-group (non-functional)
- checkbox
- select
- input
- multi-select
- formset-select
- button (non-functional)
- input-number
- textarea

The current implemented [chart](/user-interface/charts) types are:

- Text
- Markdown
- Geographical Clustering
- Geographical Geometry
- Composite
- Chart.js
- Socket Chart
- Composite Scroll
- Generic Timeseries Chart
- Time Series Data *(not documented on wiki)*
- Robotics Classification *(not documented on wiki)*
- Exoskeleton *(not documented on wiki)*
- Driver Identification *(not documented on wiki)*
- Pdf *(not documented on wiki)*

The last 5 charts are as of the summer 2020 not documented on the wiki due to a lack of documentation and since (apparently) no one is using them.

## How to run the UI locally

There are two ways of running the UI locally: using Node.js or using Docker. If you use Docker, you'll have to re-build the Docker Image everytime you make a change, whereas with Node.js, it will automatically recompile/update the running UI service as you make (and save) changes to the local UI source code. Also, yes, Docker and Node use different ports.

*NOTE: We recommend you use Node.js due to these exact pros/cons and also due to the fact that you need a little "hack" to get the UI working in Docker. However, if you can build and run the Docker image, the UI is also likely going to deploy correctly on aSTEP (since the `Dockerfile` itself performs some tests, "lint", on the source code which Node.js does not).*

Before anything, you should clone the UI project repository from the GitLab group called "aSTEP-2020 (spring)" to your computer (see [this guide](/gitlab#connecting-a-git-client-to-gitlab) from the GitLab documentation to get started).

### Using Node.js

For this method, you need to install [Node.js v10.15.1](https://nodejs.org/download/release/v10.15.1/). This version is the same as the one used in the Docker installation (see the `Dockerfile`). Simply download the installer for your system and follow the installation instructions. When you have Node.js working and you've verified that it works (try `node -v` to print the version info), follow the instructions below:

- Open a terminal and navigate to the `app` directory (located in the UI project's root-directory)
- Run `npm install` to install the dependencies required by the UI
- Run `npm start` to run the UI on [localhost:4201](http://localhost:4201)

*NOTE: After the message "*Angular Live Development Server is listening on localhost:4201*", if `npm` starts saying "compilation failed" (or the like), it may not mean that the compilation has failed (fml right?). Just try the website anyways or save any document within the app folder. Node.js will start compiling again and likely succeed.*

### Using Docker

First things first, you need to [download and install Docker](https://docs.docker.com/get-docker/) and have it running (note the different installation procedures on Windows 10 Home and Pro). When you have Docker running, follow the instructions below:

- Open a terminal and navigate to the root folder of the UI project (the folder with the file: `Dockerfile`).
- Build the docker image: `docker build -t uiapp --build-arg LARAVEL_CLIENT_ID=[id] --build-arg LARAVEL_CLIENT_SECRET=[secret] .`

`-t uiapp` builds the image with the tag (name) 'uiapp'. `--build-arg [key]=[value]` registers an environment variable `[key]` with the value `[value]`. For safety reasons, the values of `[id]` and `[secret]` can only be recovered by someone with access to [this file](https://daisy-git.cs.aau.dk/astep-2020/UserInterface/-/blob/master/app/src/environments/environment.ts) from the 2020 UI GitLab repository. The dot at the end signifies the 'current directory'.

- Execute the image: `docker run -it --rm -p 5000:5000 --name my_app uiapp:latest`

`-it` says "give me a terminal in this container". `--rm` says "remove container `my_app` if it already exists". `-p 5000:5000` says "redirect traffic on host port 5000 to container port 5000". `--name my_app` says "label the container as `my_app` in the Docker UI". `uiapp:latest` says "run the most recent image with tag `uiapp`".

The first time you build the image it may take quite some time to finish the build. Afterwards, it should be much faster. If the docker build starts giving out "lint errors", you probably wrote something in a "style deemed wrong". The console output shows you a list of files and your mistakes in them. Fix these and try again.

> All docker images you build are saved on your computer, so you may want to remove them after some time.
{.is-info}

## Inner workings

The following explains where the key elements of the aSTEP UI are defined in the UI codebase and how some things work together, but not how the whole thing is set up. We don't have enough understanding of the UI codebase to tell you that; sorry.

Since it does not really fit anywhere else: 
- The list of [Microservice Interface Standards](/user-interface/api-standard) supported by the aSTEP UI is defined in the [tool](https://daisy-git.cs.aau.dk/astep-2020/UserInterface/-/blob/master/app/src/app/models/tool.ts) model.
- In the source code, the `this.store.dispatch` calls make use of *reducers* and the `this.store.pipe` calls make use of *selectors*. Reducers and selectors are found in the [models](https://daisy-git.cs.aau.dk/astep-2020/UserInterface/-/tree/master/app%2Fsrc%2Fapp%2Fmodels) directory. The reducers comes from the *Redux* library mentioned earlier.

The [logged-in](https://daisy-git.cs.aau.dk/astep-2020/UserInterface/-/blob/master/app/src/app/logged-in) component defines the structure/content of the main page of aSTEP: top-bar with page-links, the list of services, etc.

### Page implementations

#### Main pages

In the UI source code, the 4 main pages *About*, *Contact*, *Education*, and *Research*, are defined in the components [home](https://daisy-git.cs.aau.dk/astep-2020/UserInterface/-/tree/master/app/src/app/home), [contact](https://daisy-git.cs.aau.dk/astep-2020/UserInterface/-/tree/master/app/src/app/contact), [education](https://daisy-git.cs.aau.dk/astep-2020/UserInterface/-/tree/master/app/src/app/education), and [research](https://daisy-git.cs.aau.dk/astep-2020/UserInterface/-/tree/master/app/src/app/research), respectively. Whereas the contents of *About (home)* and *Research* are statically defined in pure HTML, the contents of *Contact* is defined in the [contact.json](https://daisy-git.cs.aau.dk/astep-2020/UserInterface/-/blob/master/app/src/app/contact/contact.json) file and those of *Education* in [bibliography.json](https://daisy-git.cs.aau.dk/astep-2020/UserInterface/-/blob/master/app/src/app/education/bibliography.json). It should be fairly simple to infer how to modify/extend these files, but you can always look in the the json files' corresponding html files in order to see how the data is loaded.

The *Wiki* page is defined in the [wiki](https://daisy-git.cs.aau.dk/astep-2020/UserInterface/-/blob/master/app/src/app/wiki) component. The wiki component embeds the content taken from the actual wiki service (found at "https://wiki.astep-dev.cs.aau.dk/") in an `iframe`. The wiki-content displayed on the aSTEP website has the general URL `https://astep.cs.aau.dk/wiki/[content-url]`, where the content shown is taken from `https://wiki.astep-dev.cs.aau.dk/[content-url]`.

In order to synchronize `astep.cs.aau.dk/wiki/[content-url]` with the actual content displayed in the `iframe`, we inject some javascript code into the wiki (see the [administration > themes](https://wiki.astep-dev.cs.aau.dk/a/theme) menu) which passes messages back to the aSTEP website with the current content URL.

#### Login page

The login page is defined in the [login](https://daisy-git.cs.aau.dk/astep-2020/UserInterface/-/tree/master/app/src/app/login) component. [The central config file](https://daisy-git.cs.aau.dk/astep-2020/UserInterface/-/blob/master/app/src/config.ts) defines the link to the [Authentication service](/services/authentication-service) used for login. I don't know much about 

#### Service displays

The components for both the *single service* and *notebook* displays are found in the [tool](https://daisy-git.cs.aau.dk/astep-2020/UserInterface/-/tree/master/app/src/app/tool) directory (they are called `single-tool` and `notebook-tool` in code). [The central config file](https://daisy-git.cs.aau.dk/astep-2020/UserInterface/-/blob/master/app/src/config.ts) defines the link to the [Notebook Service](/services/notebook), which is used by the notebook component from the aSTEP website. Otherwise, my knowledge falls short here.

### Service menu and categories

[The central config file](https://daisy-git.cs.aau.dk/astep-2020/UserInterface/-/blob/master/app/src/config.ts) defines both the name of the service fetcher to use as well as all supported categories (ID + name). The *service menu* (the side bar to the left) is defined in the [left-side-bar](https://daisy-git.cs.aau.dk/astep-2020/UserInterface/-/tree/master/app/src/app/left-side-bar) component.

It is not actually the side bar, but rather the [logged-in](https://daisy-git.cs.aau.dk/astep-2020/UserInterface/-/blob/master/app/src/app/logged-in) component that fetches all the services/categories for display. The `logged-in` component supplies the list of services (or rather, categories with services) to the side bar component through its [html file](https://daisy-git.cs.aau.dk/astep-2020/UserInterface/-/blob/master/app/src/app/logged-in/logged-in.component.html).

### Field and chart implementations

#### Fields

The current allowed field types (inputTypes in the source code) for aSTEP services are defined in [the central config file](https://daisy-git.cs.aau.dk/astep-2020/UserInterface/-/blob/master/app/src/config.ts). 

There are two different field implementations which are located in the [fields](https://daisy-git.cs.aau.dk/astep-2020/UserInterface/-/tree/master/app/src/app/fields) directory: 

- *Input field*: This implementation is used when an input is defined in the `/info` endpoint (see the [2020v1](/user-interface/api-standard/standard-2020) standard). This type takes as input either, text, a file, or input from another service (supported through the [Notebook interface](/user-interface#notebook-mode)).

- *Option field*: This implementation is used when the input is defined in the `/fields` endpoint (see the [2020v1](/user-interface/api-standard/standard-2020) standard). This type supports all the [field types](https://daisy-git.cs.aau.dk/astep-2020/UserInterface/-/tree/master/app/src/app/fields) documented on this wiki.

#### Charts

The [chart-view component](https://daisy-git.cs.aau.dk/astep-2020/UserInterface/-/blob/master/app/src/app/chart-view/chart-view.component.html) is the base component for displaying charts. Depending on the chart type outputted by a service, the `chart-view component` will find the correct chart implementation and display that with the content also outputted by the service (see the `/render` endpoint in the [2020v1](/user-interface/api-standard/standard-2020) standard). You can find all chart implemntations in the [charts](https://daisy-git.cs.aau.dk/astep-2020/UserInterface/-/tree/master/app%2Fsrc%2Fapp%2Fcharts) directory.

## History

### Summer 2020

During the summer of 2020 two students from SW601F20 were employed by AAU to continue working on aSTEP during the summer. While we mostly worked on other things, we made a few modifucations to the aSTEP UI. These were:

- Update the contact page to show the correct contact persons.
- Updated the main page (the About page) with new content.
- Fixed the default values for some field types.
- Fixed the checkbox field type, where the value was not handles properly.

### Spring 2020

The 2020 semester decided to actually keep the UI from the previous semester. The primary UI developers during Spring 2020 were SW606F20, who also developed the [Notebook](/services/notebook) service. They added the [Composite Scroll chart](/user-interface/charts#composite-scroll) and the [textarea field](/user-interface/fields#textarea). 

Group SW605F20 added a feature-name display (top-right corner) to the [Geographical Geometry](/user-interface/charts#geographical-geometry) chart. The time-series groups (SW602F20, SW603F20, SW604F20), added the [Generic Timeseries Chart](/user-interface/charts#generic-timeseries-chart). Look at the project reports for more documentation. 

### Spring 2019

The 2019 semester decided to, again, replace the UI from the previous semester. The 2019 UI is decoupled from the services in the sense that all graphical design and computational logic can be programmed solely though the service. For this, they set up (most of) the system descibed in the [User Interface documentation](/user-interface) (as per spring 2020). As is explained elsewhere on this wiki, this was done to centralize UI rendering (to make services look alike) and to enable integration with Kubernetes (in order to gain enhanced testing and deployment of services).

The UI was programmed in TypeScript using the "Angular" framework and "Redux" for state management. It the project is build using either Docker or Node.js (v10.15.1). 

The spring 2019 semester made the UI with the pages: *About*, *Contact*, *Education*, *Research*, and the generic chart/service menu which is accessed through a left-hand-side service-menu with a list of all active services. They also made the login page and functionality facilitaded by the [Authentication](/services/authentication-service) service. The service-menu splits services into 5 categories:

- Path Analytics
- Trajectory Analytics
- Time Series Analytics
- Speech Analytics
- Other

The UI uses the [Service Fetcher](/services/service-fetcher) service to populate the list of active services that implement one of the [2019 Microservice Interface Standards](/user-interface/api-standard/standard-2019). Additionally, the 2019 semester defined the following [charts](/user-interface/charts):

- Text
- Markdown
- Geographical Clustering
- Geographical Geometry
- Composite
- Chart.js
- Socket Chart (makes use of the [Socket Service](/services/socket-service))
- Robotics Classification
- Exoskeleton
- Driver Identification
- Pdf
- Time Series Data

Spring 2019 also defined the input [fields](/user-interface/fields) listed below:

- file
- checkbox-group (non-functional)
- checkbox (non-functional)
- select
- input
- multi-select
- formset-select
- button (non-functional)
- input-number

### Spring 2018

Due to the lack of containerization, the spring 2018 semester decided to replace the UI from the previous semester with a more containerized approach. All services were split into a front-end and a back-end. The back-end contained all the business logic, algorithms, and other computational what-not; usually referred to as `[project]REST-API` on GitLab. The front-end of all services was coded directly into the UI and simply facilitated input of data and output/formatting of results.

### Spring 2017

The spring 2017 semester looked at all the work from spring 2016, chanted *yeetus deletus* in unison, and started over. It's very likely they had a central UI that collected all services. The 2017 UI did not use any form of containerization for the individual services and (probably) had all functionality in the UI.

### Spring 2016

The spring 2016 semester definately had something graphical, but we don't know if this was a central UI as it is today.
