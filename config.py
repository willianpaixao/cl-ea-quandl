from logging.config import dictConfig


class Config(object):
    SESSION_COOKIE_DOMAIN = False


class DevelopmentConfig(Config):
    CACHE_DEFAULT_TIMEOUT = 300
    CACHE_TYPE = "simple"
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
            },
        },
        'loggers': {
            '': {
                'level': 'DEBUG',
                'handlers': ['wsgi']
            }
        }
    })


class ProductionConfig(Config):
    CACHE_TYPE = "simple"
    DEBUG = False
    SESSION_COOKIE_SECURE = True
    TESTING = False

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
            },
        },
        'loggers': {
            '': {
                'level': 'INFO',
                'handlers': ['wsgi']
            }
        }
    })


class TestingConfig(Config):
    CACHE_TYPE = "null"
    SESSION_COOKIE_SECURE = False
    TESTING = True
