# -*- coding: utf-8 -*-
import requests

__author__ = 'lahim'


def find_place(lat, lng):
    """
    Finds place based on location.
    @param lat - latitude
    @param lng - longitude
    """

    url = 'http://query.yahooapis.com/v1/public/yql'
    query = 'select * from geo.placefinder where text = "' + lat + ',' + lng + '" and gflags = "R"',

    data = _send_request(url, query)
    woeid = data['query']['results']['Result']['woeid']

    return woeid


def get_weather(woeid):
    """
    Returns weather based on woeid param.
    @param woeid
    """

    url = 'http://query.yahooapis.com/v1/public/yql'
    query = 'select * from weather.forecast where woeid = "' + woeid + '" and u="c"'

    data = _send_request(url, query)

    weather_condition = data['query']['results']['channel']['item']['condition']

    weather = weather_condition['text']
    code = weather_condition['code']

    return weather, int(code)


def _send_request(url, query, request_format="json", diagnostics=True):
    """
    Sends request to selected URL.
    """

    params = {
        'q': query,
        'format': request_format,
        'diagnostics': 'true' if diagnostics else 'false'
    }

    resp = requests.get(url=url, params=params)
    return resp.json()