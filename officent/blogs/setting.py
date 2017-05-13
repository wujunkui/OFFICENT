import os

DEBUG = True

SECRET_KEY = 'this is a secret'

ROOT_PATH = os.path.dirname(os.path.dirname(__file__))

SQLALCHEMY_TRACK_MODIFICATIONS = False

SQLALCHEMY_DATABASE_URI = 'sqlite:////' + ROOT_PATH + '/db/test.db'
# SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost:3306/devlop'

UPLOAD_DIR = os.path.join(ROOT_PATH,'uploads')

ALLOW_FILES = ['jpg','gif','png','jpeg']