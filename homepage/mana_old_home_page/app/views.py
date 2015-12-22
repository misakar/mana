# coding: utf-8

from flask import render_template
from . import app


@app.route("/mana")
def mana():
    return render_template("Mana.html")
