import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    # will get secret key from env file, in case it can't get it he used or 'random...'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'random_acts_of_kindness!!36' 
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False # silence the deprecation warnings