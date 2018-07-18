# coding=utf-8
import os
import time

# 1、需要备份的文件与目录
source = ['C:\\Users\\sang\\Downloads\\Spring', '"C:\\Users\\Public\\Music\\Sample Music"']

# 2、备份文件存储的主备份目录
target_dir = 'C:\\Users\\sang\\Desktop'

# 如果目标目录不存在则创建目录
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

# 3、将当前日期作为主备份目录下的子目录名称
today = target_dir + os.sep + time.strftime('%Y%m%d')

# 将当前日期作为 zip 文件的文件名
now = time.strftime('%H%M%S')

# zip 文件名称格式
target = today + os.sep +now +'.zip'

# 如果子目录尚不存在则创建一个
if not os.path.exists(today):
    os.mkdir(today)
    print'Successfully created directory', today

# 4、使用 zip 命令将文件打包成 zip 格式
zip_command = 'zip -r {0} {1}'.format(target, ' '.join(source))     # 此处为重点:zip 命令处给的是绝对路径，所以第一个参数用target

# 5、运行备份
print'Zip command is:'
print zip_command
print'Running:'
if os.system(zip_command) == 0:
    print'Successful back to', target
else:
    print'Backup FAILED'
