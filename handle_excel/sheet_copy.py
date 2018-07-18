# coding=utf-8
import xlrd, xlwt
from xlutils.copy import copy

# open a xlrd.Book类型
# rb = xlrd.open_workbook('test_img_sheet.xls', formatting_info=True)
rb = xlrd.open_workbook('test.xlsx', formatting_info=False)
# make a copy of it
wb = copy(rb)
# add a sheet to the resulting Workbook
Sheet1 = wb.add_sheet('Sheet')
# if wb.get_sheet('BUR1'):
#     print 'Exist'
# else:
#     print 'Not Exist'
wb.save('1.xlsx')
