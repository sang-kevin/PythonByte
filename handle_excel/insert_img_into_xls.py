# coding=utf-8
import os
import xlrd, xlwt
from xlutils.copy import copy
from PIL import Image

file_root = r"C:\Users\sang\PycharmProjects\PythonByte\handle_excel\files"
file_path = os.path.join(file_root, "test_sheet.xls")
rb = xlrd.open_workbook(file_path, formatting_info=True)
row = rb.sheet_by_name("BUR").nrows
wb = copy(rb)
worksheet = wb.get_sheet('BUR')

img_root = r"C:\Users\sang\PycharmProjects\PythonByte\handle_excel\imgs"
file_list = os.listdir(img_root)

for file_name in file_list:
    if file_name.endswith('.bmp'):
        continue
    bmp_name = file_name.split('.')[0] + '.bmp'
    img_path = os.path.join(img_root, file_name)
    img = Image.open(img_path)
    w, h = img.size
    if bmp_name not in file_list:
        if img.mode != "RGB":
            print '{0} before convert: {1}'.format(file_name, img.mode)
            img = img.convert('RGB')  # convert to RGB mode for insert_bitmap use
            print '{0} after convert: {1}'.format(file_name, img.mode)
        bmp_path = img_path.split('.')[0] + '.bmp'
        img.save(bmp_path, 'bmp')
    else:
        bmp_path = os.path.join(img_root, bmp_name)  # if has been converted before
        print 'insert ({0}) into excel directly'.format(bmp_name)
    worksheet.insert_bitmap(bmp_path, row, 0)
    row += h / 17 + 1
# worksheet.add_sheet()
wb.save(os.path.join(file_root, "Daily_Report_Consolidation_Test.xls"))
