# coding:utf-8
from blogs import db
from flask.ext.login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class Users(db.Model,UserMixin):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(20),unique=True)
    user_psw = db.Column(db.String(128))
    user_info = db.relationship("UserInfo", backref='Users', lazy='joined',uselist=False)

    def __init__(self, username, password):
        self.user_name = username
        self.user_psw = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.user_psw,password)

    def __repr__(self):
        return '<User:{0}>'.format(self.user_name)


class UserInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.id'))
    lasted_lst = db.Column(db.JSON(none_as_null=True))
    is_vip = db.Column(db.Integer)  # 0 普通用户 1 VIP 2 管理员

