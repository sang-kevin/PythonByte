# coding=utf-8
import re

# method 1    strip, lstrip, rstrip: 无法删除中间的字符，只能在两端进行删除
s = '---abc+++'
print s.strip('+-')  # abc

# method 2 切片 + 拼接
s2 = 'abc:123'
print s2[:3] + s2[4:]  # abc123

# method 3 使用str.replace()或re.sub()来替换（删除）任意位置字符

s3 = '\tabc\t123\txyz\t'
print s3.replace('\t', '')  # 输出：abc123xyz 只能替换一种字符

s4 = '\tabc\t\r123\t\rxyz\t'
print re.sub('[\t\r]', '', s3)  # 输出：abc123xyz 功能更强大，可以同时处理多种字符

# method

# 使用str.translate
import string

# 1、加密
s5 = 'abc1224xyz'
string.maketrans('abcxyz', 'xyzabc')
print 's5 = %s' % s5.translate(string.maketrans('abcxyz', 'xyzabc'))  # xyz1224abc

# 2、删除字符
s6 = 'abc\n123\t\rxyz\t'
print 's6 = %s' % s6.translate(None, '\n\t\r')

# 使用unicode.translate
