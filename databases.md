---
title: Databases
description: This page describes the databases of aSTEP.
published: true
date: 2020-12-15T09:28:13.883Z
tags: 
editor: undefined
---

# Databases
> NOTE: This page reflects the state of the system at the end of the Fall 2020 semester.{.is-info}

> NOTE: Couchbase on DB2 is stopped.{.is-info}

The aSTEP system hosts [two database servers](/servers#db1-and-db2) called `DB1` and `DB2`. The two database servers each host a PostgreSQL database manager, capable of managing multiple databases. The figure below shows the current database setup.

`DB2` additionally hosts a Couchbase database as well, but we cannot figure out how to use it nor access it, since we don't have the credentials. Somehow the Spring 2018 semester managed to reset the password though.

![databasestructure-2020-spring.png](/database/databasestructure-2020-spring.png)

*NOTE: This figure is made using https://app.diagrams.net*

## Connecting to the databases

You can connect to the databases using any PostgreSQL compatible SQL software. This could be software with a graphical interface such as [pgAdmin](https://www.pgadmin.org/download/), or directly from one of your services, perhaps using some library. It is important to know that the two database servers can only be accessed when on the AAU network or through VPN (note that all services running on aSTEP are always able to connect to any database).

If you want to access a database, you'll need to register login credentials on the PostgreSQL installation you want to access. You'll have to ask a server administrator to do this for you. To add a new user or database, you'll first have to [SSH into the relevant database server](/servers#use-ssh-to-access-server-computers) and then [access the database's command line interface](/servers#db1-and-db2). When you enter the PostgreSQL CLI, you should see a prompt along the lines of `postgres=#`. Use the following commands to create new users or databases:

- `CREATE USER [username] WITH ENCRYPTED PASSWORD '[password]';`
- `CREATE DATABASE [db_name] WITH OWNER [username];`

Once your group's user is registered and has been given the permissions it needs, you can start connecting to the database using the URLs found in the [Server Architecture figure](/servers). Both databases listen on the port `5432`. Read the documentation for the specific software/library you use in order to establish the connection. The following is an example of the information you need to access a specific database on `DB2`:

```
Host: db2-astep.cs.aau.dk
Port: 5432
Database: my_database
User: my_username
Password: my_password
```

Another way to access the databases is to use the 2019 service [db-resolver](/services/db-resolver). However, the spring 2020 semester decided against using it, since we found it a bother.

## Database contents

The following subsections lists the databases managed by each server's PostgreSQL installation. The documentation for pre-2020 databases may be lacking since this wiki was made in Spring 2020.

### The *DB1* (native) databases

Database is empty at the moment.

### The *DB1* (docker) databases (NOT RUNNING)

 - [logistics](DB1/logistics)
 - [postgres](DB1/postgres)
 - [postgrestest](DB1/postgrestest)
 - [template_postgis](DB1/template-postgis)
 - [ts1](DB1/ts1)
 - [ts2](DB1/ts2)
 
### The *DB2* databases

- [auth_db](DB2/auth_db)
- [db_stonks](DB2/db_stonks)
- [outlier_sw504e20](DB2/outlier_sw504e20)
- [driver_identification_db](DB2/driver_identification_db)
- [exoskeletonClassification2020Fall](/databases/DB2/ExoskeletonClassification2020Fall)
- [mapdata](DB2/mapdata)
- [postgres](DB2/postgres)
- [robotics_class_db](DB2/robotics_class_db)
- [solardata](DB2/solardata)
- [sw601f20_routing](DB2/sw601f20_routing)
- [sw603f19](DB2/sw603f19)
- [sw603f20](DB2/sw603f20)
- [sw604f20](DB2/sw604f20)
- [wikidb](DB2/wikidb)
