from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

#Characters
class Character(db.Model):
    __tablename__ = 'character'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String, unique=True, nullable=False)
    height = db.Column(db.String(250), unique=False, nullable=True)
    mass = db.Column(db.String(250), unique=False, nullable=True)
    hair_color = db.Column(db.String(16), unique=False, nullable=True)
    eye_color = db.Column(db.String(16), unique=False, nullable=True)
    gender = db.Column(db.String(16), unique=False, nullable=True)
    skin_color = db.Column(db.String(250), unique=False, nullable=True)
   

    def __repr__(self):
        return '<Character %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "mass": self.mass,
            "hair_color": self.hair_color,
            "eye_color": self.eye_color,
            "gender": self.gender,
            "skin_color": self.skin_color,
        }
    

    #Planets
    
class Planet(db.Model):
    __tablename__ = 'planet'
    
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    diameter = db.Column(db.String(250), unique=False, nullable=True)
    rotation_period = db.Column(db.String(250), unique=False, nullable=True)
    gravity = db.Column(db.String(250), unique=False, nullable=True)
    climate = db.Column(db.String(250), unique=False, nullable=True)
    orbital_period = db.Column(db.String(250), unique=False, nullable=True)
    population  = db.Column(db.String(250), unique=False, nullable=True)
   
    def __repr__(self):
        return '<Planet %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "diameter": self.diameter,
            "rotation_period": self.rotation_period,
            "gravity": self.gravity,
            "climate": self.climate,
            "orbital_period ": self.orbital_period,
            "population": self.population,
            
        }
    
    #Vehicles
    
class Vehicle(db.Model):
    __tablename__ = 'vehicle'
    
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    model = db.Column(db.String(250), unique=False, nullable=True)
    manufacturer  = db.Column(db.String(250), unique=False, nullable=True)
    cost_in_credits = db.Column(db.String(250), unique=False, nullable=True)
    minimun_crew = db.Column(db.String(250), unique=False, nullable=True)
    passengers = db.Column(db.String(250), unique=False, nullable=True)
   
    def __repr__(self):
        return '<Planet %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "model": self.model,
            "manufacturer": self.manufacturer,
            "cost_in_credits": self.cost_in_credits,
            "minimun_crew": self.minimun_crew,
            "passengers ": self.passengers,
            
            
        }
    
    #Favorites
class Favorite(db.Model):
    __tablename__ = 'favorite'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'), nullable=True)
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'), nullable=True)
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'), nullable=True)
    character = db.relationship("Character")
    planet = db.relationship("Planet")
    vehicle = db.relationship("Vehicle")
   

    def __repr__(self):
        return '<Favorite %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "character_id": self.character_id,
            "planet_id": self.planet_id,
            "vehicle_id": self.vehicle_id,
            
        }
   