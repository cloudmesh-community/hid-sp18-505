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
Create and open a file named app.py.  This will be a very simple application server that runs the demo application.  

Now import the dependencies that we installed using pip.

	# File: app.py
	from flask import Flask
	from graphene import ObjectType, String, Schema
	from flask_graphql import GraphQLView

	class Query(ObjectType):
		status = String(description='Check graphql service status')
		def resolve_hello(self, args, context, info):
			return 'OK'

	view_func = GraphQLView.as_view('graphql', schema=Schema(query=Query))

	app = Flask(__name__)
	app.add_url_rule('/graphql', view_func=view_func)

	@app.route('/')
	def index():
		return 'Hello!'

	if __name__ == '__main__':
		app.run(debug=True)

	Ref: #1

If you copy and paste the code in app.py then you will have to make sure that the file has proper python indenting, otherwise 
app.py will not run.

Let's test to make sure the server application will run.  Access the command prompt in the project folder 
and type ```python app.py```.

The flask application should display information to the console that an application server has been started 
on a local IP address and the server is listening on the default port, 5000.

Open a web browser and connect to http://127.0.0.1:5000.  The browser should render a web page that displays
the message "Hello!"

We have already enabled the GraphQL endpoint by have the line in app.py that starts with "view_func".  Let's 
confirm that the GraphQL query-builder user interface is working by browsing opening the url 
http://127.0.0.1:5000/graphql in a browser window.

The resulting user interface (UI) lets a user develop and test QraphQL queries against the server created in app.py. The GraphQL 
UI has to panes.  The left pane is used to create a query and the 
right pane displays the query output.  A query can be executed by 
clicking the right-arrow (Run) button near the top of the UI.

Let's build and run our first query.
1. Click in the left pane
2. Type "{" and press the Enter key
3. Press the Control/Command key and the space bar at the same time.  This activates the UI's autocomplete feature.  The autocomplete feature knows about the query schema and can make it easier for the user to develop a query.
4. The autocomplete will display the word "status".  Highlight the status word and press the Enter key.  The query should look similar to the follwoing:
```
{
  status
}
```
5. Click the Run button.  The query will run and display output that looks similar to the following:
```
{
  "data": {
    "status": "OK"
  }
}
```

## Explore the Data
Show the graphql explorer

## References
1. Graphql Site - https://bcb.github.io/graphql/flask

* Look in resources section of project README.md and include sites that discuss justifications for grapql
