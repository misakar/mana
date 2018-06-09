# coding: utf-8

_init_blueprint_code = '''# coding: utf-8

from flask import Blueprint

%s = Blueprint(
    '%s',
    __name__,
    template_folder = 'templates',
    static_folder = 'static'
)

from . import views, forms
'''


_rest_init_blueprint_code = '''# coding: utf-8

from flask import Blueprint

%s = Blueprint('%s',__name__)

from . import auth, user
'''