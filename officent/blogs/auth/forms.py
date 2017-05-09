# -*- coding: utf-8 -*-
from flask.ext.wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import DataRequired,EqualTo

class LoginForm(FlaskForm):
    username = StringField('UserName',validators=[DataRequired()])
    password = PasswordField('PassWord',validators=[DataRequired()])
    remember = BooleanField(u"记住我")
    submit = SubmitField(u'登录')


class RegistForm(FlaskForm):
    username = StringField('UserName', validators=[DataRequired()])
    password = PasswordField('PassWord', validators=[DataRequired()])
    ensu_psw = PasswordField('PassWord', validators=[DataRequired(),EqualTo('password',u"两次输入的密码不一致")])
    submit = SubmitField(u"注册")