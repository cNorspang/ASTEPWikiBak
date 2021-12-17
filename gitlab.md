---
title: GitLab
description: Gitlab stores and manages the source code of all services and deploys new versions of services to the Kubernetes Cluster.
published: true
date: 2021-12-17T10:59:13.854Z
tags: servers, service, server, gitlab, source_code
editor: markdown
---

Sub-pages:
 - [How to make a new GitLab group](make-a-group)
 - [How to make a new GitLab project repository](make-a-repository)
 - [How to make and deploy a new service](make-and-deploy-a-service)

# GitLab
> NOTE: This page reflects the state of the system at the end of the Fall 2021 semester.
{.is-info}

In aSTEP we use "GitLab" for version management of the source code of the various aSTEP services. The projects on GitLab can be found through "https://daisy-git.cs.aau.dk/explore/groups". When you first access the GitLab page, you should create an account in there. We recommend you use your student mail for the account. Users on GitLab are separated into administrators (can do anything) and regular users (can do some things).

Apart from storing source code, GitLab also takes part in building services and deploying them to aSTEP. This is done through integrating GitLab with GitLab Runners and [Kubernetes](/kubernetes). This page describes what important actions users and administrators can do though GitLab, and what important functionality GitLab provides.

This page does not properly document/describe how to get started with GitLab in a new semester. For that, look at the [Getting Started](/getting-started) page. More specifically, look at the sub-pages listed at the top of this page.

## Location, structure, and properties of repositories

