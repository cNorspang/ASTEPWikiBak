---
title: aSTEP Python Template
description: 
published: true
date: 2021-12-19T22:12:14.916Z
tags: 
editor: markdown
---

# Python Template Service
This is a template for building a microservice compatible with the aSTEP infrastructure, in which it has implemented the starting points following the RFCs approved by aSTEP.

Currently, many of the RFCs are not properly documented or have confusing explanations. As such, this template tries to be as close to the idea behind the RFCs, but some work would be needed to make them fully compatible.
## Where to get this template
The Python TNM Template can be found at Gitlab: https://daisy-git.cs.aau.dk/astep-2021/pythontemplateservice 

## How to use
To use this service, simply clone it onto your local computer. Then either remove the (typically hidden) `.git` file, or copy paste the code into a new folder (without the `.git` file), and create a new repository on GitLab to push the code to.

## How to understand the template
The template consist of these:

- A `service.py` file, specifying all the endpoints which the service makes available.
- A `.gitignore` file, preconfigured to ignore standard python files, which should not be on GitLab.
- A `.gitlab-ci.yml` file, which runs all the configuration code for the code to be pushed to Kubernetes.
- A `Dockerfile`, which builds the program image that runs on Kubernetes. Has included a Continious Integration workflow, specifying that all tests should pass for the container to be build.
- A `README.md` file that you read right now
- A `requirements.txt` file, specifying all dependencies which will be installed as part of running the `Dockerfile`
- A `/src` folder having all application code.
- In `/src`, the `__init__.py` file signifies to python that the folder is a python module (making it possible to import/export between files in the folder)
- In `/src`, the `main.py` file has the main function, which run when calling the `/data` endpoint. It should always begin with calling the `adapter.from_json()` method, and returning the `adapter.to_json()` method.
- In `/src`, the `adapter.py` file handles the logic of deserializing the received json to some internal python representation (`from_json()`), and then serializing the internal representation back to some valid json (`to_json()`).
- In `/src`, the `/__pytest__` folder handles all the testing of the microservice, using `pytest` as the framework. 
- In `/src/__pytest__` The `conftest.py` file signifies that `/__pytest__` is a testing folder, similar to `__init__.py` signifying module folders, making it possible to test. It also holds all the fixtures that can be used by all test functions.
- in `/src/__pytest__` The `test_main.py` file holds integration tests for the whole microservice as called on the application level. It initially only tests that the json that comes in, also comes out again.
- In `/src/__pytest__` The `test_adapter.py` file holds all tests for the adapter. For pytest to register tests, all files should be named `test_*.py`. It initially holds some testcode to show pytest functionality.

# Your Service Name
Delete the text above "Your Service Name" and thereafter replace any information which is different from your service and the template in the text below.

Write some introduction, and reference what RFC, product or similar this service supports.

