# coding=utf-8
from multiprocessing import Process, Queue, Pipe
import time

x = 1

def f():
    global x
    x = 5

# 进程间通信
# 单向通信 (Queue)：
def f2(q):
    print 'start'
    print q.get()
    print 'end'

# 双向通信 (Queue)：
def f3(c):
    c.send(c.recv() * 2)

if __name__ == '__main__':
    # p = Process(target=f)
    # p.start()
    # print x

    # q = Queue()
    # p = Process(target=f2, args=(q,))
    # p.start()
    # time.sleep(5)
    # q.put(1)

    c1, c2 = Pipe()
    p = Process(target=f3, args=(c2,))
    p.start()
    c1.send(55)
    print c1.recv()
