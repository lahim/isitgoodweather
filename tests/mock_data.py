# -*- coding: utf-8 -*-
__author__ = 'lahim'

find_place = {
    'query': {
        'count': 1,
        'lang': 'en-US',
        'diagnostics': {
            'url': {
                'content': 'http://gws2.maps.yahoo.com/findlocation?pf=1&locale=en_US&flags=&offset=15&q=53.45476855261649%2c%2014.56103731404994&gflags=R&start=0&count=100',
                'execution-stop-time': '15',
                'execution-start-time': '1',
                'execution-time': '14'
            },
            'user-time': '15',
            'build-version': '0.2.1805',
            'service-time': '14',
            'publiclyCallable': 'true'
        },
        'results': {
            'Result': {
                'neighborhood': 'Szczecin',
                'house': None,
                'county': 'Szczecin',
                'street': 'Ulica Przyjaciol Ronda',
                'radius': '400',
                'quality': '72',
                'unit': None,
                'city': 'Szczecin',
                'countrycode': 'PL',
                'woeid': '22714523',
                'xstreet': None,
                'line4': 'Poland',
                'line3': None,
                'line2': '71-685 Szczecin',
                'line1': 'Ulica Przyjaciol Ronda',
                'state': 'Woj. Zachodniopomorskie',
                'latitude': '53.454769',
                'hash': None,
                'unittype': None,
                'offsetlat': '53.454769',
                'statecode': None,
                'postal': '71-685',
                'name': '53.45476855261649, 14.56103731404994',
                'uzip': '71-685',
                'country': 'Poland',
                'longitude': '14.561037',
                'countycode': None,
                'offsetlon': '14.561037',
                'woetype': '11'
            }
        },
        'created': '2013-09-22T17:59:36Z'
    }
}

get_weather = {
    'query': {
        'count': 1, 'lang':
        'en-US',
        'diagnostics': {
            'url': {
                'content': 'http://weather.yahooapis.com/forecastrss?u=c&w=22714523', 'execution-stop-time': '9',
                'execution-start-time': '0', 'execution-time': '9'}, 'user-time': '10', 'build-version': '0.2.1805',
            'service-time': '9', 'publiclyCallable': 'true'}, 'results': {
        'channel': {
            'lastBuildDate': 'Wed, 25 Sep 2013 8:29 pm CEST',
            'atmosphere': {
                'pressure': '982.05', 'rising': '0', 'visibility': '9.99', 'humidity': '82'
            },
            'description': 'Yahoo! Weather for Szczecin, PL', 'language': 'en-us',
            'title': 'Yahoo! Weather - Szczecin, PL',
            'image': {'url': 'http://l.yimg.com/a/i/brand/purplelogo//uh/us/news-wea.gif', 'width': '142',
                      'height': '18', 'link': 'http://weather.yahoo.com', 'title': 'Yahoo! Weather'}, 'item': {
            'description': '\n<img src="http://l.yimg.com/a/i/us/we/52/33.gif"/><br />\n<b>Current Conditions:</b><br />\nFair, 10 C<BR />\n<BR /><b>Forecast:</b><BR />\nWed - Light Rain. High: 14 Low: 6<br />\nThu - Partly Cloudy. High: 13 Low: 6<br />\nFri - Partly Cloudy. High: 14 Low: 6<br />\nSat - Mostly Cloudy. High: 14 Low: 3<br />\nSun - Partly Cloudy. High: 16 Low: 5<br />\n<br />\n<a href="http://us.rd.yahoo.com/dailynews/rss/weather/Szczecin__PL/*http://weather.yahoo.com/forecast/PLXX0025_c.html">Full Forecast at Yahoo! Weather</a><BR/><BR/>\n(provided by <a href="http://www.weather.com" >The Weather Channel</a>)<br/>\n',
            'pubDate': 'Wed, 25 Sep 2013 8:29 pm CEST', 'title': 'Conditions for Szczecin, PL at 8:29 pm CEST',
            'long': '14.56',
            'forecast': [
                {'code': '11', 'text': 'Light Rain', 'high': '14', 'low': '6', 'date': '25 Sep 2013', 'day': 'Wed'},
                {'code': '30', 'text': 'Partly Cloudy', 'high': '13', 'low': '6', 'date': '26 Sep 2013', 'day': 'Th'},
                {'code': '30', 'text': 'Partly Cloudy', 'high': '14', 'low': '6', 'date': '27 Sep 2013', 'day': 'Fri'},
                {'code': '28', 'text': 'Mostly Cloudy', 'high': '14', 'low': '3', 'date': '28 Sep 2013', 'day': 'Sat'},
                {'code': '30', 'text': 'Partly Cloudy', 'high': '16', 'low': '5', 'date': '29 Sep 2013',
                 'day': 'Sun'}],
            'link': 'http://us.rd.yahoo.com/dailynews/rss/weather/Szczecin__PL/*http://weather.yahoo.com/forecast/PLXX0025_c.html',
            'lat': '53.46', 'guid': {'isPermaLink': 'false', 'content': 'PLXX0025_2013_09_29_7_00_CEST'},
            'condition': {
                'date': 'Wed, 25 Sep 2013 8:29 pm CEST',
                'text': 'Fair',
                'code': '33',
                'temp': '10'
            }},
            'link': 'http://us.rd.yahoo.com/dailynews/rss/weather/Szczecin__PL/*http://weather.yahoo.com/forecast/PLXX0025_c.html',
            'location': {'city': 'Szczecin', 'region': '', 'country': 'Poland'}, 'ttl': '60',
            'units': {'distance': 'km', 'speed': 'km/h', 'temperature': 'C', 'pressure': 'mb'},
            'astronomy': {'sunset': '6:51 pm', 'sunrise': '6:50 am'},
            'wind': {'direction': '70', 'speed': '8.05', 'chill': '9'}}}, 'created': '2013-09-25T19:01:07Z'}}
