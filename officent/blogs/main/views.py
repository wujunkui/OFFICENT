# coding:utf-8
import os
from blogs import db
from blogs.main import main
from .forms import CatoryForm
from flask import request, render_template, redirect, url_for, flash, abort, session, current_app
from blogs.models import Catories
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from public import Log, save_upload_file

LOG = Log()


@main.route('/')
def index():
    catory_lst = Catories.query.all()
    return render_template('index.html', catorys=catory_lst)


@main.route('/add', methods=['GET', 'POST'])
@login_required
def add_catory():
    error = None
    form = CatoryForm()
    if form.validate_on_submit():
        new_catory = Catories()
        new_catory.show_imge = save_upload_file(form.catory_imge.data, type='img')
        if not new_catory.show_imge:
            flash(u'不支持的文件格式')
            error = u'夜话图片不是正确的图片格式'
            return render_template('add_catory.html', form=form, error=error)
        new_catory.data_name = form.catory_name.data
        new_catory.author = current_user.user_name
        new_catory.data_path = save_upload_file(form.catory_data.data, type='audio')
        if not new_catory.show_imge:
            flash(u'不支持的文件格式')
            error = u'夜话不是正确的音频格式'
            return render_template('add_catory.html', form=form, error=error)

        db.session.add(new_catory)
        db.session.commit()
        flash(u'上传成功')
        return redirect(url_for('main.index'))
    return render_template('add_catory.html', form=form, error=error)


@main.route('/catory/<catory_name>')
def catory_detail(catory_name):

    catory = Catories.query.filter_by(data_name=catory_name).first()
    catory.add_reads()
    db.session.commit()
    return render_template('catory_detail.html',catory=catory)
