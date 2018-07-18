# coding=utf-8
from functools import wraps, update_wrapper, WRAPPER_ASSIGNMENTS, WRAPPER_UPDATES

# assigned = WRAPPER_ASSIGNMENTS,指定用原函数的哪些属性直接替换包裹函数的属性 eg:('__name__', '__doc__')
# updated = WRAPPER_UPDATES 不替换，进行合并 eg:('__dict__',)

def mydecorator(func):
    @wraps(func)  # 方法四
    def wrapper(*args, **kwargs):
        '''wrapper function'''
        print 'In wrapper'
        func(*args, **kwargs)

    # wrapper.__name__ = func.__name__     # 方法一：这种方法最原始
    # update_wrapper(wrapper, func, ('__name__', '__doc__'), ('__dict__',))   # 方法二
    # update_wrapper(wrapper, func)  # 方法三：直接使用默认参数
    return wrapper


@mydecorator
def example():
    '''example function'''
    print 'In example'


print example.__name__
print example.__doc__
# print example.__dict__
# print WRAPPER_ASSIGNMENTS   # 默认为('__module__', '__name__', '__doc__')
# print WRAPPER_UPDATES      # 默认为('__dict__',)
