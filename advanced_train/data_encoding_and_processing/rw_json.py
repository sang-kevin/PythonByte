# coding=utf-8
import json

# json.dumps()：将一个python对象转换为json的字符串

l = [1, 2, 'abc', {'name': 'Bob', 'age': 13}]
print json.dumps(l)
# '[1, 2, "abc", {"age": 13, "name": "Bob"}]'   输出结果为json字符串

d = {'b': None, 'a': 5, 'c': 'abc'}
print json.dumps(d)
# '{"a": 5, "c": "abc", "b": null}'   # 注意变化：None->null

# dumps的一些参数，可以用来调整输出形式
print json.dumps(l, separators=[',', ':'])
# '[1,2,"abc",{"age":13,"name":"Bob"}]'

print json.dumps(d, sort_keys=True)  # 根据字典的key来进行排序
# '{"a": 5, "b": null, "c": "abc"}'


# json.loads()：将json的字符串转换为python的对象
l2 = json.loads('[1,2,"abc",{"age":13,"name":"Bob"}]')  # 需要传入字符串
print l2  # [1, 2, u'abc', {u'age': 13, u'name': u'Bob'}] # 此时l2又变回了一个列表

d2 = json.loads('{"a": 5, "b": null, "c": "abc"}')
print d2  # {u'a': 5, u'c': u'abc', u'b': None} 此时d2还原回了原来的字典


# dump和load：和dumps和loads功能是一致的，接口不一样，它们的接口是文件
with open('demo.json', 'w') as f:
    json.dump(l, f)  # 将l这个对象（一个列表）写入到文件当中去
    # f.write(l)  # 报错：TypeError: expected a string or other character buffer object
