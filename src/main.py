"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Favorite, Personaje, Planet
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_hello():
    all_users = User.query.all()    
    all_users = list(map(lambda x: x.serialize(), all_users))
    return jsonify(all_users), 200

@app.route('/favorite', methods=['GET'])
def allFavoritos():
    all_favorites = Favorite.query.all()    
    all_favorites = list(map(lambda x: x.serialize(), all_favorites))
    return jsonify(all_favorites), 200

@app.route('/personaje', methods=['GET'])
def allPersonaje():
    all_personaje = Personaje.query.all()    
    all_personaje = list(map(lambda x: x.serialize(), all_personaje))
    return jsonify(all_personaje), 200

@app.route('/planet', methods=['GET'])
def allPlanet():
    all_planet = Planet.query.all()    
    all_planet = list(map(lambda x: x.serialize(), all_planet))
    return jsonify(all_planet), 200



# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
