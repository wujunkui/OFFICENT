from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager

app = Flask(__name__)

app.config.from_object('blogs.setting')

db = SQLAlchemy(app)

from blogs.models import Users,UserInfo
import views

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(userid):
    return Users.query.get(int(userid))