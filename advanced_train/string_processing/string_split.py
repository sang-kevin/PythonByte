# coding=utf-8

s = 'ab;cd|efg|hi,,jkl|mn\topq;rst,uvw\txyz'

# extend
a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8]
d = [9, 10]

print s.split(';')  # split方法的返回值为一个列表
print a.extend(b)  # extend方法只能有一个参数，该方法没有返回值，返回None
print a


# method one
def mySplit(s, ds):
    res = [s]
    for d in ds:
        # print [d]   # [';']
        t = []
        map(lambda x: t.extend(x.split(d)), res)
        res = t
    return [i for i in res if i]


print mySplit(s, ";|,\t")

# method two(recommand)
import re

print re.split(r'[;|,\t]+', s)

