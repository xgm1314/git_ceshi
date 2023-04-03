from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django02.models import BookInfo
from django.views import View  # LoginView(测试类试图)
from django.contrib.auth.mixins import LoginRequiredMixin           # 用户判断只有登录用户才可以访问页面,以是否登录admin站点


# Create your views here.
def create_book(req):
    book = BookInfo.objects.create(name='fyq', pud_data='2001-05-19', )
    return HttpResponse('create')


def shop(req, city_id, shop_id):
    """URL路径传参"""
    print(city_id, shop_id)  # URL路径传参
    query_params = req.GET  # 查询字符串,得到QueryDict值,QueryDict具有字典的特性,还具有一键多值的特性
    # print(query_params)
    # hangzhou = query_params.get('hangzhou')         # 获取字符串的内容
    # hangzhou=query_params['hangzhou']               # 获取字符串的内容
    hangzhou = query_params.getlist('hangzhou')  # 获取QueryDict的多值
    # print(hangzhou)
    return HttpResponse('测试传参')


def register(req):
    data = req.POST
    # print(data)
    return HttpResponse('ok')


def json(req):
    body = req.body  # 获取json数据
    # print(body)
    body_str = body.decode()  # json形式的字符串
    # print(body_str)
    # print(type(body_str))
    import json
    body_dict = json.loads(body_str)  # 将json形式的字符串转换为字典
    # print((req.META))                   # 请求头 字典类型
    # print((req.META['SERVER_PORT']))                   # 请求头
    # print(body_dict)
    print(req.method)  # 获取请求的方式
    return HttpResponse('好')


def response(request):
    # response = HttpResponse('res', status=200)
    # response['name']='hangzhou'
    '''1、传入字典数据'''
    # info = {
    #     'name': 'hangzhou',
    #     'age': 10
    # }
    # response = JsonResponse(data=info)              # 返回的响应数据，一般是字典类型
    '''2、传入非字典数据'''
    list_dict = [
        {'name': 'xiaohong',
         'age': 10
         },
        {'name': 'xiaolv',
         'age': 20
         },
    ]
    response = JsonResponse(data=list_dict,
                            safe=False)  # safe=True表示传入的data数据是一个字典（json.loads是表示将JSON字符串转换为字典，json.dumps是将字典转换为JSON字符串）
    # import json                                                 # 检验是否转换为JSON数据
    # data=json.dumps(list_dict)
    # response=HttpResponse(data)
    return response


def redirect_(request):
    '''重定向测试'''
    return redirect('https://www.baidu.com')


def set_cookie(request):
    '''cookie测试'''
    # 访问连接http://127.0.0.1:8000/django/set_cookie/?username=hangzhou&password=123
    username = request.GET.get('username')  # 获取查询字符串
    password = request.GET.get('password')
    response = HttpResponse('set_cookie')  # 服务器设置cookie信息
    response.set_cookie('name', username, max_age=60 * 60)  # 响应对象.set_cookie方法设置cookie信息,max_age设置cookie过期时间，单位是秒
    # response.set_cookie('pwd',password)
    # response.delete_cookie('name')  # 删除cookie信息
    return response


def get_cookie(request):
    print(request.COOKIES)  # 字典数据
    name = request.COOKIES.get('name')
    return HttpResponse(name)


def set_session(request):
    '''session测试 信息保存在服务器端，需要以来cookie'''
    username = request.GET.get('username')  # 获取查询字符串
    user_id = 1
    request.session['username'] = username  # 设置session信息
    request.session['user_id'] = user_id

    # clear 删除session里的数据，保留key
    # request.session.clear()
    # flush 删除所有的数据，包括key
    # request.session.flush()

    # 设置session过期时间
    # request.session.set_expiry(60*60)

    return HttpResponse('set_session')


def get_session(request):
    '''session获取'''
    # user_id=request.session['user_id']              # 获取不到会报错
    # username=request.session['username']
    user_id = request.session.get('user_id')
    username = request.session.get('username')

    content = '{},{}'.format(user_id, username)
    return HttpResponse(content)


def login(request):
    '''请求方式获取'''
    print(request.method)
    if request.method == 'GET':
        return HttpResponse('get请求方式')
    else:
        return HttpResponse('post请求方式')


class LoginView(View):
    '''请求方式测试'''

    def get(self, request):
        return HttpResponse('get请求')

    def post(self, request):
        return HttpResponse('post请求')


class OrderView(LoginRequiredMixin,View):
    '''多继承测试'''
    def get(self,request):
        # isLogin = False
        # if not isLogin:
        #     return HttpResponse('用户未登录')
        return HttpResponse('用户已登陆')







