# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0011_auto_20150121_1626'),
    ]

    operations = [
        migrations.RunSQL("create index img_pair_coll_idx on image_pair_collect (phone_id, foreground_id, background_id)"),
        migrations.RunSQL("create index img_pair_down_idx on image_pair_download (phone_id, foreground_id, background_id)"),
    ]
