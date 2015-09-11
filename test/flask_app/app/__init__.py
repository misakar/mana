# coding: utf-8
"""

    ~~~~~~~


"""

from flask import Flask
from config import config


app = Flask(__name__)


app.config.from_object(config[config_name])


from . import views, models, forms
