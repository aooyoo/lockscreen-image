# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0003_auto_20150118_1052'),
    ]

    operations = [
        migrations.RunSQL("alter table image_background alter column images type jsonb using (images::jsonb)"),
        migrations.RunSQL("alter table image_foreground alter column images type jsonb using (images::jsonb)"),

        migrations.RunSQL("create index image_back_idx on image_background using gin (images)"),
        migrations.RunSQL("create index image_fore_idx on image_foreground using gin (images)"),
    ]
