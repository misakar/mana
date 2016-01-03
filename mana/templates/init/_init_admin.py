# coding: utf-8
"""
_init_admin_code

"""

_init_admin_code = '''# coding: utf-8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api
from flask_httpauth import HTTPBasicAuth
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from config import config

app = Flask(__name__)
app.config.from_object(config['default'])
config['default'].init_app(app)


api = Api(app)
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
auth = HTTPBasicAuth()
flask_bcrypt = Bcrypt(app)


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response


# register blueprint
from main import main
app.register_blueprint(main, url_prefix='/main')

from admin import admin
app.register_blueprint(admin, url_prefix="/admin")

'''
