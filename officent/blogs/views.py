from flask import redirect

from blogs import app, db
from blogs.models import Users,UserInfo
from flask import request,render_template,url_for,flash,abort,session
from flask.ext.login import login_required,login_user,logout_user

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login',methods=['GET','POST'])
def login():
    error = None
    if request.method.upper() != 'POST':
        return render_template('login.html',error=error)

    # session['logged_in'] = 'ok'
    user = Users.query.filter_by(user_name=request.form.get('username')).first()
    login_user(user)
    flash('Logged in success')
    return redirect(url_for('index'))

@app.route('/logout')
@login_required
def logout():
    # session.pop('logged_in')
    logout_user()
    flash('you logged out')
    return redirect(url_for('index'))
