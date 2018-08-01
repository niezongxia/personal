#!/usr/bin/env python
#coding:utf-8
import os
import sys

cur_path = sys.argv[1]
def del_file(path):
    ls=os.listdir(path)
    for i in ls:
        c_path=os.path.join(path,i)
        if os.path.isdir(c_path):
            del_file(c_path)
        else:
            os.remove(c_path)
del_file(cur_path)
print(sys.argv[2]+' clear done!')
