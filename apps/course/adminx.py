# -*- coding:utf-8 -*-
import xadmin
from .models import Course,Lesson

class CourseAdmin(object):
    list_display = ['name','course_org','desc']
    search_fields = ['name','desc']
    list_filter = ['name','desc']

class LessonAdmin(object):
    list_display=['name','course']
    search_fields=['name','course']
    list_filter=['name','course']

xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
