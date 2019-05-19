import os

from sayhello import app

database_uri = 'sqlite:///' + os.path.join(app.instance_path, 'data.sqlite3')

SECRET_KEY = os.getenv('SECRET_KEY', 'development_secret_key')
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', database_uri)
SQLALCHEMY_TRACK_MODIFICATIONS = False
DEBUG_TB_INTERCEPT_REDIRECTS = True
