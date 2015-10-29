# coding: utf-8
"""
    ~~~~~~~

"""

from flask import Blueprint


book = Blueprint("book", __name__, static_folder='static', template_folder='templates')


from . import views, forms
