# coding:utf-8
from blogs.main import main
from flask import request, render_template, url_for, flash, abort, session


@main.route('/')
def index():
    return render_template('index.html')
