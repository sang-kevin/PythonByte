# coding=utf-8
# 编写一个Dict类，这个类的行为和dict一致，但是可以通过属性来访问，用起来就像下面这样：

# >> > d = Dict(a=1, b=2)
# >> > d['a']
# 1
# >> > d.a
# 1


class Dict(dict):
    def __init__(self, **kwargs):
        super(Dict, self).__init__(**kwargs)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:    # 捕获KeyError，人为地抛出一个AttributeError
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value   # 覆写了__setattr__(), 自定义了__setattr__的功能，这里自定义为字典对象增加一个键值对


if __name__ == '__main__':
    d = Dict(a=1, b=2)
    print d['a']  # 即使不继承dict类，也可以这么使用
    print d.a
    print d['c'] # KeyError: 'c'
    # print d.c  # AttributeError: 'Dict' object has no attribute 'c'
    d.c = 3  # 此时调用__setattr__(self, key, value), c传给key,3传给value
    print d.c   # 3

# 流程，首先 d 这个对象并没有a这个属性，所以会去调用__getattr__(), d[key]存在的话就会返回key对应的value，
# 不存在的话就报错，因为是调用属性，所以不报KeyError错误，而是报AttributeError

# 之所以 d['c']报 KeyError: 'c', 是因为这里不是对象调用属性时无法找到属性，不属于对象调用属性，所以不会调用__getattr__