# -*- coding: utf-8 -*-
import unittest
from core.weather import get_weather

__author__ = 'lahim'


class WeatherTest(unittest.TestCase):
    def setUp(self):
        self.lat = 53.430261
        self.lng = 14.550909

    def test_get_weather_message(self):
        weather = get_weather(self.lat, self.lng)
        self.assertIsNotNone(weather)
        self.assertIsNotNone(weather.pressure)
        self.assertIsNotNone(weather.rising)
        self.assertIsNotNone(weather.visibility)
        self.assertIsNotNone(weather.humidity)
        self.assertIsNotNone(weather.condition_date)
        self.assertIsNotNone(weather.condition_text)
        self.assertIsNotNone(weather.condition_code)
        self.assertIsNotNone(weather.condition_temp)
        self.assertIsNotNone(weather.unit_distance)
        self.assertIsNotNone(weather.unit_speed)
        self.assertIsNotNone(weather.unit_temp)
        self.assertIsNotNone(weather.unit_pressure)
        self.assertIsNotNone(weather.forecast)