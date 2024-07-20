from flask import render_template, request, redirect, url_for, flash
from app import app, db
from app.models import User, WeatherData
import requests
import datetime

@app.route('/')
@app.route('/index')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

@app.route('/weather', methods=['POST'])
def weather():
    city = request.form['city']
    if not city:
        flash('City name cannot be empty!')
        return redirect(url_for('index'))

    user = User.query.filter_by(city=city).first()
    if not user:
        user = User(city=city)
        db.session.add(user)
        db.session.commit()

    # Получение прогноза погоды
    weather_data = get_weather_data(city)
    if weather_data:
        weather = WeatherData(city=city, timestamp=datetime.datetime.now(), weather=weather_data)
        db.session.add(weather)
        db.session.commit()
    else:
        flash('Failed to retrieve weather data.')

    return redirect(url_for('index'))

def get_weather_data(city):
    api_url = f'https://api.open-meteo.com/v1/forecast?latitude=35&longitude=139&hourly=temperature_2m'
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()['hourly']['temperature_2m'][0]
    return None
