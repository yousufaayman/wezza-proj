from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class   User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120))
    phone_number = db.Column(db.String(20))

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120))
    phone_number = db.Column(db.String(20))

class Venue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120))
    phone_number = db.Column(db.String(20))
    description = db.Column(db.Text)
    location = db.Column(db.String(200))
    price = db.Column(db.Float)
    media = db.Column(db.String(200))

class Hairdresser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120))
    phone_number = db.Column(db.String(20))
    description = db.Column(db.Text)
    location = db.Column(db.String(200))
    price = db.Column(db.Float)
    media = db.Column(db.String(200))


class Weddingplanner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120))
    phone_number = db.Column(db.String(20))
    description = db.Column(db.Text)
    location = db.Column(db.String(200))
    price = db.Column(db.Float)
    media = db.Column(db.String(200))

class Makeupartist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120))
    phone_number = db.Column(db.String(20))
    description = db.Column(db.Text)
    location = db.Column(db.String(200))
    price = db.Column(db.Float)
    media = db.Column(db.String(200))


class Venuedetails(db.Model):
    name = db.Column(db.String(180), primary_key=True, unique=True, nullable=False)
    email = db.Column(db.String(120))
    phone_number = db.Column(db.String(20))
    description = db.Column(db.Text)
    location = db.Column(db.String(200))
    price = db.Column(db.Float)
    media = db.Column(db.String(200))
