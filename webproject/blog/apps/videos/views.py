import base64
import json

from django.http import HttpResponse
from django.shortcuts import render
from .func.face import face_model
import re


# Create your views here.


def index(request):
    return render(request, 'video/demo.html')

def phone(request):
    return render(request, 'video/demo2.html')

def face(request):
    if request.method == 'POST':
        img = request.POST.get('image')
        print(img)
        print('长度：',len(img))
        # img_con = base64.b64decode(img[22:])
        if 'jpeg' in img[:25]:
            face = face_model(img[23:])  # 需要改为数据模式，不使用本地地址
        else:
            face = face_model(img[22:])
        res = face.get_face()
        print('结果返回值：')
        print(res)
        data = {}
        if res['error_msg'] == 'SUCCESS':
            data['error_msg'] = 'SUCCESS'
            for sku in res['result']['face_list']:
                data['id'] = sku['face_token']
                data['gender'] = '男' if sku['gender']['type'] == 'male' else '女'
                data['age'] = sku['age']
                emotion =  sku['emotion']['type']if sku['emotion']['type'] else 'neutral'
                em_data = {
                    'angry': '愤怒',
                    'disgust': '厌恶',
                    'fear': '恐惧',
                    'happy': '高兴',
                    'sad': '伤心',
                    'surprise': '惊讶',
                    'neutral': '无表情',
                    'pouty': '撅嘴',
                    'grimace': '鬼脸',
                }
                data['emotion'] = em_data[emotion]
                data['mask'] = '已佩戴' if sku['mask']['type'] == 1 else '未佩戴'
                return HttpResponse(json.dumps(data))
        else:
            data['error_msg'] = res['error_msg']
            return HttpResponse(json.dumps(data))

    return render(request, 'video/demo.html')
