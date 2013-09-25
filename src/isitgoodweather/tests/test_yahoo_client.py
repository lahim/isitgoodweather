# -*- coding: utf-8 -*-
import unittest
from core.yahoo_client import FindPlaceClient, GetWeatherClient, Place, Weather
from tests import logger, mock_data

__author__ = 'lahim'


class YahooRealClientTest(unittest.TestCase):
    def setUp(self):
        self.find_place_client = FindPlaceClient()
        self.get_weather_client = GetWeatherClient()

    def test_find_place(self):
        place = self.find_place_client.find_place(53.430261, 14.550909)
        self.assertIsNotNone(place)
        logger.debug('place: %s', place)

    def test_get_weather(self):
        place = self.find_place_client.find_place(53.430261, 14.550909)
        self.assertIsNotNone(place)
        logger.debug('place: %s', place)

        weather = self.get_weather_client.get_weather_by_woeid(place.woeid)
        self.assertIsNotNone(weather)
        logger.debug('weather: %s', weather)


class YahooClientObjectDeserializationTest(unittest.TestCase):
    def setUp(self):
        self.find_place_json = mock_data.find_place['query']['results']['Result']
        self.get_weather_json = mock_data.get_weather['query']['results']['channel']

    def test_find_place(self):
        place = Place.deserialized(self.find_place_json)
        self.assertIsNotNone(place)

        logger.debug('place: %s', place)

        self.assertEqual(place.neighborhood, 'Szczecin')
        self.assertEqual(place.county, 'Szczecin')
        self.assertEqual(place.street, 'Ulica Przyjaciol Ronda')
        self.assertEqual(place.city, 'Szczecin')
        self.assertEqual(place.country, 'Poland')
        self.assertEqual(place.state, 'Woj. Zachodniopomorskie')
        self.assertEqual(place.country_code, 'PL')
        self.assertEqual(place.postal, '71-685')
        self.assertEqual(place.woeid, '22714523')

    def test_get_weather(self):
        weather = Weather.deserialized(self.get_weather_json)
        self.assertIsNotNone(weather)

        logger.debug('weather: %s', weather)

        self.assertEqual(weather.pressure, '982.05')
        self.assertEqual(weather.rising, '0')
        self.assertEqual(weather.visibility, '9.99')
        self.assertEqual(weather.humidity, '82')
        self.assertEqual(weather.condition_date, 'Wed, 25 Sep 2013 8:29 pm CEST')
        self.assertEqual(weather.condition_text, 'Fair')
        self.assertEqual(weather.condition_code, '33')
        self.assertEqual(weather.condition_temp, '10')
        self.assertEqual(weather.unit_distance, 'km')
        self.assertEqual(weather.unit_speed, 'km/h')
        self.assertEqual(weather.unit_temp, 'C')

        self.assertIsNotNone(weather.forecast)
        self.assertEqual(len(weather.forecast), 5)

        self.assertIsNotNone(weather.forecast[0])
        self.assertEqual(weather.forecast[0].code, '11')
        self.assertEqual(weather.forecast[0].text, 'Light Rain')
        self.assertEqual(weather.forecast[0].high_temp, '14')
        self.assertEqual(weather.forecast[0].low_temp, '6')
        self.assertEqual(weather.forecast[0].date, '25 Sep 2013')
        self.assertEqual(weather.forecast[0].day, 'Wed')

        self.assertIsNotNone(weather.forecast[1])
        self.assertEqual(weather.forecast[1].code, '30')
        self.assertEqual(weather.forecast[1].text, 'Partly Cloudy')
        self.assertEqual(weather.forecast[1].high_temp, '13')
        self.assertEqual(weather.forecast[1].low_temp, '6')
        self.assertEqual(weather.forecast[1].date, '26 Sep 2013')
        self.assertEqual(weather.forecast[1].day, 'Th')

        self.assertIsNotNone(weather.forecast[2])
        self.assertEqual(weather.forecast[2].code, '30')
        self.assertEqual(weather.forecast[2].text, 'Partly Cloudy')
        self.assertEqual(weather.forecast[2].high_temp, '14')
        self.assertEqual(weather.forecast[2].low_temp, '6')
        self.assertEqual(weather.forecast[2].date, '27 Sep 2013')
        self.assertEqual(weather.forecast[2].day, 'Fri')

        self.assertIsNotNone(weather.forecast[3])
        self.assertEqual(weather.forecast[3].code, '28')
        self.assertEqual(weather.forecast[3].text, 'Mostly Cloudy')
        self.assertEqual(weather.forecast[3].high_temp, '14')
        self.assertEqual(weather.forecast[3].low_temp, '3')
        self.assertEqual(weather.forecast[3].date, '28 Sep 2013')
        self.assertEqual(weather.forecast[3].day, 'Sat')

        self.assertIsNotNone(weather.forecast[4])
        self.assertEqual(weather.forecast[4].code, '30')
        self.assertEqual(weather.forecast[4].text, 'Partly Cloudy')
        self.assertEqual(weather.forecast[4].high_temp, '16')
        self.assertEqual(weather.forecast[4].low_temp, '5')
        self.assertEqual(weather.forecast[4].date, '29 Sep 2013')
        self.assertEqual(weather.forecast[4].day, 'Sun')