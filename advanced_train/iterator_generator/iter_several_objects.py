# coding=utf-8
from random import randint

# 多门课一个班级的情况
chinese = [randint(60, 100) for _ in xrange(10)]
math = [randint(60, 100) for _ in xrange(10)]
english = [randint(60, 100) for _ in xrange(10)]

# method one
total = []
for i in xrange(len(math)):
    total.append(chinese[i] + math[i] + english[i])

print total

# method two(recommand)
score = []
for c, m, e in zip(chinese, math, english):  # 元组拆包
    score.append(c + m + e)

print score




# 一门课多个班级的情况：使用标准库中的itertools.chain, 它能将多个可迭代对象变成一个可迭代对象
from itertools import chain

e1 = [randint(60, 100) for _ in xrange(20)]
e2 = [randint(60, 100) for _ in xrange(21)]
e3 = [randint(60, 100) for _ in xrange(19)]
e4 = [randint(60, 100) for _ in xrange(22)]

e = chain(e1, e2, e3, e4)
# print e     # <itertools.chain object at 0x000000000281C0F0>
count = 0
for i in e:
    if i >= 90:
        count += 1
print count
