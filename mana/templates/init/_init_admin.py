# coding: utf-8
"""
_init_admin_code

"""

_init_admin_code = '''# coding: utf-8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_object(config['default'])
config['default'].init_app(app)


db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


# register blueprint
from main import main
app.register_blueprint(main, url_prefix='/main')

'''
