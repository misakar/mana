# coding: utf-8

_models_code = '''# coding: utf-8
from . import db

# write your database model here

'''

_rest_models_code ='''# coding: utf-8

import base64
from app import db
from flask import current_app
from itsdangerous import URLSafeSerializer as Serializer
from werkzeug.security import generate_password_hash, \
    check_password_hash


class Permission:
    """
    Permission 权限
    1. COMMENT: 0x01
    2. MODERATE_COMMENTS: 0x02
    3. ADMINISTER: 0x04
    """
    COMMENT = 0x01
    MODERATE_COMMENTS = 0x02
    ADMINISTER = 0x04


class Role(db.Model):
    """
    Role: 用户角色
    1. User: COMMENT 
    2. Moderator: MODERATE_COMMENTS 
    3. Administrator: ADMINISTER  
    :func insert_roles: 创建用户角色, 默认是普通用户
    """
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    default = db.Column(db.Boolean, default=False, index=True)
    permissions = db.Column(db.Integer)
    users = db.relationship('User', backref='role',
            lazy='dynamic', cascade='all')

    @staticmethod
    def insert_roles():
        roles = [
            ['User',(Permission.COMMENT, True)],
            ['Moderator', (Permission.COMMENT |
                          Permission.MODERATE_COMMENTS, False)],
            ['Administrator', (
                Permission.COMMENT |
                Permission.MODERATE_COMMENTS |
                Permission.ADMINISTER,
                False
            )]
        ]
        for r in roles:
            role = Role.query.filter_by(name=r[0]).first()
            if role is None:
                role = Role(name=r[0])
            role.permissions = r[1][0]
            role.default = r[1][1]
            db.session.add(role)
            db.session.commit()

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = "users"
    id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(20))
    password=db.Column(db.String(128))
    is_confirmed=db.Column(db.Boolean,default=False)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        # 这里是要求前端将用户的密码进行base64编码
        password_decode = base64.b64decode(password)
        self.password_hash = generate_password_hash(password_decode)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def generate_auth_token(self):
        """generate a token"""
        s = Serializer(
            current_app.config['SECRET_KEY']
            # expiration
        )
        return s.dumps({'id': self.id})

    def to_json(self):
        json_user = {
            'id': self.id,
            'email': self.email,
            'is_confirmed': self.is_confirmed,
            'role_id': self.role_id
        }
        return json_user

    @staticmethod
    def verify_auth_token(token):
        """verify the user with token"""
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return None
        # get id
        return User.query.get_or_404(data['id'])

    def can(self, permissions):
        return self.role is not None and\
               (self.role.permissions & permissions) == permissions

    def is_administrator(self):
        # is administrator
        return (self.role_id == 3)

    def __repr__(self):
        return '<User %r>' % self.email


class AnonymousUser():
    """
    AnonymousUser: 匿名用户
    :func can:
        权限判断, 匿名用户没有任何权限
    :func is_administrator:
        是否是管理员, 返回False
    :generate_auth_token:
        生成验证token, 匿名用户没有id, 不生成token
    """
    __table_args__ = {'mysql_charset': 'utf8'}

    def can(self, permissions):
        return False

    def is_administrator(self):
        return False

    def generate_auth_token(self, ):
        return None


# write your database model here


'''