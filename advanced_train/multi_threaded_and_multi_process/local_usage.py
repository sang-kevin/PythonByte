# coding=utf-8
# threading.local类可以创建线程本地数据空间，其下属性对每个线程独立存在
# 1、在主线程中实例化local
# 2、每个线程中的属性名和值都是相互独立，各不相同

# 使用场景：在python中threading.local用来表示线程相关的数据，线程相关指的是这个属性再各个线程中是独立的，互不影响

from threading import Thread, local, current_thread

local_data = local()
local_data.name = 'local_data'


class TestThread(Thread):
    def run(self):
        print current_thread()
        # print local_data.name   # AttributeError: 'thread._local' object has no attribute 'name'
        print local_data.__dict__
        local_data.name = self.getName()
        local_data.add_by_sub_thread = self.getName()
        print local_data.__dict__


if __name__ == '__main__':
    print current_thread()
    print local_data.__dict__

    t1 = TestThread()
    t1.start()
    t1.join()

    t2 = TestThread()
    t2.start()
    t2.join()

    print current_thread()
    print local_data.__dict__
