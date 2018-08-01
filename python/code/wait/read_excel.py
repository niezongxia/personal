#read_excel.py
import xlrd

fname="C:/Users/NZX/Desktop/test.xls"

rbook=xlrd.open_workbook(fname)

#row_value=xls_sheet.row_values(num-1)
#cow_value=xls_sheet.col_values(num-1)


rows=rbook.sheets()[0].nrows#获取已有行数
cols=rbook.sheets()[0].ncols#获取已有列数



for row in rows:
    value=rbook.cell_value(row,1)
    print(value)
