# -*- coding: utf-8 -*-
import logging
import urllib
from flask import render_template, request
from flask.json import jsonify
from core.weather import get_weather, get_funny_message
from isitgoodweather import app
import settings

__author__ = 'lahim'

logger = logging.getLogger('root')

attempts = settings.WEATHER_REQUEST_ATTEMPTS


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/weather/<location>")
def weather(location):
    lat, lng = location.split(",")

    attempt_number, funny_message, weather_text, weather_code, css_class = _load_weather_message(lat, lng)

    logger.info('Location: [%s, %s], weather code: [%s], weather message: %s, funny message: %s', lat, lng,
                weather_code, weather_text.lower(), funny_message)

    return jsonify(attempt_number=attempt_number, funny_message=funny_message, weather_text=weather_text,
                   weather_code=weather_code, css_class=css_class)


@app.route("/googlebf1f97b9e025c5e9.html")
def google_verify_html():
    return render_template('googlebf1f97b9e025c5e9.html')


@app.errorhandler(404)
def error_handler(error):
    return render_template('404.html')


@app.errorhandler(500)
def error_handler(error):
    return render_template('500.html')


def _load_weather_message(lat, lng):
    """
    Loads weather message if exist from cookie, else from remote API.
    @param lat: long
    @param lng: long
    @return: attempt number, funny message, weather text, weather code and css class
    """
    cookie = request.cookies.get('attempts_cookie')
    css_class = None

    if not cookie:
        attempt_number = 1
        weather_obj = get_weather(lat, lng)
        weather_text = weather_obj.condition_text
        weather_code = weather_obj.condition_code
    else:
        cookie = urllib.unquote(cookie).decode('utf-8')
        args = cookie.split(',')

        if not len(args) == 3 or not args[0] or not args[1] or not args[2]:
            attempt_number = 1
            weather_obj = get_weather(lat, lng)
            weather_text = weather_obj.condition_text
            weather_code = weather_obj.condition_code
        else:
            attempt_number = int(args[0]) + 1
            weather_text = args[1]
            weather_code = args[2]

            if attempt_number >= attempts:
                attempt_number = attempts
                css_class = 'warning-message'

    funny_message = get_funny_message(attempt_number, weather_text, weather_code)

    return attempt_number, funny_message, weather_text, weather_code, css_class