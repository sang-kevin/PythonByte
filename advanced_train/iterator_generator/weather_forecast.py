# coding=utf-8
import requests
from collections import Iterable, Iterator


class WeatherIterable(Iterable):
    def __init__(self, cities):
        self.cities = cities

    def __iter__(self):
        return WeatherIterator(self.cities)


class WeatherIterator(Iterator):
    def __init__(self, cities):
        self.cities = cities
        self.index = 0

    def next(self):
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index += 1
        return self.getWeather(city)

    def getWeather(self, city):
        r = requests.get(u'http://wthrcdn.etouch.cn/weather_mini?city=' + city)
        data = r.json()['data']['forecast'][0]
        return '%s %s: %s, %s' % (city, data['date'], data['high'], data['low'])


city_list = [u'北京', u'上海', u'东莞', u'武汉', u'荆州']
for i in WeatherIterable(city_list):
    print i
