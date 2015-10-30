# coding: utf-8
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
