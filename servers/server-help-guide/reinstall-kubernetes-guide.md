---
title: Reinstall kubernetes guide
description: A short guide that describes how we reinstalled kubernetes.
published: true
date: 2020-10-01T07:35:14.779Z
tags: 
editor: undefined
---

# A small guide to reinstalling kubernetes

## Usefull scripts

If the user homes are still available on the master node, two useful scripts are available in `/user/student.aau.dk/rlindh17/kube/`
here you would first run `sudo ./døKubernetes.sh` followed by `sudo ./comeBackKubernetes.sh` which in theory should reinstall all the stuff but I can not guarentee that it works. If it does not, follow this guide below.

First you must clean the installation on the master as well as the nodes with

```bash
sudo kubeadm reset -f
sudo rm -r /etc/cni/net.d
sudo apt-get purge kubeadm kubectl kubelet -y
sudo apt autoremove -y
sudo rm -r /opt/cni/bin
sudo iptables -F && sudo iptables -t nat -F && sudo iptables -t mangle -F && sudo iptables -X
```
Then reinstall with
```bash
sudo apt-get install kubeadm=1.17.2-00 kubectl=1.17.2-00 kubelet=1.17.2-00 -y
sudo kubeadm init --pod-network-cidr=10.244.0.0/16
```

Use flannel for networking
```bash
sudo kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml
```

## Integrating Kubernetes with Gitlab

[Follow this guide.](https://docs.gitlab.com/ee/user/project/clusters/add_remove_clusters.html)

After it is connected to gitlab you must do a couple more things...

First enable ingress and cert-manager from gitlab integration.

Then you must set the external ip of the loadbalancer, to the local ip of the master server
```bash
kubectl patch svc -n gitlab-managed-apps ingress-nginx-ingress-controller -p '{"spec":{"externalIPs":["172.19.18.16"]}}'
```

You must also enable legacy api support following [these steps.](https://gitlab.com/gitlab-org/charts/gitlab/-/issues/1562#note_225155008)

## Get https working

You must make a file called `cert.yaml`, with the following content

```bash
   apiVersion: cert-manager.io/v1alpha2
   kind: ClusterIssuer
   metadata:
     name: letsencrypt-prod
   spec:
     acme:
       # The ACME server URL
       server: https://acme-v02.api.letsencrypt.org/directory
       # Email address used for ACME registration
       email: thkn16@student.aau.dk
       # Name of a secret used to store the ACME account private key
       privateKeySecretRef:
         name: letsencrypt-prod
       # Enable the HTTP-01 challenge provider
       solvers:
       - http01:
           ingress:
             class:  nginx
```
And make another file called `cert2.yaml` with content:
```bash
apiVersion: apiextensions.k8s.io/v1beta1
kind: CustomResourceDefinition
metadata:
  name: certificates.certmanager.k8s.io
  labels:
    app: cert-manager
spec:
  additionalPrinterColumns:
  - JSONPath: .status.conditions[?(@.type=="Ready")].status
    name: Ready
    type: string
  - JSONPath: .spec.secretName
    name: Secret
    type: string
  - JSONPath: .spec.issuerRef.name
    name: Issuer
    type: string
    priority: 1
  - JSONPath: .status.conditions[?(@.type=="Ready")].message
    name: Status
    type: string
    priority: 1
  - JSONPath: .metadata.creationTimestamp
    description: |-
      CreationTimestamp is a timestamp representing the server time when this object was created. It is not guaranteed to be set in happens-before order across separate operations. Clients may not set this value. It is represented in RFC3339 form and is in UTC.

      Populated by the system. Read-only. Null for lists. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata
    name: Age
    type: date
  group: certmanager.k8s.io
  version: v1alpha1
  scope: Namespaced
  names:
    kind: Certificate
    plural: certificates
    shortNames:
    - cert
    - certs

---

apiVersion: apiextensions.k8s.io/v1beta1
kind: CustomResourceDefinition
metadata:
  name: issuers.certmanager.k8s.io
  labels:
    app: cert-manager
spec:
  group: certmanager.k8s.io
  version: v1alpha1
  names:
    kind: Issuer
    plural: issuers
  scope: Namespaced

---

apiVersion: apiextensions.k8s.io/v1beta1
kind: CustomResourceDefinition
metadata:
  name: clusterissuers.cert-manager.io
  labels:
    app: cert-manager
spec:
  group: cert-manager.io
  version: v1alpha2
  names:
    kind: ClusterIssuer
    plural: clusterissuers
  scope: Cluster

---

apiVersion: apiextensions.k8s.io/v1beta1
kind: CustomResourceDefinition
metadata:
  name: orders.certmanager.k8s.io
  labels:
    app: cert-manager
spec:
  additionalPrinterColumns:
  - JSONPath: .status.state
    name: State
    type: string
  - JSONPath: .spec.issuerRef.name
    name: Issuer
    type: string
    priority: 1
  - JSONPath: .status.reason
    name: Reason
    type: string
    priority: 1
  - JSONPath: .metadata.creationTimestamp
    description: |-
      CreationTimestamp is a timestamp representing the server time when this object was created. It is not guaranteed to be set in happens-before order across separate operations. Clients may not set this value. It is represented in RFC3339 form and is in UTC.

      Populated by the system. Read-only. Null for lists. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata
    name: Age
    type: date
  group: certmanager.k8s.io
  version: v1alpha1
  names:
    kind: Order
    plural: orders
  scope: Namespaced

---

apiVersion: apiextensions.k8s.io/v1beta1
kind: CustomResourceDefinition
metadata:
  name: challenges.certmanager.k8s.io
  labels:
    app: cert-manager
spec:
  additionalPrinterColumns:
  - JSONPath: .status.state
    name: State
    type: string
  - JSONPath: .spec.dnsName
    name: Domain
    type: string
  - JSONPath: .status.reason
    name: Reason
    type: string
  - JSONPath: .metadata.creationTimestamp
    description: |-
      CreationTimestamp is a timestamp representing the server time when this object was created. It is not guaranteed to be set in happens-before order across separate operations. Clients may not set this value. It is represented in RFC3339 form and is in UTC.

      Populated by the system. Read-only. Null for lists. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata
    name: Age
    type: date
  group: certmanager.k8s.io
  version: v1alpha1
  names:
    kind: Challenge
    plural: challenges
  scope: Namespaced

---

```

run the following to apply them:
```bash
kubectl apply -f cert2.yaml 
kubectl create -f cert.yaml 
```
At the very end you have to update the kube config file of the service fetcher with the one on `/etc/kubernetes/admin.conf`

Then, in theory, all you have to do is run the deploy job for all your microservices on gitlab.