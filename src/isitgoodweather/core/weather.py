# -*- coding: utf-8 -*-
import logging
from core.yahoo_client import FindPlaceClient, GetWeatherClient
import settings

__author__ = 'lahim'

logger = logging.getLogger('root')

messages = settings.MESSAGES

find_place_client = FindPlaceClient()
get_weather_client = GetWeatherClient()


def get_weather(lat, lng):
    place = find_place_client.find_place(lat, lng)

    if not place:
        raise ValueError('Place was not found based on location: %s, %s' % lat, lng)

    weather = get_weather_client.get_weather_by_woeid(place.woeid)

    if not weather:
        raise ValueError('Weather was not found based on woeid: %s' % place.woeid)

    return weather


def get_funny_message(attempt_number, weather_text, weather_code):
    """
    Gets funny message based on attempt number, weather text and weather code.
    @param attempt_number: int
    @param weather_text: string
    @param weather_code: int
    @return: funny string message
    """
    weather_text = str(weather_text).lower()
    weather_code = int(weather_code)

    if weather_code in [31, 32, 33, 34, 36]:
        answer = 'Yes'
    elif weather_code in [20, 29, 30, 44]:
        answer = 'So-so'
    else:
        answer = "No"

    logger.debug('Weather code: %s, answer: %s', weather_code, answer)

    if attempt_number in [1, 2]:
        funny_message = messages[attempt_number - 1] % (answer, weather_text)
    elif attempt_number is 3:
        funny_message = messages[attempt_number - 1] % weather_text
    else:
        funny_message = messages[attempt_number - 1]

    return funny_message
