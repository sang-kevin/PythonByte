# coding=utf-8
# 通过实例方法名字的字符串调用方法
class Rectangle(object):
    def __init__(self, width, height):
        self.w = width
        self.h = height

    def getArea(self):
        return self.w * self.h


class Circle(object):
    def __init__(self, radius):
        self.r = radius

    def area(self):
        return self.r ** 2 * 3.14


class Triangle(object):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_area(self):
        a, b, c = self.a, self.b, self.c
        p = (a + b + c) / 2
        area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        return area


shape1 = Circle(2)
shape2 = Triangle(3, 4, 5)
shape3 = Rectangle(6, 4)


# method_name = getattr(shape2, 'get_area', None)
# print method_name
# print method_name()

# method one
def getArea(shape):
    for name in ['area', 'get_area', 'getArea']:
        method_name = getattr(shape, name, None)
        if method_name:
            return method_name()


shapes = [shape1, shape2, shape3]
print map(getArea, shapes)

# method two
from operator import methodcaller

s = 'abc123abc456'
print s.find('abc', 4)

mc = methodcaller('find', 'abc', 4)
print mc(s)

print shape1.area()
mc = methodcaller('area')
print mc(shape1)
