#!/usr/bin/env python
# encoding: utf-8

"""
    templates.py
    ~~~~~~~~~~~~

        代码预填模版文件
"""


_config_with_sql ='''# coding: utf-8
"""
    config.py
    ~~~~~~~~~

        配置文件
"""

import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """基本配置类"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SSL_DISABLE = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_RECORD_QUERIES = True

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    """开发环境配置类"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TestingConfig(Config):
    """测试环境配置类"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')
    WTF_CSRF_ENABLED = False


class ProductionConfig(Config):
    """生产环境配置类"""
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
'''


_file_init ='''# coding: utf-8
"""

    ~~~~~~~


"""

from flask import Flask
from config import config


app = Flask(__name__)


app.config.from_object(config[config_name])


from . import views, models, forms
'''


_config_base ='''# coding: utf-8
"""
    config.py
    ~~~~~~~~~

        配置文件
"""

import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """基本配置类"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    """开发环境配置类"""
    DEBUG = True


class TestingConfig(Config):
    """测试环境配置类"""
    TESTING = True
    WTF_CSRF_ENABLED = False


class ProductionConfig(Config):
    """生产环境配置类"""

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
'''


_file_init_with_sql = '''# coding: utf-8
"""

    ~~~~~~~


"""

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from config import config


app = Flask(__name__)


app.config.from_object(config[config_name])


db = SQLAlchemy(app)

from . import views, models, forms
'''


_sql_models_file = '''# coding: utf-8
"""
    models.py
    ~~~~~~~~~

        数据库文件
"""
from . import db

'''


_manage_py='''# coding: utf-8

import sys
from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.admin import Admin
from flask.ext.admin.contrib.sqla import ModelView
from app import app
from db import db


# 编码设置
reload(sys)
sys.setdefaultencoding('utf-8')


manager = Manager(app)
migrate = Migrate(app, db)
admin = Admin(app, name=project_name)


def make_shell_context():
    """自动加载环境"""
    return dict(
        app = app,
        db = db
    )


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


# 后台数据库管理界面
admin.add_view(ModelView([models], db.session))


@manager.command
def test():
    """运行测试"""
    import unittest
    tests = unittest.TestLoader().discover('test')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    app.debug = True
    manager.run()
'''
