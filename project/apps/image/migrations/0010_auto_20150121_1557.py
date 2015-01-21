# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0009_auto_20150121_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagepairforcollect',
            name='background_id',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='imagepairforcollect',
            name='foreground_id',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='imagepairfordownload',
            name='background_id',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='imagepairfordownload',
            name='foreground_id',
            field=models.TextField(),
        ),
    ]
