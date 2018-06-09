# coding: utf-8

_rest_decorators_code =  '''# coding: utf-8

"""
    decorators.py
    `````````````
    : 装饰器模块
    : @permission_required 装饰器: 用户权限管理
    : @admin_required 装饰器: 管理员token权限管理
    : @moderator_required 装饰器: 运营权限
    ...........................................
    : copyright: (c) 2016 by MuxiStudio
    : license: MIT
"""

from functools import wraps
from flask import abort, request, g, redirect, url_for
from app.models import User,Permission
import base64


def permission_required(permission):
    """
    用户权限装饰器
    :param permission: 特定权限
        COMMENT:           0x01
        MODERATE_COMMENTS: 0x02
        ADMINISTER:        0x04
    """
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not g.current_user.can(permission):
                abort(403)
            return f(*args, **kwargs)
        return decorated_function
    return decorator


def admin_required(f):
    """
    管理员token装饰器
    :param f: 被修饰视图函数(API函数)
    HTTP Basic 验证格式: Basic base64('token:')
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        token_header = request.headers.get('authorization', None)
        if token_header:
            token_hash = token_header[6:]
            token_8 = base64.b64decode(token_hash)
            token = token_8[:-1]
            g.current_user = User.verify_auth_token(token)
            if not g.current_user.is_administrator():
                abort(403)
            return f(*args, **kwargs)
        else:
            abort(401)
    return decorated




def moderator_required(f):
    """
    协管员token装饰器
    :param f: 被修饰视图函数(API函数)
    HTTP Basic 验证格式: Basic base64('token:')
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        token_header = request.headers.get('authorization', None)
        if token_header:
            token_hash = token_header[6:]
            token_8 = base64.b64decode(token_hash)
            token = token_8[:-1]
            g.current_user = User.verify_auth_token(token)
            if not g.current_user.can(Permission.MODERATE_COMMENTS):
                abort(403)
            return f(*args, **kwargs)
        else:
            abort(401)
    return decorated


'''
