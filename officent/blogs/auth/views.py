from hashlib import md5
from flask import redirect
import blogs
from blogs.auth import auth
from blogs.models import Users, UserInfo
from flask import request, render_template, url_for, flash, abort, session
from flask.ext.login import login_required, login_user, logout_user
from .forms import LoginForm


@auth.route('/')
def index():
    return render_template('index.html')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    form = LoginForm()
    if request.method.upper() == 'POST':
        user = Users.query.filter_by(user_name=form.username.data).first()
        psw = request.form.get('password')

        if user and user.check_password(psw):
            login_user(user)
            flash('Logged in success')
            return redirect(url_for('index'))
        else:
            error = "Password error!"
    return render_template('login.html', error=error,form=form)


@auth.route('/logout')
@login_required
def logout():
    # session.pop('logged_in')
    logout_user()
    flash('you logged out')
    return redirect(url_for('index'))

@auth.route('/register')
def user_register():
    if request.method.upper() == 'POST':
        pass
    return render_template('register.html')
