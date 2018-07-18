# coding=utf-8
import os
import shutil
import zipfile
import xlrd, xlwt
from xlutils.copy import copy
import openpyxl


class ExcelImgRead(object):

    def copy_file_to_zip(self, file_path, old_name, new_type='.zip'):
        """
        复制指定目录下的文件并修改类型为'.zip'
        :param file_path:
        :param old_name:
        :param new_type:
        :return:
        """
        old_path = os.path.join(file_path, old_name)
        if not os.path.exists(old_path):
            print ('No such File! :%s' % old_path)
            return False
        new_name = str(old_name.split('.')[0]) + new_type
        new_path = os.path.join(file_path, new_name)
        if os.path.exists(new_path):
            os.remove(new_path)
        # os.rename(old_path, new_path)
        shutil.copyfile(old_path, new_path)

    def unzip_file(self, file_path):
        """
        解压缩指定目录下的Zip文件
        :param file_path:
        :return:
        """
        file_list = os.listdir(file_path)
        for file_name in file_list:
            if file_name.split('.')[-1] == 'zip':
                try:
                    file_abs_path = os.path.join(file_path, file_name)
                    target_dir = file_name.split('.')[0]
                    target_abs_dir = os.path.join(file_path, target_dir)
                    if os.path.exists(target_abs_dir):
                        shutil.rmtree(target_abs_dir)
                    zipf = zipfile.ZipFile(file_abs_path, 'r')
                    zipf.extractall(target_abs_dir)  # 解压到指定文件目录
                    zipf.close()
                    os.remove(file_abs_path)
                except:
                    print 'Unzip Zipfile Failed '
                    shutil.rmtree(target_abs_dir)

    def get_excel_pic(self, file_path, file_name):
        """
        解压缩的excel目录下获取图片
        :param file_path:
        :param file_name:
        :return list():
        """
        pic_dir = 'xl\media'
        pic_path = os.path.join(file_path, file_name.split('.')[0], pic_dir)
        if not os.path.exists(pic_path):
            print ('No such directory!:%s' % pic_path)
            return ''
        file_list = os.listdir(pic_path)
        paths = []
        for file_name in file_list:
            if file_name.split('.')[1] == 'png':
                path = os.path.join(pic_path, file_name)
                paths.append(path)
        return paths


def excel_pic_read(file_path, file_name):
    """
    读取excel中的图片
    :param file_path:
    :param file_name:
    :return:图片的path
    """
    eir = ExcelImgRead()
    eir.copy_file_to_zip(file_path, file_name)
    eir.unzip_file(file_path)
    return eir.get_excel_pic(file_path, file_name)


if __name__ == '__main__':
    eir = ExcelImgRead()
    file_path = r"C:\Users\sang\PycharmProjects\PythonByte\handle_excel\files"
    file_name = 'test_img_0711.xlsx'
    paths = excel_pic_read(file_path, file_name)

    workbook = openpyxl.load_workbook(
        os.path.join(file_path, file_name))
    new_file_name = file_name.split('.')[0] + '.xls'
    workbook.save(os.path.join(file_path, new_file_name))

    # open a xlrd.Book类型
    rb = xlrd.open_workbook(os.path.join(file_path, new_file_name), formatting_info=True)
    # 行不通，会报错，仅仅修改后缀名并不能真正转换格式，实际上这还是一个.xlsx格式的excel

    wb = copy(rb)
    worksheet = wb.get_sheet('BUR')
    row = 80
    for path in paths:
        worksheet.insert_bitmap(path, row, 0, 400, 400)
        row += 21
    # worksheet.add_sheet()
    wb.save(os.path.join(file_path, "Daily_Report_Consolidation_Test.xls"))
