from app import create_app, db
from app.models import User, WeatherData

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'WeatherData': WeatherData}

if __name__ == '__main__':
    app.run(debug=True)
