# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '15-1-18'

from django import forms

class LoginForm(forms.Form):
    udid = forms.CharField()
    phone = forms.CharField()

