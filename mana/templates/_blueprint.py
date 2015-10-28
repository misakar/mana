# coding: utf-8

"""
    _blueprint.py
    ~~~~~~~~~~~~

        蓝图代码模版
"""

_blueprint_py='''# coding: utf-8
"""
    ~~~~~~~

"""

from flask import Blueprint


%s = Blueprint("%s", __name__, static_folder='static', template_folder='templates')


from . import views, forms
'''
