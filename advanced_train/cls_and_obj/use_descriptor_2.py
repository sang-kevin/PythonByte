# coding=utf-8
# 使用描述符对实例属性做类型检查


class Attr(object):
    def __init__(self, name, _type):
        self.name = name
        self._type = _type

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self._type):
            raise TypeError("expected an %s" % self._type)
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


class A(object):
    name = Attr('name', str)
    age = Attr('age', int)
    height = Attr('height', float)


a = A()
a.name = 'sangyu'
print a.__dict__  # {'name': 'sangyu'}
a.age = 22
a.height = 1.79
print a.__dict__  # {'age': 22, 'name': 'sangyu', 'height': 1.79}

print a.name
del a.height
print a.__dict__  # {'age': 22, 'name': 'sangyu'}

a.age = 'abc'  # TypeError: expected an <type 'int'>
