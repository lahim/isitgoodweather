# -*- coding: utf-8 -*-

__author__ = 'lahim'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s - %(asctime)s - %(thread)d - %(filename)s - %(lineno)d - %(message)s'
        }
    },
    'handlers': {
        'root': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'isitgoodweather.log',
            'formatter': 'verbose'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'root': {
            'handlers': ['console', 'root'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

DEBUG = False

WEATHER_REQUEST_ATTEMPTS = 4

MESSAGES = [
    "%s. It's %s.",
    "What is wrong with you? I said, %s. It's %s.",
    "Are you blind? It's %s.",
    "I'm busy right now! Get lost!"
]