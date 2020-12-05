from logging.config import dictConfig


class Config(object):
    DATABASE_URI = ':memory:'
    DEBUG = False
    SESSION_COOKIE_SECURE = True
    TESTING = False


class DevelopmentConfig(Config):
    DEBUG = True
    SESSION_COOKIE_SECURE = False

    dictConfig({
        'version': 1,
        'disable_existing_loggers': True,
        'formatters': {
            'default': {
                'format': '[%(asctime)s] %(levelname)s: %(message)s',
            }
        },
        'handlers': {
            'wsgi': {
                'class': 'logging.StreamHandler',
                'stream': 'ext://flask.logging.wsgi_errors_stream',
                'formatter': 'default'
            }
        },
        'root': {
            'level': 'DEBUG',
            'handlers': ['wsgi']
        }
    })


class ProductionConfig(Config):
    pass


class TestingConfig(Config):
    SESSION_COOKIE_SECURE = False
    TESTING = True
