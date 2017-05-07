import os

DEBUG = True

SECRET_KEY = 'this is a secret'

SQLALCHEMY_TRACK_MODIFICATIONS = False

# SQLALCHEMY_DATABASE_URI = 'sqlite:////' + os.path.dirname(os.path.dirname(__file__)) + 'test.db'
SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost:3306/devlop'