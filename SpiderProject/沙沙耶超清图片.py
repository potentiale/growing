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
    # show_list = CrawlImg().get_cate()
    show_list = [
        {'tagname': ['手机壁纸', '电脑壁纸'],
         'cateId': 14,
         'catename': '壁纸'
         }, {'1': 'a', 'tagname': ['建筑', '街道', '城堡', '楼梯', '教堂', '电影院', '商场', '车站', '游乐场', '餐厅', '路', '桥'], 'cateId': 21, 'catename': '建筑空间'}, {'1': 'a', 'tagname': ['美女', '帅哥', '女人', '男人', '女孩', '男孩', '孩子', '老人', '肖像', '开心', '手'], 'cateId': 5, 'catename': '人物百态'}, {'1': 'a', 'tagname': ['电脑', '键盘', '手机', '桌面', '黑板', '照相机', '笔', '智能', '设备', '商业', '报纸'], 'cateId': 13, 'catename': '商业办公'}, {'1': 'a', 'tagname': ['天空', '云', '山', '田', '雪', '海', '日出', '日落', '沙滩', '草原', '沙漠', '森林', '悬崖', '瀑布', '岩石', '雪山', '山谷', '公园', '夜景', '草地', '烟花'], 'cateId': 9, 'catename': '自然风景'}, {'1': 'a', 'tagname': ['美食', '水果', '蔬菜', '面包', '柠檬', '南瓜', '苹果', '沙拉', '番茄', '辣椒', '酒'], 'cateId': 22, 'catename': '餐饮食物'}, {'1': 'a', 'tagname': ['汽车', '船', '飞机', '自行车', '帆船', '车', '车辆', '出租车', '面包车', '摩托车', '电车', '地铁', '运输', '指示牌'], 'cateId': 11, 'catename': '汽车交通'}, {'1': 'a', 'tagname': ['树', '叶', '花', '植物', '草', '绿色', '草坪', '玫瑰', '雏菊'], 'cateId': 4, 'catename': '植物摄影'}, {'1': 'a', 'tagname': ['猫', '狗', '鸟', '马', '猪', '鱼', '鹅', '蜗牛', '昆虫', '宠物', '水母', '蜜蜂', '骆驼', '大象', '兔子', '野生动物'], 'cateId': 7, 'catename': '动物摄影'}, {'1': 'a', 'tagname': ['家居', '书', '钱', '杯子', '台灯', '风筝', '信封', '箱包', '蜡烛', '玩具', '灯笼', '雨伞', '碗', '酒瓶', '口红', '瓶子'], 'cateId': 17, 'catename': '学习生活'}, {'1': 'a', 'tagname': ['户外', '运动', '球', '滑雪', '足球', '赛跑', '游戏', '体育', '游泳', '篮球', '棒球', '网球'], 'cateId': 16, 'catename': '户外运动'}, {'1': 'a', 'tagname': [], 'cateId': 12, 'catename': '其他'}]
    print(show_list)
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


