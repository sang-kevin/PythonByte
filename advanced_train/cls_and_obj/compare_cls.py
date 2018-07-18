# coding=utf-8
from functools import total_ordering
from abc import ABCMeta, abstractmethod


@total_ordering  # 只需要定义等于和 大于或者小于中的一个 就可以比较所有
class Shape(object):

    @abstractmethod
    def area(self):
        pass

    def __lt__(self, obj):
        print 'in __lt__'
        if not isinstance(obj, Shape):
            raise TypeError('obj is not Shape')
        return self.area() < obj.area()

    def __eq__(self, obj):
        print 'in __eq__'
        if not isinstance(obj, Shape):
            raise TypeError('obj is not Shape')
        return self.area() == obj.area()

    # def __le__(self, obj):    # 使用@total_ordering之后就不再需要写了
    #     return self < obj or self == obj


class Rectangle(Shape):
    def __init__(self, width, height):
        self.w = width
        self.h = height

    def area(self):
        return self.w * self.h


class Circle(Shape):
    def __init__(self, radius):
        self.r = radius

    def area(self):
        return self.r ** 2 * 3.14


r1 = Rectangle(4, 4)
r2 = Rectangle(4, 4)
print r1 < r2  # r1.__lt__(r2)
print '-' * 30
print r1 <= r2  # r1.__le__(r2)
print '-' * 30

print r1 > r2  # 虽然没有实现'__gt__', 但使用了@total_ordering之后可以进行比较
print '-' * 30

c1 = Circle(2)  # c, r从同一抽象类继承
print c1 < r1
