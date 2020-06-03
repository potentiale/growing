#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/25 21:16
# @Author  : Aquarius
# @File    : 图片经纬度解析.py
# @Software: PyCharm

import jsonpath as jsonpath
import requests
import exifread

def func(la, lo, LaRef, LoRef):
    # 维度计算
    LatRef = LaRef.printable
    Lat = la.printable[1:-1].replace(" ", "").replace("/", ",").split(",")
    Lat = float(Lat[0]) + float(Lat[1]) / 60 + float(Lat[2]) / float(Lat[3]) / 3600
    if LatRef != "N":
        Lat = Lat * (-1)
    # 经度计算
    LonRef = LoRef.printable
    Lon = lo.printable[1:-1].replace(" ", "").replace("/", ",").split(",")
    Lon = float(Lon[0]) + float(Lon[1]) / 60 + float(Lon[2]) / float(Lon[3]) / 3600
    if LonRef != "E":
        Lon = Lon * (-1)
    return Lat, Lon

def get_info(lat, lng):
    '''
     注意 网站的经纬度接口格式是 h.mmsssssss
    :param lat:  纬度
    :param lng:  经度
    :return: 返回地址信息
    '''
    url = r'http://www.gpsspg.com/apis/maps/geo/?output=json&lat={}&lng={}&type=0&callback=jQuery110209178036150146593_1559380618496&_=1559380618502'.format(lat, lng)
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
        'Referer': 'http://www.gpsspg.com/iframe/maps/baidu_181109.htm?mapi=1',
        'Host': 'www.gpsspg.com',
    }
    r = requests.get(url, headers=headers)
    # 返回的是一个json字符串文本 使用 r.json()方法 转化为python字典
    info = r.json()
    print(info)
    # 使用jsonpath 查找地址信息
    address = jsonpath.jsonpath(info, '$..address')[0]
    print(address)

def FindGPS(Filepath):
    f = open(Filepath, 'rb')
    tags = exifread.process_file(f)
    print(tags)# 原始数据
    print('GPS纬度参考:', tags['GPS GPSLatitudeRef'])
    LatRef = tags['GPS GPSLatitudeRef']
    la = tags['GPS GPSLatitude']
    print('GPS经度参考:', tags['GPS GPSLongitudeRef'])
    LonRef = tags['GPS GPSLongitudeRef']
    lo = tags['GPS GPSLongitude']
    Lat, Lon = func(la, lo, LatRef, LonRef)
    print('GPS经纬度:', Lat, Lon)
    print('GPS GPS高度:', tags['GPS GPSAltitude'])
    print('GPS日期:', tags['GPS GPSDate'])
    get_info(Lat,Lon)
    print(Lat, Lon)


if __name__ == '__main__':
    FindGPS('图片名.jpg')
