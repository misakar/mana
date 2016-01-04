# coding: utf-8

_auth_forms_code = '''# coding: utf-8

from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(Form):
    username = StringField('username', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])
    submit = SubmitField('login!')

'''
