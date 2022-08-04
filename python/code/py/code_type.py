#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
import sys
import chardet

############## 倒计时函数 ##################
def Windows_close(close_times):
    for x in range(close_times,-1,-1):
        mystr = "程序执行完毕！窗口将在" + str(x) + "秒后关闭！！！"
        print(mystr,end = "")
        print("\b" * (len(mystr)*2),end = "",flush = True)
        time.sleep(1)

############ 格式识别函数 ##################
def fileListFunc(filePathList):
    with open('./code_type.csv','w') as rf:
        rf.write("编码格式,精准度,文件路径\r")
        for filePath in filePathList:
            i = 0
            for top, dirs, nondirs in os.walk(filePath):
                for item in nondirs:
                    home_path = os.path.join(top, item).replace('\\','/')
                    with open(home_path ,'rb') as f:
                        data = f.read()
                    rf.write(str(chardet.detect(data).get("encoding"))+","+str(chardet.detect(data).get("confidence"))+","+str(home_path)+"\r")

home = os.getcwd().replace('\\','/') + '/'#获取当前工作目录
filePathtext = sys.argv[1].replace('\\','/')
filePathList = filePathtext.split(',')
fileListFunc(filePathList)

print("格式识别已全部完成,请到以下路劲中查看识别结果："+str(home)+"code_type.csv")
Windows_close(60)
