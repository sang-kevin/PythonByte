# coding=utf-8
print'Simple Assignment'
shoplist = ['apple','mango','carrot','banana']

# mylist 只是指向同一对象的另一种名称
mylist = shoplist

# 购买了第一项，将它从列表中删除
del shoplist[0]

print'shoplist is',shoplist
print'mylist is',mylist
# 可以确认它们指向的是同一对象

print'copy by making a full slice'
# 通过生成一份完整的切片制作一份列表的副本
mylist = shoplist[:]
# 删除第一个项目
del shoplist[0]

print'shoplist is',shoplist
print'mylist is',mylist
# 此时两份列表不同

