# REST Services

## Exercise 33.2 
Set up a python environment that works for your platform. Provide explicit reasons why anaconda and other prepackaged python versions have issues for cloud related activities. When may you use anaconda and when should you not use anaconda. Why would you want to use pyenv?  

According to the class document Anaonda and Miniconda can or do interfere with a system's built-in python interpreters (von Laszewski et. al., p. 241).  Another argument against Anaconda is that it is a full-implementation of Python and may contain many libraries and packages that may not be needed for a project (https://unidata.github.io/online-python-training/choosing.html).  A specialized or light-weight version of Python may be the prefered starting point for a project.  The lighter version, if configured properly, will all additional libraries and packages to be added when needed.

Pyenv allows for the creation of a specialized Python development environment where the developer can add dependencies to a project on an as-needed basis.  For example, a Python project may have a requirements analysis that sets the version of python to 2.7.4 and has a requests, pytz, django as package dependencies.  Pyenv lets the developer(s) expliclity define a development virtual environment (virtualenv) that has the specified version of python and the dependencies.  Another feature is using approprate packaging techniques in a pyenv based project makes the project much more portable betweeen developers and between test/development and production systems.

## Excercise 33.3
What is the meaning and purpose of links, child, and href?  

Links is the list of endpoints available throught the web API.  Having a list of endpoints makes the different services discoverable in the API.

Child represents a resource that is available in the list of links.  A child represents an explicit resource that is available.  For example the URI https://webapi/students might be represented as a child named "students" in the list of links in an API specification.

href represenst the URI that references a specific resource or object.

## Exercise 33.4
In this case, how many child resources are available through the API?  

In the case of the Eve tutorial, there is one child resource, named student in the API.

## Exercise 33.5
Develop a REST service with Eve and start and stop it.  

## Exercise 33.6
Define curl calls to store data into the service and retrieve it.  

## Exercise 33.7
Write a Makefile and in it a target clean that cleans the data base.  Develop additional targets such as start and stop, that start and stop the mongoDB but also the Eve REST service.  

## Exercise 33.8
Issue the command curl -i http://127.0.0.1:5000/people  
What does the _links section describe?  
What does the _items section describe?  
```json
{
    "_items": [],
    "_links": {
        "self": {
            "href": "people",
            "title": "people"
        },
        "parent": {
            "href": "/",
            "title": "home"
        }
    },
    "_meta": {
        "max_results": 25,
        "total": 0,
        "page": 1
    }
}
```
## Exercise 33.9
Write a RESTful service to determine a useful piece of information off of your
computer i.e. disk space, memory, RAM, etc.  

