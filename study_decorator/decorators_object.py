# coding=utf-8
# 类装饰器
# 装饰器在Python使用如此方便都要归因于Python的函数能像普通的对象一样能作为参数传递给其他函数，可以被赋值给其他变量，可以作为返回值，可以被定义在另外一个函数内。

class Foo():
    def __init__(self, func):
        self._func = func

    def __call__(self):
        print('class decorator runing')
        self._func()
        print('class decorator ending')


@Foo    # 相当于bar = Foo(bar)，传入一个函数，返回一个对象，返回的这个对象因为类中定义了__call__方法，所以该对象(bar)可以模拟函数的行为，像函数一样使用它，即bar()
def bar():
    print('bar')


bar()
