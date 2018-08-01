#!/usr/bin/env python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
 
sender = 'system@bocforms.com'
receivers = ['system@bocforms.com','chejingwen@bocforms.com','hanlidong@bocforms.com','duanzengzheng@bocforms.com','guoduanzheng@bocforms.com','hjf@bocforms.com','zhangshan@bocforms.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
 
#创建一个带附件的实例
message = MIMEMultipart()
message['From'] = Header("system@bocforms.com", 'gbk')
message['To'] =  Header("黄俊峰,车静文,韩力冬,郭端正,段曾争,张山", 'gbk')
message['Subject'] = Header('war包发包记录<系统邮件，请勿回复>', 'gbk')
'''
#同步计数
fns=['backup_result.txt','backup.bat']
lst=[]
for fn in fns:
    s=open(fn,'r').read()
    done=s.count('update done.')
    lst.append(done)
fna='backup_result.txt'
t=open(fna,'r').read()
do1=t.count('Committed revision')
do2=t.count('Copied properties for revision')
if do1==do2:
    do=do1
else:
    do='update error'
'''
#邮件正文内容
message.attach(MIMEText('各位，\n      附件为war包发包记录，请查阅。\n\n'))#+"本次同步版本库总数: %s 个；" % lst[1]+'\n\n'+"同步成功: %s 个；" % lst[0]+'\n\n'+"总提交次数：  %s  ；" % do+'\n\n详情请查阅附件！', 'plain', 'gbk'))

lj='D:/SVN/test/auto_test_plan/'
fnames=['war_install_record_report.xls']
for fname in fnames:
    att = MIMEText(open(lj+fname, 'rb').read(), 'base64', 'gbk')
    att["Content-Type"] = 'application/octet-stream'
# 这里的filename直接引用附件文件名
    att["Content-Disposition"] = 'attachment;filename='+fname
    message.attach(att)

try:
    smtpObj = smtplib.SMTP_SSL('22.11.236.164',465)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print ("邮件发送成功")
except smtplib.SMTPException:
    print ("Error: 无法发送邮件")

