# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0012_auto_20150121_1627'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imagepairforcollect',
            old_name='phone_id',
            new_name='phone_udid',
        ),
        migrations.RenameField(
            model_name='imagepairfordownload',
            old_name='phone_id',
            new_name='phone_udid',
        ),
    ]
