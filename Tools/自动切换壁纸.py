#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/3 15:33
# @Author  : Aquarius
# @File    : 自动切换壁纸.py
# @Software: PyCharm
# @QQ      : 1903257388

import random
import ctypes
import time
import os

path = "C:\\Users\\dar\\Desktop\\Tool\\background\\" # 本地图片库

while True:
    file = os.listdir(path)  # 打开存储图片文件夹中的图片目录
    filepath = path + random.choice(file)  # 随机选取某张图片，建立绝对地址
    ctypes.windll.user32.SystemParametersInfoW(20, 0, filepath, 0)  # 设置桌面壁纸
    time.sleep(60)  # 壁纸切换时间：60秒
