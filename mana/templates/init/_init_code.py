# coding: utf-8

_init_code = '''# coding: utf-8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config


db = SQLAlchemy()


def create_app(config_name):

    # create flask app
    app = Flask(__name__)

    # import config
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # init flask ext with app
    db.init_app(app)

    # regist your blueprint here
    from main import main
    app.register_blueprint(main, url_prefix='/main')

    return app
'''
