# coding: utf-8
"""
    ~~~~~~~

"""

from flask import Blueprint


test = Blueprint("test", __name__, static_folder='static', template_folder='templates')


from . import views, forms
