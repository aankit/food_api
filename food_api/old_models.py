from food_api import app
from food_api import db

#secondary tables
food_environments = db.Table('food_environments', db.Model.metadata,
    db.Column('food_id', db.Integer, db.ForeignKey('food.id'), nullable=False),
    db.Column('environment_id', db.Integer, db.ForeignKey('environment.id'), nullable=False))

food_social_groups = db.Table('food_social_groups', db.Model.metadata,
    db.Column('food_id', db.Integer, db.ForeignKey('food.id'), nullable=False),
    db.Column('social_id', db.Integer, db.ForeignKey('social.id'), nullable=False))

food_policies = db.Table('food_policies', db.Model.metadata,
    db.Column('food_id', db.Integer, db.ForeignKey('food.id'), nullable=False),
    db.Column('policy_id', db.Integer, db.ForeignKey('policy.id'), nullable=False))

food_fuels = db.Table('food_fuels', db.Model.metadata,
    db.Column('food_id', db.Integer, db.ForeignKey('food.id'), nullable=False),
    db.Column('fuel_id', db.Integer, db.ForeignKey('fuel.id'), nullable=False))

class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    food = db.Column(db.String(200), unique=True)
    food_group = db.Column(db.String(200))
    species = db.Column(db.String(200))
    water = db.relationship('Water', backref='food')
    environments = db.relationship('Environment', backref='foods', secondary="food_environments")
    social_groups = db.relationship('Social', backref='foods', secondary="food_social_groups")
    policies = db.relationship('Policy', backref='foods', secondary="food_policies")
    fuels = db.relationship('Fuel', backref='foods', secondary="food_fuels")

    def __repr__(self):
        return '<Food %r>' % self.food

class Water(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gallons = db.Column(db.Integer)
    usage = db.Column(db.String(200))
    food_id = db.Column(db.Integer, db.ForeignKey('food.id'))

    def __repr__(self):
        return '<Water %r>' % self.gallons

class Environment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    environment = db.Column(db.String(200), unique=True)
    category = db.Column(db.String(200))
    population = db.Column(db.Integer)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)

    def __repr__(self):
        return '<Environment %r>' % self.environment

class Social(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    social_group = db.Column(db.String(200), unique=True)
    consumption = db.Column(db.Integer)
    culture = db.Column(db.String(200))
    income = db.Column(db.Integer)
    # food_id = db.Column(db.Integer, db.ForeignKey('food.id'))

    def __repr__(self):
        return '<Social %r>' % self.social_groups

class Policy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    policy = db.Column(db.String(200), unique=True)
    level = db.Column(db.String(200))
    # food_id = db.Column(db.Integer, db.ForeignKey('food.id'))

    def __repr__(self):
        return '<Food %r>' % self.policy

class Fuel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fuel = db.Column(db.String(200), unique=True)
    quantity = db.Column(db.Integer)
    # food_id = db.Column(db.Integer, db.ForeignKey('food.id'))

    def __repr__(self):
        return '<Fuel %r>' % self.fuel

# models for which we want to create API endpoints
app.config['API_MODELS'] = { 'food': Food, 
    'water': Water, 
    'environment': Environment, 
    'social': Social, 
    'policy': Policy, 
    'fuel': Fuel
    }

# # models for which we want to create CRUD-style URL endpoints,
# # and pass the routing onto our AngularJS application
# app.config['CRUD_URL_MODELS'] = { 'post': Post }
