#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/18 12:18
# @Author  : Aquarius
# @File    : urls.py
# @Software: PyCharm


from django.urls import path
from . import views
app_name = 'index'

urlpatterns = [
    path('', views.index, name="index"),
    path('book/<str:article_cate>/', views.book, name="book"),
    path('tech/<str:article_cate>/', views.tech, name="tech"),
    path('edit/<int:article_id>/', views.edit_page, name='edit'),
    path('edit/action/', views.edit_action, name='edit_action'),
    path('article/<int:article_id>/', views.text_page, name='article_page'),
]



