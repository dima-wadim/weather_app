import os
from dotenv import load_dotenv

# Загрузка переменных окружения из файла .env
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://your_postgres_user:your_postgres_password@localhost/your_database_name'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
