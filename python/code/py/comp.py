#unzip.py
import os,sys,zipfile

filenamef=sys.argv[1]
filenamed=sys.argv[2]
file=sys.argv[3]+'/'+'uplog.txt'

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
    fobj=open(file,'w')
    fobj.write('内容无变化。\n')
    fobj.close()
else:
    print ('与本批次首次发布的版本相比：<br />缺失：<br />'+f.replace(',','<br />')+'<br />'+'新增：<br />'+d.replace(',','<br />')+'<br />')
    fobj=open(file,'w')
    fobj.write('与本批次首次发布的版本相比：\n缺失：\n'+f.replace(',','\n')+'\n'+'新增：\n'+d.replace(',','\n')+'\n')
    fobj.close()
print ('<br />首次目录：<br />'+c.replace(',','<br />'))
fobj=open(file,'a')
fobj.write('\n首次目录：\n'+c.replace(',','\n'))
fobj.close()

azip.close()
bzip.close()
