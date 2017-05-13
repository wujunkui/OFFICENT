# coding:utf-8
import os

from public import Log
from flask import redirect, current_app
from blogs import db
from blogs.auth import auth
from blogs.models import Users, UserInfo
from flask import request, render_template, url_for, flash, abort, session
from flask.ext.login import login_required, login_user, logout_user, current_user
from .forms import LoginForm, RegistForm
from werkzeug.utils import secure_filename

LOG = Log()


@auth.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    form = LoginForm()
    if request.method.upper() == 'POST':
        user = Users.query.filter_by(user_name=form.username.data).first()
        psw = request.form.get('password')

        if user and user.check_password(psw):
            login_user(user)
            flash(u'登录成功')
            return redirect(url_for('main.index'))
        else:
            error = u"用户名或密码错误!"
    return render_template('login.html', error=error, form=form)


@auth.route('/logout')
@login_required
def logout():
    # session.pop('logged_in')
    logout_user()
    flash(u'退出登录状态')
    return redirect(url_for('main.index'))


@auth.route('/register', methods=['POST', 'GET'])
def user_register():
    form = RegistForm()
    error = None
    if form.validate_on_submit():
        new_user = Users(form.username.data, form.password.data)
        db.session.add(new_user)
        try:
            db.session.commit()
            return redirect(url_for('main.index'))
        except Exception as e:
            LOG.error(str(e))
            error = u"用户已被注册"

    return render_template('register.html', form=form, error=error)


@auth.route(r'/info/<name>')
def user_info(name):
    username = name
    # username = request.args.get('username')
    flash(u"Hi {0}".format(username))
    return ""


@auth.route('/upload/<name>', methods=['POST'])
def upload_file(name):
    f = request.files['file_up']
    real_filename = secure_filename(f.filename)
    ext = real_filename.rsplit('.', 1)[1]
    if not ext in current_app.config['ALLOW_FILES']:
        LOG.error(real_filename)
        flash(u'不支持的文件格式')
        return redirect(url_for('main.index'))
    save_filepath = os.path.join(current_app.config['UPLOAD_DIR'], current_user.user_name)
    if not os.path.exists(save_filepath):
        os.mkdir(save_filepath)

    f.save(os.path.join(save_filepath, real_filename))
    flash(u'上传文件成功')
    return redirect(url_for('main.index'))
