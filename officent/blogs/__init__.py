from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
import setting


bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'

from blogs.models import Users,Catories

def create_app():
    app = Flask(__name__)
    app.config.from_object('blogs.setting')
    db.init_app(app)
    login_manager.init_app(app)
    bootstrap.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix='/auth')
    return app



@login_manager.user_loader
def load_user(userid):
    return Users.query.get(int(userid))
