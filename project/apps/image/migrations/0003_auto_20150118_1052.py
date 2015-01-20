# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps.image.models


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0002_auto_20150118_1034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foregroundcategory',
            name='icon',
            field=models.FileField(upload_to=apps.image.models.upload_foreground_category_to),
        ),
    ]
