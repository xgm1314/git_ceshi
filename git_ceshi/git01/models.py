from django.db import models


# Create your models here.
class Book(models.Model):
    """书籍类"""
    name = models.CharField(verbose_name='书名', max_length=32)

    def __str__(self):
        # print(self.name)
        return self.name


class PeopleInfo(models.Model):
    """人物类"""
    name = models.CharField(verbose_name='人物名字', max_length=16)
    gender_choices = ((1, '男'), (2, '女'))
    gender = models.SmallIntegerField(verbose_name='性别', choices=gender_choices)
    book = models.ForeignKey(verbose_name='书名ID', to=Book, to_field='id', on_delete=models.CASCADE)

    # 在pycharm中获取choices的属性值self.get_gender_display()
    def __str__(self):
        # print(self.name, self.book, self.get_gender_display())
        # print(type(self.name))
        # print(type(self.book))
        # print(type(self.get_gender_display()))
        return self.name
