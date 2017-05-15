# coding:utf-8

from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,FileField
from wtforms.validators import DataRequired

class CatoryForm(FlaskForm):
    catory_imge = FileField(u'展示图片')
    catory_name = StringField(u'音频标题',validators=[DataRequired()])
    catory_data = FileField(u'上传夜话',validators=[DataRequired()])
    submit = SubmitField(u'发布')
