# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phone', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='phone',
            options={'ordering': ['-last_login'], 'verbose_name': '\u624b\u673a', 'verbose_name_plural': '\u624b\u673a'},
        ),
        migrations.AlterField(
            model_name='phone',
            name='first_login',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe9\xa6\x96\xe6\xac\xa1\xe7\x99\xbb\xe5\xbd\x95'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='last_login',
            field=models.DateTimeField(verbose_name=b'\xe6\x9c\x80\xe8\xbf\x91\xe7\x99\xbb\xe5\xbd\x95', db_index=True),
        ),
        migrations.AlterField(
            model_name='phone',
            name='phone',
            field=models.TextField(verbose_name=b'\xe5\x9e\x8b\xe5\x8f\xb7'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='udid',
            field=models.TextField(serialize=False, verbose_name=b'UDID', primary_key=True),
        ),
    ]
