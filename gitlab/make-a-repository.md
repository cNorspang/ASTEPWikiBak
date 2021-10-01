---
title: How to make a new GitLab project repository
description: This guide outlines the details of creating a new GitLab project repository, setting it up, and adding users to it.
published: true
date: 2020-11-26T15:56:48.522Z
tags: 
editor: undefined
---

# How to make a new GitLab project repository

Once your project-group has created GitLab accounts and has been added to your semester's GitLab group, you can start making a project repository to store the source code of your services. 

## Create a repository in your semester's GitLab group

- Navigate to the new GitLab group's main page (https://daisy-git.cs.aau.dk/[new-gitlab-group]). 
- Press the "*New project*" button in the top right corner.
- Enter a fitting name for your new service.
- Ensure that the "*Project URL*" is set to "https://daisy-git.cs.aau.dk/[new-gitlab-group]".
- There is no real rule for setting the project repository's "*Visibility Level*", so if you have "secret stuff" make it private, else make it public or internal.
- Check the "Initialize repository with a README" option if you aren't gonna push existing code to the new repository.

Press "Create Project" at the bottom of the screen. You now have a blank (except the README) project repository. Congratulations!

> NOTE: Your project repository's URL will become: "https://daisy-git.cs.aau.dk/[new-gitlab-group]/[project-slug]". 
{.is-info}

> Be carefull with long repository names. A too long name can cause all development branches to fail, to deploy, exept the master branch.
{.is-warning}

> Be carefull with special charaters in branch names. They can cause a branch to fail to deploy. ```'_'``` and ```'-'``` should work.
{.is-warning}

## Enable the group runner

As is explained in the [GitLab documentation](/gitlab#continuous-integration-how-gitlab-deploys-services), the runner is (in short) the system that GitLab uses to actually build/compile your service. To enable a group runner for your project, follow these instructions:

- Go to your repository's "*Settings > CI / CD*" menu.
- Expand the "*Runners*" tab and scroll down to the "*Group Runners*" section.
- Press "*Enable group runners for this project*" is necessary.
- Select the (likely only) group runner available.
  - If no group runner is available, there is likely something wrong with the GitLab group's setup.

## Enable the Container Registry

As is explained in the [GitLab documentation](/gitlab#continuous-integration-how-gitlab-deploys-services), the Container Registry is (in short) the place GitLab stores your compiled services. To enable the Container Registry for your project, follow these instructions:

- Go to your repository's "*Settings > General*" menu.
- *Enable Container Registry*: In the repository's general settings, enable the "*Container Registry*" option under the "*Visibility, project features, permissions*" section.

Now that the registry is enabled, remember to [keep it clean](/gitlab#clean-the-continer-registry).

## Next steps

When you have a working repository set up, you can start [making and deploying a new service](/gitlab/make-and-deploy-a-service).
