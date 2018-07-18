# coding=utf-8
import ConfigParser

# 注：因为文件是load 到内存中的，所以进行各种操作时，是在内存中进行修改，并不是在实际的磁盘进行修改
cfg = ConfigParser.ConfigParser()
cfg.read('study_record')
print cfg.sections()  # ['userinfo', 'study']

for se in cfg.sections():
    print se
    print cfg.items(se)

cfg.set('userinfo', 'pwd', '12345')

for se in cfg.sections():
    print se
    print cfg.items(se)

cfg.remove_option('userinfo', 'pwd')
# cfg.remove_section()
for se in cfg.sections():
    print se
    print cfg.items(se)
