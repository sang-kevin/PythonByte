# coding=utf-8
import ConfigParser
import os


class StudentInfo(object):
    def __init__(self, recordfile):
        self.logfile = recordfile
        self.cfg = ConfigParser.ConfigParser()

    def cfg_read(self):
        self.cfg.read(self.logfile)

    def cfg_dump(self):
        print ">>>>>>>>>>>>>遍历一次配置文件"
        se_list = self.cfg.sections()
        for se in se_list:
            print se
            print self.cfg.items(se)

    def delete_item(self, section, option):
        self.cfg.remove_option(section, option)

    def delete_section(self, section):
        self.cfg.remove_section(section)

    def add_section(self, section):
        self.cfg.add_section(section)

    def set_option(self, section, option, value):
        """添加或编辑一个option"""
        self.cfg.set(section, option, value)

    # 重点理解该方法的逻辑：开始没有open所有变量值的改动实际是在内存中进行，后面write，
    # 使用open来打开将内存值存入，单次运行在内存中的改变是连续的
    def save(self):
        f = open(self.logfile, 'w')
        self.cfg.write(f)
        f.close()


if __name__ == '__main__':
    info = StudentInfo('study_record')
    info.cfg_read()
    info.cfg_dump()
    info.set_option('userinfo', 'pwd', '12345')
    info.cfg_dump()
    info.add_section('login')
    info.set_option('login', 'sangyu', 'imissyou')
    info.cfg_dump()
    info.delete_item('study', 'python_base')
    info.cfg_dump()
    info.delete_section('userinfo')
    info.cfg_dump()
    info.save()