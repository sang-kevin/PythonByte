# coding=utf-8
import redis


# 并不需要特别创建频道的步骤，直接以字符串在publish中输入即可

class RedisHelper(object):
    def __init__(self):
        self._conn = redis.Redis(host='localhost', port=6379)
        self.channel = 'monitor'  # 定义频道名称

    def publish(self, msg):
        self._conn.publish(self.channel, msg)
        return True

    def subscribe(self):
        pub = self._conn.pubsub()  # 打开收音机
        pub.subscribe(self.channel)  # 调频道
        pub.parse_response()  # 准备接收,未阻塞，再调用一次就阻塞
        return pub
