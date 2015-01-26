# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0005_auto_20150126_2349'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='uploadbackground',
            options={'ordering': ['-upload_at'], 'verbose_name': '\u4e0a\u4f20\u80cc\u666f\u5305', 'verbose_name_plural': '\u4e0a\u4f20\u80cc\u666f\u5305'},
        ),
        migrations.AlterModelOptions(
            name='uploadforeground',
            options={'ordering': ['-upload_at'], 'verbose_name': '\u4e0a\u4f20\u524d\u666f\u5305', 'verbose_name_plural': '\u4e0a\u4f20\u524d\u666f\u5305'},
        ),
    ]
