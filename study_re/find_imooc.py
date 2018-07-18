# coding=utf-8

def find_start_imooc(filename):
    with open(filename) as f:
        for line in f:
            if line.startswith('imooc'):
                print(line)


def find_in_imooc(filename):
    with open(filename) as f:
        for line in f:
            if line.startswith('imooc') \
                    and line[:-1].endswith('imooc'):
                print(line)

# 匹配一个下划线或字母开头的变量名
a = '1_value1'
print a and (a[0] == '_' or 'a' <= a[0] <= 'z')

# if __name__ == '__main__':
#     find_in_imooc('imooc.txt')
