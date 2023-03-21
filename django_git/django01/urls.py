# _*_coding : uft-8 _*_
# @Time : 2023/3/15 18:01
# @Author : 
# @File : urls
# @Project : django_git
from django.urls import path
from django01.views import index, index_add, revise, delete,get_query,count

urlpatterns = [
    path('index/', index),
    path('add/', index_add),
    path('revise/', revise),
    path('delete/', delete),
    path('get/', get_query),
    path('count/', count),
]
