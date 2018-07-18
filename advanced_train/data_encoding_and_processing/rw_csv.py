# coding=utf-8

# 读写CSV文件

# from urllib import urlretrieve
import csv

# urlretrieve('http://table.finance.yahoo.com/table.csv?s=000001.sz', 'pingan.csv')
#
# csv_f = open('102.csv', 'r')
# reader = csv.reader(csv_f)  # reader是一个迭代器(iterator)，只有next()这一个方法
# print reader.next()
# print reader.next()

with open('102.csv', 'r') as rf:
    reader = csv.reader(rf)
    with open('102_copy.csv', 'w') as wf:
        headers = reader.next()
        writer = csv.writer(wf)
        writer.writerow(headers)
        for row in reader:
            if row[0] > '4.7':  # 注意此处的这种写法是有效的
                break
            if row[4] == 'Compliance':
                writer.writerow(row)
print '---end---'
