# coding: utf-8
"""
    ~~~~~~~

"""

from flask import Blueprint


share = Blueprint("share", __name__, static_folder='static', template_folder='templates')


from . import views, forms
