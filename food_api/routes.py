from flask import render_template
from food_api import app

# routing for API endpoints (generated from the models designated as API_MODELS)
from food_api import api_manager
from food_api.models import *

for model_name in app.config['API_MODELS']:
	model_class = app.config['API_MODELS'][model_name]
	api_manager.create_api(model_class, methods=['GET', 'POST'])

@app.route('/')
def add():
	return render_template('index.html')

@app.route('/about')
def about():
	return render_template('about.html')