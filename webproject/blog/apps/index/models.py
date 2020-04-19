from django.db import models


# Create your models here.
# 数据迁移： python manage.py makemigrations
# 提交迁移：python manage.py migrate
# 生成数据表：python manage.py sqlmigrate 应用名 文件id 查看SQL语句


class Article(models.Model):
    'alter table tablename auto_increment=0'
    title = models.CharField(max_length=32, default='Title')
    content = models.TextField(null=True)
    category = models.CharField(max_length=16, default='美文')
    views = models.PositiveIntegerField('阅读量', default=0)

    def __str__(self):
        return self.title

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])
