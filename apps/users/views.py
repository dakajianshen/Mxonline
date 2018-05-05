#coding=utf-8
from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.hashers import make_password

from .models import Banner,UserProfile
from course.models import Course
from .forms import RegisterForm

class LoginView(View):
    def get(self,request):
        return render(request, 'login.html', {})
    def post(self,request):
        user_name = request.POST.get("username","")
        pass_word = request.POST.get("password","")
        user = authenticate(username = user_name,password =pass_word)
        if user is not None:
            login(request,user)
            return render(request,'index.html',{})
        else:
            return render(request,'login.html',{})

    # def post(self):

class IndexView(View):
    def get(self,request):
        all_banner = Banner.objects.order_by('index')[:5]
        banner_courses = Course.objects.filter(is_banner=True)[:3]
        return render(request,'index.html',{'all_banner':all_banner,
                                            "banner_courses":banner_courses})
class UserInfoView(View):
    def get(self,request):
        return render(request,'usercenter-info.html',{})

class LogoutView(View):
    def get(self,request):
        logout(request)

class RegisterView(View):
    def get(self,request):
        register_form = RegisterForm()
        return render(request,'register.html',{'register_form':register_form,
                                               })
    def post(self,request):
        register_form = RegisterForm()
        if register_form.is_valid():
            user_name = request.POST.get('email','')
            if UserProfile.objects.filter(email=user_name):
                return render(request,'register.html',{'register_form':register_form,'msg':u'用户已存在'})
            pass_word = request.POST.get('password','')

            user_profile = UserProfile()
            user_profile.username = user_name
            user_profile.email = user_name

            user_profile.is_active = False
            user_profile.password = make_password(pass_word)
            user_profile.save()
            return render(request,'login.html')
        else:
            return render(request,'register.html',{'register_form':register_form,
                                               })