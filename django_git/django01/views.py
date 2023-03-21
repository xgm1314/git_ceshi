from django.shortcuts import render, HttpResponse

from django01.models import BookInfo, PeopleInfo


# Create your views here.
def index(request):
    books = BookInfo.objects.all()
    print(books)
    return HttpResponse('index')


def index_add(request):
    """保存数据方式1"""
    # books = BookInfo(name='django_', pud_data='2023-3-17')
    # books.save()
    # return HttpResponse('添加成功')
    """保存数据方式2 objects"""
    BookInfo.objects.create(name='想干嘛富雅倩你是傻子吗', pud_data='2013-5-7', read_count=30, comment_count=1, is_delete=False)
    return HttpResponse('objects添加成功')


def revise(request):
    """修改1"""
    # books = BookInfo.objects.get(id=21)
    # books.name = '不要你管'
    # books.save()
    # return HttpResponse('revise修改1')
    """修改2"""
    BookInfo.objects.filter(id=11).update(name='想干嘛富雅倩你是傻子吗', comment_count=666)
    BookInfo.objects.filter(id=15).update(name='爱你呦', comment_count=999)
    return HttpResponse('revise修改2')


def delete(req):
    """删除1"""
    # book = BookInfo.objects.get(id=19)
    # book.delete()
    """删除2"""
    # BookInfo.objects.filter(id=5).delete()
    BookInfo.objects.get(id=6).delete()
    return HttpResponse('delete删除成功')


def get_query(req):
    """get查询"""
    try:
        # book = BookInfo.objects.all()
        book = BookInfo.objects.filter(id=1)
        print(book)
        return HttpResponse('查询成功')
    except BookInfo.DoesNotExist:
        print('该查询不存在')
        return HttpResponse('该查询不存在')


def count(req):
    """count统计"""
    BookInfo.objects.all().count()
    # BookInfo.objects.count()
    return HttpResponse('统计数量')


def query(req):
    """查询的解释"""
    # 查询id=1的值
    BookInfo.objects.get(id=1)  # 返回的是一个数据
    BookInfo.objects.filter(id=1)  # 返回的是一个列表
    # 查询包含 ”湖“的数据
    BookInfo.objects.filter(name__contains='湖')
    # 查询以”部“结尾的数据
    BookInfo.objects.filter(name__endswith='部')
    # 查询为空的数据
    BookInfo.objects.filter(name__isnull=True)
    # 查询编号为1，3，5编号的数据
    BookInfo.objects.filter(id__in=[1, 3, 5])
    # 查询编号大于3的数据(gt：大于；gte：大于等于；lt：小于；lte：小于等于)
    BookInfo.objects.filter(id__gt=3)
    # 查询编号不等于3的数据
    BookInfo.objects.exclude(id=3)
    # 查询某年发布的图书数据
    BookInfo.objects.filter(pud_data__year=1980)
    # 查询某天以后的数据
    BookInfo.objects.filter(pud_data__gt='1990-1-1')


from django.db.models import F

# 查询阅读量大于评论量的书（两个属性的比较）
BookInfo.objects.filter(read_count__gt=F('comment_count'))
# 并且(and)查询
# 阅读量大于20，并且编号小于3
BookInfo.objects.filter(read_count__gt=20).filter(id__lt=3)
BookInfo.objects.filter(read_count__gt=20, id__lt=3)
from django.db.models import Q

BookInfo.objects.filter(Q(read_count__gt=20) & Q(id__lt=3))
# 或(or)者查询
BookInfo.objects.filter(Q(read_count__gt=20) | Q(id__lt=3))
# 非(not) 查询
BookInfo.objects.filter(~Q(id=20))

# 聚合函数
from django.db.models import Sum, Max, Min, Avg, Count

BookInfo.objects.aggregate(Sum('read_count'))
# 排序
BookInfo.objects.all().order_by('read_count')

# 级联查询（联表查询）
# 查询id=1的书籍下的所有人的名字
# 方式1(一对多查询)：
book = BookInfo.objects.get(id=1)
book.peopleinfo_set.all()
# 方式2：
PeopleInfo.objects.filter(book=1)
# 查询名字为1的书籍(多对一查询)
person = PeopleInfo.objects.get(id=1)
person.book

# 关联过滤查询
# 查询图书含有郭靖人物的书籍
BookInfo.objects.filter(peopleinfo__name__exact='郭靖')
BookInfo.objects.filter(peopleinfo__name='郭靖')
# 查询图书中的人物描述包含”八“的图书
BookInfo.objects.filter(peopleinfo__description__contains='八')

# 查询书名为”天龙八部“的所有人物
PeopleInfo.objects.filter(book__name='天龙八部')
PeopleInfo.objects.filter(book__name__exact='天龙八部')

# 查询图书阅读量大于30的所有人物
PeopleInfo.objects.filter(book__read_count__gt=30)



















































































