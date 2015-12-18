# coding: utf-8

"""
    _config_sql.py

"""

_config_sql_code = '''# coding: utf-8

import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """基本配置类"""
    SECRET_KEY = os.environ.get("SECRET_KEY") or "hard to guess string"
    SSL_DISABLE = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_RECORD_QUERIES = True
    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    """开发环境配置类"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DEV_DATABASE_URL") or\
        "sqlite:///" + os.path.join(basedir, "data-dev.sqlite")


class TestingConfig(Config):
    """测试环境配置类"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("TEST_DATABASE_URL") or\
        "sqlite:///" + os.path.join(basedir, "data-test.sqlite")
    WTF_CSRF_ENABLED = False


class ProductionConfig(Config):
    """生产环境配置类"""
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or\
        "sqlite:///" + os.path.join(basedir, "data.sqlite")
    @classmethod
    def init_app(cls, app):
        Config.init_app(app)


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig
}
'''
