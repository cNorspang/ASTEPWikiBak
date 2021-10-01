---
title: Getting started
description: By reading this guide you should get a basic understanding of the aSTEP system and how to use its components.
published: true
date: 2021-09-29T20:32:18.347Z
tags: 
editor: undefined
---

# Getting started: a new semester
> NOTE: This page reflects the state of the system at the end of the Spring 2020 semester.
{.is-info}

This guide will first give you a broad introduction to the most general parts of the aSTEP system. Following that, it'll take you through the process of getting new source code onto GitLab and deploying a service. Then, it'll explain how to access the databases and (for administrators) the server computers in general. Lastly, the guide tells you where to go next on this wiki and what information to seek.

Hopefully, some of this process will have been covered during the handover from the previous semester to yours, but in case that hasn't been done, all steps to getting started are documented here.

## Before you start
Before starting diving into the code and website, it is strongly adviced that your primary contact person organize the first meeting as fast as possible.

During this meeting, you will have to decide how you want to organize how you want to cooperate together. 

To see how the students before you organized themselves, take a look at [RFC0019](https://wiki.astep-dev.cs.aau.dk/en/rfc/0019), and update it such that it matches how you work.

An RFC is a description of a specific standard which the further development of aSTEP is strongly adviced to uphold, and is described in more detail in [RFC0001](https://wiki.astep-dev.cs.aau.dk/rfc/0001).

It is strongly adviced that you follow/improve the current RFC's, since they describe the general interfaces and standardisation of the aSTEP system as a whole.

## Getting familiar with the aSTEP system

> The following are very basic introductions, so you should read more after you finish this guide. The last section will tell you where to go next.
{.is-info}

Firstly, you should know about the two websites associated with the aSTEP project: the [aSTEP website itself](https://astep.cs.aau.dk) and the [GitLab website](https://daisy-git.cs.aau.dk/explore/groups). You should create an account on GitLab using your student mail for the account, making it easier to find you in the user-list. (Of course, there are many more URLs/web-resources in the aSTEP system, but that is not important right now.)

The aSTEP website follows a "microservice architecture", meaning that many small (micro)services together make up the website's functionality. Through the aSTEP website you can use/interact with the wide variety of services listed in the left-hand service-menu. The link above will likely lead you to a login page. Use the email `demo@astep.cs.aau.dk` and the password `demodemo` to gain access.

The GitLab website stores the source code for all aSTEP services and is responsible for handling the compilation and deployment of services to the aSTEP website. The GitLab link above leads to the list of all current "groups". These groups stores the source code for the various semester's projects as will be explained further in the next section.

Lastly, you should know about the general structure of aSTEP's back-end, which consists of various interconnected server-computers. The introduction at the top of the [Server Architecture documentation](/servers) displays and explains a figure of the current aSTEP server-setup (you shouldn't read anymore than the introduction for now).

Now that you have some general knowledge about the project, the next section will explain how your project group gets your first service up and running.

## From nothing to a running service

This section is split into three steps: "*Setting up a GitLab group*", "*Setting up a repository in the GitLab group*", and "*Creating and deploying a service*". A GitLab group stores repositories and a repository stores the source code for a service.

The first step is reserved for the main contact person or a server administrator. Follow the guide on how to [make a new GitLab group](/gitlab/make-a-group) and come back here. Once the GitLab group has been set up and you've been given access to it, you can proceed to the next step.

*If you are not going to make a new service, you may just read and understand the next two steps and not actually carry them out. However, feel free to make a test project for the sake of practice.*

For the second step, follow the guide on how to [make a new GitLab repository](/gitlab/make-a-repository). For the third step, follow the guide on how to [make and deploy a service](/gitlab/make-and-deploy-a-service) and come back here. With this, you should have pushed some code to the new repository and have a service running on the aSTEP system.

## Access to databases

It's likely that you want to connect your service to one of the astep databases. Or, that you want to browse the databases using software such as [pgAdmin](https://www.pgadmin.org/download/). There are two databases, each running a PostgresSQL installation. The [database documentation](/databases) gives you an overview over these.

You can access the aSTEP databases as long as you are on the AAU network or have VPN activated and have a login set up on the database server you want to access. A server administrator must set up those credentials. The database documentation has a [guide for accessing databases](/databases#connecting-to-the-databases).

## Getting access the server computers

This section is for the main contact person and the server administrators, so anyone but them can skip this. Administrators will have to log into the server computers at some point to do maintenence and the sorts. To log into the server computers, follow [this guide to using SSH](http://wikiproxy.seanprogramming.com/servers#use-ssh-to-access-server-computers) from the server architecture documentation.

The login credentials referred to by the guide is given to your semester's main contact person during the handover meeting at the start of the semester, and it is for them to distribute the credentials to the relevant parties. If you haven't been given these credentials, contact the [previous semester](https://astep.cs.aau.dk/contact).

## What to read next?

After reading this guide, you should have a basic understanding of how to navigate the aSTEP system. The next step would be to get an understanding of the finer details. (You'll probably have read parts of the pages referenced in the following already.)

You should read the [User Interface documentation](/user-interface) as well as its sub-pages, the main [GitLab documentation](/gitlab), and the [databases documentation](/databases). It is also adviced to read the [Kubernetes documentation](/kubernetes).

If you are going to work with an existing service, look for it in the [list of service documentation](/services).

If you are the main contact person or a server administrator, you should read and understand the [Server Architecture documentation](/servers) as well.
