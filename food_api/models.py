from food_api import app
from food_api import db


class Entity(db.Model):
    __table__name = 'entity'
    id = db.Column(db.Integer, primary_key=True)
    individual = db.Column(db.String(140))
    organization = db.Column(db.String(140))
    art = db.Column(db.String(140))
    intervention = db.Column(db.String(140))
    activism = db.Column(db.String(140))
    food = db.Column(db.String(140))
    water = db.Column(db.String(140))
    fuel = db.Column(db.String(140))
    non_profit = db.Column(db.String(140))
    for_profit = db.Column(db.String(140))
    b_corp = db.Column(db.String(140))
    community = db.Column(db.String(140))
    national = db.Column(db.String(140))
    local = db.Column(db.String(140))
    climate = db.Column(db.String(140))
    health = db.Column(db.String(140))
    social = db.Column(db.String(140))

# models for which we want to create API endpoints
app.config['API_MODELS'] = { 'entity': Entity}