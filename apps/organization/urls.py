from django.conf.urls import url

from organization.views import OrgView,AddAskView,OrgHomeView,OrgCourseView,OrgDescView,OrgTeachersView,AddFavView
from organization.views import TeacherListView,TeacherDetail
urlpatterns = [
    url(r'^list/$',OrgView.as_view(), name='org_list'),
    url(r'^add_ask/$',AddAskView.as_view(),name='add_ask'),
    url(r'^home/(?P<course_id>\d+)/$',OrgHomeView.as_view(),name='org_home'),
    url(r'^course/(?P<course_id>\d+)/$', OrgCourseView.as_view(), name='org_course'),
    url(r'^desc/(?P<course_id>\d+)/$', OrgDescView.as_view(), name='org_desc'),
    url(r'^teachers/(?P<course_id>\d+)/$', OrgTeachersView.as_view(), name='org_teachers'),
    url(r'^add_fav/$', AddFavView.as_view(), name='add_fav'),
    url(r'teacher/list/$',TeacherListView.as_view(),name='teacher_list'),
    url(r'teacher/detail/(?P<teacher_id>\d+)/$',TeacherDetail.as_view(),name='teacher_detail')

]
