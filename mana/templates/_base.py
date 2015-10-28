# coding: utf-8

"""
   _base.py
   ~~~~~~~~

        基础预填代码
            app/__init__.py
"""


_init_py ='''# coding: utf-8
"""

    ~~~~~~~

"""

from flask import Flask
from config import config


app = Flask(__name__)


app.config.from_object(config[config_name])


from . import views, models, forms
'''


_init_sql_py = '''# coding: utf-8
"""

    ~~~~~~~

"""

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from config import config


app = Flask(__name__)


app.config.from_object(config[config_name])


db = SQLAlchemy(app)

# blueprint register
%s

from . import views, models, forms
'''
