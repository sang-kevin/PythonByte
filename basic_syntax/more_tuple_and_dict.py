# coding=utf-8
def powersum(power, *args):
    '''Return the sum of each argument raised to the specified power'''
    total = 0
    for i in args:
        total += pow(i, power)
    return total


print(powersum(2, 3, 4))
print(powersum(2, 10))


def foo(x, **kwargs):  # 任意数量的参数，也包括0个
    print(x)
    print(kwargs)


foo(1, y=1, a=2, b=3, c=4)  # 将y=1,a=2,b=3,c=4以字典的方式给了kwargs
foo(1)
