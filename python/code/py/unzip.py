#unzip.py
import sys
import os
import zipfile

azip=zipfile.ZipFile(sys.argv[1]).decode("utf-8")
#a=azip.read("")
azip.extractall("C:/xampp/htdocs/ewm/ins/batch/"+sys.argv[2])
