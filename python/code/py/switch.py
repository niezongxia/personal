#switch.py
import sys
import pickle
import re
import codecs
import string
import shutil
from win32com import client as wc

def doc2docx(doc_name,docx_name):
    try:
        word=wc.DispatchEx("Word.Application")
        doc=word.Documents.Open(doc_name)
        doc.SaveAs(docx_name,16)#8:html;16:docx;11:xml
        doc.Close()
        word.Quit()
    except:
        pass
if __name__ == '__main__':
    doc2docx('D:/Users/Desktop/操作手册.doc','D:/Users/Desktop/do/安装手册.docx')
    
