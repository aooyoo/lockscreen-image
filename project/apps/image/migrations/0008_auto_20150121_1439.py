# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0007_auto_20150121_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageforeground',
            name='categories',
            field=django.contrib.postgres.fields.ArrayField(default=[], base_field=models.IntegerField(), size=None),
        ),
    ]
