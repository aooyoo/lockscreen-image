# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0017_auto_20150209_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagebackground',
            name='images',
            field=jsonfield.fields.JSONField(default=b'{}'),
        ),
        migrations.AlterField(
            model_name='imageforeground',
            name='images',
            field=jsonfield.fields.JSONField(default=b'{}'),
        ),
    ]
