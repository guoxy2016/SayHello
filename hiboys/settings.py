import os

from hiboys import app

database_uri = 'sqlite:///' + os.path.join(os.path.dirname(app.root_path), 'data.sqlite3')

SECRET_KEY = os.getenv('SECRET_KEY', 'development_secret_key')
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', database_uri)
SQLALCHEMY_TRACK_MODIFICATIONS = False
