# coding=utf-8
class Data(object):
    def __init__(self, value, owner):
        self.owner = owner
        self.value = value

    def __str__(self):
        return "%s's data, value is %s" % (self.owner, self.value)

    def __del__(self):
        print 'in Data.__del__'


class Node(object):
    def __init__(self, value):
        self.data = Data(value, self)

    def __del__(self):
        print 'in Node.__del__'


node = Node(10)
print node.data         # <__main__.Node object at 0x000000000271AE10>'s data, value is 10 /Data类中没有实现__str__时，运行，输出为：<__main__.Data object at 0x000000000275ADA0>
print node.data.owner   # <__main__.Node object at 0x00000000028BAE10>
# del node    # Node类的析构函数没有被调用，因为引用计数不为0，生成的Data类的对象的属性也引用了node这个对象

# import gc
# gc.collect()    # 强制回收，但是这里我们定义了每个类的析构函数__del__，所以即便使用这种强制回收方式仍不能将它们回收掉
raw_input('wait...')

