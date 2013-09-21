# -*- coding: utf-8 -*-
import os

if os.environ.get('WEATHER_DEVELOPMENT') == '1':
    from development import *
else:
    from production import *

__author__ = 'lahim'
