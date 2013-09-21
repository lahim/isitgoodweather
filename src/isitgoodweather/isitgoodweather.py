# -*- coding: utf-8 -*-
import logging
import logging.config
from flask import Flask
from werkzeug.contrib.fixers import ProxyFix
import settings

__author__ = 'lahim'

app = Flask(__name__)

logging.config.dictConfig(settings.LOGGING)
logger = logging.getLogger('root')

from web.views import *

app.wsgi_app = ProxyFix(app.wsgi_app)

if __name__ == '__main__':
    app.run(debug=settings.DEBUG)
