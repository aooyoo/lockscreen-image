from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.postgres.fields


def cover_category_name_to_id(apps, scheme_editor):
    ImageForeground = apps.get_model("image", "ImageForeground")
    Category = apps.get_model("image", "ForegroundCategory")

    for image in ImageForeground.objects.all():
        if not image.categories:
            continue

        ids = Category.objects.filter(name__in=image.categories).values_list('id', flat=True)
        ids = list(ids)
        ImageForeground.objects.filter(id=image.id).update(categories_tmp=ids)



class Migration(migrations.Migration):

    dependencies = [
        ('image', '0006_auto_20150120_0829'),
    ]

    operations = [
        migrations.RunSQL("alter table image_foreground add column categories_tmp integer[]"),
        migrations.RunPython(cover_category_name_to_id),
        migrations.RunSQL("alter table image_foreground drop column categories"),

        migrations.RunSQL("alter table image_foreground rename column categories_tmp to categories"),
        migrations.RunSQL("alter table image_foreground alter column categories set not null"),
        migrations.RunSQL("create index img_fore_categories_idx on image_foreground using gin (categories)"),
    ]
