# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps.upload.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0002_uploadforeground_categories'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='uploadbackground',
            options={'verbose_name': '\u4e0a\u4f20\u80cc\u666f\u5305', 'verbose_name_plural': '\u4e0a\u4f20\u80cc\u666f\u5305'},
        ),
        migrations.AlterModelOptions(
            name='uploadforeground',
            options={'verbose_name': '\u4e0a\u4f20\u524d\u666f\u5305', 'verbose_name_plural': '\u4e0a\u4f20\u524d\u666f\u5305'},
        ),
        migrations.AlterField(
            model_name='uploadbackground',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, max_length=32, serialize=False, editable=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='uploadbackground',
            name='package',
            field=models.FileField(upload_to=apps.upload.models.upload_background_zip_to, verbose_name=b'ZIP\xe5\x8c\x85'),
        ),
        migrations.AlterField(
            model_name='uploadforeground',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, max_length=32, serialize=False, editable=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='uploadforeground',
            name='package',
            field=models.FileField(upload_to=apps.upload.models.upload_foreground_zip_to, verbose_name=b'ZIP\xe5\x8c\x85'),
        ),
    ]
