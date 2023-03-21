from django.db import models


# Create your models here.
class BookInfo(models.Model):
    """图书表测似乎"""
    name = models.CharField(verbose_name='名字', max_length=20, unique=True)
    pud_data = models.DateField(verbose_name='发布日期', null=True)
    read_count = models.IntegerField(verbose_name='阅读量', default=0)
    comment_count = models.IntegerField(verbose_name='评论量', default=0)
    is_delete = models.BooleanField(verbose_name='逻辑删除', default=False)

    # 自动创建peopleinfo_set=[PeopleInfo,PeopleInfo,PeopleInfo...]

    class Meta:
        """更改数据库表名"""
        db_table = 'bookinfo'  # 指明数据库表名
        verbose_name = '图书'  # 在admin站点中显示的名称

    def __str__(self):
        return self.name


class PeopleInfo(models.Model):
    """人物，测试外键"""
    name = models.CharField(verbose_name='名字', max_length=10, unique=True)
    gender_choice = (
        (1, '男'),
        (2, '女')
    )
    gender = models.SmallIntegerField(verbose_name='性别', choices=gender_choice, default=1)
    description = models.CharField(verbose_name='简介', max_length=100, null=True)
    is_delete = models.BooleanField(verbose_name='逻辑删除', default=False)
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)

    class Meta:
        db_table = 'peopleinfo'

    def __str__(self):
        return self.name
