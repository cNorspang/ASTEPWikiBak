---
title: Kubernetes Dashboard
description: A small guide to accessing the kubernetes dashboard
published: true
date: 2020-12-19T12:28:37.818Z
tags: 
editor: undefined
---

# Kubernetes dashboard
> Needs improvement. If you can understand this and make it work, please update the page.
{.is-info}

The kubernetes dashboard has full privileges to perform any action so click around the dashboard with care. 

A External guide was followed to setup the kubernetes dashboard, it was simple enough. The trouble arrises when we want to access the dashboard.

## Creating the tunnel
The main trouble is reaching the dashboard since it is only avaible locally on the master. The master is also not aviable from the outside since it is a part of the local AAU network.

A workaround requires a couple ssh tunnels and propper credentials.

It works like this: Master <-tunnel-> Proxy <-tunnel-> YourPC

PORT = 8001 (kubernetes dashboard defualt)
IP-OF-MASTER = 172.19.18.16
IP-OF-PROXY = astep.cs.aau.dk
USERNAME = Your personal username on the server 

Be aware that your username on the Master and Proxy server may be different. As of 2020 Fall your username on the Proxy is the name before @ in your AAU email and on the Master it is your full AAU email. 


While inside the AAU proxy server (astep.cs.aau.dk) type:
```ssh -L PORT:127.0.0.1:PORT -N -l  USERNAME  IP-OF-MASTER ```
There is now a tunnel: Master <-tunnel-> Proxy




While on your own machine type:
```ssh -L PORT:127.0.0.1:PORT -N -l USERNAME IP-OF-PROXY ```
There is now a tunnel: Proxy <-tunnel-> YourPC

So by extension we have: Master <-tunnel-> Proxy <-tunnel-> YourPC

You can now access the dashboard in your own machine by going to: ```http://localhost:PORT/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/#/login```

## Getting the token

You need to provide a token with priviliges to login to the kubernetes dashboard.

While on the master type:
``` kubectl get secrets ```

Note the name of the secret that has a name with "dashboard" in it.
Now type:
``` kubectl describe secret SECRETE-NAME ```

It will return you the token for use in the browser-dashboard. Remember to close the connections when done. The data stream should be encrypted from your machine to the master however you should still close the connections when not in use.