# coding=utf-8
import os

import sys

if os.getuid() != 0:
    print '当前用户不是root用户，请以root用户执行脚本'
    sys.exit(1)

version = raw_input("请输入你想安装的python版本：（2.7/3.6）")

if version == '2.7':
    url = 'https://www.python.org/ftp/python/2.7.14/Python-2.7.14.tgz'
    package_name = 'Python-2.7.14'
elif version == '3.6':
    url = 'https://www.python.org/ftp/python/3.6.4/Python-3.6.4.tgz'
    package_name = 'Python-3.6.4.tgz'
else:
    print "你输入的版本号不支持，请输入（2.7/3.6）"
    sys.exit(1)

cmd = 'wget' + url
if os.system(cmd) != 0:
    print '下载源码失败'
    sys.exit(1)

cmd = 'tar -xzvf ' + package_name + '.tgz'  # *.tar.gz和*.tgz 用 tar -xzf 解压
if os.system(cmd) != 0:
    os.system('rm -r ' + package_name + '.tgz')
    print "解压源码包失败，请重新运行该脚本下载源码包"
    sys.exit(1)

cmd = 'cd ' + package_name + '&& ./configure --prefix=/usr/loacl/python && make && make install'
if os.system(cmd) != 0:
    print "编译python源码失败，请检查是否缺少依赖库"
    sys.exit(1)
