#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/23 16:01
# @Author  : Aquarius
# @File    : face.py
# @Software: PyCharm
import json

import requests
import base64


class face_model:
    client_id = 'w7lGqHQrCrFqvSVVQgtukdzo'
    client_secret = 'Nkn6LCPu9wCEWDwLwR9yuWzYEiaigYSq'

    def __init__(self, filepath):
        self.filepath = filepath

    def get_token(self):
        host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=%s&client_secret=%s' % (
            self.client_id, self.client_secret)
        response = requests.get(host)
        if response:
            res = response.json()
            return res['access_token']

    def get_img_con(self):
        f = None
        try:
            f = open(self.filepath, 'rb')
            img = base64.b64encode(f.read())
            # print(img)
            return img
        except:
            print('read image file fail')
            return None
        finally:
            if f:
                f.close()

    def get_face(self):
        # img_content = self.filepath
        img_content = self.filepath
        request_url = "https://aip.baidubce.com/rest/2.0/face/v3/detect"
        print('图片接收信息：', img_content)
        params = {
            "image": img_content,
            "image_type": "BASE64",
            "face_field": "age,gender,race,emotion,mask",
        }
        access_token = self.get_token()
        request_url = request_url + "?access_token=" + access_token
        headers = {'content-type': 'application/json'}
        response = requests.post(request_url, data=params, headers=headers)
        if response:
            res = response.json()
            return res
# if __name__ == '__main__':
#     a = {'error_code': 0, 'error_msg': 'SUCCESS', 'log_id': 1016594001843, 'timestamp': 1584957631, 'cached': 0, 'result': {'face_num': 1, 'face_list': [{'face_token': '1d9f3b5e752d4864b8d1f2987571c39f', 'location': {'left': 222.69, 'top': 163.44, 'width': 132, 'height': 140, 'rotation': -2}, 'face_probability': 1, 'angle': {'yaw': -8.8, 'pitch': 6.22, 'roll': -5}, 'age': 22, 'gender': {'type': 'male', 'probability': 1}, 'race': {'type': 'yellow', 'probability': 1}, 'emotion': {'type': 'neutral', 'probability': 1}, 'mask': {'type': 0, 'probability': 1}}]}}
#     print(json.dumps(a, indent=4))
#     a = face_model('test.jpg')
#     print(a.get_face())
