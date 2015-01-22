# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps.image.models


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0014_auto_20150121_1747'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='foregroundcategory',
            options={'verbose_name': '\u524d\u666f\u5206\u7c7b', 'verbose_name_plural': '\u524d\u666f\u5206\u7c7b'},
        ),
        migrations.AlterModelOptions(
            name='imagebackground',
            options={'verbose_name': '\u80cc\u666f\u56fe\u7247', 'verbose_name_plural': '\u80cc\u666f\u56fe\u7247'},
        ),
        migrations.AlterModelOptions(
            name='imageforeground',
            options={'verbose_name': '\u524d\u666f\u56fe\u7247', 'verbose_name_plural': '\u524d\u666f\u56fe\u7247'},
        ),
        migrations.AlterModelOptions(
            name='imagepairforcollect',
            options={'verbose_name': '\u6536\u85cf\u8bb0\u5f55', 'verbose_name_plural': '\u6536\u85cf\u8bb0\u5f55'},
        ),
        migrations.AlterModelOptions(
            name='imagepairfordownload',
            options={'verbose_name': '\u4e0b\u8f7d\u8bb0\u5f55', 'verbose_name_plural': '\u4e0b\u8f7d\u8bb0\u5f55'},
        ),
        migrations.AddField(
            model_name='foregroundcategory',
            name='name_en',
            field=models.TextField(default='', verbose_name=b'\xe8\x8b\xb1\xe6\x96\x87\xe5\x90\x8d\xe5\xad\x97'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='foregroundcategory',
            name='icon',
            field=models.FileField(upload_to=apps.image.models.upload_foreground_category_to, verbose_name=b'\xe5\x9b\xbe\xe6\xa0\x87'),
        ),
        migrations.AlterField(
            model_name='foregroundcategory',
            name='id',
            field=models.IntegerField(serialize=False, verbose_name=b'ID', primary_key=True),
        ),
        migrations.AlterField(
            model_name='foregroundcategory',
            name='name',
            field=models.TextField(unique=True, verbose_name=b'\xe4\xb8\xad\xe6\x96\x87\xe5\x90\x8d\xe5\xad\x97'),
        ),
    ]
