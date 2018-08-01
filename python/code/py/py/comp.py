#unzip.py
import sys
import os
import zipfile

filenamef=sys.argv[1]
filenamed=sys.argv[2]

azip=zipfile.ZipFile(filenamef)
bzip=zipfile.ZipFile(filenamed)

a=azip.namelist()
b=bzip.namelist()


difz=set(set(b)^set(a))&set(b)
difj=set(set(b)^set(a))&set(a)

c=str(a)[1:len(str(a))-1]
d=str(difz)[1:len(str(difz))-1]
f=str(difj)[1:len(str(difj))-1]

if set(b)^set(a)==set():
    print('内容无变化。<br /><br />')
else:
    print ('与本批次首次发布的版本相比：<br />缺失：<br />'+f.replace(',','<br />')+'<br />')
    print ('新增：<br />'+d.replace(',','<br />')+'<br />')
print ('<br />首次目录：<br />'+c.replace(',','<br />'))

azip.close()
bzip.close()
