# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# File       : 合并ts文件并转化格式.py
# Time       ：2022/1/13 11:52
# Author     ：jieWei_yang
# version    ：python 3.7.9
# Description：
"""


import os
path='ts格式'

# files = os.listdir(path )
filePath = "./ts格式"
file_list = sorted(os.listdir(filePath))
with open("./JX.mp4", "wb+") as f:
    for file in file_list:
        print(file)
        f.write(open("./ts格式/"+file, "rb").read())