## Content
- [What it does](#what-it-does)
- [How to run it](#how-to-run-it)
- [Input](#input)
- [Output](#output)
- [Endpoints](#endpoints)

## What it does
Describe what it does in such a detail, such that a person who have no context can understand your service (such as the semester coming right after you)

## How to run it
### Run local
To run the code locally,first install docker, and then cd into the service folder, and write

- `docker build --tag your_name .`
The build command runs all tests and if the tests succeed it produces a docker image called your_name

- `docker run -p 5001:5000 your_name`
this function runs the image.

The service will then run on `localhost:5001/` in your browser, as a docker container with the name your_name.

### Run on local ui
To try the UI of this template run the UI locally:
wiki documentation: https://wiki.astep-dev.cs.aau.dk/services/user-interface#how-to-run-the-ui-locally for the latest info.


Git clone the userinterface-21 repo 
```shell
git clone git@daisy-git.cs.aau.dk:astep-2021/userinterface-21.git
```
dc to the destination where you cloned the userinterface-21 repo
start up docker desktop.
from the terminal build the dockerimage from the Dockerfile in the repo and run it:
```shell
docker build -t uiapp --build-arg LARAVEL_CLIENT_ID=<client> --build-arg LARAVEL_CLIENT_SECRET=<secret> .
```
the CLIENT_ID and LARAVEL_CLIENT_SECRET can be found here: https://daisy-git.cs.aau.dk/astep-2020/UserInterface/-/blob/master/app/src/environments/environment.ts

let the image build, then run the dockerimage:
```shell
docker run -it --rm -p 5040:5000 --name my_app uiapp:latest  
```

when the ui is running start your service:
cd to your service folder and write in the terminal:
```shell
docker build --tag your_name .
docker run -p 5001:5000 your_name
```

to display your service open a browser on the following url:
- `http://localhost:5040/tool/localhost:5001/`

the first part is the ui service
- `localhost:5040/tool`

and the last part is your service:
- `localhost:5001/`


### Run on aSTEP
To run the code on the aSTEP servers, go to Gitlab and in your project, find the CI/CD option and go to Pipeline. Then run the pipeline, which will make sure the `Dockerfile` and `.gitlab-ci.yml` file is run, building the image and pushing it to Kubernetes.

When viewing the pipeline, if the build goes through, the review step will show which url exposes the service.

### Install dependencies
To add new libraries to the `requirements.txt` folder, either just add the libraries following the notation in the `requirements.txt` folder, or create a virtual environment, where you activate the environment, cd into the service folder and then run
- `pip install -r requirements.txt`
- `pip install your_package1, your_package2, ... your_packageN`
- `pip freeze > requirements.txt`

The old dependencies, as well as the new ones, should be in the new `requirements.txt` file, as well as any needed supplementary dependencies.

### Add tests
All tests will run, which are written in files named `test_some_name.py`
All functions in those files, which have a name `test_your_function()` will run as part of the test.
There are examples in `test_main.py` and `test_adapter.py` in the `src/__pytest__` folder. These give examples of a simple test, how to use parametrization (using the same test suite, testing with different values) and mocking (replacing dependencies, to better isolate implementation code)

## Input
Make a presentation of valid input to the service on json format.

```json
{
	"example":{
  	"json": True
  }
}
```

## Output
Make a presentation of valid output to the service on json format.

```json
{
	"example":{
  	"json": True
  }
}
```

## Endpoints

### [service url]/ 
The default endpoint can be used to check if the service is accessible.
```python 
@service.route("/")   
def hello():
    return "Hello aSTEP! Python template service at your service"
```


### [service url]/info
The info endpoint places the microservice in the Ui in the leftmost column. -1 places it in the "Other" category where as Category 4 places it in the "Transportation Network" category. 
```python
@service.route('/info')
def info():
    return jsonify({
		'id': 'TNM-python-template',       #the identifyer, allows name and identifyer to be different 
		'name': 'TNM-python-template',     #the displayed name
		'version': '2020v1',               #this is the UI version
		'category': -1                     #this selects what section in the leftmost menu will contain the microservice -1,0,1,2,3,4 (4:Transportation network)
	})
 ```


### [service url]/readme
The readme endpoint displays the README.md file in the content view in the rightmost view. It is called by the UI when the service is initially called, and when the info button is clicked
```python
@service.route("/readme")
def readme():
    with open('README.md', 'r+') as file : 
	    content = file.read()
    return jsonify({'chart_type': 'markdown', 'content': content})
```


   
### [service url]/fields
The Fields endpoint represents the input of the service. This is where input "parameters" are specified and named. this is displayed in the middle column by the UI
the userFields array can contain any of the predefined input fields described in the wiki under User interface.
```python
@service.route('/fields')
def fields():
	return jsonify({
		'user_fields': [
            {
				'type': 'input-number',
                'name': 'number1',
				'label': 'input nr 1',
				'default': '0',
			},
			{
				'type': 'input-number',
                'name': 'number2',
				'label': 'input nr 2',
				'default': '0',
			},
            {
				'type': 'input-number',
                'name': 'number3',
				'label': 'input nr 3',
				'default': '0',
			},
		],
		'developer_fields': [
		]
	})
```
### [service url]/render
The Render endpoint is called when the "Visualize results" button is clicked, the return value is displayed in the rightmost area of the UI. This is where you handle the data processing
```python
@service.route('/render', methods=['GET', 'POST'])
def render():
	number1 = request.form.get('number1','0')    #number1 is the name attribute used in the /fields userfields name: 'number1',  the 0 is the default value if number1 is null.
    number2 = request.form.get('number2','0')
    number3 = request.form.get('number3','0')
    
	#this is how to call a service url, the url is a url generated by the CI/CD  and can be found in gitlabs CI/CD log when building a microservice.
    #model = requests.get("http://astep-2021-tnn-creator-service-review-limit-mtlaqb.astep-dev.cs.aau.dk/main")   #if you want to pass data (.../main, add data=[somejson] )   
    #contentOfRender =  model.content

    contentOfRender['content']=int(number1)+int(number2)+int(number3)
    print(contentOfRender)
    #contentOfRender.append(content)

    # render has to return one of the predefined charts. Charts are described in the wiki: 
	return {
		'chart_type': 'markdown',
		'content':  f'result was: {str(contentOfRender)}'
	}
 ```

### [service url]/data
The data endpoint is expected to return a json with the last rendered result.
```python
@service.route("/data", methods=['GET', 'POST'])
def master():
    return contentOfRender
 ```


### [service url]/dosomething
You can add other endpoints and implement what ever functionality you'd like
```python
@service.route("/dosomething", methods=['GET', 'POST'])
def dosomething():
    data = request.json
    if not data:
        data = json.dumps("The url was called with no arguments")
    return main(data) 
 ```
