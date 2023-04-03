from django.contrib import admin

# Register your models here.
from .models import BookInfo, PeopleInfo

admin.site.register(BookInfo)                   # 激活admin站点的models类
admin.site.register(PeopleInfo)                 # 激活admin站点的models类

admin.site.site_header = '设置网站页头'
admin.site.site_title = '设置页面标题'
admin.site.index_title = '设置首页标语'
