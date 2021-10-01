---
title: Server architecture
description: A description of aSTEP's server architecture.
published: true
date: 2021-09-29T08:56:13.245Z
tags: 
editor: undefined
---

# Server Architecture
> NOTE: For a more in-depth description of the server setup during 2018, refer to group SW602F18's (a server administrator) project report.
> NOTE: Group SW601F19's (a server administrator) project report documents  some of the process of updating some servers and the setup of the Kubernetes Cluster.
{.is-info}

The aSTEP system runs on a range of server computers (virtual machines) hosted by the IT department of AAU (ITS). They all run some version of Ubuntu. The system hosts all services running on aSTEP, their source code, and their data on databases. Furthermore, services are automatically build and run, when changes are made to a service's source code. The current server setup for aSTEP can be seen in the following figure.

![serverarchitecture-2020-fall.png](/server_architecture/serverarchitecture-2020-fall.png)
*NOTE: This figure is made using https://app.diagrams.net*

The following is a broad description of how the servers work together. When a developer pushes changes to a service's source code on GitLab (the Daisy-git server), the changed code is sent to the GitLab-Runner, which builds a [Docker (Container) Image](https://www.docker.com/resources/what-container) of the code. This image is sent back to GitLab and is stored in the [Container Registry](/gitlab#the-container-registry) and a request is sent to Kubernetes, telling it to fetch and run the new image (likely in place of an older version of the service).

