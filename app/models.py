from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(64), index=True, unique=True)

class WeatherData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(64), index=True)
    timestamp = db.Column(db.DateTime, index=True)
    weather = db.Column(db.String(128))
