---
title: Kubernetes (K8S)
description: The Kubernetes Cluster hosts all services running on aSTEP (this wiki included).
published: true
date: 2020-12-05T15:58:25.155Z
tags: 
editor: undefined
---

# Kubernetes (aka. K8S)
> NOTE: This page reflects the state of the system at the end of the Spring 2020 semester.
> NOTE: Thoughout this page, the terms: "version of a service", "service-version", "service", and "pod" (the executable unit on Kubernetes) is used interchangably.
{.is-info}

The Kubernetes Cluster was installed by the 2019 semester to improve management and versioning of aSTEP services by integrating it with [GitLab](/gitlab). This feature allows for services to build and deploy to aSTEP automatically, when [changes are pushed to a service's sorce code](/gitlab#continuous-integration-how-gitlab-deploys-services). The cluster [consists of 3 computers](/servers#kubernetes-cluster) working together to execute all the services on aSTEP.

Kubernetes can be managed directly through the master-computer of the cluster or partly though the [GitLab Admin Area](/gitlab#admin-area). Kubernetes does most things automatically, so you'll usually only have to touch it when you need to maintain or debug it.

## Run multiple versions of services

As is also explained in the [GitLab documentation](/gitlab#continuous-integration-how-gitlab-deploys-services), the project repository associated with a service may contain any number of code-brances. One master branch and various development branhes. For each branch Kubernetes will host a service based on the source code from that branch.

Whenever changes are made to a branch, the currently running version for that branch (if it exists) is swapped for the newest version. In this way the Kubernetes cluster will automatically make sure that all versions of a service are up-to-date, which makes deploying and testing new versions easy for developers.

> Please, for the love of everything holy, don't push multiple TensorFlow images or very demanding services unto the cluster. The cluster will start behaving errativally and evicting (closing/stopping) other running services.
{.is-info}

### Auto-generate URLs

The Kubernetes application "*Ingress*" manages and automatically generates URLs for all versions of all services running on Kubernetes. Ingress is hit when attempting to access the cluster through port 80 or 443 (for https), and redirects traffic to the correct service.

Versions of a service fall into one of two categories: "Production" or "Development" ([see the GitLab documentation](/gitlab#one-version-per-branch)). Depending on the category, a service-version's URL has the following general structure:

- Production: `[group]-[repository].astep-dev.cs.aau.dk`
- Development: `[group]-[repository]-review-[branch]-[random].astep-dev.cs.aau.dk`

The `[group]-[repository]` part is based on the [group and repository](/gitlab#location-structure-and-properties-of-repositories) from which the service originates in GitLab. For development versions, the `[branch]` part is the name of the branch the version is based on and `[random]` is just a random string of about 5 characters. You can find the link for each version of a service as described [here](/gitlab#one-version-per-branch) in the GitLab documentation.

You can easily test development versions on the aSTEP website as described in [this guide from the User Interface documentation](/user-interface#support-for-multiple-versions-of-a-service).

> NOTE: Ingress redirects all web-traffic to the service's port 5000. Therefore, any service must listen for web-traffic on port 5000.
{.is-info}

## Renew https certificates

Https certificates are needed in order to access the services in the UI, since AAU requires https communication over their network. The Kubernetes application [cert-manager](https://cert-manager.io/docs/) automatically creates and renews https certificates for all versions of all services (in contrast to the renewal of the [certificate for legacy services](/servers#ui-proxy-docker-host)). That is, you don't implement anything HTTPS related, since Kubernetes does it for you. 

Cert-manager runs in a pod in the Kubernetes cluster. Find the pod by using the command: 
- `kubectl get pods --all-namespaces | grep certmanager`


The certificates are generated using [Let's Encrypt](https://letsencrypt.org/) - a Certificate Authority (CA) that provides free TLS certificates. By default, the certificates are valid for 90 days, but cert-manager will try to renew them 30 days before expiration. 

To show the certificate expiration date for a particular service, find the certificate associated with the service: 

- `kubectl get certificates --all-namespaces`

Then look for the *Not After* field in the certificate details: 

- `kubectl describe certificate [CERTIFICATE_NAME] -n [NAMESPACE]`

To get a concise overview of expiration dates for all certificates in the cluster, print the certificate details for every namespace and pipe the result to the *grep* and *sort* command: 

- `kubectl describe certificates --all-namespaces | grep "Not After" | sort -k 2`

## Kubernetes maintenance and debugging

In case you are going to need it, here are some nice-to-know things about the management of Kubernetes.


### List all registered pods

To get a list of all running/crashed/failed versions of all services (as well as other processes hosted on Kubernetes), use the following command:

- `kubectl get pods --all-namespaces`

You should be able to derive the entry that corresponds to your service-version based on the `NAME` column. You can search for services within a single `NAMESPACE` (see the column header), by using the command:

- `kubectl get pods --namespace [NAMESPACE]`

To get a more detailed description of a pod, use:

- `kubectl get pod -n [NAMESPACE] [POD_NAME] -o yaml`

### Print output-log for pod

If your service behaves oddly or craches without any sensible output, you can try getting the service's output-log by using the command below:

- `kubectl logs --namespace [NAMESPACE] [NAME]`



Use the list of registered pods to find your service's pod's `NAMESPACE` and `NAME`.

### Close pod
The simplest way to tell Kubernetes to terminate a pod is by running these commands.

- `kubectl get deployments --all-namespaces` 

This command display all deployments. Copy and paste the namespace and deployment, for the pod you wish to terminate, into the command below

- `kubectl delete -n NAMESPACE deployment DEPLOYMENT`

If you run the 'get pods' command from above, you should now see the pod is in terminating state, and soon is removed from kubernetes.

### Close evicted pods

Pods or service-versions can stay after being closed on GitLab or if the system evicts (closes/stops) them to free up resources in the case that Kubernetes runs low on resources. These should be removed. You can use the following command to delete all evicted pods:

- `kubectl get pods --all-namespaces --field-selector 'status.phase==Failed' -o json | kubectl delete -f -`

See the [documentation](https://kubernetes.io/docs/reference/kubectl/cheatsheet/#deleting-resources) for the command `kubectl delete` to get additional syntax for deleting pods.

### Close 'terminating' pods
Sometimes pods are stuck in 'terminating' state. This can happen for various reasons, and can be solved by a simple command. 
If you want to force close a single pod use the following command
- `kubectl delete pod --grace-period=0 --force --namespace [NAMESPACE] [POD_NAME]`

If more than one pod is stuck, or you want to clean out evicted and terminating pods, the following command force closes every pod which is not in the 'running' state. Kubernetes will try and fetch some of the images again, so check back again soon to verify everything is working as expected.
- `kubectl get pod --all-namespaces | awk '{if ($4 != "Running") system ("kubectl -n " $1 " delete pods " $2 " --grace-period=0 " " --force ")}'`

### When pods won't even start

Sometimes you may encounter that your service does not even start. In that case, try using the command below here. It will output general information about your service's setup on Kubernetes, as well as an event-log during creation/startup of the pod at the bottom.

- `kubectl describe [NAME]`



Use the list of registered pods to find your pod's `NAME`.

### When certificates are not generated or renewed

If a certificate has not been automatically generated or a problem occured during the renewal process, it is possible to investigate the error and possibly perform a renewal manually. 

When cert-manager generates a certificate for a service, it is stored in a *secret* for that particular service. By deleting the secret, cert-manager will be invoked and try to generate a new certificate.  

Run the following command to list all certificates, name of secrets and their current status:  

- `kubectl get certificates --all-namespaces`

For services/namespaces with a invalid certificate (ready status `false`), the following command can be used to investigate possible errors: 

- `kubectl get certificates -n [NAMESPACE]`

Look under *Status* where any information about errors will appear.  

The secret can be deleted (thereby renewing the certificate) using the command: 

- `kubectl delete secret [SECRET_NAME] -n [NAMESPACE]`

## Monitoring the kubernetes dashboard
See the guide for accessing the [kubernetes dashboard](kubernetes-dashboard).

## Server trouble?

Take a look at the [Server help guide](/servers/server-help-guide).
