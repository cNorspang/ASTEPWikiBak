---
title: WeightCompletion
description: 
published: true
date: 2020-12-19T15:42:29.723Z
tags: 
editor: undefined
---

# Weight Completion
The Weight Completion Service is an aSTEP service that was developed in fall 2020 by the group **SW502E20**.

---

**Weight Completion** is a service that uses machine learning to fill out missing weights in a road network, for a specified time interval. At the moment, the Weight Completion Service can only do weight completion in the chinese city, **Chengdu**. 

The Weight Completion service uses the algorithm [GraphCompletion](https://github.com/hujilin1229/GraphCompletion), created by Jilin Hu, Chenjuan Guo, Bin Yang and Christian S. Jensen. The algoritm was created as a part of the scientific paper **"Stochastic Weight Completion for Road Networks Using Graph Convolutional Networks"**, which can be found [here](http://people.cs.aau.dk/~byang/papers/ICDE2019-GCWC.pdf).

The Weight Completion Service creates a road network, based on the information stored in the Map Matching Service's database. To learn more about the Map Matching Service [click here](https://wiki.astep-dev.cs.aau.dk/en/services/map-matching-service-fall-2020). The road network is needed by the **GraphCompletion** algorithm, in order for it to understand how the different edges are connected with each other. These connections is represented as a adjacency matrix in the implemention of the road network. Another thing created by Weight Completion Service is a **dataframe** containing the speeds, for all the edges, for all the time intervals. The columns of the dataframe is all the edges that is a part of the road network. The rows of the dataframe is the all the different time intervals, with a 15 minutes interval. The cells contains all speeds, associated with a specific edge within a specific time interval.

All information created by the **GraphCompletion** algorithm is saved in .pickle files, stored in the service, including the results of the weight completion.

## Details/Important
If it is needed in the future to change some things in the implementation of the Weight Completion Service, it is important to note that the **GraphCompletion** algorithm was created as a part of a scientific paper, and not created to be a seperate library for others to use. This means that in order to make use of the algorithm, some changes had to be made in the source code of the algorthm, in order for it to be usable with data from the Map Matching Service.

Currently, both the creation of the road network and the dataframe with all speeds per time interval, is created as a part of the **GraphCompletion** algorithm. The reason for that the road network is created within the algorithm is that the algorithm, already contains the functionality for creating a road network in the specific form needed, based on data given to it.

It is also important to be aware of the dependencies used by the algorithm. The group had several problems with dependencies issues as the respository for the algorithm, did not contain a requirements file. The final requirements file with correct versions can be found [here](https://daisy-git.cs.aau.dk/astep-2020-fall/weightcompletion/-/blob/master/requirements.txt).

## Input
Currently, when using the Weight Completion Service, the user can select both a date and a specific time interval on that date, as input, which the user wants the road network to be weight completed within.


## Output
The output of the is in the form of the results of the **GraphCompletion** algorithm within the specified time interval, and shows it on a map, where it is possible to see the weights for each edge in the network.

## Respository
The respository for the Weight Completion Service, can be found [here](https://daisy-git.cs.aau.dk/astep-2020-fall/weightcompletion).