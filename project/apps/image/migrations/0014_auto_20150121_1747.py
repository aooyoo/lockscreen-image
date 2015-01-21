# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0013_auto_20150121_1634'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagepairforcollect',
            name='background_key',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='imagepairforcollect',
            name='foreground_key',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='imagepairfordownload',
            name='background_key',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='imagepairfordownload',
            name='foreground_key',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
