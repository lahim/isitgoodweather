# -*- coding: utf-8 -*-
import logging
import logging.config
import settings

__author__ = 'lahim'

logging.config.dictConfig(settings.LOGGING)
logger = logging.getLogger('root')
