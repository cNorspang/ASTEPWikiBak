---
title: robotics_class_db
description: The robotics_class_db is a database stored on the DB2 server computer. It is not currently known which services (if any, anymore) makes use of it.
published: true
date: 2020-08-31T12:24:38.635Z
tags: 
editor: undefined
---

# robotics_class_db

> NOTE: This page reflects the state of the database at the end of the Spring 2020 semester.
> NOTE: This page was not created by the original creators of the database.
> NOTE: What services (if any) that use the database is currently unknown. Any information on this page is therefore assumed.
> <span style="color:red">NOTE: This page was HELL to document due to the sheer lack of actual use of its content. Both this page and what it documents are worth less than nothing. It literally was a WASTE of time :tired_face:</span>.

{.is-info}

The *robotics_class_db* is a database stored on the DB2 server. It is not currently known which services (and therefore, which corresponding reports) use the service.

The database contains 6 schemas:

- _timescaledb_cache
- _timecaledb_catalog
- _timecaledb_config
- _timecaledb_internal
- public
- timescaledb_information

## _timescaledb_cache

This schema contains 3 tables:

- cache_inval_bgw_job
  - Contains no columns or rows
- cache_inval_extension
  - Contains no columns or rows
- cache_inval_hypertable
  - Contains no columns or rows



## _timecaledb_catalog

The schema contains 8 tables:

- chunk
  - Contains no rows, but has four columns.
    - <u>id</u> of type INTEGER
    - hypertable_id of type INTEGER
    - schema_name of type name
    - table_name of type name.
- chunk_constraint
  - Contains no rows, but has four columns.
    - chunk_id of type INTEGER
    - dimension_slice_id of type INTEGER
    - constraint_name of type name
    - hypertable_constraint_name of type name.
- chunk_index
  - Contains no rows, but has four columns.
    - chunk_id of type INTEGER
    - index_name of type name
    - hypertable_id of type INTEGER
    - hypertable_index_name of type name
- dimension
- dimension_slide
  - Contains no rows, but has four columns.
    - <u>id</u> of type INTEGER
    - dimension_id of type INTEGER
    - range_start of type BIGINT
    - range_end of type BIGINT
- hypertable
- installation_metadata
- tablespace
  - Contains no rows, but has three columns
    - <u>id</u> of type INTEGER
    - hypertable_id of type INTEGER
    - tablespace_name of type name

###### hypertable

This table has 9 columns.

| Column name              | Type     | Explanation       |
| ------------------------ | -------- | ----------------- |
| <u>id</u>                | INTEGER  | Unique identifier |
| hypertable_id            | INTEGER  | Unknown           |
| column_name              | name     | Unknown           |
| column_type              | REGTYPE  | Unknown           |
| aligned                  | BOOLEAN  | Unknown           |
| num_slices               | SMALLINT | Unknown           |
| partitioning_func_schema | name     | Unknown           |
| partitioning_func        | name     | Unknown           |
| interval_length          | BIGINT   | Unknown           |

###### hypertable

This table has 9 columns.

| Column name              | Type     | Explanation       |
| ------------------------ | -------- | ----------------- |
| <u>id</u>                | INTEGER  | Unique identifier |
| schema_name              | name     | Unknown           |
| table_name               | name     | Unknown           |
| associated_schema_name   | name     | Unknown           |
| associated_table_prefix  | name     | Unknown           |
| num_dimensions           | SMALLINT | Unknown           |
| chunk_sizing_func_schema | name     | Unknown           |
| chunk_sizing_func_name   | name     | Unknown           |
| chunk_target_size        | BIGINT   | Unknown           |



###### installation_metadata

This table contains 2 columns.

| Column name | Type | explanation       |
| ----------- | ---- | ----------------- |
| <u>key</u>  | name | Unique identifier |
| value       | Text | Unknown           |



## _timecaledb_config

This schema contains 3 tables:

- bgw_job
- bgw_policy_drop_chunks
  - Contains no rows, but has 4 columns.
    - <u>job_id</u> of type INTEGER
    - hypertable_id of type INTEGER
    - older_than of type INTERVAL
    - cascade of type BOOLEAN
- bgw_policy_reorder
  - Contains no rows, but has 3 columns.
    - <u>job_id</u> of type INTEGER
    - hypertable_id of type INTEGER
    - hypertable_index_name of type name

###### bgw_job

This table has 7 columns.

| Column name       | Type     | Explanation       |
| ----------------- | -------- | ----------------- |
| <u>id</u>         | INTEGER  | Unique identifier |
| application_name  | name     | Unknown           |
| job_type          | name     | Unknown           |
| schedule_interval | INTERVAL | Unknown           |
| max_runtime       | INTERVAL | Unknown           |
| max_retries       | INTEGER  | Unknown           |
| retry_period      | INTERVAL | Unknown           |



## _timecaledb_internal

This schema contains two tables:

- bgw_job_stat
- bgw_policy_chunk_stats
  - Contains no rows, but has four columns.
    - job_id of type INTEGER
    - chunk_id of type INTEGER
    - num_times_job_run of type INTEGER
    - last_time_job_run of type timestamp with time zone

###### bgw_job_stat

This table contains 12 columns.

| Column name          | Type                     | Explanation       |
| -------------------- | ------------------------ | ----------------- |
| job_id               | INTEGER                  | Unique identifier |
| last_start           | timestamp with time zone | unknown           |
| last_finish          | timestamp with time zone | unknown           |
| next_start           | timestamp with time zone | unknown           |
| last_run_success     | BOOLEAN                  | unknown           |
| total_runs           | BIGINT                   | unknown           |
| total_duration       | INTERVAL                 | unknown           |
| total_successes      | BIGINT                   | unknown           |
| total_failures       | BIGINT                   | unknown           |
| total_crashes        | BIGINT                   | unknown           |
| consecutive_failures | INTEGER                  | unknown           |
| consecutive_crashes  | INTEGER                  | unknown           |



## public

This schema contains 7 tables, none of which contains any rows:

- datacollection
  - Contains no rows, but has 4 columns.
    - <u>id</u> of type INTEGER
    - collectiondate of type timestamp without time zone
    - subjectid of type INTEGER
    - frequency of type NUMERIC
- measurement
  - Contains no rows, but has 15 columns.
- model
  - Contains no rows, but has nine columns.
    - <u>id</u> of type INTEGER
    - modeltype of type CHARVAR
    - trainedon of type INTEGER
    - datetrained of type timestamp without time zone
    - model of type TEXT
    - datatype of type TEXT
    - windowlength of type INTEGER
    - sensors of type TEXT[]
    - features of type TEXT[]
- normalbounds
  - Contains no rows, but has four columns.
    - <u>sensorid</u> of type INTEGER
    - <u>colid</u> of type INTEGER
    - lowerbound of type numeric
    - upperbound of type numeric
- subject
  - Contains no rows, but has four columns.
    - <u>id</u> of type INTEGER
    - age of type INTEGER
    - weight of type NUMERIC
    - height of type NUMERIC
- tested
  - Contains no rows, but has six columns.
    - <u>id</u> of type INTEGER
    - modelid of type INTEGER
    - testedon of  type INTEGER
    - datatested of type timestamp without time zone
    - resultsum of type text
    - score of type DOUBLE PRECISION
- testresult
  - Contains no rows, but has four columns.
    - <u>id</u> of type INTEGER
    - <u>testid</u> of type INTEGER
    - classification of type VARCHAR
    - label of type VARCHAR

## timescaledb_information

This schema contains no tables.