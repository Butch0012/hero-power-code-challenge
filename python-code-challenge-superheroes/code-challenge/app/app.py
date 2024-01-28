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
    # Create a dictionary with hero details including id, name, and associated powers
    hero_data = {'id': hero.id, 'name': hero.name, 'powers': [hp.power.description for hp in hero.powers]}
    return jsonify(hero_data)

# Get all powers
@app.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    # Create a list of powers with their id, description, and associated heroes
    powers_data = [{'id': power.id, 'description': power.description, 'heroes': [hp.hero.name for hp in power.heroes]} for power in powers]
    return jsonify(powers_data)

# Get a power by ID
@app.route('/powers/<int:id>', methods=['GET'])
def get_power_by_id(id):
    power = Power.query.get_or_404(id)
    # Create a dictionary with power details including id, description, and associated heroes
    power_data = {'id': power.id, 'description': power.description, 'heroes': [hp.hero.name for hp in power.heroes]}
    return jsonify(power_data)

# Update power description by ID using PATCH method
@app.route('/powers/<int:id>', methods=['PATCH'])
def update_power_description(id):
    power = Power.query.get_or_404(id)
    data = request.get_json()
    # Update the power description with the provided value or keep the existing one
    power.description = data.get('description', power.description)
    db.session.commit()
    # Return the updated power details
    return jsonify({'id': power.id, 'description': power.description})
 #Create a new hero_power relationship using POST method
@app.route('/hero_powers', methods=['POST'])
def create_hero_power():
    data = request.get_json()
    hero_id = data.get('hero_id')
    power_id = data.get('power_id')
    strength = data.get('strength')
     # Get the hero and power objects from the database
    hero = Hero.query.get_or_404(hero_id)
    power = Power.query.get_or_404(power_id)
