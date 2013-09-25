# -*- coding: utf-8 -*-
import unittest
from core.weather import get_weather_message

__author__ = 'lahim'


class WeatherTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_get_weather_message(self):
        attempt_number, weather_message, weather, code, css_class = get_weather_message(53.430261, 14.550909)

        self.assertIsNotNone(attempt_number)
        self.assertIsNotNone(weather_message)
        self.assertIsNotNone(weather)
        self.assertIsNotNone(code)
        self.assertIsNotNone(css_class)