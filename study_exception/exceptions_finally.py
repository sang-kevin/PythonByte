import sys
import time

f = None
try:
    # 我们常用的文件阅读风格
    f = open("poem.txt")
    while True:
        line = f.readline()
        print(len(line))    # 第一行虽然是空白行但长度还是会输出1，因为有【换行符】，最后一行是空白行但是不会被输出，因为最后一行是没有换行符的
        if len(line) == 0:
            break
        print(line, end='')
        sys.stdout.flush()
        print("Press ctrl+c now")
        # 为了确保它能运行一段时间
        time.sleep(2)
except IOError:
    print("Could not find file poem.txt")
except KeyboardInterrupt:
    print("!! You cancelled the reading from the file.")
finally:
    if f:
        f.close()
        print("(Cleaning up: Closed the file)")
