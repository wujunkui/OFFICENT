# coding:utf-8
from blogs import db


class Users(db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(20))
    user_psw = db.Column(db.String(80))

    def __init__(self, username, password):
        self.user_name = username
        self.user_psw = password

    def __repr__(self):
        return '<User:{0}>'.format(self.user_name)


class UserInfo(db.Model):
    __tablename__ = 'UserInfo'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.ForeignKey(Users.id))
    lasted_lst = db.Column(db.JSON(none_as_null=True))
    is_vip = db.Column(db.Integer())  # 0 普通用户 1 VIP 2 管理员
