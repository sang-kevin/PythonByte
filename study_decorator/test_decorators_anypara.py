# 参数传递的路径 (1)->(2)->(3)
def logger(func):
    def inner(*args, **kwargs):  # (2) 能够接受任意数量和类型的参数并把它们传递给被包装的方法（即闭包捕获的函数）
        print("Arguments were: %s, %s" % (args, kwargs))
        return func(*args, **kwargs)  # (3) 参数在这里传递

    return inner


@logger
def foo1(x, y=1):
    return x * y


@logger
def foo2():
    return 2


print(foo1(5, 4))   # (1)
# Arguments were: (5, 4), {}
# 20
print(foo1(1, y=2))  # 这里的 fool1 实质上是一个 inner 函数
# Arguments were: (1,), {'y': 2}
# 2
print(foo2())
# Arguments were: (), {}
# 2
