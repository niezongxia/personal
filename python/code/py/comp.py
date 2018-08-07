#unzip.py
import os,sys,zipfile

def file_ls(uat,sp):
    a=[]
    b=[]
    file=sys.argv[3]+'/'+'uplog.txt'
    uls=os.listdir(uat)
    sls=os.listdir(sp)
    for k in uls:
        filenamef=os.path.join(uat,k)
        azip=zipfile.ZipFile(filenamef)
        a=a+azip.namelist()
    for v in sls:
        filenamed=os.path.join(sp,v)
        bzip=zipfile.ZipFile(filenamed)
        b=b+bzip.namelist()
    difz=set(set(b)^set(a))&set(b)
    difj=set(set(b)^set(a))&set(a)

    c=str(a)[1:len(str(a))-1]
    d=str(difz)[1:len(str(difz))-1]
    f=str(difj)[1:len(str(difj))-1]

    if set(b)^set(a)==set():
        print('内容无变化。\n')
        fobj=open(file,'w')
        fobj.write('内容无变化。\n')
        fobj.close()
    else:
        print ('与uat版本相比：<br />缺失：<br />'+f.replace(',','<br />')+'<br />'+'新增：<br />'+d.replace(',','<br />')+'<br />')
        fobj=open(file,'w')
        fobj.write('与uat版本相比：\n缺失：\n'+f.replace(',','\n')+'\n'+'新增：\n'+d.replace(',','\n')+'\n')
        fobj.close()
    print ('\nuat目录：\n'+c.replace(',','\n'))
    fobj=open(file,'a')
    fobj.write('\nuat目录：\n'+c.replace(',','\n'))
    fobj.close()

    azip.close()
    bzip.close()


file_ls(sys.argv[1],sys.argv[2])

