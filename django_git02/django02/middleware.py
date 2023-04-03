# _*_coding : uft-8 _*_
# @Time : 2023/3/30 12:30
# @Author : 
# @File : middleware
# @Project : django_git02
from django.utils.deprecation import MiddlewareMixin

'''
中间件创建:请求(get)程序是由上往下执行中间件;响应(post)程序是由下往上执行中间件
'''


class TestMiddlewareMixin(MiddlewareMixin):
    def process_request(self, request):
        username = request.COOKIES.get('name')
        if username is None:
            print('没有用户信息')
        else:
            print('有用户信息')
        print('每次请求前都会调用')

    def process_response(self, request, response):
        print('每次响应前都会调用')
        return response
