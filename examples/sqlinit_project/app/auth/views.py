# coding: utf-8
from . import auth
from flask import render_template


# test views
@auth.route('/test/')
def test():
    return "<h1>just tell you everything is ok!</h1>"

