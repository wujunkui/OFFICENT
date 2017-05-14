# coding:utf-8
from blogs import db
from flask.ext.login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class Users(db.Model, UserMixin):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(20), unique=True)
    user_psw = db.Column(db.String(128))
    # user_info = db.relationship("UserInfo", backref='Users', lazy='joined',uselist=False)
    user_avatar = db.Column(db.String(128))
    email_addr = db.Column(db.String(128))
    last_login_time = db.Column(db.DateTime())
    registed_time = db.Column(db.DateTime())
    loves_carory = db.Column(db.String(256))  # 储存用户喜欢文章的ID的序列
    # lasted_lst = db.Column(db.JSON(none_as_null=True))
    is_vip = db.Column(db.Integer, default=0)  # 0 普通用户 1 VIP 2 管理员
    user_catory = db.relationship("Catories", backref='Users', lazy='joined')

    def __init__(self, username, password):
        self.user_name = username
        self.user_psw = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.user_psw, password)

    def __repr__(self):
        return '<User:{0}>'.format(self.user_name)


# class UserInfo(db.Model):
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('Users.id'))
#


class Catories(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    show_imge = db.Column(db.String(128))
    data_name = db.Column(db.String(128),unique=True)
    data_path = db.Column(db.String(256))
    author = db.Column(db.String(20), db.ForeignKey('Users.user_name'))
    read_num = db.Column(db.Integer, default=0)
    collect_num = db.Column(db.Integer, default=0)

    # comments_num = db.Column(db.Integer, default=0)

    def __repr__(self):
        return '<Catory:%r>' % self.data_name

    def add_reads(self, num=1):
        self.read_num += num

    def add_collects(self, num=1):
        self.read_num += num
