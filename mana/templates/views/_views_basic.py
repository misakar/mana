# coding: utf-8

"""
    _views_basic.py

"""

_views_basic_code = '''# coding: utf-8
from . import app
from flask import render_template


# test views
@app.route('/test/')
def test():
    return "<h1>just tell you everything is ok!</h1>"

# you can writing your views here

'''

