# -*- coding:utf-8 -*-

import xadmin
from xadmin import views

from .models import EmailVerityCode,Banner

class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True

class GlobalSettings(object):
    site_title = u'慕学在线后台系统'
    site_footer = u'慕学科技'
    menu_style = 'accordion'
class EmailVerityCodeAdmin(object):
    list_display = ['code','email','send_type','send_time']
    search_fields = ['code','email','send_type','send_time']
    list_filter = ['code','email','send_type','send_time']

class BannerAdmin(object):
    list_display = ['title','image','url','index','add_time']
    search_fields =  ['title','image','url','index','add_time']
    list_filter =  ['title','image','url','index','add_time']

xadmin.site.register(EmailVerityCode,EmailVerityCodeAdmin)
xadmin.site.register(Banner,BannerAdmin)
xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSettings)
