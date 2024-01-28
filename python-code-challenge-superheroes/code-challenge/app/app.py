from flask import Flask, jsonify, request
from models import db, Hero, Power, HeroPower

app = Flask(__name__)