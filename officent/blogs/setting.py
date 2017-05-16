import os

DEBUG = True

SECRET_KEY = 'this is a secret'

# APP_PATH = os.path.dirname(__file__)

ROOT_PATH = os.path.dirname(os.path.dirname(__file__))

STATIC_PATH = os.path.join(ROOT_PATH,'blogs/static/')

SQLALCHEMY_TRACK_MODIFICATIONS = False

SQLALCHEMY_DATABASE_URI = 'sqlite:////' + ROOT_PATH + '/db/test.db'
# SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost:3306/devlop'

UPLOAD_DIR = os.path.join(ROOT_PATH,'blogs/static/uploads')

ALLOW_IMGE = ['jpg','gif','png','jpeg']

ALLOW_AUDIO = ['mp3','ogg','wmv']
