# encoding=utf-8

class ShortInputException(Exception):
    '''一个由用户定义的异常类'''
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

try:
    text = input('Enter something --> ')
    if len(text) < 3:
        # 通过 raise 显式（主动）地引发异常
        raise ShortInputException(len(text), 3)
    # 一旦执行的 raise 语句， raise 后面的语句将不能执行
    print("continue run")
except EOFError:
    print("Why did you do an EOF on me?")
except ShortInputException as ex:
    print(('ShortInputException: The input was {0} ' + 'long, excepted at least {1}').format(ex.length, ex.atleast))
else:
    print('No exception was raised.')