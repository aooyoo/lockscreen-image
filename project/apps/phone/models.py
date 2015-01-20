# -*- coding: utf-8 -*-

from django.db import models

class Phone(models.Model):
    udid = models.TextField(primary_key=True)
    phone = models.TextField()
    first_login = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(db_index=True)

    class Meta:
        db_table = 'phone'
        ordering = ['-last_login']

