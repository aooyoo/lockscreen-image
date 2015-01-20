# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps.upload.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UploadBackground',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, max_length=32, serialize=False, primary_key=True)),
                ('upload_at', models.DateTimeField(auto_now_add=True)),
                ('done', models.BooleanField(default=False)),
                ('package', models.FileField(upload_to=apps.upload.models.upload_background_zip_to)),
            ],
            options={
                'db_table': 'upload_background',
            },
        ),
        migrations.CreateModel(
            name='UploadForeground',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, max_length=32, serialize=False, primary_key=True)),
                ('upload_at', models.DateTimeField(auto_now_add=True)),
                ('done', models.BooleanField(default=False)),
                ('package', models.FileField(upload_to=apps.upload.models.upload_foreground_zip_to)),
            ],
            options={
                'db_table': 'upload_foreground',
            },
        ),
    ]
