# -*- coding:utf-8 -*-
import xadmin
from .models import UserAsk

class UserAskAdmin(object):
    list_display = ['name','mobile']
    search_fields = ['name','mobile']
    list_filter =['name','mobile']



xadmin.site.register(UserAsk, UserAskAdmin)
