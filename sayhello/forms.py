from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class HelloForm(FlaskForm):
    username = StringField('姓名', validators=[DataRequired('这是必填的字段'), Length(2, 20, '姓名长度在2-20之间')])
    body = TextAreaField('内容', validators=[DataRequired('这是必填的字段'), Length(1, 200, '最长不超过200个字符')])
    submit = SubmitField('提交')
