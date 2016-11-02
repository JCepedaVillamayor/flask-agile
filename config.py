import os

basedir = os.path.abspath(os.path.dirname(__file__))

class BasicConfig():
    SECRET_KEY = os.getenv('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

class DevelopmentConfig(BasicConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(basedir,
                                                                 'dev.sqlite'))

class TestingConfig(BasicConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(basedir,
                                                                 'test.sqlite'))

config = { 'development': DevelopmentConfig,
           'testing': TestingConfig,
           'default': DevelopmentConfig
}
