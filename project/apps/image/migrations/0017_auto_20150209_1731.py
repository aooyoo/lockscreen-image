# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0016_auto_20150122_1452'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagebackground',
            name='hide',
            field=models.BooleanField(default=False, db_index=True),
        ),
        migrations.AddField(
            model_name='imageforeground',
            name='hide',
            field=models.BooleanField(default=False, db_index=True),
        ),
    ]
