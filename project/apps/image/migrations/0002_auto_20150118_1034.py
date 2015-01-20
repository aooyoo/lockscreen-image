# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps.image.models


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foregroundcategory',
            name='icon',
            field=models.FileField(upload_to=apps.image.models.upload_to),
        ),
    ]
