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
	$pip install -r requirements.txt
	$python
	>>from food_api import db
	>>db.create_all()
	>>quit()
	$python runserver.py


###API Documentation

Currently you can GET data from and POST data to **/api/entity**. It accepts JSON objects with the following fields with string data up to 140 characters:

* individual
* organization
* art
* intervention
* activism
* food
* water
* fuel
* non_profit
* for_profit
* b_corp
* community
* national
* local
* climate
* health
* social

The API allows clients to GET and POST to individual database tables. To query the database follow the Flask-Restless documentation:

[Flask Search Query Documentation](http://flask-restless.readthedocs.org/en/latest/searchformat.html#searchformat)




