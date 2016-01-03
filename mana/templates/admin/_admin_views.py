# coding: utf-8

_admin_views_code = '''# coding: utf-8

from flask import g
from flask_restful import Resource
from app import api, db, auth, flask_bcrypt
from app.models import User
from forms import UserCreateForm, SessionCreateForm
from serializers import UserSerializer


@auth.verify_password
def verify_password(email, password):
    user = User.query.filter_by(email=email).first()
    if not user:
        return False
    g.user = user
    return flask_bcrypt.check_password_hash(user.password, password)


class UserView(Resource):
    def get(self):
        users = User.query.all()
        return UserSerializer(users, many=True).data

    def post(self):
        form = UserCreateForm()
        user = User(email=form.email.data,
            password=flask_bcrypt.generate_password_hash(form.password.data),
            username=form.username.data)
        db.session.add(user)
        db.session.commit()
        return UserSerializer(user).data


class SessionView(Resource):
    def post(self):
        form = SessionCreateForm()
        user = User.query.filter_by(email=form.email.data).first()
        if user and flask_bcrypt.check_password_hash(user.password, form.password.data):
            return UserSerializer(user).data, 201
        return '', 401


api.add_resource(UserView, '/api/v1/users/')
api.add_resource(SessionView, '/api/v1/sessions/')

'''
