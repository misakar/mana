# coding: utf-8

"""
    _views_blueprint.py

"""

_views_blueprint_code = '''# coding: utf-8
from . import %s
from flask import render_template


# test views
@%s.route('/test/')
def test():
    return "<h1>just tell you everything is ok!</h1>"

'''

