# import pyexcel as p
#
# p.save_book_as(file_name='files/test_sheet001.xls',
#                dest_file_name='files/test_sheet001.xlsx')


import openpyxl
workbook = openpyxl.load_workbook('files/test_img001.xlsx')
workbook.save('files/test_imgaaaa.xls')
