# -*- coding:utf-8 -*-

from django import forms
from .models import UserProfile
from captcha.fields import CaptchaField

class UpdateImageForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image', ]

class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True,min_length=5,max_length=20)
    captcha = CaptchaField()

