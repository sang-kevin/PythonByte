# coding=utf-8

# 字典
d = {}
d['sy'] = (1, 11)
d['xq'] = (2, 22)
d['jf'] = (3, 33)
for k in d:
    print k

# 有序字典
from collections import OrderedDict

d1 = OrderedDict()
d1['sy'] = (1, 11)
d1['xq'] = (2, 22)
d1['jf'] = (3, 33)
for k in d1:
    print k

print "-------答题计时比赛-------"
from time import time
from random import randint

players = list('abcdefgh')
start = time()
d = OrderedDict()

for i in xrange(8):
    raw_input("this is a game: ")
    p = players.pop(randint(0, 7 - i))
    end = time()
    print i + 1, p, end - start
    d[p] = (i + 1, end - start)

print "-" * 20
for i in d:
    print i, d[i]
