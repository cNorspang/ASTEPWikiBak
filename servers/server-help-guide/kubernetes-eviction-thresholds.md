---
title: kubernetes eviction thresholds
description: 
published: true
date: 2020-11-30T09:42:30.784Z
tags: 
editor: undefined
---

# Kubernetes eviction thresholds
By *default* kubernetes will begin to evict pods from a node when these tresholds are broken:

memory < 100Mi
nodefs.available < 10%.
nodefs.inodesFree < 5%.
imagefs.available < 15 %.
imagefs.inodesFree no default.

So even if ```df -h``` or ```df -i``` looks good there might be less obvious thresholds broken causing the evictions.

Read more here: [Configure Out of Resource Handling](https://kubernetes.io/docs/tasks/administer-cluster/out-of-resource/)