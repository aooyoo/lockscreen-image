# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0018_auto_20150310_1608'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagebackground',
            name='show_at',
            field=models.DateTimeField(default='2015-01-20 00:00:00+08', db_index=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='imageforeground',
            name='show_at',
            field=models.DateTimeField(default='2015-01-20 00:00:00+08', db_index=True),
            preserve_default=False,
        ),
    ]
