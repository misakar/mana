# coding: utf-8
from . import hello
from flask import render_template


# test views
@hello.route('/test/')
def test():
    return "<h1>just tell you everything is ok!</h1>"
