#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/26 18:45
# @Author  : Aquarius
# @File    : main.py
# @Software: PyCharm

import datetime
import re
import sys
import time
import requests
from selenium import webdriver


class QQManagement(object):
    def __init__(self, qq, cookie):
        self.writer = open('result.txt', 'w+', newline='', encoding='gbk')
        self.sess = requests.Session()
        cookies = {
            "cookie": cookie,
        }
        self.bkn = ''
        self.sess.cookies.update(cookies)
        self.headers = {
            "referer": "https://qun.qq.com/member.html",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36",
        }
        self.req = webdriver.Chrome()
        self.qq = qq
        self.now_day = datetime.datetime.now().strftime('%Y%m%d')

    def main(self):
        """
        selenium登录站点，获取cookies并更新Session
        :return: None
        """
        self.req.get("https://qun.qq.com/index.html")
        print('首页访问')
        self.req.find_element_by_class_name("user-info").click()
        iframe = self.req.find_element_by_tag_name("iframe")
        self.req.switch_to_frame(iframe)
        # 登录。电脑需要提前登录账号
        self.req.find_element_by_id("img_out_" + self.qq).click()
        # 退出iframe标签
        self.req.switch_to.default_content()

        cookie = self.req.get_cookies()
        self.req.close()
        cookies = {}
        for item in cookie:
            cookies[item['name']] = item['value']
        print(cookies)
        self.sess.cookies.update(cookies)
        self.bkn = self.sess.cookies
        self.bkn = self.get_bkn(self.bkn['cookie'])
        # 获取创建群和管理群信息
        group_sum = self.get_group_id()
        # 遍历群组提取详细信息
        for sku in group_sum:
            time.sleep(0.5)
            max_people = self.get_max_group(sku['gc'])
            self.writer.write("# " + sku['gn'] + "# " + str(sku['gc']) + "\n")
            self.writer.write("# QQ,# 入群时间\n")
            print('\n正在下载群组：', sku['gn'], '群组人数：', max_people)
            self.get_group_data(sku['gc'], max_people)

    def get_bkn(self, cookie):
        """
        计算bkn值保持登录状态
        :param cookie:
        :return:
        """
        re_skey = re.findall(r'; skey=(.*?);', cookie)
        import execjs
        js = """function csrftest(skey) {
            var e = skey;
            if (e) {
                for (var t = 5381, r = 0, n = e.length; r < n; ++r)
                    t += (t << 5) + e.charAt(r).charCodeAt();
                return 2147483647 & t
            }}
        """
        try:
            bkn = execjs.compile(js).call('csrftest', re_skey[0])
            return bkn
        except:
            print("登陆失败")
            sys.exit()

    def get_max_group(self, group_gc):
        """
        群组最大人数统计
        :param group_gc: 群号
        :return: 最大人数
        """
        group_url = 'https://qun.qq.com/cgi-bin/qun_mgr/search_group_members'
        group_data = {
            'gc': group_gc,
            'st': '0',
            'end': '20',
            'sort': '0',
            'bkn': self.bkn,
        }
        greq = self.sess.post(url=group_url, data=group_data)
        try:
            page = greq.json()
            search_count = page['search_count']
            return search_count
        except Exception as e:
            print("群组人数解析失败...请隔一段时间后重新登录。")
            print("ErrorInformation:", e)
            sys.exit()

    def get_group_data(self, gc, max_people):
        """
        获取群成员详细信息
        :param end:群成员人数 <int>
        :return:
        """
        group_url = 'https://qun.qq.com/cgi-bin/qun_mgr/search_group_members'

        if max_people % 20 != 0:
            max_people = max_people + 20
        st = 0
        for end in range(20, max_people, 20):
            time.sleep(0.3)
            group_data = {
                'gc': gc,
                'st': st,
                'end': end,
                'sort': '0',
                'bkn': self.bkn,
            }
            st = end
            greq = self.sess.post(url=group_url, data=group_data)
            try:
                page = greq.json()
                for sku in page['mems']:
                    self.writer.write(
                        str(sku.get('uin')) + ',' + str(self.timestamp_to_format(sku.get('join_time'))) + "\n")
            except Exception as e:
                print("群成员详细信息解析失败...请隔一段时间后重新登录。")
                print("ErrorInformation:", e)
                sys.exit()

    def get_group_id(self):

        """
        获取管理群和创建群
        :return:
        """
        url = 'https://qun.qq.com/cgi-bin/qun_mgr/get_group_list'
        data = {
            'bkn': str(self.bkn)
        }
        req = self.sess.post(url=url, data=data)
        try:
            rdata = req.json()
            print(rdata)
        except Exception as e:
            print("Bkn数据解析失败...请隔一段时间后重新登录。")
            print(req.text)
            print("ErrorInformation:", e)
            sys.exit()

        create_list = rdata.get('create')
        manage_list = rdata.get('manage')

        group_list = []
        group_list.extend(create_list)
        group_list.extend(manage_list)
        return group_list

    def timestamp_to_format(self, timestamp=None, format='%Y-%m-%d'):
        """
        时间戳转换格式
        :param timestamp:时间戳 <int>
        :param format: 时间格式 <str>
        :return: 时间格式 <str>
        """
        if timestamp:
            time_tuple = time.localtime(timestamp)
            res = time.strftime(format, time_tuple)
        else:
            res = time.strftime(format)
        return res


if __name__ == '__main__':
    qq_uin = input("qq号：")
    # 需要使用网页登录后 Ajax 请求的cookie。本文中Cookies参数未完全自动处理
    cookie = input("cookie：")
    QQManagement(qq_uin, cookie).main()
