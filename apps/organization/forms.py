# -*- coding:utf-8 -*-
import re

from django import forms

from operation.models import UserAsk,UserProfile

class UserAskForm(forms.ModelForm):
    class Meta:
        model = UserAsk
        fields = ['name','mobile','course']

    def clean_mobile(self):
        mobile = self.cleaned_data['mobile']
        REGEX_MOBILE = "^1[358]\d{9}$|^147\d{8}$|^176\d{8}$"
        p = re.compile(REGEX_MOBILE)
        if p.match(mobile):
            return mobile
        else:
            raise forms.ValidationError(u'非法手机号码',code = 'mobie_invalid')

class UpdateImageForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image',]
