# _*_coding : uft-8 _*_
# @Time : 2023/3/21 17:34
# @Author : 
# @File : urls
# @Project : django_git02
from django.urls import path
from django02.views import create_book, shop, register, json, response, redirect_, set_cookie, get_cookie, set_session, \
    get_session,login

from django02.views import LoginView,OrderView

# from django.urls import converters  # <转换器名称：变量名> 转换器会对变量数据进行正则的验证
from django.urls.converters import register_converter


# 1、定义转换器
class MobileConverter:
    # 验证数据的关键是正则
    regex = '1[3-9]\d{9}'

    # 验证没有问题的数据给视图函数
    def to_python(self, value):
        return int(value)

    # 将匹配结果用于反向解析传值时使用
    def to_url(self, value):
        return str(value)


# 2、注册转换器
'''
    converter：转换器的类 
    type_name：转换器的名字
'''
register_converter(MobileConverter, 'tel')

urlpatterns = [
    path('create/', create_book),
# 3、调用转换器
    path('<int:city_id>/<tel:shop_id>/', shop),  # <转换器名称：变量名>
    path('register/', register),
    path('json/', json),
    path('res/', response),
    path('req/', redirect_),
    path('set_cookie/', set_cookie),
    path('get_cookie/', get_cookie),
    path('set_session/', set_session),
    path('get_session/', get_session),
    path('login/', login),
    # 类试图引导
    path('163login/', LoginView.as_view()),
    path('order/', OrderView.as_view()),
]
