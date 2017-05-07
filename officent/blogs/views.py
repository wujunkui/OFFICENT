from flask import redirect

from blogs import app, db
from flask import request,render_template,url_for,flash,abort,session

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login',methods=['GET','POST'])
def login():
    error = None
    if request.method.upper() != 'POST':
        return render_template('login.html',error=error)

    session['logged_in'] = 'ok'
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.pop('logged_in')
    flash('you logged out')
    return redirect(url_for('index'))
