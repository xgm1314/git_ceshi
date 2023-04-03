from django.apps import AppConfig


class Django02Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'django02'
    verbose_name = u'测试'                # 1/2设置admin站点的名称
