#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
import sys
import chardet

def fileListFunc(filePathList):
    with open('./code_type.csv','w') as rf:
        for filePath in filePathList:
            i = 0
            for top, dirs, nondirs in os.walk(filePath):
                for item in nondirs:
                    home_path = os.path.join(top, item).replace('\\','/')
                    with open(home_path ,'rb') as f:
                        data = f.read()
                    print(chardet.detect(data).get("encoding")+','+home_path)
                    rf.write(str(chardet.detect(data).get("encoding"))+","+str(home_path)+"\r")
filePathtext = sys.argv[1].replace('\\','/')
print(filePathtext)
filePathList = filePathtext.split(',')
print(filePathList)
fileListFunc(filePathList)
