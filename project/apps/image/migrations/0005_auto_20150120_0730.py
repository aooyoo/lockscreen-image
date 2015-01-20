# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0004_auto_20150120_0547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foregroundcategory',
            name='id',
            field=models.IntegerField(serialize=False, primary_key=True),
        ),
    ]
