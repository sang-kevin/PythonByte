# coding=utf-8
# public key in dicts

from random import randint, sample

print sample('abcdefg', 3)
print sample('abcdefg', randint(3, 6))

s1 = {x: randint(1, 4) for x in sample('abcdefg', randint(3, 6))}
s2 = {x: randint(1, 4) for x in sample('abcdefg', randint(3, 6))}
s3 = {x: randint(1, 4) for x in sample('abcdefg', randint(3, 6))}

# method one
res = []
for i in s1:  # 直接遍历的就是字典中的key
    if i in s2 and i in s3:
        res.append(i)
print res

# method two
print s1.viewkeys()  # a set-like object providing a view on D's keys

print map(dict.viewkeys, [s1, s2, s3])
print reduce(lambda a, b: a & b, map(dict.viewkeys, [s1, s2, s3]))
