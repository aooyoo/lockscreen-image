# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0005_auto_20150120_0730'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagebackground',
            name='score',
            field=models.IntegerField(default=0, db_index=True),
        ),
        migrations.AddField(
            model_name='imageforeground',
            name='score',
            field=models.IntegerField(default=0, db_index=True),
        ),
    ]
