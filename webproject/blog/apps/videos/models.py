from django.db import models

# Create your models here.
# 数据迁移： python manage.py makemigrations
# 提交迁移：python manage.py migrate
# 生成数据表：python manage.py sqlmigrate 应用名 文件id 查看SQL语句


class Article(models.Model):
    image = models.CharField(max_length=32, default='Title')
