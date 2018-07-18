# coding=utf-8
class Foo(object):
    def __call__(self, x):
        print("__call__ x  = %s" % x)


f = Foo()
f(1)    # 该对象可以模拟函数的行为，像函数一样使用它，且一定会调用__call__方法
