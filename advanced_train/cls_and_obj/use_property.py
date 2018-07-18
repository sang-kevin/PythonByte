# coding=utf-8
from math import pi


class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return round(self.radius)

    def set_radius(self, value):
        if not isinstance(value, (int, long, float)):
            raise ValueError('wrong type.')
        self.radius = value

    def getArea(self):
        return self.radius ** 2 * pi

    R = property(get_radius, set_radius)


c = Circle(3.2)
print c.radius
c.radius = 5
print c.radius
print c.getArea()
c.R = 'abc'

