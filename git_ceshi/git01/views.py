from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    # return HttpResponse('hao')
    """
    request,                请求
    template_name,          目录
    context = None,         参数
    """
    context = {
        'name': '双十一'
    }
    return render(request, 'git01/index.html', context)
