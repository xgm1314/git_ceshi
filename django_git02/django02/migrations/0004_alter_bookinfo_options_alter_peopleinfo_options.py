# Generated by Django 4.1.7 on 2023-04-01 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django02', '0003_alter_peopleinfo_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinfo',
            options={'verbose_name': '图书', 'verbose_name_plural': '图书'},
        ),
        migrations.AlterModelOptions(
            name='peopleinfo',
            options={'verbose_name': '人物', 'verbose_name_plural': '人物'},
        ),
    ]
