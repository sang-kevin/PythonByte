# coding=utf-8
import time
import logging
from random import randint


def warn(timeout):
    timeout = [timeout]  # python2 的写法

    def decorator(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            res = func(*args, **kwargs)
            used = time.time() - start
            if used > timeout[0]:
                msg = '"%s": %s > %s' % (func.__name__, used, timeout[0])
                logging.warn(msg)
            return res

        def setTimeout(k):
            # nonlocal timeout # python3 可以这么使用
            timeout[0] = k  # python2 这么写

        wrapper.setTimeout = setTimeout
        return wrapper

    return decorator


@warn(1.5)
def test():
    print('In test')
    while randint(0, 1):
        time.sleep(0.5)


for _ in range(30):
    test()

print('*' * 30)

# test.setTimeout = 1 # 错误写法
test.setTimeout(1)
for _ in range(30):
    test()
