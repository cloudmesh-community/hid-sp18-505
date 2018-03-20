# GraphQL
Advanced Cloud Computing  
Indiana University Data Science Program  
Spring 2018  
Averill Cate, Jr

## Introduction
The purpose of this tutorial is to provide an example of using GraphQL as a 
mechanism for creating and developing web APIs.

This tutorial has a few software requirements.  The following is the list of 
the software needed to complete the tutorial.  Installation of all of the tools 
or software libraries will not be covered in this tutorial.  It will be the 
reader's responsibility to install some of the software packages like python.  
However, the tutorial will provide guidance for installing the packages that 
is in the tutorial's application code.

## Required Software

+ python 3.x&#42;  
+ pyenv&#42;  
+ pyenv virtualenv  
+ graphene  
+ flask  
+ json server  
+ pip&#42;  
+ git&#42;  
+ docker&#42;  
+ text editor&#42;  

^* = installation not covered in the tutorial

## Assumptions

+ User knows how to work at the command line.
+ User has installed python 3+
+ User has installed and configured pyenv
+ User has installed and knows how to use a text editor like emacs, or vscode.
+ Working on a Unix/Linux/OSX based operating system.
+ User has a .bashrc (using bash shell)

## Steps/Procedures

1. Install python 3.x - Assumed to have been completely by the user.
2. Install pyenv - Assumed to have been completely by the user.
3. Create virtualenv for tutorial

The preferred method for developing python based projects is to use a separate environment for each python project.  There are several ways to accomplish this.  The first is by creating a docker image and container for the project.  This is recommended, but not covered in this tutorial.  The second method is by installing and using pyenv's virtualenv plugin, this assumes the user has already installed and configured pyenv.

## Using Virtualenv

First, access the command line. Next, install pyenv-virtualenv while following the instructions provided at 

* <https://github.com/pyenv/pyenv-virtualenv>

Or better, use our handbook and follow the instructions provided there. At the command prompt type:

	git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
	echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
	exec "$SHELL"
	pyenv virtualenv graphqltut

We now have a python virtualenv that is specifically for this project.

## Installing Graphql

Before we start we create a a project folder and cd into it

	mkdir ~/cloudmesh/graphql

The tutorial has a few python library dependencies.  We need to install those dependencies into the python virtualenv we created.

At the command prompt type 

	pyenv activate graphqltut 
	
This makes sure we are using the local python  development virtualenv and not the global python environment. Now Type 

	pip freeze 

which should *not* display a list of libraries since our virtualenv was just created.  
We do this step to make sure you do not overwrite or modify your default python environment. Now install flask and graohene:

	pip install flask  
	pip install graphene  
	pip install flask-graphql

We now have the minimum environment to build a Python GraphQL server and client.  One last step though.  It is a good idea to keep track of Python dependencies as we install them.  To do that, at the command line type:  

	pip freeze > requirements.text

This command saves the list of libraries we have installed plus the depdencies of the libraries we installed.  If for some reason you need to re-create 
the python virtualenv or someone else does then once the virtualenv is created the python libraries are easily re-installed my issued the command:

	pip install -r requirements.txt

## Build a graphql Application
Create and open a file namee run.py.  This will be a very simple application server that runs the demo application.  

Now import the dependencies that we installed using pip.

	# File: run.py
	from flask import Flask
	from graphene import ObjectType, String, Schema
	from flask_graphql import GraphQLView

	class Query(ObjectType):
		status = String(description='Check graphql service status')
		def resolve_hello(self, args, context, info):
			return 'OK'

	view_func = GraphQLView.as_view('graphql', schema=Schema(query=Query))

	app = Flask(__name__)
	app.add_url_rule('/', view_func=view_func)

	if __name__ == '__main__':
		app.run()

	Ref: #1

## Explore the Data
Show the graphql explorer

## References
1. Graphql Site - https://bcb.github.io/graphql/flask

* Look in resources section of project README.md and include sites that discuss justifications for grapql
