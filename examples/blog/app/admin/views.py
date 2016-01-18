# coding: utf-8

"""
    admin site

    use: Flask-Admin
    -- https://flask-admin.readthedocs.org/en/latest/

"""

import flask_login as login
import flask_admin as admin
from flask_login import current_user
from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView
from app import app, db
from app.models import AnonymousUser
from flask import redirect, flash, url_for


class MyAdminIndexView(admin.AdminIndexView):
    def is_accessible(self):
        return login.current_user.is_admin()

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('auth.login'))


admin = Admin(
    app,
    name="admin site",
    template_mode="bootstrap3",
    index_view=MyAdminIndexView(),
    base_template='admin/logout.html'
)


# sql models management
from app.models import User
admin.add_view(ModelView(User, db.session))

