# coding=utf-8
import re

# ma = re.match(r'[a-z]*', '1zzz')
# print ma.span()  # (0, 0)

ma = re.match(r'[a-zA-Z]*', 'zzzzzzZZZZZZzzz')
print ma.span()  # (0, 0)
print ma.group()
print

ma = re.match(r'[\w*]', 'zzz')  # 中括号的含义是只有一个字符
print ma.group()  # z

ma = re.match(r'\w*', 'zzz')
print ma.group()  # zzz
print

ma = re.match(r'\[[\w]\]', '[z]')
print ma.group()  # [z]

ma = re.match(r'\[\w*\]', '[zzz]')
print ma.group()  # [zzz]

# 变量命名规则
ma = re.match(r'[_a-zA-Z]+[_\w]*', '__asb12')
print ma.group()

# 1-99
ma = re.match(r'[1-9]?[0-9]', '2')
print ma.group()
ma = re.match(r'[1-9]?[0-9]', '09')
print ma.group()  # 0

# 匹配指定次数
ma = re.match(r'\w{6}', '213awe')  # 即6位字符，而不是6+1位
print ma.group()  # 213awe

# 分组匹配
print ">>>>>分组匹配"

ma = re.match(r'<([\w]+>)', '<table>')
print ma.group()
print ma.groups()  # ('table>',)

ma = re.match(r'<([\w]+>)\1', '<table>table>')
print ma.group()

ma = re.match(r'<([\w]+>)[\w]*</\1', '<table></table>')
print ma.group()  # <table></table>

ma = re.match(r'<([\w]+>)[\w]+</\1', '<table>p</table>')
print ma.group()  # <table>p</table>

ma = re.match(r'<(?P<mark>[\w]+>)[\w]+</(?P=mark)', '<table>p</table>')
print ma.group()
