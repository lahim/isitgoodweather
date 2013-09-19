# -*- coding: utf-8 -*-
import os

if os.environ.get('DEVELOPMENT') == '1':
    from development import *
else:
    from production import *

__author__ = 'lahim'
