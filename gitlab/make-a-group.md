---
title: How to make a new GitLab group
description: This guide outlines the details of creating a new GitLab group, setting it up, and adding users to it.
published: true
date: 2021-09-16T13:20:47.759Z
tags: 
editor: undefined
---

# How to make and setup a new GitLab group

Preferrably, the main contact person or main server administrator should do the set up, since you only need one group per semester. For this guide you must have: access to a GitLab admin account and SSH access to the [astep-run01 server](/servers). The official GitLab website has a guide for [creating groups and adding users](https://docs.gitlab.com/ee/user/group/#create-a-new-group) (users themselves can also request access, where a group owner or admin must accept them) so use this to find your way though aSTEP's GitLab if need be. 

## Create the group

First, you go to the [new group page](https://daisy-git.cs.aau.dk/groups/new) on GitLab. Enter a fitting name for your new GitLab group (e.g. "*aSTEP-[semester]*" as with previous years), add a description and or an avatar if you want, and leave your group as "*public*" so later semesters can see it exists.

Press "*Create Group*" at the bottom of the screen. You now have a blank group. Congratulations!
___
> The following steps must be done by the group admin {.is-danger}
## Set up environment variables

Next, you need to add two environment valiables to your new GitLab group. To find the list of environment variables, go to the new GitLab group's "*Setting > CI / CD*" menu and expand the "*Variables*" tab. Press "*Add Variable*" and add each of the environment variables listed below. 

<table>
  <thead>
    <tr><th>Type</th><th>Key</th><th>Value</th><th>Protected</th><th>Masked</th></tr>
  </thead>
  <tbody><tr>
    <td>Var</td><td>AUTO_DEVOPS_DOMAIN</td><td>astep-dev.cs.aau.dk</td><td>false</td><td>false</td></tr>
    <tr><td>Var</td><td>KUBERNETES_VERSION</td><td>1.17.4</td><td>false</td><td>false</td></tr>			
  </tbody>
</table>

> If you ever update Kubernetes, you may have to return here and update the version number.
{.is-warning}

## Add a Group Runner

Installing a new GitLab runner and registering it in GitLab is quite simple. This kind of runner can be selected for use in any repository from the corresponding group. You simply do the following:

- Make sure you are on the AAU wifi or connected to it through a VPN.
- Go to your group's "*Setting > CI / DC*" menu and open the "*Runners*" tab and scroll down until you find the "*Set up a group Runner manually*" section.
 	- Ignore point 1 and 2, GitLab is already installed on the `astep-run01` server.
  - Take note of the `registration token` in point 3.
- Connect to the `astep-run01` server on IP 172.19.0.242 through SSH, using the admin username you received from the previous group, and password. 
	- Run the command `ssh -l username 172.19.0.242`, and type in the password.
  -  OBS: Make sure the IP address is correct if this doesn't work. Go to "Server Architechture" to see the present IP address of `astep-run01`.password.
	- Run the command `sudo gitlab-runner register`.
	- Enter `https://daisy-git.cs.aau.dk/` for the first prompt.
  - Enter the `registration token` from GitLab you took note of.
  - Enter a fitting description for the runner (e.g. `astep-run01-spring-2020`).
  - Leave the promt for *tags* blank (just press enter).
  - Enter `true` for the prompt about "locking".
  - Enter `docker` as the "*executor*".
  - Enter `alpine:latest` as the "*default docker image*".
- After the runner is created it’s necessary to change a few things in the runners config file.
  - Start by opening the file with the command: `sudo nano /etc/gitlab-runner/config.toml` to start editing.
  - First, locate your runner. (It should be the last one in the file)
  - After that, add the line `privileged = true` below `image = “alpine:latest”`.
  - Then, copy the `volumes` and `extra_hosts` variables from one of the previous runners and use them instead of your own.
  - Optional(but strongly suggested): you can add the `pull_policy="if-not-present"` this makes it possible for the runner to use locally stored images if present, which lowers the amount of images pulled from dockerhub.
  - Exit and save using `ctrl + x` then press `y` to save the file.
 
If you refresh the GitLab page with the runners, the new runner should now show up. You can now select it in the repositories.

> If you ever remove/unregister a runner and wonder why it keep showing up when you call `sudo gitlab-runner list` and cannot be removed by `sudo gitlab-runner unregister RUNNER_NAME`, simply run the command `sudo gitlab-runner verify --delete` to remove the removed runners.
{.is-info}

## Add users to the group

Lastly, to add the new users to the new groups, you (the owner or an administrator) can add all the new users as "*Developers*" in your GitLab group's "*Members*" menu. Alternatively, all the new users can enter the new GitLab group and press "*Request access*", after which the owner/admin must accept their request in the "*Members*" menu.

Do whatever you find easiest.

## Next steps

When you have a GitLab group set up and your users have access, you can all start [making project repositories](/gitlab/make-a-repository) where you will store your services' source code.
