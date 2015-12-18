# coding: utf-8

from flask import Blueprint

hello = Blueprint(
    'hello',
    __name__,
    template_folder = 'templates',
    static_folder = 'static'
)

from . import views, forms

