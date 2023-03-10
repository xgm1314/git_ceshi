from django.contrib import admin

# Register your models here.
from git01.models import Book, PeopleInfo
# 注册模型
admin.site.register(Book)
admin.site.register(PeopleInfo)
