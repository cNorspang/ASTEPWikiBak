---
title: Field types
description: A list of all the available field types in the aSTEP user interface.
published: true
date: 2021-11-19T10:54:26.872Z
tags: fields, ui, user_
editor: markdown
---

# Field Types
> NOTE: This page reflects the state of the system at the end of the Spring 2020 semester.
{.is-info}

Just as with the [charts](/user-interface/charts), the field types are pre-defined graphical elements rendered by the UI (and not the microservice), such that services look alike. The user can input data to a microservice though these fields. For context, the [input is sent to microservices as *form-data*](/user-interface/api-standard#input-and-output-formats).

Fields are defined and sent to the UI in JSON format. There are a range of field properties that usually have the same meanings except for in certain cases. These are:

- `type` defines the type of field.
- `name` defines the field's name and is used as the form-data-key when sent to the microservice.
- `label` defines the text-value displayed just above the field in the UI.
- `default` defines the default value of the field.
- `placeholder` defines the grayed-out text displayed in the field when the user have entered no value.
- `help_text` defines the "help text" displayed in small font just below a field's input box.

---

- `options` is optional, but required when type is "select".
- `fields` is a list of subfields (so it's recursive)

Any additional properties are explained later. The following shows examples of how to define each type of field.

## Input
The 'input' field is a single-line textbox.

```json
{
  "type": "input",
  "name": "variable_name",
  "label": "My Label",
  "default": "hello world",
  "placeholder": "Input some text",
  "help_text": "Is this helpful?"
}
```
Optional: `default`, `placeholder`, `help_text`.

## Textarea
The 'textarea' field is a resizeable, multi-line textbox.

```json
{
	"type": "textarea",
	"name": "variable_name",
	"label": "My label",
  "default": "Some default input",
	"placeholder": "Input a lot of text",
  "help_text": "Is this helpful?"
}
```
Optional: `default`, `placeholder`, `help_text`.

## File
The 'file' field lets the user upload files to the microservice. Simply press "*Browse*", then navigate to and select the file to upload.

```json
{
  "type": "file",
  "name": "variable_name",
  "label": "My Label",
  "placeholder": "Input some text",
  "help_text": "Is this helpful?"
}
```
Optional: `placeholder`, `help_text`.

## Checkbox
The 'checkbox' field is a checkbox (a boolean choice).

```json
{
  "type": "checkbox",
  "name": "variable_name",
  "label": "My Label",  
  "default": "true",
  "help_text": "Is this helpful?"
}
```
Optional: `default`, `help_text`.

## Checkbox group [broken]

The 'checkbox-group' field creates a list of checkboxes that can be (un)checked individually. Since no one is using this field, it has not been maintained. Currently, the value of "*variable_name*" in the form-data will be the value of just the first checkbox in the group, which is not the intended behaviour. Later semesters may fix this, if they need this field (parhaps the value of "*variable_name*" in form-data could be the concatenation of the `name`s of the checked checkboxes).

The syntax below is the intended syntax.

```json 
(Fix here)
{
    "type": "checkbox-group",
    "name": "variable_name",
    "label": "My Label",
    "help_text": "Is this helpful?",
    "checkboxes": [list of 
        {
            "name": "group_chb_1",
            "label": "I am option",  
            "default": "true"
        }
    ]
}
```
Optional: `checkboxes[x].default`, `help_text`.

## Numeric
The 'input-number' field allows only for numerical values to be entered (integers and decimal numbers). If the value of the 'input-number' field is *not* in a proper number format, the value sent to the microservice will be the empty string.

```json
{
    "type": "input-number",
    "name": "variable_name",
    "label": "My Label",
    "default": "1234",
    "placeholder": "Input some text",
    "help_text": "Is this helpful?"
}
```
optional: `default`, `placeholder`, `help_text`.

## Select (dropdown)
The 'select' field creates a dropdown menu. The `options` property contains the list of all available options, with their display-`name` and their selection-`value`. The `value` property is the value sent to the microservice. The `default` property should refer to the `value` of one of the options.

```json
{
  "type": "select",
  "name": "variable_name",
  "label": "My Label",
  "default": "encoder_decoder",
  "help_text": "Is this helpful?",
  "options": [ 
    {
      "name": "Encoder Decoder",
      "value": "encoder_decoder"
    },
    {
      "name": "CNN",
      "value": "cnn"
    } 
  ]
}
```
optional: `default`, `help_text`.

## Select (dropdown, with sub elements)
The 'formset-select' creates a dropdown menu just like '[select](#select-dropdown)', however, depending on the selected value it will display different fields below it. The `options` property contains the list of all available options, with their display-`name`, their selection-`value`, and the list of `fields` to show when that option is selected. And yes, you can make formset-selects inside formset-selects.

```json
{
    "type": "formset-select",
    "name": "variable_name",
    "label": "My Label",
    "default": "encoder_decoder",
    "help_text": "Is this helpful?",
    "options": [ 
        {
            "name": "Encoder Decoder",
            "value": "encoder_decoder",
            "fields": [list of [field]]
        },
        {
            "name": "CNN",
            "value": "cnn",
            "fields": [
                {
                    "type": "input-number"
                    "name": "variable_name",
                    "label": "My Label",
                    "default": 1234,
                    "placeholder": "Input some text",
                }
            ]
        } 
    ]
}
```
Optional: `default`, `help_text`.

## Select (List)

The 'multi-select' field produces a list of options of which you can select one element at a time. (NOTE: You can select multiple elements, but only the first selection from the top is recorded.)

The `options` property contains the list of all available options, with their display-`name` and their selection-`value`. The `value` property is the value sent to the microservice. The `size` property sets the height of the selection field to fit exactly `size` elements.

```json
{
    "type": "multi-select",
    "name": "variable_name",
    "label": "My Label",
    "default": "opt_value",
    "size": 5,
    "help_text": "Is this helpful?",
    "options": [list of
        {
            "name": "opt_name",
            "value": "opt_value"
        }
    ]
}
```
Optional: `default`, `size`, `help_text`.

## Button [broken]
While the 'button' field does exist, it does not currently have any functionality. The syntax is:

```json
{
    "type": "button"
    "name": "variable_name",
    "label": "My Label",
    "help_text": "Is this helpful?"
}
```