---
title: TNM Controller
description: The controller service of TNM is responsable for calling all other services in TNM and linking it together
published: true
date: 2021-12-07T11:06:01.557Z
tags: 
editor: markdown
---

# TNM Controller

The controller contains a static list of services and their respective URLs. These lists are used to create instances of the class *microservice*, which is later used to dynamically create UI and retrieve user preferences.

## Service abstraction and validation
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

## Add new weighter or router
To add a new weighter or router you simply has to add it to the two corresponding lists depending on whether it is a weighter or router. The index in the two lists has to match for it to be added correctly. 


## UI creation

The lists of weighterServices and routerServices are used to dynamically create UI. For each element in weighterServices a JSON object of the **field type** [```input-number```](/user-interface/fields#numeric) was created with a label containing the name of the respective service. These fields are used to input the preference of weighter service.

Next a dropdown menu of the **field type** ([```select```](/user-interface/fields#select(dropdown))) is created from routerServices. It is a dropdown menu, as it only makes sense to use a single routing method at one time. As before, for each element in routerServices an element is added to the dropdown menu. 

## Visualise Result

Once the user clicks "visualise results", it runs the *render()* function. 

It retrieves user input, those being preferences for weighter services and the chosen router.

It then validates the input, which involves the weighter preferences being positive (>=0) and summing to 1, and that chosen router is available.

It then retrieves the model from the **Creator** service, and uses multi-threading to send the model to all weighter services with a preference larger than 0. 

Once it receives all the models from the weighter services, it sends it to the **Combiner** service.

Once it receives the model from the **Combiner** service, it sends the model to the chosen router service.

The result from the router service is sent to the **UI** and the route is drawn to a map on the UI.

## Endpoints in the controller
Here is a short explaination of the different endpoints of the controller.

#### /
The root endpoint simply just returns a string saying: "Working as intended" to say that the service is running.

#### /info
This endpoint is used by the UI for creating its entry in the UI. This endpoint returns a JSON object telling the name of the service and what category on aSTEP it belongs to.

#### /fields
This endpoint is used by the UI to create the input fields of the service. These has been made dynamic so that they change depending on the users input.

#### /render
This endpoint is called whenever the "Visualise Result" button is pressed. It is here the controller does all the heavy lifting of contacting different services and lastly returning a map with the route to the UI.

#### /readme
This endpoint simply returns the readme file located in the repository. Furthermore this file is written to the UI before the "Visualise Result" button is clicked, which is why it is used to write instructions on how to use the service.


## How to run locally
Firstly the repository for the controller has to be installed. Then the packages in the **requirements.txt** file has to be downloaded. When the packages has been downloaded, one can simple run the **service.py** file and acces the UI through this link: https://astep.cs.aau.dk/tool/localhost:5000 .
This is useful when working/tweaking with the UI, since updates can be seen much faster than if the whole gitlab pipeline has to be passed first.

## How to use the controller
The controller is the only part of TNM that interacts with the UI, and because of this it has a lot of options to represent the different services in TNM. When a user has navigated to the "Transportation Network" tab in the UI they will see the entry of this controller, which at the moment is the only entry in this section. When the controller is clicked new options will pop up together with a guide how to use the service. The UI then dynamicly changes depending on what options a user chooses. When a user is content with their input they can click the "Visualise Restult" button to activate the controller with the given parameters. The results in a map being drawn with the created route.





