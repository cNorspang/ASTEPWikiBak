---
title: python36 ASTEP form utils
description: Module for easily integrating the aSTEP 2019 form area into a flask micro-service, and utilizing different tools without duplicating code.
published: true
date: 2020-08-26T20:29:17.474Z
tags: 
editor: undefined
---

Module helps with generating field sets and fields for usage in the architecture
aSTEP-2019 (At Aalborg Uversity). This can be used for any service written in flask, to make sure you don't 
create too much duplicate code. it's strongly inspired by Django. 
> NOTE: This libary isn't compatible with notebook.
{.is-warning}

## Supported versions
Python >=3.5

## Example
Create an instance of `FieldSet` which handles the different fields 
both visualized in the `/fields/` endpoint as well as verified with `/render/`

An example with with basis in fields could be:

```python
from astep_form_utils import FieldSet, StringField, FloatField
from flask import Flask, jsonify

app = Flask(__name__, static_url_path="")

@app.route("/fields")
def fields():
    field_set = FieldSet(
        StringField("my_name", label="Input Your Name:"),
        FloatField("my_age", label="Input Your Age:")
    )
    return jsonify(field_set.as_form_fields())
```

which will return json as follows: 
```json
[
  {
    "label": "Input Your Name:",
    "name": "my_name",
    "type": "input"
  },
  {
    "label": "Input Your Age:",
    "name": "my_age",
    "type": "input-number"
  }
]
```

You can also use enums:

```
from astep_form_utils import FieldSet, EnumField
from enum import Enum

class MyModel(Enum):
    PRETTY_MODEL = auto()
    UGLY_MODEL = auto()

field_set = FieldSet(
    EnumField("my_string", MyModel, label="Pick a model")
)
```
'

You can use a fieldset in your `/render/` endpoint as well, to validate data:


```python
from astep_form_utils import FieldSet, StringField, FloatField, is_data_empty
from flask import Flask, jsonify, request

app = Flask(__name__, static_url_path="")

@app.route("/render")
def render():
    field_set = FieldSet(
        StringField("my_name", label="Input Your Name:"),
        FloatField("my_age", label="Input Your Age:")
    )
    

    if is_data_empty(request):
        return jsonify({'chart_type':'text', 'content':'Supply data please!'})

    if field_set.is_valid(request):
        my_name = field_set.cleaned_data['my_name']
        my_age = field_set.cleaned_data['my_age']
        
        return jsonify({
            'chart_type':'text',
            'content':f'Hello my name is {my_name} and i am {my_age} years old.'
        })
```

To make it more DRY and reuse the FieldSet definition, you can utilize the factory
function `field_set_factory`, to reuse the same definition like this:

```python

from astep_form_utils import StringField, FloatField, \
    is_data_empty, field_set_factory
from flask import Flask, jsonify, request

app = Flask(__name__, static_url_path="")
# returns a method that creates a FieldSet with the two fields
FIELD_SET_FACTORY = field_set_factory(
        StringField("my_name", label="Input Your Name:"),
        FloatField("my_age", label="Input Your Age:")
)
@app.route("/render")
def render():
    # Creates a fieldset with the defined fields
    field_set =  FIELD_SET_FACTORY()

    if is_data_empty(request):
        return jsonify({'chart_type':'text', 'content':'Supply data please!'})

    if field_set.is_valid(request):
        my_name = field_set.cleaned_data['my_name']
        my_age = field_set.cleaned_data['my_age']
        
        return jsonify({
            'chart_type':'text',
            'content':f'Hello my name is {my_name} and i am {my_age} years old.'
        })
        
    raise NotImplementedError()
         
@app.route("/fields")
def fields():
    field_set = FIELD_SET_FACTORY() 
    return jsonify(field_set.as_form_fields())
```

A complete solution can be found in the
implementation of the [chart type test](https://daisy-git.cs.aau.dk/aSTEP-2019/charttypetest/)
microservice. 


