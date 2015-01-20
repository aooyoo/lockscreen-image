# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.postgres.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ForegroundCategory',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, max_length=32, serialize=False, primary_key=True)),
                ('name', models.TextField(unique=True)),
                ('icon', models.FileField(upload_to=b'')),
                ('key', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'category_foreground',
            },
        ),
        migrations.CreateModel(
            name='ImageBackground',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, max_length=32, serialize=False, primary_key=True)),
                ('upload_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('images', models.TextField()),
            ],
            options={
                'db_table': 'image_background',
            },
        ),
        migrations.CreateModel(
            name='ImageForeground',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, max_length=32, serialize=False, primary_key=True)),
                ('upload_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('images', models.TextField()),
                ('categories', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), size=None)),
            ],
            options={
                'db_table': 'image_foreground',
            },
        ),
        migrations.CreateModel(
            name='ImagePairForCollect',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone_id', models.TextField(db_index=True)),
                ('foreground_id', models.TextField(db_index=True)),
                ('background_id', models.TextField(db_index=True)),
                ('action_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'image_pair_collect',
            },
        ),
        migrations.CreateModel(
            name='ImagePairForDownload',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone_id', models.TextField(db_index=True)),
                ('foreground_id', models.TextField(db_index=True)),
                ('background_id', models.TextField(db_index=True)),
                ('action_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'image_pair_download',
            },
        ),
    ]
