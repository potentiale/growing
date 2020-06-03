#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/30 21:06
# @Author  : Aquarius
# @File    : 百度文库抓取.py
# @Software: PyCharm

import requests
import re, json
from docx import Document

# 目标：免费抓取百度文库。

url = input("请输入下载文章链接：")
# session
sess = requests.Session()
# 主页面请求
sess = sess.get(url)
title = re.search('id="doc-tittle-0">(.*?)<',sess.text).group(1)
# 找到 WkInfo.htmlUrls
res = re.search(r"WkInfo.htmlUrls = '(.*?)'", sess.text).group(1)
# 去掉干扰数据
res = res.replace('\\x22','\"')
# 数据格式化->字典
data = json.loads(res)
# 保存论文正文
result = ''
document = Document()
# 遍历列表
for sku in data['json']:
    url = sku['pageLoadUrl']
    # 去掉url干扰数据
    url = url.replace('\\', '')
    # 请求正文内容
    data = requests.get(url).content.decode('utf-8')
    # 提取正文
    res = re.search(r'wenku_\d*\((.*)\)',data,re.S).group(1)
    content = json.loads(res)
    try:
        for cont_data in content['body']:
            if cont_data['t'] == 'word':
                # 统一文本格式
                result += str(cont_data.get('c'))
    except:
        print('文件解析错误')
document.add_paragraph(result)
document.save(title+'.docx')
print('文件保存成功')

