# No Free Lunch API

###Running server locally

These instructions are for Mac OSX.

If you don't have Python virtual environments installed run:

	pip install virtualenv

If you don't have pip installed:
	
	sudo easy_install pip

Once you have virtual environments installed, you're ready to setup the server!
	

	$git clone https://github.com/aankit/food_api
	$cd food_api
	$virtualenv venv
	$source venv/bin/activate
	$python
	>>from food_api import db
	>>db.create_all()
	>>quit()
	$python runserver.py


###API Documentation

The backend is currently using Flask, SQL Alchmey, SQLite, and Flask-Restless to create the API interface. The API allows clients to GET and POST to individual database tables. The endpoints are:

/api/food
/api/water
/api/environment
/api/social
/api/policy
/api/fuel

The database is centered on food - meaning each one of the tables at the non-food endpoints can be related to a food, but not to each other. This can be changed easily, but for now this change is pending specific feedback from users.



