# coding=utf-8
import sys
import os

print sys.path
print os.getcwd()
# 文件标准输入（sys.stdin）
print type(sys.stdin)
print sys.stdin.fileno()
# raw_input("Enter something: ")
# print sys.stdin.read()  # 没法判断什么时候结束

# a = raw_input('Enter something: ')  # raw_input()实际上是调用sys.stdin来读取数据的
# print a
# print type(a)  # <type 'str'>


# 文件标准输出(sys.stdout)
sys.stdout.write('1000')  # 调用print()的时候实际上调用的是sys.stdout.write


# 文件标准错误(sys.stderr)
# 调用一些error函数的时候会自动地打到stderr这个控制台里面