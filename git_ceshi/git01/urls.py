# _*_coding : uft-8 _*_
# @Time : 2023/3/13 17:40
# @Author : 
# @File : urls
# @Project : git_ceshi
"""在app里添加urls路径进行分类"""
from django.urls import path
from git01.views import index
# 固定写法 urlpatterns = []
urlpatterns = [
    path('index/', index)
]
