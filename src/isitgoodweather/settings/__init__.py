# -*- coding: utf-8 -*-
import os

__author__ = 'lahim'

if os.environ.get('WEATHER_DEVELOPMENT') == '1':
    from development import *
else:
    from production import *
