# -*- coding: utf-8 -*-

from django.db import models

class FeedBack(models.Model):
    udid = models.TextField()
    phone = models.TextField()
    email = models.TextField(blank=True)
    country = models.TextField(blank=True)
    content = models.TextField()

    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'feedback'
        verbose_name = '反馈'
        verbose_name_plural = '反馈'
