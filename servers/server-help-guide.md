---
title: Server help guide
description: This page is intended to help with common issues with the server.
published: true
date: 2020-11-30T10:00:29.563Z
tags: 
editor: undefined
---

# Server help guide

This page lists some questions we had regarding fixing servers during the semetser. Refer to the [server architecture documentation](/servers) for a list of server IPs and a guide to using SSH. SSH access is enabled for all servers, however, only some people may have access to the SSH credentials.

## Linux servers in general

**Q:** How do I verify that a service (not to be confused with an aSTEP service) is running?
**A:** `sudo systemctl status "Service Name"`

**Q:** How do I start a service (still not aSTEP service)?
**A:** `sudo systemctl start "Service Name"`

## Gitlab

**Q:** ERROR: Job failed (system failure): Error response from daemon: Cannot link to a non running container: $CONTAINER AS $OTHER_CONTAINER
**A:** Look at the top of build logs in gitlab it should say: 
WARNING: Service $SERVICE didn't start properly.
 Error response from daemon: Conflict. The container name $CONTAINER is already in use by container $IMPORTANT_CONTAINER
 
Go into the runner and type: 
```bash
sudo docker stop $IMPORTANT_CONTAINER
sudo docker rm $IMPORTANT_CONTAINER
```

**Q:** Gitlab is running out of space?
**A:** There exists multiple commands to clean gitlab like: ```sudo gitlab-ctl registry-garbage-collect -m ``` simply run it on the gitlab server. Try googleing others as it might be some other garbage that need cleaned.

## Kubernetes

**Q:** What services should be running on the nodes?
**A:** At least: "*Docker*" and "*kubelet*" 

**Q:** Kubelet wont start?
**A:** `htop` -> swap must say 0k (zero-k) to verify swap is disabed

**Q:** How do I disable swap?
**A:** `sudo swapoff -a` (it resets after every reboot by defualt)

**Q:** Connection refused when doing kubectl commands?
**A:** You have no or an outdated kubectl config file (`admin.conf`). Follow the instructions [here](/servers#kubernetes-cluster) to fix it.

**Q:** Pods get evicted/closed randomly?
**A:** You are probably running out of resources, check DISK - RAM - CPU usage of the cluster nodes. Try closing some (resource consuming) development versions of services (you didn't push a CPU intensive 4GB RAM TensorFlow machine learning image, did you?). The [kubernetes eviction thresholds](kubernetes-eviction-thresholds) are quite stringent.

**Q** How do I get more disk space on a node? Pods are sometimes evictied due to Disk pressure?
**A** In fall 2020 the two workers were upgraded with 200gb more space each. For the foreseable future it should not be necessary to extend the workers with more space, however this becomes an necessity ask ITS for more space. An old solution was to create a symlink to an external disk: [increased disk space on node](increased-disk-space-on-node).

**Q:** How to remove many evicted pods at once?
**A:** `kubectl get pods --all-namespaces --field-selector 'status.phase==Failed' -o json | kubectl delete -f -`

**Q** I need to completely reinstall all of kubernetes!
**A** We suggest you follow the steps we did as it took quite a long time to arrive at them [Reinstall Kubernetes Guide](reinstall-kubernetes-guide).

