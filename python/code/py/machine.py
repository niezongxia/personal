#write.py
import os,sys,xlrd,xlwt
from xlutils.copy import copy
import datetime
import datetime as dt
from datetime import date

model = './缤纷生活 - 测试组设备管理-模版.xls'

while True:
    Date = input('请输入需要生成文档的截止日期(不输直接回车默认当前日期）,形如 YYYYMMDD ：')
    if Date == '':#如果不输入就默认取当天的日期
        filedate = str(dt.date.today()).replace('-','')
        break
    else:
        # 判断输入是否有非法字符或者长度是否为8个数字
        if Date.isdigit() == False or len(Date) == 8:
            # 比较日期格式是否正确
            try:
                formdate = datetime.datetime.strptime(Date, '%Y%m%d')
                filedate = Date
                break
            except ValueError:
                print("输入日期的格式不合法哦，请重新检查")
        else:
            print("输入格式不合法！请按照样例格式输入日期！")

filename='./缤纷生活 - 测试组设备管理-'+filedate+'.xls'#'C:/xampp/htdocs/ewm/ins/war_install_record_report.xls'#
print(filename)

dateFormat=xlwt.XFStyle()
dateFormat.num_format_str='yyyy/mm/dd'

#open file
rb=xlrd.open_workbook(filename,formatting_info=True)#)#
rows=rb.sheets()[0].nrows#获取已有行数
#copy rb
wb=copy(rb)

#本文重点，该函数中定义：对于没有任何修改的单元格，保持原有格式。
def setOutCell(outSheet, col, row, value):
    def _getOutCell(outSheet, colIndex, rowIndex):#Change cell value without changing formatting.
        row = outSheet._Worksheet__rows.get(rowIndex)#HACK: Extract the internal xlwt cell representation.
        if not row: return None
        cell = row._Row__cells.get(colIndex)
        return cell
 
    
    previousCell = _getOutCell(outSheet, col, row)# HACK to retain cell style.
    outSheet.write(row, col, value)# END HACK, PART I
    if previousCell:# HACK, PART II
        newCell = _getOutCell(outSheet, col, row)
        if newCell:
            newCell.xf_idx = previousCell.xf_idx

#print type(wb)
#get first sheet
outsheet=wb.get_sheet(0)
for rr in(rows-2):
    row=rr+2
    outsheet.write(row,6,datetime.datetime.strptime(filedate, '%Y-%m-%d'),dateFormat)
    outsheet.write(row,7,datetime.datetime.strptime(filedate, '%Y-%m-%d'),dateFormat)


#print type(sheet)
#os.remove(filename)
wb.save(filename)
print("写入成功")