The service associated with the image may then be accessed directly though its [auto generated URL](/kubernetes#auto-generate-urls) or through the UI if the service implements the [Microservice Interface Standard](/user-interface/api-standard).

## The current server computers

The list below presents very broad descriptions of the elements in the figure above. The following sections describe the elements of the figure above in more detail.

- **UI Proxy + Docker Host**: Redirects traffic from "https://astep.cs.aau.dk" to the user intarface. Also hosts 2018 services.
- **Daisy-git**: Version Control (Git) for all aSTEP services. Automatic deployment of services to the aSTEP website.
- **aSTEP-run01**: Compiles services' source code into Docker images. Images are stored on GitLab (Daisy-git).
- **Kubernetes Cluster**: Hosts all 2019+ services.
- **GPU server**: This server is dedicated to Machine Learning use.
- **DB1 and DB2**: Both host a number of databases used by various services.
- **Data + Backup**: Stores backups and miscellaneous data related to aSTEP, which does not belong in the database or inside services (e.g. demonstration videos).

### UI Proxy + Docker Host

**Proxy to the user interface:**
The *UI Proxy + Docker Host* server may be accessed through the public aSTEP domain "https://astep.cs.aau.dk" and serves as a proxy from said domain to the User Interface service (see the [UI documentation](/user-interface) and the [UI service documentation](/services/user-interface) for more). Redirection of internet traffic to the UI is handled by [*Nginx*](https://nginx.org/en/docs/http/ngx_http_proxy_module.html#example). The proxy configuration is stored in the file `/etc/nginx/nginx.conf`.

> You may stumble upon the `astep-api-registry` service. It was used to listen for "update [2018-service] requests". Depending on the "*service identifier*" received, it would pull the corresponding latest version from GitLab and execute that in place of the old version.
{.is-info}

**Hosting services from 2018:**
Secondly, this server uses [*Docker*](https://docs.docker.com/get-started/overview/) to host the services from 2018 (the Kubernetes Cluster was created in 2019 and hosts all services from then and forth). The program [*UFW*](https://help.ubuntu.com/community/UFW) is used to block/allow traffic on network ports. If ever the 2018 services stop working, you can restart them with the command `bash /home/start-docker-images.sh`. These services are accessed through the service called [*Legacy Services*](https://astep.cs.aau.dk/tool/astep-2019-legacyservices.astep-dev.cs.aau.dk) (see the [service's wiki-page](https://wiki.astep-dev.cs.aau.dk/services/legacy-services) for more).

> NOTE: Group SW607F18's service's backend "[*Vehicle to Grid (V2G)*](/services/vehicle-to-grid)" broke in 2020, after attepting to reinstall it with the correct HTTP-Certificate.
{.is-info}

> NOTE: An attemp to move the 2018 services to Kubernetes was made in 2020 Fall. However, this was not feasible as several of the old services cannot compile. Additionally, the database in Docker on **DB1** that these services use cannot run. Future semesters could investigate this issue further. {.is-info}



**Renewing HTTPS-Certificates:**
Speaking of certificates; when the certificates for the 2018 services expire, you can renew them with the command `sudo certbot`. Select the `astep.cs.aau.dk` (number 1) domain and follow the prompts to renew the certificate. When it asks you if you want to enforce encrypted communication, just answer "yes", since encrypted communication is already enforced by AAU.

When certbot is finished, navigate to the certificate directory and run the "certificate conversion script" using the two commands:

- `cd /etc/letsencrypt/live/astep.cs.aau.dk-0001`
- `sudo ./gen-p12.sh`

The certificate directory is mounted into each of the 2018 service docker containers, which use the converted certificate instead of the original (idk why, I didn't make it). Finally, restart the services (one method is described further above). Now the services should work again.

### Daisy-git

The *Daisy-git* server hosts a [GitLab](https://about.gitlab.com/what-is-gitlab/) instance which is accessable on: "https://daisy-git.cs.aau.dk/". The gitlab installation and "other data" is located in the directory `/srv/app/gitlab` (I am unsure if more folders are related to the GitLab installation).

GitLab is the version control system used to host/manage the source code for all aSTEP services. A daily cron-job runs the "GitLab registry garbage collecter" in order to save disk-space. GitLab has *300 GB* of space, so remember to [keep GitLab clean](/gitlab#gitlab-maintenance). For more information about GitLab not directly related to the gitlab-server-compurter itself, look at the [GitLab documentation page](/gitlab).

### aSTEP-run01

The *aSTEP-run01* server hosts a number of "GitLab Runners". The GitLab installation on the *Daisy-git* server uses the Runners to compile (and test) services, whenever changes are pushed to a GitLab project repository. The Runners compile the code into Docker Images, which are sent back to and stored in the GitLab installation. After compilation the Kubernetes Cluster is then told to fetch the new image and execute it.

The Runners are installed using the program `gitlab-runner`. For example, `sudo gitlab-runner list` lists all registered runners. Remember to always use `sudo`, else it can simply show wrong results without displaying any errors (give me a heart attack will ya?). The process of registering a new Runner in GitLab is described in the [GitLab documentation](/gitlab/make-a-group#add-a-group-runner).

### Kubernetes Cluster

*NOTE: This section may be lacking, since I am not that knowledgeable about these servers.*

The *Kubernetes Cluster* consists of three server computers: one master node and two worker nodes. The master node automatically distributes the running aSTEP services for execution among all three nodes in the cluster. Made in 2019, the Kubernetes Cluster replaces the 2018 system for hosting services (which happens on the [UI Proxy + Docker Host](#ui-proxy-docker-host) server).

The cluster is controlled from the master node through the program `kubectl`. A user does not have access to `kubectl` by default. For new users or in case Kubernetes was reinstalled, you are required to do the following:

- `mkdir -p $HOME/.kube`
- `sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config` (copy credentials file)
- `sudo chown $(id -u):$(id -g) $HOME/.kube/config` (set ownership of copy to yourself)

> NOTE: While you are free to create new users on all other server computers, only ITS may create new users on the cluster computers (idk why). These new users are linked directly to your AAU login. Ask ITS to create new accounts if you need them.
{.is-info}

### GPU server

This server is dedicated to facilitate fast(er) Machine Learning.  

#### How to access the gpu server:
Connect with SSH: ```ssh username@student.aau.dk@cs-gpu02.srv.aau.dk```
* 'username' is your AAU alias used with your mail, or Moodle
* The password is the same that you use for your university mail, or Moodle.
* Please note that you need to be on the university network to access the GPU server.


#### How to start training:
One way of transferring your project files to the server is to create a git repository with all involved files. You can then clone the project to your preferred folder on the GPU server: 
``` git clone https://github.com/username/repository.git ```

Alternatively, you can use the Secure Copy Protocol (SCP) to transfer files or entire folders to and from the GPU server, if the ```scp``` command is available on your system, using the syntax:
```scp [OPTIONS] [SOURCE] [DESTINATION]```

For instance, to copy an entire folder to the remote server, run:
```scp -r pathto/myprojectfolder/ username@student.aau.dk@cs-gpu02.srv.aau.dk:/user/student.aau.dk/username/myprojectfolder/ ```
Please note that the ***full*** path to the destination folder is written after the host name in the DESTINATION argument.

A reliable way to install your dependencies, such as Keras or Scikit-Learn, is by using a Python virtual environment, or similar. This way, you can control precisely which dependencies are in effect for your project, without affecting the system-wide Python installation. Cleaning up after your training runs is also simple. When you have transferred your files, ```cd``` to your project folder, and create a virtual environment:
```python3 -m virtualenv venv ```

(If the command cannot be found by python3, you can try to install the package: ```pip3 install virtualenv```)

This will in effect make a new local Python installation inside a folder named venv/. The 'venv' name is only a convention, and you can pick something else if preferred.

To activate the environment, run:
```source venv/bin/activate```

Now the command prompt should look something like this:
```(venv) username@student.aau.dk@cs-gpu02:~$```

This means that all pip packages you install with the virtual environment are now only local to venv/ - in fact, they are contained inside this folder. You can now install all of your pip dependencies from scratch by writing their package names in a requirement.txt file, and running:
```pip3 install -r requirements.txt```

You can also install packages 'normally' with ```pip3 install mypackage``` etc.

> Please note that you might need to specify concrete package versions in the requirements.txt file in order to make your dependencies work, and your project run, like:
> ```keras==2.3.1```
{.is-warning}


After sorting out your dependencies (which rely on the Python version on the server, check with ```python3 --version```), you should be able to run your script, when the environment is activated. When you are done, you simply run ```deactivate``` to exit the virtual environment. 

> You are required to run ```rm -r venv``` etc. to clean up ***all*** of the files you created on the server to avoid cluttering it over time.  
{.is-warning}

> If you used a git repository to transfer your files, you can push your trained model file etc. in order to get it a hold of it outside the GPU server.
{.is-info}



### DB1 and DB2

The *DB1* and *DB2* servers each hosts a database manager. DB1 hosts a Postgres server in a Docker container and DB2 hosts a Postgres server natively (outside Docker). To access these databases through the CLI (Command Line Interface), first SSH into the desired server computer and use the commands shown below:

- DB1:
  - `sudo docker exec -it postgresdb bash`
  - If you get an `error response from daemon: Container XXXXX is not running`, use this command and try again: `sudo docker start postgresdb`
  - `psql -U postgres`
  - You should now see psql(9.6.2) and `postgres=#`, and can now execute queries in the database.
- DB2: 
  - `sudo -u postgres psql`

You can also access the databases remotely using software such as pgAdmin. The postgres servers on both DB1 and DB2 listen on the standard Postgres port *5432*. Remember that the databases can only be accessed from within the AAU network or through VPN. The CLI can be accessed through the AAU network, VPN, or the SSH gateway.

> Note: Additionally, DB2 also hosts a Couchbase database server in a Docker container, but I cannot gain access to it nor reset the password. Also, apparently the documentation for Couchbase 4.6 has been wiped from the face of the internet. I know it was used in 2017 and 2018, and that 2018 managed to reset the password.
{.is-info}

> Note 2: The 2018 service (legacy serivice) called "*Logistics*" uses a service hosted using Docker on DB1 called "*OSRM_service*" (Open Source Routing Machine). *OSRM_service* is a pathfinder and uses the road network graph stored in the database `DB1/postgres` to find paths between two nodes.
{.is-info}

### Data + Backup

The *Data + Backup* server was created near the end of the Spring 2020 semester. The Fall 2020 semester installed SQLbak on this server, as well as on the 2 databases, as it is a free to use tool and easy to use. 

As of now, the data stored on database 1 & 2 are sheduled to make 2 backups during a month. These backups are stored on a google drive account, made for this purpose. Access to this account, as well as to the SQLbak tool, is shared in the start of each semester by the previous years semester.

> There's only installed SQLbak on this server. It is up to a future semester (hopefully Fall 2021) to set this server up to store backups locally. The plan is to store backups of databases and source code from the beginning (or perhaps more often) of each semester, such that critical failures on these servers may be reversible. Perhaps you could also store some miscellaneous data such as drawio-files or helper scripts from various server computers.
{.is-warning}

## The past server computers

For historical reasons, this section presents server computers that has been closed.

### Artifactory

The 2017 semester created this server and used it to host Maven Repositories (remotely hosted libraries, kinda like nuget) to use in the development/compilation of their services. For reference, they used "JFrog Artifactory" to manage these repositories. The 2018 semester also used this server. The server was closed in 2019 since it was deemed "superfluous".

We can no longer compile 2018 services unless we change the way they resolve libraries or make a new artifactory with all the old libraries. This may never be necessary though unless development on an old service must continue.

## Use SSH to access server-computers

Depending on the server-computer, you may or may not be able to access it from outside AAU's internet. Only *Daisy-git*, *Kubernetes Cluster*, and *UI Proxy + Docker Host* are accessible (any internet traffic) from outside AAU. To gain full accessibility, either be on the AAU network itself, use AAU's [VPN](https://www.en.its.aau.dk/instructions/VPN/), or use the [Gateway server](https://www.en.its.aau.dk/instructions/Username+and+password/SSH) (though, after a suspected security breach in August 2020 the gateway was made unavailable without VPN, so this may not be an option in the future). To SSH into a server, use the command below:

- `ssh [username]@[ip/domain]`

The username must be registered on the computer you want to access. Use the IPs/URLs shown in the figure at the top of this page. After sending the SSH request, you'll be prompted to enter your password. *Never send the password in plain text with the request*. The following example should give you an idea of how to use SSH:

- `ssh student00@student.aau.dk@sshgw.aau.dk` (yes, '@' twice when you log in with student credentials)
  - Password: [your student password]
- `ssh myuser@db2-astep.cs.aau.dk`
  - Password: [the password of *myuser* on the server]
  
You have now accessed the *DB2* server though the Gateway.

## Updating/reinstalling software on the servers
Before updating anything on the servers, make sure to have read relevant software update guides and made proper backups before proceeding. Updating packages on server computers or software such as GitLab, Kubernetes, or the wiki may cause the system to break or different parts to become incompatible. *(We can update GitLab! Runners and Kubernetes dies...)*

Rule of thumb is "unless you need newer features or to patch integrity/security faults, don't update", aka. "if it ain't broken, don't fix it".

### Updating the Operating Systems

Short story: "We don't" (major Ubuntu versions at least. Perhaps we can update minor versions; not sure). The servers are virtual machines hosted by ITS and as such only ITS gets to do this. Also, updating the OS requires that you wipe the virtual machine completely (at least when we updated), so only do this if you are prepared, if it is necessary, and you have backups.

### Updating GitLab or Kubernetes

While we did manage to update GitLab and Kubernetes during the semester, I don't know how, nor do the people who did it remember. Sorry, but you are on your own here. It is possible to look back in the user-command-logs (list of the commands a user has executed on a machine) to see if you can find anything there.

Just remember that updating GitLab can break Kubernetes- and Runner integration, and updating Kubernetes can also break the integration with GitLab. Make sure that updating GitLab or Kubernetes does not destroy existing data within them, even though this should be a rare occurrence.

### How to update/reinstall the wiki

The aSTEP wiki is hosted and manually installed on the Kubernetes Cluster. If you SSH into the master node and navigate to the directory `/user/student.aau.dk/shyber17/`, you'll find two files: `clean-wiki`and `deploy-wiki`. `clean-wiki` uninstalls the wiki from the cluster and `deploy-wiki` installs it. The files called `*.yaml` are used to configure all the components necessary to run the wiki. To re-install the current or update to a new version, first run the following commands:

- `sudo cd /user/student.aau.dk/shyber17/`
- `sudo nano wiki-deployment.yaml`

Find the line `image: requarks/wiki:*` and ensure the desired version is specified (2.4 as of writing this). Do note that a version of `2` translates to the latest `2.*.*`, that a version of `2.4` translates to the latest `2.4.*`, etc. When the correct version has been entered, save the document. Now, simply run the clean and deploy scripts:

- `sudo ./clean-wiki`
- `sudo ./deploy-wiki`

Give it a minute and the wiki should be running again. If not, run the command: 

- `sudo kubectl get pods`

Find the `NAME` of the wiki service, which should be something along the lines of `wiki-js-*-*`. Check if the `STATUS` of the wiki is an error code. If yes, run the following command to get the error logs (shown at the bottom):

- `sudo kubectl describe pod wiki-js-*-*` (where `wiki-js-*-*` is replaced by the `NAME` you found before)

Act according to the error or ask someone for help.

## Rollback of a server-computer

If a server-computer should happen to go complete FUBAR, you may request AAU's IT Support (ITS) to make a "rollback". Just give ITS the IP of the server(s) involved and the specific date you want to roll each server back to. Then ITS will restore the server(s) to the requested date.

Generally, you can rollback up to 14 days on Linux-based servers (all aSTEP servers are Linux), but this can vary depending on the setup. We don't know the specific limit for the aSTEP servers. Sometimes, ITS can be a bit slow (we talk days) to respond, so play it safe and request the rollback within a week of when the problem happened.

## Server trouble?

Take a look at the [Server help guide](/servers/server-help-guide).
