# coding: utf-8

_rest_auth_code = '''# coding: utf-8

"""
    authentication.py
    `````````````````
    : API验证模块
    : API采用用户注册邮箱和token两种形式验证
    : 建议使用token，更加安全
    .....................................
    : copyright: (c) 2016 by MuxiStudio
    : license: MIT
"""



from flask import g, jsonify,abort
from flask_httpauth import HTTPBasicAuth
from . import api
from ..models import User, AnonymousUser

auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(email_or_token, password):
    """
    验证回调函数
    :param email_or_token:
        验证字段: HTTP Basic: email
                : Token: token
    :param password: 密码
    """
    if email_or_token == '':
        g.current_user = AnonymousUser()
        return True

    if password == '':
        g.current_user = User.verify_auth_token(email_or_token)
        g.token_used = True
        return g.current_user is not None

    # authentication field: email
    user = User.query.filter_by(email=email_or_token).first()
    if not user:
        return False

    g.current_user = user
    g.token_used = False
    return user.verify_password(password)


@api.route('/token/', methods=['GET'])
@auth.login_required  # 只有登录用户可以请求token
def get_token():
    """
    token api
    获取特定用户的token字符串, login required:D
    """
    if isinstance(g.current_user, AnonymousUser) or g.token_used:
        abort(401)
    return jsonify({
        'token': g.current_user.generate_auth_token()
    })
    
@auth.error_handler
def auth_error():
    """auth failed callback function"""
    return jsonify({"message":"auth failed"}), 403


'''
