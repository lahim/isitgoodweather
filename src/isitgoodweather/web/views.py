# -*- coding: utf-8 -*-
from flask import render_template
from flask.json import jsonify
from isitgoodweather import app
from web.weather import get_weather_message

__author__ = 'lahim'


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/googlebf1f97b9e025c5e9.html")
def google_verify_html():
    return render_template('googlebf1f97b9e025c5e9.html')


@app.route("/weather/<location>")
def weather(location):
    lat, lng = location.split(",")

    attempt_number, weather_message, weather, code, css_class = get_weather_message(lat, lng)

    return jsonify(attempt_number=attempt_number, weather_message=weather_message, weather=weather, weather_code=code,
                   css_class=css_class)


@app.errorhandler(404)
def error_handler(error):
    print error
    return render_template('404.html')


@app.errorhandler(500)
def error_handler(error):
    print error
    return render_template('500.html')
