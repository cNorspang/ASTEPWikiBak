---
title: How to increase disk space on a node in kubernetes
description: 
published: true
date: 2020-11-30T10:01:50.664Z
tags: 
editor: undefined
---

# Increasing disk space on kubernetes
> NOTE: This is a outdated solution, which is not recommended.
{.is-warning}

Increasing disk space on kubernetes using a second mounted volume was acomplished like so:

ssh into the master and type:
```bash 
kubectl get nodes
```

Take the full name of the "problem" node and type:
```bash 
kubectl drain NODE_NAME --force=true --delete-local-data=true --ignore-daemonsets=true
```

Wait for the drain to finish.
ssh into the node with the "problem" and edit ``` /lib/systemd/system/docker.service ``` change line:

```bash
ExecStart=/usr/bin/docker daemon -H fd://
INTO:
ExecStart=/usr/bin/docker daemon -g /new/path/docker -H fd://
```

```/new/path/docker``` is a path to a mounted volume with even more space.


stop, reload and start docker with:
```bash
systemctl stop docker
systemctl daemon-reload
systemctl start docker
```

Now you must untaint the node so it can recieve pods again: 
```bash
kubectl uncordon NODE_NAME
```
Now you have moved the docker images to a new and bigger volume. You may need to start some deployments/pods again from the gitlab pipeline if they failed to fit on the remaining nodes while the upgrade ran.