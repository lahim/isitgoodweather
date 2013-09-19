# -*- coding: utf-8 -*-
import urllib
from flask import request
import settings
import web.yahoo_api as yahoo_api

__author__ = 'lahim'

attempts = settings.WEATHER_REQUEST_ATTEMPTS
messages = settings.MESSAGES


def get_weather_message(lat, lng):
    cookie = request.cookies.get('attempts_cookie')
    css_class = None

    if not cookie:
        attempt_number = 1
        weather, code = _get_weather(lat, lng)
    else:
        cookie = urllib.unquote(cookie).decode('utf-8')
        args = cookie.split(',')

        if not len(args) == 3:
            attempt_number = 1
            weather, code = _get_weather(lat, lng)
        else:
            attempt_number = int(args[0]) + 1
            weather = args[1]
            code = args[2]

            if attempt_number >= attempts:
                attempt_number = attempts
                css_class = "warning-message"

    weather_message = _get_messages(attempt_number, weather, code)

    return attempt_number, weather_message, weather, code, css_class


def _get_weather(lat, lng):
    woeid = yahoo_api.find_place(lat, lng)
    weather, code = yahoo_api.get_weather(woeid)
    return weather, code


def _get_messages(attempt_number, weather, code):
    """
    Response codes are available here:
        http://developer.yahoo.com/weather/#response
    """

    weather = str(weather).lower()
    result = 'Yes' if code in [31, 32, 33, 34, 36] else 'No'

    if attempt_number in [1, 2]:
        return messages[attempt_number - 1] % (result, weather)
    elif attempt_number is 3:
        return messages[attempt_number - 1] % weather
    else:
        return messages[attempt_number - 1]