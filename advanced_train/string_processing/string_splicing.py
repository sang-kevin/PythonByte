# coding=utf-8

# 使用 "+" 来拼接
s1 = 'abcdefg'
s2 = '12345'
print s1 + s2
print str.__add__(s1, s2)

# s1 + s2 用到了运算符重载，实际调用的是str.__add__()

print s1 > s2
print str.__gt__(s1, s2)

# 使用 "join"来拼接  S.join(iterable) -> string
print ';'.join(['abc', '123', 'xyz'])  # abc;123;xyz

print ''.join(['abc', '123', 'xyz'])  # abc123xyz

print '-' * 30

# join 的特殊使用
l = ['abc', 123, 45, 'xyz']  # 列表中包含非字符串的情况

# 使用列表解析，生成了新列表，开销较大
print ''.join([str(x) for x in l])

# 使用生成器，不生成列表，存储上要小得多
print (str(x) for x in l)  # <generator object <genexpr> at 0x00000000026C53F0>
print ''.join(str(x) for x in l)    # 作为参数的时候可以不写括号
