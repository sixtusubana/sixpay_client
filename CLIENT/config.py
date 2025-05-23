"""Flask config."""
import os
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config:
    """Base config."""
    SECRET_KEY = os.getenv("SECRET_KEY")
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'


# class ProdConfig(Config):
#     FLASK_ENV = 'production'
#     DEBUG = False
#     TESTING = False
#     #SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
#     SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL").replace('postgres://', 'postgresql://', 1)
#     SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(Config):
    FLASK_ENV = 'development'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///freelance.db'
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URI')