GitLab structures project repositories into "Groups", the list of which is found [here](https://daisy-git.cs.aau.dk/explore/groups). For example, most semesters have a group called "*aSTEP-[year]*" (2020 may be become odd since there is both a spring and fall semester). 

A group contains the repositories for all services/projects made that semester. A repository's structure is the usual Git-style, with a single "master" branch and zero to many development brances. 

When on a group's main page, a *maintainer* or *owner* of the group may access the *Settings* menu, in which they (among other things) can configure common [environment variables](https://medium.com/chingu/an-introduction-to-environment-variables-and-how-to-use-them-f602f66d15fa) for all services in that group, as well as add GitLab Runners used to build/compile services.
All environment variables in the GitLab pipeline should have the prefix  `K8S_SECRET_`. The `K8S_SECRET_` part of the environment variable will be removed in the Docker container, thus it should not be a prefix in the actual code.

When inside a repository, a *maintainer* or *owner* may access the *Settings* menu, in which they (among other things) can configure environment variables, select the GitLab Runner to use, and enable the Container Registry (important for [deploying services](#continuous-integration-how-gitlab-deploys-services)). There are a few additional important menus in a repository:

- *Packages > Container Registry*: Shows the list of [images build by the Runner](#continuous-integration-how-gitlab-deploys-services) for each branch in the repository.
- *Operations > Environments*: Shows the list of currently running [versions](#one-version-per-branch) (one production and multiple development/review) on the Kubernetes cluster.
- *CI / CD > Pipelines*: Shows the list of all pipelines. A pipeline is a "description of an attempt to build and deploy a service". You can troubleshoot problems with your service by looking at the output from the latest pipeline for your branch.

Lastly, groups have a "*Members*" menu, whereas repositories have a "*Settings > Members*" menu. While administrators can do anything, regular users must have proper permissions through their "role" in a group/repository to be able to do certain things. The standard role is "*Developer*" which is allowed to push code to all non-master branches, though they can make pull-requests to the master. The role "*maintainer*" and can push to the master and accept pull-requests to the master.

> In spring 2020 we forked 2019 services into the 2020 group to continue development, but this became messy so we recommend you just continue in the old group if you need to work on an old service.
{.is-info}

## Connecting a git-client to GitLab

After registering an account on GitLab and signing in, you should connect your git-client of choice to GitLab, so you can start cloning repositories to your computer. Of course, the git-client should support "GitLab-selfhosted" integration (e.g. GitKraken).

To do this, you need to provide your git-client with the host you want to connect to ("https://daisy-git.cs.aau.dk" in our case) and a "*Personal Access Token*" (in GitKraken at least; hopefully the same everywhere). To create such a token, go to the page linked below:

- https://daisy-git.cs.aau.dk/profile/personal_access_tokens

Fill in a "*Name*" for the token and leave the expireation date blank. Your git-client should tell you what "Scopes" you need to activate (likely just "api" and "read_user"). Now press "*Create Personal Access Token*" and copy the new token to your git-client. Press "*Connect*" (or something alike) and now you should have access to GitLab.

To be able to clone a repository to your computer, you need to be a member of its enclosing group and *likely* also the repository itself (as an administrator, I don't really know about the restrictions of normal users).

## Continuous Integration: How GitLab deploys services
GitLab automatically facilitates the deployment of new versions of services to aSTEP. GitLab uses a GitLab Runner to build the service from the source code and tells the Kubernetes Cluster to execute the new version (likely in place of an old version). If configured, the Runner can also run tests inside the "project"/"source code" and only deploy if these tests pass.

The Runner produces a "*Docker Image*" containing the executable code for the service and Kubernetes executes the code inside this image. The smart thing about Docker is that the service can be developed in just about any programming language. In order to enable Continuous Integration, four criteria must be upheld (a "*Maintainer*" and upwards is sure to be able to achieve all these things):

- *Select a Runner*: In the repository's *Settings > CI / CD* menu, select the runner, which should build the service.
- *Enable Container Registry*: In the repository's general settings, enable the "*Container Registry*" option under the "*Visibility, project features, permissions*" section.
- *Create a Dockerfile*: The root directory of the repository must contain a "*Dockerfile*". This file defines exactly how the source code should be transformed into an executable Docker Image.
- *Create .gitlab-ci.yml*: The root directory of the repository must contain a *.gitlab-ci.yml* file. This file defines the build, test, deploy, etc. stages which the runner will execute.

### The Container Registry
When a runner has finished building a Docker Image of your service, this image is stored on GitLab in what is called the "*Container Registry*". This is also where the Kubenetes Cluster fetches images from.

### One version per branch
GitLab will automatically try to build and deploy a version of the service for each of the branches. If the branch already has a running service, this one is swapped out with the new version. When a user pushes changes to a branch, the contents of this branch is sent to the repository's selected GitLab Runner, and so the process descibed above begins. 

The version associated with the `master` branch is referred to as the "production version", whereas all other versions are "development versions". These version-types are [treated differently by the UI](/user-interface#support-for-multiple-versions-of-a-service). Kubernetes [automatically generates URLs](/kubernetes#auto-generate-urls) for each of the branches'. You can find these links in the *Operations > Environments* menu by pressing the "*Open live environment*" button to the left of the environment/version name. The "*Open live environment*" button only shows up if the version was successfully build and deployed to Kubernetes.

## Admin Area

Administrators can access the "*Admin Area*" by pressing the *"Admin-Area-wrench"* displayed in the top-bar of GitLab. The following sub-sections describe some of the pages we believe future semesters should know of.

- The "*Overview > Users*" page lists all registered users. Generally, this is where administrators unblock users and resets their passwords when they've failed to login too many times. This is also where users can be upgraded to administrators.

- The "*Monitoring > System Info*" page shows the current resource usage on the GitLab server. Use this to check when you should start deleting some unsued files. The server tries to clean up once a day, but we cannot guarentee this will keep working.

- The "*Kubernetes*" page is used to integrate GitLab with Kubernetes Clusters and manage (some of) the configuration/setup of the cluster(s). For example, from here you can see all the applications/add-ons installed on any Kubernetes Cluster. (Many are supported, but we have just one.)

- The "*Applications*" page is used to integrate GitLab and other applications. For example, we used this page to allow people to sign into this wiki using their GitLab login.

## GitLab maintenance

Finally, both administrators and regular users should help out keeping GitLab "clean". GitLab only has 100 GB of storage, so make sure to delete whatever can be deleted. This is not an exhaustive list of ways to save storage space on gitlab.

### Clean the Continer Registry

The Container Registry stores all images ever made for each branch unless you delete them. In your repository's "*Packages > Container Registry*" menu, you should regularly delete old images (those that are not newest, since they are still in use in the cluster). Also, if a development branch has been deleted, do delete the "image-list" for that entire branch.

The server hosting the GitLab installation tries to clean up the Container Registry once a day through a cron-job, but we cannot guarentee this will keep working forever.

### Close unused environments

As you create and delete branches thoughout the development of your project, environments will be created in the repository's "*Operations > Environments*" menu, reflecting running pods/services in the Kubernetes Cluster. Delete these unused environments to help free up resources on the cluster.

## Server trouble?

Take a look at the [Server help guide](/servers/server-help-guide).
