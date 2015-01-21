# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '15-1-21'

from django import forms

class ImagePairForm(forms.Form):
    background = forms.CharField(required=True)
    foreground = forms.CharField(required=True)
