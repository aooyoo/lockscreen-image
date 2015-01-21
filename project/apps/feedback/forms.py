# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '15-1-21'

from django import forms

class FeedbackForm(forms.Form):
    email = forms.CharField(required=False)
    country = forms.CharField(required=False)
    content = forms.CharField(required=True)
