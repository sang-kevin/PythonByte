# coding=utf-8
class Descriptor(object):
    def __get__(self, instance, owner):
        print 'in __get__', instance, owner

    def __set__(self, instance, value):
        print 'in __set__', instance, value

    def __delete__(self, instance):
        print 'in __delete__', instance


class A(object):  # 必须继承自object, 才会具有类属性的特性
    x = 10
    y = Descriptor()

    def __init__(self, z):
        self.z = z

    def __del__(self):
        print 'in A.__del__'


a = A(20)
# 实例属性
print a.__dict__
del a.z  # 可以使用del删除对象的属性
print a.__dict__

# 类属性
print a.x
# del a.x  # 报错 AttributeError: x

# 类属性（是一个描述符对象）
print '*' * 30
a.y  # in __get__ <__main__.A object at 0x000000000277ACF8> <class '__main__.A'>
A.y  # in __get__ None <class '__main__.A'>

a.y = 5  # in __set__ <__main__.A object at 0x000000000270ACF8> 5

del a.y  # in __delete__
