# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0003_auto_20150122_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadbackground',
            name='upload_at',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='uploadforeground',
            name='upload_at',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
    ]
