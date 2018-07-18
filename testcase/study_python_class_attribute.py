# coding=utf-8
class A(object):
    def __init__(self, x):
        self.x = x
        self.y = 'yyy'

    def __setattr__(self, key, value):
        print 'call __setattr__ key = %s, value = %s' % (key, value)
        object.__setattr__(self, key, value)


if __name__ == '__main__':
    a = A(1)  # call __setattr__ key = x, value = 1   # call __setattr__ key = y, value = yyy
    print a.x  # 1
    a.z = 'zzzzz'  # call __setattr__ key = z, value = zzzzz
    print a.z  # zzzzz
    print a.__dict__  # {'y': 'yyy', 'x': 1, 'z': 'zzzzz'}
    del a.x
    print a.__dict__  # {'y': 'yyy', 'z': 'zzzzz'}

"""
**1、python是一门动态语言，可以对类的对象动态添加或删除属性
2、__setattr__在实例初始化以及动态添加属性时被调用
"""
