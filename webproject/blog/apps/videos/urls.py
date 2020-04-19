#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/23 12:03
# @Author  : Aquarius
# @File    : urls.py
# @Software: PyCharm


from django.urls import path
from . import views
app_name = 'index'

urlpatterns = [
    path('index/', views.index, name="index"),
    path('face/', views.face, name="face"),
    path('phone/', views.phone, name="phone"),
]










