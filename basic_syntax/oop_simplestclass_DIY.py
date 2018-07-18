# coding=utf-8
from oop_simplestclass import Person

p1 = Person()
print p1

'''
<oop_simplestclass.Person instance at 0x0000000001FF4748>
<oop_simplestclass.Person instance at 0x000000000278F9C8>
会显示两行，原因如下：
当模块第一次被导入时，它所包含的代码将被执行
'''