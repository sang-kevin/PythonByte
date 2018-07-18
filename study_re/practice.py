# coding=utf-8
import re

str = 'imooc python'
# 创建Pattern对象
pa = re.compile(r"imooc")
# 创建Match对象
ma = pa.match(str)

# 使用Match对象获取需要的result
print ma
print ma.group()
print ma.span()  # 前闭后开
print ma.string
print ma.re  # Pattern对象
print

# 跳过创建Pattern对象这一步
ma = re.match(r'(imooc)', str)
print ma.group()
print ma.groups()
print

# 忽略大小写
str1 = 'ImoOc Python'
pa1 = re.compile(r'imooc', re.I)
ma1 = pa1.match(str1)
print ma1.group()

# 返回一个元组
pa2 = re.compile(r'(imooc)')
ma2 = pa2.match(str)
print ma2.group()  # imooc
print ma2.groups()  # ('imooc',)
