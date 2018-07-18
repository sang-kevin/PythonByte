# coding=utf-8
from threading import Thread, Event


def f(e):
    print 'f 0'
    e.wait()
    print 'f 1'


e = Event()

t = Thread(target=f, args=(e,))
t.start()
# f 0

e.set()
# f 1


# 调用set()之后再调用e.wait()就阻塞不住了，如果想重复使用，需要调用e.clear()，之后才能重新阻塞，实现事件通知。
