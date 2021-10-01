---
title: Bucketizer
description: A general bucketizer service meant for separating a data set into appropriate buckets.
published: true
date: 2020-07-11T00:24:40.376Z
tags: 
editor: undefined
---

# Bucketizer
Welcome to the Bucketizer service documentation. This service was created as a way of making a microservice to group data together. Together with the new 2020 interface this will be able to group data from any service that also follows the 2020 interface.
## Details
The bucketizer tool has been created to allow bucketization of arbitrary data submitted in JSON formats.

Three functions are available for generic data, along with seven functions specifically for time interpretation. To access these functions, a small query language has been created.


## Query language
The grammar for the query language can be found in [EBNF](https://en.wikipedia.org/wiki/Extended_Backus%E2%80%93Naur_form) form with some RegEx below:

```
start = rule {"->" rule}

rule = count_func | field_func | num_func | text_func
count_func = "count(" ( field_func | num_func | text_func ) ")"
field_func = FFNAME "(" field_spec ")"
num_func = "num(" ( field_spec | field_func ) {"," num_param} ")"
num_param = "size" INTERVAL
text_func = "text(" ( field_spec | field_func ) {"," text_param} ")"
text_param = "case" CASE
field_spec = field {"." field}
field = "\"" /[^"]+/ "\"" (* "-delimited string that does not contain " *)
     | "'" /[^']+/ "'" (* '-delimited string that does not contain ' *)
     |  /[^ ().,]+/  (* string without any whitespace, parentheses, periods or commas *)

CASE = "sensitive" | "insensitive"
INTERVAL = /[0-9]+/ (* All numbers *)
FFNAME = "year" | "month" | "day" | "weekday" | "hour" | "minute" | "second"
All whitespace in a query is ignored, unless it is part of a field name delimite by " or ' (as can be seen in the field rule in the grammar).

```

## Semantics
The grammar of the language limits most of what is allowed to be written in the language, with just a few details to explain.

### Functions

**The count function (count)** can only be used as the outermost function of a query. It will count the amount of results of the sub-query given as input.

**The numerical function (num)** is used to group results in larger buckets. This can be useful to group for example age ranges or yearly quarters.

**The textual function (text)** is used to group results that have the same textual value. This can be useful to group for example all results that are in some location or have the same options.

**The field functions (field, like year, day, hour, etc)** are used to group by some given timestamp attribute. The names of the functions indicate what attribute they group by. By default, the functions will group every distinct number, but with use of the num function, larger time ranges can be achieved.

Note that the functions require that the data found in the input field is a timestamp given as a string, in the form `%Y-%m-%dT%H:%M:%S` where:

- `%Y` is a year,
- `%m` is a month,
- `%d` is a day,
- `%H` is the hour,
- `%M` is the minute,
- `%S` is the seconds.

Any character not immediately following a percentage sign is the literal character. See examples at the bottom of the document.

The num function and text function are allowed to have any number of their optional parameters set, but only the last will be used!

The bucketizer is intended to be used with uniform data. That is, all data points should have the same fields in the same formats.

Note that field names can be in the form `"field_name"`, `'field_name'`, or just `field_name`. These can also be mixed as subfields are selected, such that `"field_1".field_2.'field_3'` would be a valid selection.

## Examples

### Query examples
`num("age", size 10)`

This query would group all data points in buckets of age `0-10`, `11-20`, `21-30`, etc.

---

`count(text("name"), case sensitive)`

This query would count how many data points there are for each name. `"name"` could be switched with any other field that exists in the data. For example, it may output `{"john": 7, "bill": 10, "BiLl": 1}`

---

`count(text(eyeColor, case insensitive))`
 
This query would count the amount of people with certain eye colors. For example, it may output `{'blue': 20, 'green': 30, 'brown': 5}`. The query is also case insensitive, so `blue` and `bLuE` would be treated the same.

---

`num(day('time'), size 7) -> num(month('time'), size 3)`

This query would group all data per week, and then per quarter. For example, this may output the following:
```JSON
"output": {
    "months1-3": {
        "days15-21": {
            "1": {
                "time":"2020-01-16T14:32:17"
            },
            "2": {
                "time":"2020-02-17T14:32:17"
            },
            "3": {
                "time":"2020-03-18T14:32:17"
            }
        }
    },
    "months4-6": {
        "days15-21": {
            "1": {
                "time":"2020-04-19T14:32:17"
            },
            "2": {
                "time":"2020-05-20T14:32:17"
            },
            "3": {
                "time":"2020-06-21T14:32:17"
            }
        }
    }
}
```

---

`text("road_name") -> num(speed, size 10) -> count(weekday('time'))`

This query would first group all data by road name. Then, it will group the data per road in increments of 10 based on their speed attribute. Finally, it will group this data for each weekday. As such, the final result would be an overview of the speeds driven on each road, on each weekday, in 10 km/h buckets.

### Ignored Parameters Examples
`num(speed, size 2, size 5, size 10, size 20)`
This is a valid query, but each size argument aside from size 20 will be ignored.

---

`text('country'.'city'.'roadname', case insensitive, case insensitive, case sensitive)`

This is a valid query, but each case argument aside from case sensitive will be ignored. The cases are not applied on a per-field-selector basis.

### Timestamp Examples
**Example 1:** `2020-04-28T14:32:17`
**Example 2:** `1980-01-01T00:00:01`
**Example 3:** `2037-01-19T03:14:08`

## Current status
The service in it's current state works as intended and so far it seems like there is no need for aditional improvements with the way aSTEP currently is. It could be neccesary to add additional extentions to the query language.

## History