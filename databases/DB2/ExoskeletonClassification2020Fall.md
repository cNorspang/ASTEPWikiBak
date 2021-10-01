---
title: Exoskeleton Classification 2020 Fall db
description: This page describes which tables and what data the database contains
published: true
date: 2020-12-17T10:19:44.859Z
tags: 
editor: undefined
---

# Exoskeleton Classification 2020 Fall DB
This page describes which tables the Exoskeletion Classification 2020 fall database contains and what data is in them. This database is used by the [Exoskeleton Classifier](/services/ExoskeletonClassifier) service.

---
## Tables
The database contains 1 table named "datasets", this table contains the following columns:

<div style="overflow-x:auto;">
<table border="4px solid #000" overflow-x:="auto" class="a">
  <tr>
		<th>id</th>
    <th>data</th>
    <th>name</th>
  </tr>
</table>
</div>

Id is an integer, name is a varchar(128), and data is text.

### Contents of the database
The database contains 4 datasets, and among these, 3 datasets contain labels, and 1 doesn't. They are stored as ZIP files to improve performance when querying the larger datasets from a service.