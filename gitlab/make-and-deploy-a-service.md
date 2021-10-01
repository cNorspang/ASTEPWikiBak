---
title: How to make and deploy a new service
description: This guide explains what files/code you need in order to deploy a new service to aSTEP.
published: true
date: 2020-12-15T06:45:08.373Z
tags: 
editor: undefined
---

# How to make and deploy a new service
> NOTE: This page reflects the state of the system at the end of the Spring 2020 semester.
{.is-info}

After setting up a GitLab group for your semester and a project repository for your service, time has finally come to write some code and deploy it to aSTEP. This guide assumes that the group/repository is set up correctly and that you have [cloned your repository to your computer](/gitlab#connecting-a-git-client-to-gitlab) (if you don't know what git-clients and cloning is: google it).

## The example service

For a simple barebones service that can be deployed please visit "https://daisy-git.cs.aau.dk/astep-2020/helloservice". It is a "flask app" written in Python, that only exposes the root endpoint responding with "Hello aSTEP 2020!". 

Please note, however, that this service is not actually visible in the service-menu on the aSTEP UI, since it does not implement a version of the [Microservice Interface Standard](/user-interface/api-standard), and not all services should be visible. This includes the meta/utility services like the [Service Fetcher](/services/service-fetcher), the [Authentication](/services/authentication-service) service, or the [User Interface](/services/user-interface) itself.

## Making your own service

One nice thing about the current aSTEP system is that there are virtually no restrictions on the programming language and framework you use for your service, as long as it has the ability to support HTTP(S) communication. There are some restrictions on your service's setup though:

- The service *must* listen on 5000 for HTTP web-traffic (aSTEP handles HTTPS encryption for you), since Ingress ([see here](/kubernetes#auto-generate-urls)) redirects all web-traffic to the service's port 5000.

- You must serve "some kind of" (text is fine) output on your service's `/` (root) endpoint, since Kubernetes uses this to perform a "*Health Check*" upon deployment. 

- If the service should be visible in the UI's service-menu, it must implement a version of the [Microservice Interface Standard](/user-interface/api-standard). It would also be a good idea for you to read the main page of the [User Interface documentation](/user-interface).

You can use `/` as a redirect to your service within the User Interface (https://astep.cs.aau.dk/tool/[url-to-your-service]), such that clicking "Preview App" in your repositories "*Operations > Environments*" menu will send you directly to your service in the User Interface. Initially you could just implement `/` only and just return some simple text to ensure that your service is able to deploy and is running.

Now, to make GitLab actually [build and deploy](/gitlab#continuous-integration-how-gitlab-deploys-services) your service, you'll need to create two files located in your project reoisitory's root directory: the `Dockerfile` and the `.gitlab-ci.yml` file (yes, DOT at the beginning).

### Making the `Dockerfile`

The `Dockerfile` directs how your service should be build and depends on the programming language and specific implementation. While you can consult Google about how to make a `Dockerfile` for your service, many modern IDEs have build in functionality (or extensions) to support autogeneration of the `Dockerfile` (examples are: Visual Studio, VS Code, and Intellij). Do note that you may be required to manually change the `Dockerfile`, if some port do not open correctly or if some files are not added to the Docker Image.

As an example, you can take a look at the [2020 helloservice's](https://daisy-git.cs.aau.dk/astep-2020/helloservice/-/blob/master/Dockerfile) `Dockerfile` (or any other service's `Dockerfile` for that matter). 

After creating the `Dockerfile`, you will be able to [build and run your service in Docker](https://docs.docker.com/get-started/part2/) (if you [have Docker installed](https://docs.docker.com/get-docker/), of course). The [User Interface documentation](/user-interface#support-for-multiple-versions-of-a-service) explains how you can test your locally running service through the aSTEP UI (if your service is graphical, of course). However, to deploy it to aSTEP, you'll also need the `.gitlab-ci.yml` file.

### Making the `.gitlab-ci.yml` file

The `.gitlab-ci.yml` file directs how GitLab should handle the building, testing, and deployment of your service (more specifically, the GitLab Runner executes the script within the file, but that is less important).

For the `.gitlab-ci.yml` file, we recommend you simply copy it from another existing project (e.g. [2020 helloservice](https://daisy-git.cs.aau.dk/astep-2020/helloservice/-/blob/master/.gitlab-ci.yml)). The [RFC 0009](/rfc/0009#code-changes) from 2019 stats that another method was to make a minor modification to the Auto-DevOps template, but GitLab has changed the templates, making this process more cumbersome.

### Deploying the service

Now all that is left to do is to push your service's source code together with the `Dockerfile` and the `.gitlab-ci.yml` file to your project repository on Gitlab. GitLab's CI/CD will automatically trigger, and start the building, testing, and deployment of your service. You can follow this process in the latest "*pipeline*" in the project repository's "*CI /CD > Pipelines*" menu. (you have to define your tests yourself in the `.gitlab-ci.yml` file; google it).

You can check if your service is running by going to your repository's "*Operations > Environments*" menu and pressing "Preview App". This will open a new tab in your browser at the `/` endpoint of your service.

If your want your service to be visible on the aSTEP website: depending on whether you push to the `master`-branch or to a non-`master`-branch, your service will or will not be visible in the aSTEP UI's service-menu. Remember, the [User Interface documentstion](/user-interface#support-for-multiple-versions-of-a-service) explains the difference and how to access your service through the aSTEP UI.

## Troubleshooting

If your service gets stuck in the deployment phase in the pipeline at/around the line "*Waiting for deployment 'my-deployment' rollout to finish: 0 of 1 updated replicas are available...*" for more than 5 minutes, there are some likely errors:

- You forgot to expose the `/` endpoint.
- Your service is not listening on port 5000 for HTTP web-traffic.
- Your [CORS](/user-interface/api-standard#cors) is configured incorrectly.
- Your service crashed. Ask a server administrator to [get the output-logs](/kubernetes#print-output-log-for-pod) from your service.

If your service is running and accessible through its direct link, but not showing up in the service-menu in the aSTEP UI (and you want it to), refter to the [troubleshooting section](/user-interface#troubleshooting-a-service-not-appering-in-the-service-menu) from the User Interface documentation.

## Next steps?

Apart from getting some programming done and generally continue to learn about the aSTEP system, you should also remember to document your service in the [list of service documentation](/services) and follow the [service documentation standard](/services/documentation-standard).

Since it's likely you came here from the [Getting Started](/getting-started) page, you can continue from where you left off over there.
