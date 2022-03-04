# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# File       : 获取ts文件.py
# Time       ：2022/1/13 11:38
# Author     ：jieWei_yang
# version    ：python 3.7.9
# Description：
"""




import time
import os
import requests
import random

header = {
    'Referer': 'https://www.amazon.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
}

# https://www.amazon.com/vdp/0d4986d43b804dd9bc69332cf7ce7948?ref=dp_vse_rvc_1

for i in range(1,13):
    count=str(i).rjust(2,'0')
    url=f'https://m.media-amazon.com/images/S/vse-vms-transcoding-artifact-us-east-1-prod/4a7210ba-4bd1-4c82-b7a0-d011f8370c02/default.jobtemplate.hls360_000{count}.ts'
    file_name=url.split('/')[-1]
    print(file_name)
    with open(f'./ts格式/{file_name}', 'wb') as f:
        r = requests.get(url,   headers=header)
        r.raise_for_status()
        r.encoding = 'utf-8'
        f.write(r.content)
        time.sleep(2)


