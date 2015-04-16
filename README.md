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

Currently you can GET data from and POST data to **/api/entity**. It will accept the following fields in JSON format:

* individual: "String",
* organization: "String",
* art: "String",
* intervention: "String",
* activism: "String",
* food: "String",
* water: "String",
* fuel: "String",
* non_profit: "String",
* for_profit: "String",
* b_corp: "String",
* community: "String",
* national: "String",
* local: "String",
* climate: "String",
* health: "String",
* social: "String"

The API allows clients to GET and POST to individual database tables. To query the database follow the Flask-Restless documentation:

[Flask Search Query Documentation](http://flask-restless.readthedocs.org/en/latest/searchformat.html#searchformat)




