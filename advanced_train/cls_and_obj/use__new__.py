# coding=utf-8


class IntTuple(tuple):

    def __new__(cls, iterable):
        g = (x for x in iterable if isinstance(x, int) and x > 0)
        return super(IntTuple, cls).__new__(cls, g)  # 注意写法，必须加 return 和__new(cls, g)

    def __init__(self, iterable):
        # before
        # print self
        # super(IntTuple, self).__init__([1, 3, 5])
        super(IntTuple, self).__init__(iterable)
        # after


t = IntTuple([-1, 1, 'abc', 3, 5])
print t
