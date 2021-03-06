#coding=utf-8
from django.shortcuts import render
from django.views.generic import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.db.models import Q

from .models import CityDict,CourseOrg,Teacher
from .forms import UserAskForm
from operation.models import UserFavorite

# Create your views here.
class OrgView(View):
    def get(self,request):
        citys = CityDict.objects.all()
        courseOrgs = CourseOrg.objects.all()
        hot_org = courseOrgs.order_by('students')[:2]

        search_keywords = request.GET.get('keywords','')

        if search_keywords:
            courseOrgs = courseOrgs.filter(Q(name__icontains=search_keywords))

        city_id = request.GET.get('city',"")
        if city_id:
            courseOrgs = courseOrgs.filter(city_id=int(city_id))

        category = request.GET.get('ct',"")
        if category:
            courseOrgs=courseOrgs.filter(category=category)

        count_num = courseOrgs.count()
        sort = request.GET.get('sort','')
        if sort=="students":
            courseOrgs = courseOrgs.order_by("-students")
        elif sort=="courses":
            courseOrgs = courseOrgs.order_by("-course_nums")
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1


        p = Paginator(courseOrgs,2, request=request)
        courseOrgs = p.page(page)
        return render(request,'org-list.html',{'citys':citys,
                                               'courseOrgs':courseOrgs,
                                               'city_id':city_id,
                                               'category':category,
                                               'count_num':count_num,
                                               'hot_org':hot_org,
                                               'sort':sort})
class AddAskView(View):
    def post(self,request):
        user_ask_form = UserAskForm(request.POST)
        if user_ask_form.is_valid():
            user_ask = user_ask_form.save(commit=True)
            return HttpResponse('{"status":"success"}',content_type='application/json')
        else:
            return HttpResponse('{"status":"fail","msg":u"字段错误"}',content_type='application/json')
class OrgHomeView(View):
    def get(self,request,course_id):
        has_fav = False
        current_page = "home"
        course_org = CourseOrg.objects.get(id=int(course_id))
        all_course = course_org.course_set.all()[:3]
        all_teacher = course_org.teacher_set.all()[:2]
        if  request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
                has_fav = True
        return render(request,'org-detail-homepage.html',{"all_course":all_course,
                                                          "all_teacher":all_teacher,
                                                          "course_org":course_org,
                                                          "current_page":current_page,
                                                          "has_fav":has_fav})
class OrgCourseView(View):
    def get(self,request,course_id):
        current_page = "course"
        course_org = CourseOrg.objects.get(id=int(course_id))
        all_course = course_org.course_set.all()
        has_fav = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
                has_fav = True
        return render(request,'org-detail-course.html',{"all_course":all_course,
                                                          "course_org":course_org,
                                                        "current_page": current_page,
                                                          "has_fav":has_fav})
class OrgDescView(View):
    def get(self,request,course_id):
        current_page = "desc"
        course_org = CourseOrg.objects.get(id=int(course_id))
        all_course = course_org.course_set.all()
        has_fav = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
                has_fav = True
        return render(request,'org-detail-desc.html',{"all_course":all_course,
                                                          "course_org":course_org,
                                                        "current_page": current_page,
                                                          "has_fav":has_fav})

class OrgTeachersView(View):
    def get(self, request, course_id):
        current_page = "teachers"
        course_org = CourseOrg.objects.get(id=int(course_id))
        all_teachers = course_org.teacher_set.all()
        has_fav = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
                has_fav = True
        return render(request,'org-detail-teacher.html',{"current_page":current_page,
                                                          "has_fav":has_fav,
                                                         "all_teachers":all_teachers,
                                                         "course_org": course_org,
                                                         })

class AddFavView(View):
    def post(self,request):
        fav_id = request.POST.get('fav_id',0)
        fav_type = request.POST.get('fav_type',0)

        if not request.user.is_authenticated():
            return HttpResponse('{"status":"fail","msg":"用户未登录"}',content_type='application/json')
        exist_records = UserFavorite.objects.filter(user=request.user,fav_id=int(fav_id),fav_type=int(fav_type))

        if exist_records:
            exist_records.delete()
            return HttpResponse('{"status":"fail","msg":"收藏"}',content_type="application/json")
        else:
            user_fav = UserFavorite()
            if int(fav_id)>0 and int(fav_type)>0:
                user_fav.user = request.user
                user_fav.fav_id = int(fav_id)
                user_fav.fav_type = int(fav_type)
                user_fav.save()
                return HttpResponse('{"status":"success","msg":"已收藏"}',content_type="application/json")
            else:
                return HttpResponse('{"status":"fail","msg":"收藏出错"}',content_type="application/json")

class TeacherListView(View):
    def get(self,request):
        all_teachers = Teacher.objects.all()
        count_num = all_teachers.count()

        return render(request,'teachers-list.html',{"all_teachers":all_teachers,
                                                    "count_num":count_num
                                                    })

class TeacherDetail(View):
    def get(self,request,teacher_id):
        teacher = Teacher.objects.get(id=int(teacher_id))
        all_course = teacher.course_set.all()
        return render(request,'teacher-detail.html',{"teacher":teacher,"all_course":all_course})

