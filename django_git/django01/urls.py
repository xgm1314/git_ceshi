# _*_coding : uft-8 _*_
# @Time : 2023/3/15 18:01
# @Author : 
# @File : urls
# @Project : django_git
from django.urls import path
from django01.views import index

urlpatterns = [
    path('index/', index)
]
