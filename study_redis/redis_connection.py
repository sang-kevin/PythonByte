# coding=utf-8
import redis

# 1、连接方式
# r = redis.Redis(host='localhost', port=6379)
# r.set('name', 'sangyu')
# print r.get('name')
#
# # 2、连接池
# pool = redis.ConnectionPool(host='localhost', port=6379, max_connections=5)
# r = redis.Redis(connection_pool=pool)
# r.set('sangyu', 'good')
# print r.get('sangyu')

# 4、管道
pool = redis.ConnectionPool(host='localhost', port=6379, max_connections=5)
r = redis.Redis(connection_pool=pool)
pipe = r.pipeline(transaction=True)
r.lpush('xueqin', 'good')
r.lpush('xueqin', 'cool', 'aspirant')
pipe.execute()
print r.lrange('xueqin', 0, -1)

# 5、发布和订阅
