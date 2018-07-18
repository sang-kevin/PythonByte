# coding=utf-8
# 装饰器的理解和使用


class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Coord: " + str(self.__dict__)  # __dict__：对象输出的只是对象拥有的普通变量而已


def wrapper(func):
    def checker(a, b):  # 嵌套函数    接收两个参数，传递给闭包捕获的函数
        if a.x < 0 or a.y < 0:
            a = Coordinate(a.x if a.x > 0 else 0, a.y if a.y > 0 else 0)
        if b.x < 0 or b.y < 0:
            b = Coordinate(b.x if b.x > 0 else 0, b.y if b.y > 0 else 0)
        ret = func(a, b)  # 之所以能用得到函数func, 是因为闭包：嵌套定义在非全局作用域里面的函数能够记住它在被定义的时候它所处的封闭命名空间。这能够通过查看嵌套函数的func_closure
        # 属性得出结论，这个属性里面包含封闭作用域里面的值（只会包含被捕捉到的值，比如func，如果在wrapper里面还定义了其他的值，这个属性里面是不会有的)
        if ret.x < 0 or ret.y < 0:
            ret = Coordinate(ret.x if ret.x > 0 else 0, ret.y if ret.y > 0 else 0)
        return ret  # 嵌套函数 checker 被调用后的返回值应该为 加上装饰器之后的加强版 func

    return checker  # 如果嵌套函数 checker 不被返回, 那么它将无法被调用


@wrapper  # 用来代替 add = wrapper(add)
def add(a, b):
    return Coordinate(a.x + b.x, a.y + b.y)


@wrapper
def sub(a, b):
    return Coordinate(a.x - b.x, a.y - b.y)


one = Coordinate(100, 200)
two = Coordinate(300, 200)
three = Coordinate(-100, -100)
sub(one, two)  # 输出结果   Coord: {'y': 0, 'x': -200}
add(one, three)  # Coord: {'y': 100, 'x': 0}

# add = wrapper(add)  # 返回值为嵌套函数checker，便于理解：checker1 =  wrapper(add), 然后 checker1(one, three),checker1运行时用到的 func 即为参数传入的 add
# sub = wrapper(sub)
add(one, three)  # Coord: {'y': 200, 'x': 100}
sub(one, two)  # Coord: {'y': 0, 'x': 0}
