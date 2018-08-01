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
    return ftp
def ftp_up(ftp,filename):
    file_handler=open(filename,'rb')
    ftp.storbinary('STOR %s' %os.path.basename(filename),file_handler)
    file_handler.close()
    print("ftp up done.")
def ftp_close(ftp):
    ftp.set_debuglevel(0)
    ftp.quit()
ftp=ftp_open(sys.argv[1],sys.argv[2],sys.argv[2])
ftp_up(ftp,sys.argv[3])
ftp_close(ftp)
