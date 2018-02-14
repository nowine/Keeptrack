# coding=utf-8

import os

basedir = os.path.dirname(os.path.abspath(__file__))

class Config(object):
    WTF_CSRF_ENABLED = True
    SECRET_KEY = 'Yy12345^'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    @staticmethiOd
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')


class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test.db')


configs = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
