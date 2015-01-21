# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Config',
            fields=[
                ('name', models.TextField(serialize=False, primary_key=True)),
                ('value', models.TextField()),
            ],
            options={
                'db_table': 'project_config',
            },
        ),
    ]
