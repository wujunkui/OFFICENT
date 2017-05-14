# coding:utf-8
from blogs.main import main
from flask import request, render_template, url_for, flash, abort, session
from blogs.models import Catories
from flask_login import login_required



@main.route('/')
def index():
    catory_lst = Catories.query.all()
    return render_template('index.html',catorys=catory_lst)
