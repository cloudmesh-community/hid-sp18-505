# GraphQL
\label{s:graphql}
\index{GraphQL}

Advanced Cloud Computing  
Indiana University Data Science Program  
Spring 2018  

## Introduction

We are in the information age.  Possibly, the information overload age.
Regradless, information or data are the commodity of this technological era.
Given that a significant number, if not most of the world's industries are
dependent on the internet and the exchange of data it is probably safe to
assume that how the data are exchanged is an important thing to understand.
It is probably import to also understand how the exchange mechanisms have been
changing over time.

In the early 2000s, Simple Object Access Protocol (SOAP) based web services 
emerged as the preferred mechanism for exchanging data electronically.  
Typically, SOAP was data exchange the protocol and eXtensible Markup Language 
(XML) was the data format.

Web services, why, history, soap/xml, rest/json, graphql, others...

The purpose of this tutorial is to provide an example of using GraphQL as a 
mechanism for creating and developing web APIs.

This tutorial has a few software requirements.  The following is the list of 
the software needed to complete the tutorial.  Installation of all of the tools 
or software libraries will not be covered in this tutorial.  It will be the 
reader's responsibility to install some of the software packages like python.  
However, the tutorial will provide guidance for installing the packages that 
is in the tutorial's application code.

## Required Software

+ python 3.x^*  
+ pyenv^*  
+ pyenv virtualenv  
+ graphene  
+ flask  
+ json server  
+ pip^*  
+ git^*  
+ docker^*  
+ text editor^*  

## Assumptions

+ User knows how to work at the command line.
+ User has installed python 3+
+ User has installed and configured pyenv
+ User has installed and knows how to use a text editor like emacs, or vscode.
+ Working on a Unix/Linux/OSX based operating system.
+ User has a .bashrc (using bash shell)

^* = installation not covered in the tutorial

## Steps/Procedures

1. Install python 3.x - Assumed to have been completely by the user.
2. Install pyenv - Assumed to have been completely by the user.
3. Create virtualenv for tutorial

The preferred method for developing python based projects is to use a separate environment for each python project.  There are several ways to accomplish this.  The first is by creating a docker image and container for the project.  This is recommended, but not covered in this tutorial.  The second method is by installing and using pyenv's virtualenv plugin, this assumes the user has already installed and configured pyenv.

**GVL: DO NOT USE NUMBERS HERE AS SECTION NUMBERS MUST STAY VARIABLE**

## Using Virtualenv

First Access the command line. Next, install pyenv-virtualenv while following the instructions provided at 

* <https://github.com/pyenv/pyenv-virtualenv>

Or better use our handbook and follow the instructions provided there. At the command prompt type:

	git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
	echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
	exec "$SHELL"
	pyenv virtualenv graphqltut

We now have a python virtualenv that is specifically for this project.

## Installing Graphql

Before we start we create a a project folder and cd into it

	mkdir ~/cloudmesh/graphql

The tutorial has a few python library dependencies.  We need to install those dependencies into the python virtualenv we created.

At the command prompt: 

1. Type pyenv activate graphqltut (this makes sure we are using the local python  development virtualenv and not the global python environment)  

2. Type pip freeze -- this should *not* display a list of libraries since our virtualenv was just created.  

Now install flask and graohene:

	pip install flask  
	pip install graphene  

We now have the minimum environment to build a Python GraphQL server and client.  One last step though.  It is a good idea to keep track of 
Python dependencies as we install them.  To do that, at the command line type:  

	pip freeze > requirements.text

This command saves the list of libraries we have installed plus the depdencies of the libraries we installed.  If for some reason you need to re-create 
the python virtualenv or someone else does then once the virtualenv is created the python libraries are easily re-installed my issued the command:

	pip install -r requirements.txt

7. Build the server.py/app.py file

8. Show the graphql explorer



## References/Citations

Graphql site
Look in resources section of project README.md and include sites that discuss justifications for grapql

## Optional

liquidprompt
