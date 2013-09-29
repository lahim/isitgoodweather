# -*- coding: utf-8 -*-
import logging
import requests

__author__ = 'lahim'

logger = logging.getLogger('root')


class ObjectJson(object):
    """
    Abstract class represents JSON object with implemented deserialized function.
    """

    _json_fields_ = {}

    @classmethod
    def deserialized(cls, json):
        deserialized_object = cls()

        for field, json_mapping in cls._json_fields_.items():
            deserialized_function = None
            value = json

            if isinstance(json_mapping, tuple):
                deserialized_mapping = json_mapping[0]
                deserialized_function = json_mapping[1]
            else:
                deserialized_mapping = json_mapping

            for key in deserialized_mapping.split('.'):
                value = value.get(key, None)

            try:
                deserialized_object.__getattribute__(field)
            except AttributeError, e:
                logger.error("Attribute error. Json field '%s' was omitted. Message: %s", field, e.message)
                continue

            if deserialized_function and hasattr(deserialized_function, '__call__'):
                value = deserialized_function(value)

            deserialized_object.__setattr__(field, value)

        return deserialized_object


class WeatherForecast(ObjectJson):
    _json_fields_ = {
        'code': 'code',
        'text': 'text',
        'high_temp': 'high',
        'low_temp': 'low',
        'date': 'date',
        'day': 'day'
    }

    code = None
    text = None
    high_temp = None
    low_temp = None
    date = None
    day = None

    @classmethod
    def deserialized_forecast(cls, json_value):
        return [WeatherForecast.deserialized(json_forecast) for json_forecast in json_value]

    def __str__(self):
        return "code: %s, text: %s, high temp: %s, low temp: %s, date: %s, day: %s" % (
            self.code, self.text, self.high_temp, self.low_temp, self.date, self.day
        )

    def __repr__(self):
        return self.__str__()


class Weather(ObjectJson):
    _json_fields_ = {
        'pressure': 'atmosphere.pressure',
        'rising': 'atmosphere.rising',
        'visibility': 'atmosphere.visibility',
        'humidity': 'atmosphere.humidity',
        'condition_date': 'item.condition.date',
        'condition_text': 'item.condition.text',
        'condition_code': 'item.condition.code',
        'condition_temp': 'item.condition.temp',
        'unit_distance': 'units.distance',
        'unit_speed': 'units.speed',
        'unit_temp': 'units.temperature',
        'unit_pressure': 'units.pressure',
        'forecast': ('item.forecast', WeatherForecast.deserialized_forecast),
    }

    pressure = None
    rising = None
    visibility = None
    humidity = None
    condition_date = None
    condition_text = None
    condition_code = None
    condition_temp = None
    unit_distance = None
    unit_speed = None
    unit_temp = None
    unit_pressure = None
    forecast = None

    def __str__(self):
        return "pressure: %s %s, rising: %s, visibility: %s %s, humidity: %s, date: %s, text: %s, code: %s, " \
               "temp: %s %s, forecast: %s" % (
                   self.pressure, self.unit_pressure, self.rising, self.visibility, self.unit_distance, self.humidity,
                   self.condition_date, self.condition_text, self.condition_code, self.condition_temp, self.unit_temp,
                   self.forecast
               )


class Place(ObjectJson):
    _json_fields_ = {
        'neighborhood': 'neighborhood',
        'county': 'county',
        'street': 'street',
        'city': 'city',
        'country': 'country',
        'state': 'state',
        'country_code': 'countrycode',
        'postal': 'postal',
        'woeid': 'woeid'
    }

    neighborhood = None
    county = None
    street = None
    city = None
    country = None
    state = None
    country_code = None
    postal = None
    woeid = None

    def __str__(self):
        return "neighborhood: %s, county: %s, street: %s, city: %s, country: %s, state: %s, countrycode: %s, " \
               "postal: %s, woeid: %s" % (self.neighborhood, self.county, self.street, self.city, self.country,
                                          self.state, self.country_code, self.postal, self.woeid)


class YahooClient(object):
    """
    Base class represents Yahoo API client.
    """
    _url_ = None
    _query_ = None

    def __init__(self, request_format="json", diagnostics=True):
        self.request_format = request_format
        self.diagnostics = diagnostics

    def _send_request(self, *args, **kwargs):
        """
        Sends request to selected URL according to query.
        """

        query = self._query_ % kwargs

        logger.debug('args: %s, query: %s', args, query)

        params = {
            'q': query,
            'format': self.request_format,
            'diagnostics': 'true' if self.diagnostics else 'false'
        }

        resp = requests.get(url=self._url_, params=params)
        return resp.json()


class FindPlaceClient(YahooClient):
    """
    Class represents Yahoo API client for find place service.
    """
    _url_ = 'http://query.yahooapis.com/v1/public/yql'
    _query_ = 'select * from geo.placefinder where text = "%(lat)s, %(lng)s" and gflags = "R"'

    def find_place(self, lat, lng):
        """
        Finds places based on location (latitude, longitude).
        @param lat: long
        @param lng: long
        @return: Place deserialized object
        """
        json = self._send_request(lat=lat, lng=lng)
        logger.debug("find_place json: %s", json)
        return Place.deserialized(json['query']['results']['Result'])


class GetWeatherClient(YahooClient):
    """
    Class represents Yahoo API client for weather.
    Response code are available here: http://developer.yahoo.com/weather/#response
    """
    _url_ = 'http://query.yahooapis.com/v1/public/yql'
    _query_ = 'select * from weather.forecast where woeid = "%(woeid)s" and u="c"'

    def get_weather_by_woeid(self, woeid):
        """
        Gets weather by woeid.
        @param woeid: string
        @return: Weather deserialized object
        """
        json = self._send_request(woeid=woeid)
        logger.debug('get_weather json: %s', json)
        return Weather.deserialized(json['query']['results']['channel'])
