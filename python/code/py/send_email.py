#!/usr/bin/env python
import sys,smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
 
sender = 'system@bocforms.com'
if sys.argv[7]=='niezongxia':
    receivers = [sys.argv[7]+'@bocforms.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
else:
    receivers = [sys.argv[7]+'@bocforms.com','niezongxia@bocforms.com','hanlidong@bocforms.com','zhangshan@bocforms.com','duanzengzheng@bocforms.com','chejingwen@bocforms.com']
name={'niezongxia':'聂宗霞','dinghe':'丁鹤','litingting':'李婷婷','jiangzhen':'蒋朕','zhouliting':'周丽婷',"22.11.236.24":"聂宗霞","22.11.235.102":"韩力冬","22.11.235.59":"陈雷","22.11.236.168":"刘博","22.11.235.92":"罗海平","22.11.236.247":"解玉新","22.11.235.90":"林鹏鹏","22.11.235.71":"徐振楠"}
OPerT={'all':'全量部署','add':'增量部署'}

#创建一个带附件的实例
message = MIMEMultipart()
message['From'] = Header("system@bocforms.com", 'gbk')
message['To'] =  Header("admin", 'gbk')
message['Subject'] = Header('WAR package deployment!', 'gbk')

#邮件正文内容
if sys.argv[4] == "0":
	if sys.argv[8] in name.keys():
	    message.attach(MIMEText('部署环境：'+sys.argv[1]+'\n\n所属批次：'+sys.argv[2]+'\n\n部署方式：'+OPerT.pop(sys.argv[3])+'\n\n问题数：'+sys.argv[4]+'\n\n备注：'+sys.argv[6]+'\n\n主测：'+name.pop(sys.argv[7])+'\n\n开发者：'+name.pop(sys.argv[8])+'\n\n安装包下载链接：\n\n'+sys.argv[5], 'plain', 'gbk'))
	else:
	    message.attach(MIMEText('部署环境：'+sys.argv[1]+'\n\n所属批次：'+sys.argv[2]+'\n\n部署方式：'+OPerT.pop(sys.argv[3])+'\n\n问题数：'+sys.argv[4]+'\n\n备注：'+sys.argv[6]+'\n\n主测：'+name.pop(sys.argv[7])+'\n\n开发者：'+sys.argv[8]+'\n\n安装包下载链接：\n\n'+sys.argv[5], 'plain', 'gbk'))
else:
	if sys.argv[8] in name.keys():
	    message.attach(MIMEText('部署环境：'+sys.argv[1]+'\n\n所属批次：'+sys.argv[2]+'\n\n部署方式：'+OPerT.pop(sys.argv[3])+'\n\n问题数：'+sys.argv[4]+'\n\n问题描述：\n\n'+sys.argv[9].replace('ppppp','\n')+'\n\n备注：'+sys.argv[6]+'\n\n主测：'+name.pop(sys.argv[7])+'\n\n开发者：'+name.pop(sys.argv[8])+'\n\n安装包下载链接：\n\n'+sys.argv[5], 'plain', 'gbk'))
	else:
            message.attach(MIMEText('部署环境：'+sys.argv[1]+'\n\n所属批次：'+sys.argv[2]+'\n\n部署方式：'+OPerT.pop(sys.argv[3])+'\n\n问题数：'+sys.argv[4]+'\n\n问题描述：\n\n'+sys.argv[9].replace('ppppp','\n')+'\n\n备注：'+sys.argv[6]+'\n\n主测：'+name.pop(sys.argv[7])+'\n\n开发者：'+sys.argv[8]+'\n\n安装包下载链接：\n\n'+sys.argv[5], 'plain', 'gbk'))
##lj=sys.argv[9]
##fnames=['uplog.txt']
##for fname in fnames:
##    att = MIMEText(open(lj+fname, 'rb').read(), 'base64', 'gbk')
##    att["Content-Type"] = 'application/octet-stream'
### 这里的filename直接引用附件文件名
##    att["Content-Disposition"] = 'attachment;filename='+fname
##    message.attach(att)

try:
    smtpObj = smtplib.SMTP_SSL('22.11.236.164',465)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print ("已邮件通知测试！")
except smtplib.SMTPException:
    print ("Error: send fail.")
