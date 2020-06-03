#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import threading
import multiprocessing
import json
import time
import os


class Img:
    def __init__(self, cate1, cate2, name='', url=''):
        self.cate1 = cate1
        self.cate2 = cate2
        self.name = name
        self.url = url

    def __str__(self):
        return '{}-{}:{}:{}'.format(self.cate1, self.cate2, self.name, self.url)

    __repr__ = __str__


class CrawlImg:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
        }

    def get_cate(self):
        data = {'parentId': '1'}
        self.headers['Referer']='https://www.ssyer.com/cate/1'
        self.headers['Content-Type']='application/json'
        url = "https://www.ssyer.com/apis/30001"
        response = requests.post(url=url,headers=self.headers, data=json.dumps(data))
        data = response.json()
        result = []
        if data['code'] == 200:
            for sku in data['data']:
                res = {}
                res['tagname'] = []
                res['cateId'] = sku['id']
                res['catename'] = sku['name']
                for i in sku['tags']:
                    res['tagname'].append(i['name'])
                result.append(res)
        return result

    def get_ajax(self,data):
        url = "https://www.ssyer.com/apis/20001"
        for i in range(1,21):
            cateId = data['cateId']
            for tagname in data['tagname']:
                req_data = {
                    'cateId': '1',
                    'order': '2',
                    'page': {'showCount': '20', 'currentPage': str(i)},
                    'currentPage': '1',
                    'showCount': '20',
                    'recommendType': '1',
                    'subCateId': cateId,
                    'tagName': "%s"%tagname,
                }
                self.headers['Referer'] = 'https://www.ssyer.com/cate/1'
                self.headers['Content-Type'] = 'application/json'
                tagdata = requests.post(url=url,headers=self.headers,data=json.dumps(req_data))
                data = tagdata.json()
                for sku in data['data']:
                    img_name = sku['title'].replace('/','_')
                    subCateName = sku['subCateName']
                    print(img_name)
                    self.get_img(url=sku['showUrl'],img_name=img_name,subCateName=subCateName)


    def get_img(self, url,img_name,subCateName):
        req = requests.get(url=url, headers=self.headers)
        img_type = url.split('.')[-1]
        self.save_img(data=req.content,img_name=img_name,img_type=img_type,subCateName=subCateName)

    def save_img(self, data,img_name,img_type,subCateName):
        folder = os.path.exists('img/%s'%(subCateName))
        if not folder:
            os.makedirs(f'img/{subCateName}')
        with open('./img/%s/%s.%s'%(subCateName,img_name,img_type),'wb') as f:
            f.write(data)



    @staticmethod
    def thread_download():
        """多线程抓取"""
        pass


if __name__ == '__main__':
    # 初始化
    InFo = CrawlImg()
    show_list = CrawlImg().get_cate()
    while True:
        print("--------SSYER Spider--------")
        print(" | ".join([name['catename'] for name in show_list]))
        catename = input("输入需要抓取的类目：")
        folder = os.path.exists('img/%s' % catename)
        if folder:
            print("相册已存在")
            continue
        for sku in show_list:
            time.sleep(0.3)
            if catename == sku['catename']:
                InFo.get_ajax(sku)


