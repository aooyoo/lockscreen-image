# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('udid', models.TextField()),
                ('phone', models.TextField()),
                ('email', models.TextField(blank=True)),
                ('country', models.TextField(blank=True)),
                ('content', models.TextField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'feedback',
            },
        ),
    ]
