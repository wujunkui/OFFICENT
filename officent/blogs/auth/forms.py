# -*- coding: utf-8 -*-
from flask.ext.wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('UserName',validators=[DataRequired()])
    password = PasswordField('PassWord',validators=[DataRequired()])
    remember = BooleanField(u"记住我")
    submit = SubmitField(u'登录')
