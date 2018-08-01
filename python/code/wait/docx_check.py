#docx_check.py
import docx
from docx import Document
import os
import sys
import zipfile
import pickle
import re
import codecs
import string
import shutil
from win32com import client as wc




azip=zipfile.ZipFile("MLIFE-APPS_V01.00_B144.zip")
#a=azip.read("")
azip.extractall()#"D:/users/desktop/do/"

home="C:/Users/NZX/Desktop/test"
path=home+"/MLIFE-APPS_V01.00_B144/执行码/"
ls=[]
for cpath in os.listdir(path):
    ls.extend(os.listdir(path+cpath))
print (ls)
print('\n')

def doc2docx(doc_name,docx_name):
    try:
        word=wc.DispatchEx("word.Application")
        doc=word.Documents.Open(doc_name)
        doc.SaveAs(docx_name,16)
        doc.Close()
        word.Quit()
    except:
        pass
if __name__ == '__main__':
    doc2docx(home+'/test/MLIFE-APPS_V01.00_B144/安装手册.doc',home+'/test/MLIFE-APPS_V01.00_B144/安装手册.docx')

file=docx.Document(home+'/test/MLIFE-APPS_V01.00_B144/安装手册.docx')
filer='check.txt'

list=[]
lst=[]
for para in file.paragraphs:
    list.append(para.text)

str=['cp','lrt']

flr=open(filer,'w')
for y in str+ls:
    c=[i for i,x in enumerate(list) if x.find(y)!=-1]
    for t in c:
        flr.write(list[t]+'\n')
        print(list[t]+'\n')
        lst.append(list[t])
    flr.write('/n')
    print('\n')
flr.close()

cur_path = home+'/test/MLIFE-APPS_V01.00_B144/安装手册.docx'
def del_file(path):
    ls=os.listdir(path)
    for i in ls:
        c_path=os.path.join(path,i)
        if os.path.isdir(c_path):
            del_file(c_path)
        else:
            os.remove(c_path)
del_file(cur_path)
print(' clear done!')
