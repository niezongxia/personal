#test_1.py
import os,sys
from ftplib import FTP

def ftp_open(host,user,pwd):
    ftp=FTP()
    ftp.set_debuglevel(2)
    ftp.connect(host)
    ftp.login(user,pwd)
    print(ftp.getwelcome())
    ftp.cwd('/ydweb/war')
    bufsize=-1
    return ftp
def ftp_up(ftp,filename):
    file_handler=open(filename,'rb')
    ftp.storbinary('STOR %s' %os.path.basename(filename),file_handler)
    file_handler.close()
    print("ftp up done.")
def ftp_close(ftp):
    ftp.set_debuglevel(0)
    ftp.quit()
def file_ls(path):
    ls=os.listdir(path)
    for i in ls:
        cur_path=os.path.join(path,i)
        if os.path.isdir(cur_path):
            file_ls(cur_path)
        else:
            c_path=cur_path.replace("\\","/")
            print(c_path)
            ftp_up(ftp,c_path)
            os.remove(c_path)
ftp=ftp_open(sys.argv[1],sys.argv[2],sys.argv[2])
file_ls(sys.argv[3])
ftp_close(ftp)
