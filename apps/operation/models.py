#coding=utf-8

from __future__ import unicode_literals

from django.db import models
from datetime import datetime

from users.models import UserProfile

# Create your models here.
class UserAsk(models.Model):
    name = models.CharField(max_length=10,verbose_name=u'姓名')
    mobile = models.CharField(max_length=11,verbose_name=u'电话')
    course = models.CharField(max_length=50,verbose_name=u'课程名')
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'我要学习'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class UserFavorite(models.Model):
    user = models.ForeignKey(UserProfile,verbose_name=u'用户')
    fav_id = models.IntegerField(default=0,verbose_name=u'数据id')
    fav_type = models.IntegerField(choices=((1,"课程"),(2,"课程机构"),(3,"教师")),verbose_name=u'收藏类型')
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'收藏'
        verbose_name_plural = verbose_name

