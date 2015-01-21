# -*- coding: utf-8 -*-

from django.db import models

class Phone(models.Model):
    udid = models.TextField('UDID', primary_key=True)
    phone = models.TextField('型号')
    first_login = models.DateTimeField('首次登录', auto_now_add=True)
    last_login = models.DateTimeField('最近登录', db_index=True)

    class Meta:
        db_table = 'phone'
        ordering = ['-last_login']
        verbose_name = '手机'
        verbose_name_plural = '手机'

