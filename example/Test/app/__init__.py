# coding: utf-8
"""

    ~~~~~~~

"""

from flask import Flask


app = Flask(__name__)
app.config["SECRET_KEY"] = "I love mana!"  # you can change it :)


from . import views, forms
