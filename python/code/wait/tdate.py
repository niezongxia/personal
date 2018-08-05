#date.py
import xlwt
import datetime as dt

workbook=xlwt.Workbook()
worksheet=workbook.add_sheet('test1')
dateFormat=xlwt.XFStyle()
dateFormat.num_format_str='yyyy/mm/dd'
worksheet.write(0,0,dt.date.today(),dateFormat)
workbook.save('test.xls')
