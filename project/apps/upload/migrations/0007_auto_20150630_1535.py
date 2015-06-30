# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0006_auto_20150126_2350'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadbackground',
            name='show_at',
            field=models.DateTimeField(default='2015-01-20 00:00:00+08'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='uploadforeground',
            name='show_at',
            field=models.DateTimeField(default='2015-01-20 00:00:00+08'),
            preserve_default=False,
        ),
    ]
