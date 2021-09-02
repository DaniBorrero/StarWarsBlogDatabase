from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,            
        }

class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    nameFavorite = db.Column(db.String(30), unique= False, nullable=False)
    typeFavorite = db.Column(db.String(30), unique= False, nullable=False)
    rel = db.relationship('User')

    def __repr__(self):
        return '<Favorite %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "name_Favorite": self.nameFavorite,
            "type_Favorite": self.typeFavorite,
        }

class Personaje(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    namePersonaje = db.Column(db.String(30), unique= False, nullable=False)
    urlPersonaje = db.Column(db.String(30), unique= False, nullable=False)
    imgPersonaje = db.Column(db.String(30), unique= False, nullable=False)
    heightPersonaje = db.Column(db.String(30), unique= False, nullable=False)
    massPersonaje = db.Column(db.String(30), unique= False, nullable=False)
    hairColorPersonaje = db.Column(db.String(30), unique= False, nullable=False)
    skinColorPersonaje = db.Column(db.String(30), unique= False, nullable=False)
    eyeColorPersonaje = db.Column(db.String(30), unique= False, nullable=False)
    homeWorldPersonaje = db.Column(db.String(30), unique= False, nullable=False)
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'))
    relPlanet = db.relationship('Planet')  

    def __repr__(self):
        return '<Personaje %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "planet_id": self.planet_id,
            "namePersonaje": self.namePersonaje,
            "urlPersonaje": self.urlPersonaje,
            "imgPersonaje": self.imgPersonaje,
            "heightPersonaje": self.heightPersonaje,
            "massPersonaje": self.massPersonaje,
            "hairColorPersonaje": self.hairColorPersonaje,
            "skinColorPersonaje": self.skinColorPersonaje,
            "eyeColorPersonaje": self.eyeColorPersonaje,
            "homeWorldPersonaje": self.homeWorldPersonaje,            
        }

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    diameterPlanet = db.Column(db.String(30), unique= False, nullable=False)
    gravityPlanet = db.Column(db.String(30), unique= False, nullable=False)
    populationPlanet = db.Column(db.String(30), unique= False, nullable=False)
    climatePlanet = db.Column(db.String(30), unique= False, nullable=False)
    terrainPlanet = db.Column(db.String(30), unique= False, nullable=False)    
    #rel = db.relationship('User')  

    def __repr__(self):
        return '<Planet %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "diameterPlanet": self.diameterPlanet,
            "gravityPlanet": self.gravityPlanet,
            "populationPlanet": self.populationPlanet,
            "climatePlanet": self.climatePlanet,
            "terrainPlanet": self.terrainPlanet,                        
        }   
