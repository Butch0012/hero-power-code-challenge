from flask import Flask, jsonify, request
from models import db, Hero, Power, HeroPower

app = Flask(__name__)

# Set the database URI for SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database_name.db'
db.init_app(app)

# Routes

# Get all heroes
@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    # Create a list of heroes with their id, name, and associated powers
    heroes_data = [{'id': hero.id, 'name': hero.name, 'powers': [hp.power.description for hp in hero.powers]} for hero in heroes]
    return jsonify(heroes_data)

# Get a hero by ID
@app.route('/heroes/<int:id>', methods=['GET'])
def get_hero_by_id(id):
    hero = Hero.query.get_or_404(id)