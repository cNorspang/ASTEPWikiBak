---
title: Echelon
description: The service "Echelon" is a speech-to-text tool, which - using MI - can subtitle audio-files. It was created by group SW614F19 during the Spring 2019 semester.
published: true
date: 2020-12-09T13:24:24.040Z
tags: 
editor: undefined
---

# Echelon

> NOTE: This page reflects the state of the service at the end of the Spring 2020 semester.
> NOTE: This page was not created by the original creators of the service and thus does not follow the Service Documentation Standard.
> NOTE: We have, as of the end of Spring 2020, been unable to make the service function. It might be broken.
> NOTE: The Gitlab repository is not accessible unless you are a maintainer for Spring 2019
{.is-info}

The **Echelon** service was made by the group *SW614F19* during the Spring 2019 semester. The purpose of the service is to take audio files, and put them through a speech-recognition package in order to create a textual representation of the file's contents, which can be read by hearing-impaired people.

## Details
In order to perform the speech-to-text conversion, the service makes use of a machine learning technique called *Deep Speech*, based on a [paper](https://arxiv.org/abs/1412.5567) written by researchers at *Baidu Research*. Specifically, the service uses Mozilla's open-souce [`DeepSpeech`](https://github.com/mozilla/DeepSpeech) engine. This engine also includes a pre-trained English-language model.
> The "DeepSpeech" implementation makes use of Google's *TensorFlow*.
{.is-info}

The service already utilizes predetermined audio files, which means the input data is also predetermined. The service does require you to choose a model, as well as which dataset to use. The output is text which is deciphered from the audio files.

The service is written in Python, and the repository containing the code can be found [here](https://daisy-git.cs.aau.dk/aSTEP-2019/sw614f19).