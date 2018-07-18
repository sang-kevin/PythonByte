# coding=utf-8
from redis_helper import RedisHelper

obj = RedisHelper()
redis_sub = obj.subscribe()

# obj.publish('hello world')

while True:
    msg = redis_sub.parse_response()  # 有消息则打印，无消息则阻塞
    print msg
