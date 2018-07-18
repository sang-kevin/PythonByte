# coding=utf-8

poem = '''
Programming is fun
when the work is done
if you wanna make your work also fun:
    use python
'''

# 打开文件以编辑
var = 'poem.txt'
f = open(var, 'w')
# 向文件中写入文本
f.write(poem)
# 关闭文件
f.close()

# 没有指定则默认为'read'模式
f = open(var)
while True:
    Line = f.readline()
    if len(Line) == 0:
        break
    print Line
    # print(Line, end='')

# 关闭文件
f.close()