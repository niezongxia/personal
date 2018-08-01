#write.py
import xlrd
import xlwt
from xlutils.copy import copy
import os
import sys
import datetime as dt

filename=sys.argv[1]#'C:/xampp/htdocs/ewm/ins/war_install_record_report.xls'#
OPerT={'all':'全量部署','add':'增量部署'}
name={'niezongxia':'聂宗霞','dinghe':'丁鹤','litingting':'李婷婷','jiangzhen':'蒋朕','zhouliting':'周丽婷'}
dateFormat=xlwt.XFStyle()
dateFormat.num_format_str='yyyy/mm/dd'

values=['date']

#open file
rb=xlrd.open_workbook(filename)#,formatting_info=True)
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
row=rows
for value in values:
    outsheet.write(0,7,'=SUM(F3:INDIRECT("f"&COUNTA(F:F)))')
    outsheet.write(0,5,'=DATEDIF(A3,INDIRECT("a"&COUNTA(A:A)),"d")')
    outsheet.write(0,3,'=countif(g:g,"c:/*")')
    outsheet.write(0,1,'=countif(g:g,"c:/*")/DATEDIF(A3,INDIRECT("a"&COUNTA(A:A)),"d")')
    outsheet.write(row,0,value)
    outsheet.write(row,0,dt.date.today(),dateFormat)
    outsheet.write(row,1,sys.argv[2])
    outsheet.write(row,2,sys.argv[3])
    outsheet.write(row,3,sys.argv[4])
    outsheet.write(row,4,OPerT.pop(sys.argv[5]))
    outsheet.write(row,5,int(sys.argv[6]))
    outsheet.write(row,6,sys.argv[7])
    outsheet.write(row,7,sys.argv[8])
    outsheet.write(row,8,sys.argv[9])
    outsheet.write(row,9,name.pop(sys.argv[10]))
    row+=1
#print type(sheet)
#os.remove(filename)
wb.save(filename)
print("写入成功")
