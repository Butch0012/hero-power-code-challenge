from flask_sqlalchemy import SQLAlchemy

# Create an instance of the SQLAlchemy class to use with the Flask app
db = SQLAlchemy()

# Define the Hero model with a primary key, name, and a relationship to HeroPower
class Hero(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    powers = db.relationship('HeroPower', backref='hero', lazy=True)