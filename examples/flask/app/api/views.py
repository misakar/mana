# coding: utf-8
from . import api
from flask import render_template


# test views
@api.route('/test/')
def test():
    return "<h1>just tell you everything is ok!</h1>"

