#docx_check.py
import docx
from docx import Document
import os
import sys

path="D:/Users/Desktop/MLIFE-APPS_V01.00_B146/执行码/"
ls=[]
for cpath in os.listdir(path):
    ls.extend(os.listdir(path+cpath))
print (ls)
print('\n')

file=docx.Document('d:/users/desktop/do/安装手册.docx')
filer='check.txt'

list=[]
lst=[]
for para in file.paragraphs:
    list.append(para.text)

str=['cp','lrt','.sql']

flr=open(filer,'w')
for y in set(str+ls):
    c=[i for i,x in enumerate(list) if x.find(y)!=-1]
    for t in c:
        flr.write(list[t]+'\n')
        print(list[t]+'\n')
        lst.append(list[t])
    flr.write('/n')
    print('\n')
flr.close()
