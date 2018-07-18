# coding=utf-8
# 带参数的装饰器
import logging


def use_logging(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if level == 'warn':
                logging.warning('{} is running'.format(func.__name__))
            return func(*args, **kwargs)

        return wrapper

    return decorator


@use_logging(level='warn')
def foo(name):
    print('i am ' + name)


foo('foo')
