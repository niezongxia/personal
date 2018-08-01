#decide.py coding=utf-8
import os
import re
import sys
import zipfile
import shutil

hdir = sys.argv[4]
batch = sys.argv[1]
input_file = sys.argv[2]
file_path = sys.argv[3]
tdir=hdir+"batch/"+batch
restr =u'^MLIFE版本提交checklist.xlsx|安装手册.doc|程序完成清单.xlsx|软件产品版本说明书.doc|下发清单.xls|.sql|.war|.jar|.war.zip|.doc|.docx|.xls|.xlsx|.ppt|mlifeWeb.zip|AppServer.zip|AppPrj.zip|paidNotice.jar|AppPay.zip|AppLt.zip|回退.sql|回滚.sql|rollback.sql|return.sql|rollback'
restr1 =u'^MLIFE版本提交checklist.xlsx|安装手册.doc|程序完成清单.xlsx|软件产品版本说明书.doc|下发清单.xls'
restr2 =u'^war.zip|.war|.jar'
restr3 =u'^回退.sql|回滚.sql|rollback.sql|return.sql|rollback'
restr4 =u'^mlifeWeb.zip|AppServer.zip|AppPrj.zip|paidNotice.jar|AppPay.zip|AppLt.zip'
restr5 =u'^ppt|.doc|.docx|.xls|.xlsx'
restr6 ='.sql'

if os.path.exists(tdir)==True:
    ls=os.listdir(tdir)
    for l in ls:
        s=os.path.join(tdir,l)
        if os.path.isdir(s):
            if s.lstrip().startswith(hdir+"batch/"):
                s1=s.replace("\\","/").split("/")
                c_dir=s1[7]
else:
    os.makedirs(tdir)
    ls=os.listdir(tdir)
    for l in ls:
        s=os.path.join(tdir,l)
        if os.path.isdir(s):
            if s.lstrip().startswith(hdir+"batch/"):
                s1=s.replace("\\","/").split("/")
                c_dir=s1[7]

if re.search(restr,input_file)==None:
    azip=zipfile.ZipFile(file_path)
    azip.extractall(tdir)
    print("解压成功，若需删除文件，请联系管理员！")
elif re.search(restr1,input_file)!=None:
    shutil.copyfile(file_path,tdir+"/"+c_dir+"/"+input_file)
    print("文档已存档！")
elif re.search(restr2,input_file)!=None:
    shutil.copyfile(file_path,tdir+"/"+c_dir+"/"+"执行码/war/"+input_file)
    print("执行码已存档！")
elif re.search(restr3,input_file)!=None:
    if os.path.exists(tdir+"/"+c_dir+"/"+"执行码/回滚")==True:
        shutil.copyfile(file_path,tdir+"/"+c_dir+"/"+"执行码/回滚/"+input_file)
        print("回滚sql已存档！")
    else:
        os.makedirs(tdir+"/"+c_dir+"/"+"执行码/回滚")
        shutil.copyfile(file_path,tdir+"/"+c_dir+"/"+"执行码/回滚/"+input_file)
        print("回滚sql已存档！")
elif re.search(restr4,input_file)!=None:
    shutil.copyfile(file_path,tdir+"/"+c_dir+"/"+"源代码/"+input_file)
    print("源码已存档！")
elif re.search(restr5,input_file)!=None:
    shutil.copyfile(file_path,tdir+"/"+c_dir+"/"+"文档/"+input_file)
    print("需求文档已存档！")
elif re.search(restr6,input_file)!=None:
    if os.path.exists(tdir+"/"+c_dir+"/"+"执行码/sql")==True:
        shutil.copyfile(file_path,tdir+"/"+c_dir+"/"+"执行码/sql/"+input_file)
        print("执行sql已存档！")
    else:
        os.makedirs(tdir+"/"+c_dir+"/"+"执行码/sql")
        shutil.copyfile(file_path,tdir+"/"+c_dir+"/"+"执行码/sql/"+input_file)
        print("执行sql已存档！")
else:
    print("执行失败")
