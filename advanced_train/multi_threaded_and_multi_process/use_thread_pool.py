# coding=utf-8
from concurrent import futures
from urllib2 import urlopen
import time

URLS = ['http://www.163.com', 'http://www.baidu.com', 'https://github.com', 'http://sina.com', 'http://sohu.com']


def load_url(url):
    response = urlopen(url, timeout=60)
    print '%s page is %d bytes' % (url, len(response.read()))


executor = futures.ThreadPoolExecutor(max_workers=2)

# 使用submit()方法
for url in URLS:
    future = executor.submit(load_url, url)
    print future.done()

# 使用map()方法
# executor.map(load_url, URLS)

print '主线程'
