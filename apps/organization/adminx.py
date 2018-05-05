# -*- coding:utf-8 -*-
import xadmin
from .models import CityDict,CourseOrg,Teacher

class CityDictAdmin(object):
    list_display = ['name','desc','add_time']
    search_fields = ['name','desc']
    list_filter = ['name','desc']

class CourseOrgAdmin(object):
    list_display=['name','desc','category']
    search_fields=['name','desc','category']
    list_filter=['name','desc','category']

class TeacherAdmin(object):
    list_display = ['name','org','work_years','work_company']
    search_fields = ['name','org','work_years','work_company']
    list_filter = ['name','org','work_years','work_company']


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)

