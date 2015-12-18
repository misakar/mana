# coding: utf-8

_init_basic_code = '''# coding: utf-8

from flask import Flask


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key is here'


from . import views, forms
'''
