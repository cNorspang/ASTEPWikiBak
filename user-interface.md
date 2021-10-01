---
title: User Interface
description: This page describes the user interface for aSTEP.
published: true
date: 2020-12-09T12:44:54.242Z
tags: 
editor: undefined
---

Sub-pages:
- [Microservice Interface Standard](api-standard)
- [Field types](fields)
- [Chart types](charts)
- [Notebook Interface User Guide](notebook-use-guide)

# User Interface

The aSTEP website follows the "microservice architecture". This means that the website consists of numerous small programs or services (the microservices), which communicate in order to provide functionality to the website. The user interface itself on the [aSTEP website](https://astep.cs.aau.dk/) is a microservice; as are the services displayed in the service-menu located to the left in the UI. Microservices are all web-based and communicate using the HTTP protocol. These microservices are all hosted on the [Kubernetes Cluster](/kubernetes), and their source code is stored and managed by [GitLab](/gitlab). The UI service's wiki-page is found [here](/services/user-interface).

The image below shows how services are categorized in the service-menu and displayed in the aSTEP UI. You must be logged in to use the website. Ask a student from a previous semester or Bin Yang for the demo credentials.

![astep-ui-2020-spring.jpg](/userinterface/astep-ui-2020-spring.jpg)

## How the UI interacts with Microservices
The UI can automatically find and display a service in the service-menu, if that service implements a version of the [Microservice Interface Standard](api-standard). The standards define the HTTP endpoints necessary for the UI to: "know the service", "know it's input", and "get it's output". One of the base principles of this UI is to make the services' look alike (input-wise and output-wise).

The UI uses the [Service Fetcher](/services/service-fetcher) service to get information (name, category, etc.) about the available services. Services output their information through their `/info` endpoint.

Once you select a service, the service's `/fields` endpoint outputs a description of the various input the service requires from the user (the middle column in the image above). The UI itself is tasked with transforming the field-descriptions into graphical input elements. The various types of fields are explained in the [Fields documentation](fields). The UI has a toggle-button for switching between displaying *user fields* and *developer fields*. If available, the `/readme` endpoint outputs an introduction and user guide to the service (the right-most column on the image above).

Upon filling out the input fields and pressing "*Visualize Results*", the input is sent to the service's `/render` endpoint, which then outputs its result in a textual representaiton that is converted into a "chart". These charts are standardized graphical elements rendered by the UI itself. The various types of charts are documented in the [Charts documentation](charts). If the service implements the `2020v1` standard, the UI will show the button "*Print Raw Results*". If pressed, the UI sends the input to the services `/data` endpoint, which then outputs a pure textual representation of the result. Pressing the "*Documentation*" button shows the introduction and user guide from the `/readme` endpoint.

It is possible to make use of a package called [astep-forms-utils](/services/python36-astep-form-utils) which should make it easier to create fields without typos, by abstracting over the JSON code and instead creating the fields as classes.

## Support for multiple versions of a service

There are three types of "service versions": *Production*, *Development*, and *Local*.

As the [GitLab documentation](/gitlab#one-version-per-branch) explains, aSTEP can host multiple versions of the same service. There is up to one "production version" and zero or more "development versions". While only the production version is shown in the UI's service-menu, you can still access the development versions though the UI. All services have their own unique ([automatically generated](/kubernetes#auto-generate-urls)) link along the lines of:

- `[name-of-version-of-service].astep-dev.cs.aau.dk`

By entering a service-link into the URL template below here, the UI can find, display, and use the corresponding version of that service (if the service exposes the correct endpoints, of course).

- `https://astep.cs.aau.dk/tool/[service-link]` 

In the case of development versions, it is important that you first open the link `[name-of-version-of-service].astep-dev.cs.aau.dk` in your browser and *accept the https certificate*, else you cannot access the development version through the UI.

Lastly, the UI can also access a local version hosted on your own computer. The local service should be accessible using the link `localhost:5000` (port is specified by the [Microservice Interface standard](api-standard)), so if you run your service on your local machine, you can access the service through the UI with the link shown below:

- `https://astep.cs.aau.dk/tool/localhost:5000`

You can also [run the User Interface locally](/services/user-interface#how-to-run-the-ui-locally) if you need to test new UI functionallity and use the following link to access either online or local versions of a service:

- `http://localhost:4201/tool/[service-link/localhost]`

## Notebook mode

The UI has a "notebook mode" and a "single-tool mode" (which is the standard). In spring 2020, a new "Notebook Interface" was added to the UI. It is accessed by pressing the button "*Notebook*" located at the top right part of the aSTEP website. The Notebook Interface allows the user to chain multiple services together as explained in the [Notebook Interface User Guide](notebook-use-guide). The `2020v1` interface standard was made to support this functionality. Additional documentation on the Notebook Interface is found in [RFC 0013](/rfc/0013).

A service's `/combined` endpoint outputs both the data from `/data` and `/render` at the same time. This allows for showing both representations in the notebook, while not having to compute the output twice. The Notebook service's wiki-page is found [here](/services/notebook).

## Troubleshooting a service not appering in the service-menu

In case your service does not show up in the aSTEP user interface (and you want it to), ensure that the service correctly implements the [Microservice Interface Standard](/user-interface/api-standard) (ports, endpoints, CORS, etc.) and check what the [pipeline](/gitlab#location-structure-and-properties-of-repositories) on GitLab says about the deployment of your service. Also re-read the restrictions from the [how to deploy a service](/gitlab/make-and-deploy-a-service#making-your-own-service) guide.

If the above does not yield a solution, try and see if one of the cases below can give you any insights. All cases makes use of the [Service Fetcher](/services/service-fetcher) service, which can be accessed using the URL:

- `https://astep-2020-servicefetcher.astep-dev.cs.aau.dk/[endpoint]`

1. Make sure that the Service Fetcher has actually found the service using the `/services` endpoint. If your service is not listed here this means that your service is: not deployed correctly, not running in the Kubernetes cluster, or that the Service Fetcher may be malfunctioning.
   
2. If your service is listed in the `/services` endpoint you can check the `/errors` endpoint for a reason why your service is not listed in the `/infos` endpoint (which is where it would show up if everything worked).

3. If your service is not listed under the `/errors` endpoint, but *IS* listed under the `/infos` endpoint, then the UserInterface may be malfunctioning, or you could be at the wrong astep domain.


## How to fork the User Interface to a new repo
First of all, you need to be a maintainer or admin of your gitlab group.
The user interface should only be forked if you intend to make changes to it!
> Be aware that it can lead to a lot of issues when forking the user interface. This guide covers the main steps that you need to make sure is done. Additional troubleshooting should be expected. 
{.is-warning}


### Fork the UI:
1. On Gitlab, locate the currently running version of the user interface. (Should be in the previously semesters group) 
	- Fork this project to your own group.
2. In the current(old) user interface, go to 'settings' in the panel on the left, and then 'CI/CD' --> 'Variables' and take note of the two variables.
3. Go to your newly forked user interface and again go to 'variables' and insert the two variables from the current UI.  

> If the user interface gets forked, deleted and forked again, some naming issues can occur. These can be fixed by SSH into the gitlab server and manually deleting the repository and its branches.
{.is-warning}


### Get rid of the old UI:
> The commands below are listed on the [Kubernetes](/kubernetes) page
{.is-info}
1. The admin should archive the current(old) user interface.
2. Make sure that the new user interface has no build errors on gitlab.
3. SSH into the Kubernetes master node. 
4. Get all pods on kubernetes, and check that the new UI pod is running in kubernetes.
5. Then delete the old user interface pod


### Update the proxy settings:
1. SSH into the UI Proxy. 
2. Then edit the configuration in `/etc/nginx/nginx.conf`
3. Change these lines under 'Virtual Host Configs' and 'server' to point to the new user interface: 
   - `proxy_set_header HOST` 
   - `proxy_pass`

