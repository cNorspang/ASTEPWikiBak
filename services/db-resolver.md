---
title: DB-Resolver
description: This service uses GraphQL to access data from the aSTEP databases.
published: true
date: 2020-12-09T13:58:15.512Z
tags: 
editor: undefined
---

# DB-Resolver

> NOTE: This page reflects the state of the service at the end of the Spring 2020 semester.
> NOTE: This page was not created by the original creators of the service and thus does not follow the Service Documentation Standard.
{.is-info}

During the Spring 2019 semester, it was decided to make a common database-access service called "[db-resolver](https://daisy-git.cs.aau.dk/aSTEP-2019/db-resolver)". The service makes use of GraphQL, for which a cheatsheet can be found [here](https://wehavefaces.net/graphql-shorthand-notation-cheatsheet-17cd715861b6).

> The Spring 2020 semester decided not to use this service.
{.is-info}

## Running the db-resolver project locally

To run the project, either build the docker image and run it or run it locally.

Docker (example commands):

1. `docker build -t astep-2019/db-resolver .`
2. `docker run -p 5000:5000 astep-2019/db-resolver:latest`

Locally (requires [Node.js](https://nodejs.org/en/)):

1. `npm install`
2. `npm start` / `npm run dev`

Note: `npm run dev` watches for file changes, automatically restarting when they occur.

### dotenv files
[Dotenv](https://www.npmjs.com/package/dotenv) makes it easier to work with environment variables locally.
Basically, you create a file: `.env`, in which you place the relevant environment variables.

Example:
```
OSM_DATABASE=mysupersecretpassword
```

`.env` should _not_ be placed in source control, and is just a convenience for local development.
The program will also run fine without any .env file.

## Add your project to the resolver

To add your endpoints to GraphQL, follow these steps:

1. Add the types you need in the `buildSchema` function call in `app/server.js`.
2. Add your endpoints as methods in `app/resolver.js` and put them in a region, to structure the file a bit.
3. Add a connector to your database to the `app/db-connector.js` and create a client in `app/server.js`.

Remember that the id or ids are available on the class via

```js
this.id
this.ids
```

Furthermore it is required to edit the following files `db-resolver.js`, `resolver.js` and `server.js` and add data about your database for them to be integrated properly.

## Security 
The db-resolver used to be open for public queries, however, due to security concerns and NDA agreements, a token is now required. The `graphql` endpoint will only accept HTTP connections where the autorization header uses a bearer token like this:

```
"bearer supersecretetoken"
```

The token can be found in the aSTEP 2019 and 2020 GitLab groups in an enviroment variable called:

```
K8S_SECRET_DATABASE_AUTH_TOKEN
```

Add this to your new GitLab group if necessary. It will be added by GitLab during deployment so all applications can access the service, but no person besides the gitlab admin has access to the actual token thus keeping the service secure.
