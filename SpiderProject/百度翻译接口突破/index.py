#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/18 16:37
# @Author  : Aquarius
# @File    : index.py
# @Software: PyCharm

import requests
import json
import execjs
import re
indata = input("输入(退出：q)：")
while True:
    if indata =='q':
        break
    data = re.findall("[\u4e00-\u9fa5]+",indata)  # 匹配中文
    if data:
        fdata = 'zh'
        tdata = 'en'
    else:
        fdata = 'en'
        tdata = 'zh'

    url = "https://fanyi.baidu.com/v2transapi"
    headers = {
        "cookie": "BIDUPSID=53A638832F0884CDA112B4824704BCF6; PSTM=1588675530; BAIDUID=53A638832F0884CD52EF49925859DDBE:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDUSS=Wp2S2JsRGZIWVdCSFZNV2g4ZmtibHp3a25QTWkzZWNhRHhycFJaTloya1kwOXhlRVFBQUFBJCQAAAAAAAAAAAEAAADH0YVLyM7M7DE1MTMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABhGtV4YRrVeV; MCITY=-158%3A; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; H_PS_PSSID=31357_1449_31670_21114_31253_31592_31606_31271_31463_30823_26350; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1589790194,1589790765,1589867270,1589867665; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1589867665; yjs_js_security_passport=9cd83fd9915d5c42020d8512d5ebbf3c499d705c_1589867673_js; delPer=0; PSINO=6",
        "referer": "https://fanyi.baidu.com/",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36",
    }

    urldata = {"from": fdata,"to": tdata}

    with open('baidu.js') as f:
        jsdata = f.read()
    sign = execjs.compile(jsdata).call("e",indata)
    data = {
        "from": fdata,
        "to": tdata,
        "query": indata,
        "transtype": "realtime",
        "simple_means_flag": "3",
        "sign": sign,
        "token": "26a496d671c84dfeb5abd8ef56679dc6",
        "domain": "common",
    }

    req = requests.post(url=url, headers=headers, data=data, params=json.dumps(urldata))
    res = req.json()['trans_result']['data'][0]['dst']
    print("翻译：", res)
