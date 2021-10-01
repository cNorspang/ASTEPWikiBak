---
title: wikidb
description: The wikidb datbase is used by Wiki.js (this wiki) to store all information.
published: true
date: 2020-08-25T19:16:27.841Z
tags: 
editor: undefined
---

# wikidb

> NOTE: This page reflects the state of the database at the end of the Spring 2020 semester.
{.is-info}

The `wikidb` database from the `DB2` database server contains about 30 mostly self-explanatory tables. These tables stores information about pages, users, assets, settings, and any other type of information related to the aSTEP wiki. These tables will not be documented here since the database is made automatically by third-party software, and since there are too many.

The wiki database and the current installation of Wiki.js are two separate entities, allowing for the current verison of Wiki.js to be swapped for a newer version without affecting the database (except what the updated version does to the database upon launch). A guide to updating/reinstalling the wiki can be found [here](/servers#how-to-updatereinstall-the-wiki).
