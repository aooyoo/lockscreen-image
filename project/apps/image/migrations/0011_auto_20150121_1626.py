# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0010_auto_20150121_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagepairforcollect',
            name='phone_id',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='imagepairfordownload',
            name='phone_id',
            field=models.TextField(),
        ),
    ]
