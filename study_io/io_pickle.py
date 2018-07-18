# coding=utf-8
import pickle

shoplistfile = 'shoplist.data'

shoplist = ['apple', 'mango', 'carrot']

# write to the file
f1 = open(shoplistfile, 'wb')
pickle.dump(shoplistfile, f1)
pickle.dump(shoplist, f1)
f1.close()

# 删除这个对象
del shoplist

# 从存储对象的文件中重新读取
f2 = open(shoplistfile, 'rb')
storedlistfile = pickle.load(f2)
storedlist = pickle.load(f2)
print(shoplistfile)
print(storedlist)
f2.close()

