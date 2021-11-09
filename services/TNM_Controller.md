---
title: TNM Controller
description: xd
published: true
date: 2021-11-09T11:10:05.817Z
tags: 
editor: markdown
---

# Controller Description

The controller contains a static list of services and their respective URLs. These lists are used to create instances of the class *microservice*, which is later used to dynamically create UI and retrieve user preferences.

### Service abstraction and validation
Below you can see the creation of the instances of the microservices.
```python
class microservice:
	name: str
	url: str
	userPref: int
	model: str

weighterNames = ["weighterService1", "weighterService2", "weighterService3"]	
weighterURLs = ["URL1", "URL2", "URL3"]
routerNames = ["routerService1", "routerService2", "routerService3"]
routerURLs = ["URL4", "URL5", "URL6"]

serviceInfoValidation()

for idx, serviceName in enumerate(weighterNames):
		weighterServices.append(microservice(name=serviceName, url=weighterURLs[idx], userPref=None, model=None))
for idx, routerName in enumerate(routerNames):
		routerServices.append(microservice(name=routerName, url=routerURLs[idx], userPref=None, model=None))
```

*ServiceInfoValidation()* ensures that the length of the arrays are equal, i.e. there are no weigtherNames without an URL and vice versa. It also ensures that there are no duplicate URLs, as this would indicate a copy-paste error. 

### UI creation

The lists of weighterServices and routerServices are used to dynamically create UI. For each element in weighterServices a JSON object of the **field type** [```input-number```](/user-interface/fields#numeric) was created with a label containing the name of the respective service. These fields are used to input the preference of weighter service.

Next a dropdown menu of the **field type** ([```select```](/user-interface/fields#select(dropdown))) is created from routerServices. It is a dropdown menu, as it only makes sense to use a single routing method at one time. As before, for each element in routerServices an element is added to the dropdown menu. 

### Visualise Result

Once the user clicks "visualise results", it runs the *render()* function. 

It retrieves user input, those being preferences for weighter services and the chosen router.

It then validates the input, which involves the weighter preferences being positive (>=0) and summing to 1, and that chosen router is available.

It then retrieves the model from the **Creator** service, and uses multi-threading to send the model to all weighter services with a preference larger than 0. 

Once it receives all the models from the weighter services, it sends it to the **Combiner** service.

Once it receives the model from the **Combiner** service, it sends the model to the chosen router service.

The result from the router service is sent to the **UI**.







