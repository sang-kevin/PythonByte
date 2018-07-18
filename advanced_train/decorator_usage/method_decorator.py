# coding=utf-8
# 斐波那契数列（Fibonacci Sequence），又称黄金分割数列指的是这样一个数列:1,1，2,3,5,8,13,21
# 这个数列从第三项开始，每一项都等于前两项之和。求数列第n项

# 改写这个函数
def fibonacci2(n, cache=None):
    if cache is None:
        cache = {}
    if n in cache:
        return cache[n]
    if n <= 1:
        return 1
    cache[n] = fibonacci2(n - 1, cache) + fibonacci2(n - 2, cache)
    return cache[n]


# 编写装饰器
def memo(func):
    cache = {}

    def wrap(*args):
        print args
        # print cache
        if args not in cache:
            cache[args] = func(*args)
        # print cache
        return cache[args]

    return wrap


@memo
def fibonacci(n):
    if n <= 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


# n阶台阶，一次可能走[1, 2, 3]步，一共有多少种走法？
# 回溯法问题：逐步构造减，使用递归
@memo
def climb(n, steps):
    count = 0
    if n == 0:
        count = 1
    elif n > 0:
        for step in steps:
            count += climb(n - step, steps)
    return count


print climb(10, (1, 2, 3))

# fibonacci = memo(fibonacci)
# print fibonacci(20)
