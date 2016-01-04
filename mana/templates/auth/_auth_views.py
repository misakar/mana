# coding: utf-8

_auth_views_code = '''# coding: utf-8

from . import auth
from flask import render_template, url_for, redirect, flash
from flask_login import login_user, logout_user, current_user, login_required
from app.models import User
from .forms import LoginForm
from app import bcrypt


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user is not None and bcrypt.check_password_hash(user.password_hash, form.password.data):
            login_user(user)
            return redirect('/admin')
    return render_template('auth/login.html', form=form)


@login_required
@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

'''
