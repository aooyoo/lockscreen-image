# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('udid', models.TextField(serialize=False, primary_key=True)),
                ('phone', models.TextField()),
                ('first_login', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(db_index=True)),
            ],
            options={
                'ordering': ['-last_login'],
                'db_table': 'phone',
            },
        ),
    ]
