# coding=utf-8
import re

str1 = "imooc videonum = 1000"

# 使用String的find()方法
print str1.find('1000')

# 使用re的search()方法
info = re.search(r'\d+', str1)
print info.group()
str2 = "c++=100, java=90, python=80"
info = re.search(r'\d+', str2)
print info.group()  # 100

# 使用re的findall()方法
result = re.findall(r'\d+', str2)
print result  # ['100', '90', '80']
# 列表解析
print sum(int(x) for x in result)  # 270

# 使用re的sub()方法
str3 = 'imooc videonum = 1000'
result = re.sub(r'\d+', '1001', str3)  # 注意1001这里的参数必须是一个字符串
print result  # sub()的返回值为替换后的新字符串

print'>>>>进阶理解和使用'


# sub(pattern, repl, string)的业务逻辑
# 从string中查找pattern匹配，查找之后这个匹配是一个Match()对象，如果repl是一个函数的话，那么这个Match对象就会传入函数中
def add(match):
    val = match.group()
    num = int(val) + 1
    return str(num)


result = re.sub(r'\d+', add, str3)  # add不能加(),python中函数也是对象
print result

# 使用re的split()方法
str4 = 'imooc c c++ python java'
print str4.split(' ')  # ['imooc', 'c', 'c++', 'python', 'java']
str5 = 'imooc:c c++ python java,c#'
print re.split(r':| |,', str5)  # ['imooc', 'c', 'c++', 'python', 'java', 'c#']
