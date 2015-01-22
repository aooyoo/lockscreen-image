# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0015_auto_20150122_1407'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='foregroundcategory',
            options={'ordering': ['order_id'], 'verbose_name': '\u524d\u666f\u5206\u7c7b', 'verbose_name_plural': '\u524d\u666f\u5206\u7c7b'},
        ),
        migrations.AddField(
            model_name='foregroundcategory',
            name='order_id',
            field=models.IntegerField(default=0, verbose_name=b'\xe6\x8e\x92\xe5\xba\x8f\xe5\xba\x8f\xe5\x8f\xb7', db_index=True),
            preserve_default=False,
        ),
    ]
