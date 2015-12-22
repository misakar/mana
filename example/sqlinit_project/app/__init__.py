# coding: utf-8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config


app = Flask(__name__)
app.config.from_object(config['default'])
config['default'].init_app(app)


db = SQLAlchemy(app)


# register blueprint
from main import main
app.register_blueprint(main, url_prefix='/')

from auth import auth
app.register_blueprint(auth, url_prefix="/auth")
