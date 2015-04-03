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




