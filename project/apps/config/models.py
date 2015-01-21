# -*- coding: utf-8 -*-

from django.db import models

class Config(models.Model):
    name = models.TextField(primary_key=True)
    value = models.TextField()

    class Meta:
        db_table = 'project_config'
        verbose_name = '设置'
        verbose_name_plural = '设置'


    @classmethod
    def get_value(cls, key):
        try:
            return cls.objects.get(name=key).value
        except cls.DoesNotExist:
            return ''
