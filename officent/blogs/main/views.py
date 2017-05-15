# coding:utf-8
import os
from blogs import db
from blogs.main import main
from .forms import CatoryForm
from flask import request, render_template, redirect, url_for, flash, abort, session, current_app
from blogs.models import Catories
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from public import Log, get_time_str

LOG = Log()


@main.route('/')
def index():
    catory_lst = Catories.query.all()
    return render_template('index.html', catorys=catory_lst)


def save_upload_file(file_hander):
    real_filename = secure_filename(file_hander.filename)
    ext = real_filename.rsplit('.', 1)[1]
    if not ext in current_app.config['ALLOW_FILES']:
        LOG.error(real_filename)
        return None
    save_dirpath = os.path.join(current_app.config['UPLOAD_DIR'], current_user.user_name)
    if not os.path.exists(save_dirpath):
        os.mkdir(save_dirpath)
    file_path = os.path.join(save_dirpath, get_time_str() + '_' + real_filename)
    file_hander.save(file_path)
    url_path = 'uploads/' + current_user.user_name + '/' + get_time_str() + '_' + real_filename
    return url_path


@main.route('/add', methods=['GET', 'POST'])
@login_required
def add_catory():
    error = None
    form = CatoryForm()
    if form.validate_on_submit():
        new_catory = Catories()
        new_catory.show_imge = save_upload_file(form.catory_imge.data)
        if not new_catory.show_imge:
            flash(u'不支持的文件格式')
            error = u'夜话图片不是正确的图片格式'
            return render_template('catory_info.html', form=form, error=error)
        new_catory.data_name = form.catory_name.data
        new_catory.author = current_user.user_name
        new_catory.data_path = save_upload_file(form.catory_data.data)
        if not new_catory.show_imge:
            flash(u'不支持的文件格式')
            error = u'夜话不是正确的音频格式'
            return render_template('catory_info.html', form=form, error=error)

        db.session.add(new_catory)
        db.session.commit()
        flash(u'上传成功')
        return redirect(url_for('main.index'))
    return render_template('catory_info.html', form=form, error=error)
