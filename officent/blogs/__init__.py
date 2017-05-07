from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object('blogs.setting')

db = SQLAlchemy(app)

from blogs.models import Users
import views
