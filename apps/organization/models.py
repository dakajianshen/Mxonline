#coding=utf-8
from __future__ import unicode_literals
from datetime import datetime

from django.db import models

# Create your models here.
class CityDict(models.Model):
    name = models.CharField(max_length=20,verbose_name=u'城市')
    desc = models.CharField(max_length=200,verbose_name=u'描述')
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')

    class Meta:
        verbose_name=u'城市'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class CourseOrg(models.Model):
    ORG_CHOICES =(
        ('pxjg',u'培训机构'),
        ('gx',u'高校'),
        ('gr',u'个人'),
    )
    name = models.CharField(max_length=20,verbose_name=u'机构名称')
    desc = models.TextField(verbose_name=u'机构描述')

    category = models.CharField(max_length=20,choices=ORG_CHOICES)
    click_nums = models.IntegerField(default=0,verbose_name=u'点击数')
    fav_nums = models.IntegerField(default=0,verbose_name=u'收藏数')

    image = models.ImageField(upload_to="org/%Y/%m",verbose_name=u'logo',max_length=100)

    address = models.CharField(max_length=100,verbose_name=u'地址')

    city = models.ForeignKey(CityDict,on_delete=models.CASCADE,verbose_name=u'所在城市')

    students = models.IntegerField(default=0,verbose_name=u'学习人数')
    course_nums = models.IntegerField(default=0,verbose_name=u'课程数')
    add_time = models.DateTimeField(default=datetime.now,verbose_name='添加时间')

    class Meta:
        verbose_name=u'课程机构'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.name

class Teacher(models.Model):
    org = models.ForeignKey(CourseOrg,verbose_name=u'所属机构',null=True,blank=True)
    name = models.CharField(max_length=15,verbose_name=u'教师名称',null=True,blank=True)
    work_years = models.IntegerField(default=0,verbose_name=u'工作年限')
    work_company = models.CharField(max_length=20,verbose_name=u'所在公司',null=True,blank=True)
    fav_num = models.IntegerField(default=0,verbose_name=u'收藏数')
    image = models.ImageField(upload_to='org/%Y/%m',max_length=100,null=True,blank=True,verbose_name=u'头像')
    add_time = models.CharField(default=datetime.now,verbose_name=u'添加时间',max_length=50)

    class Meta:
        verbose_name=u'教师'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name