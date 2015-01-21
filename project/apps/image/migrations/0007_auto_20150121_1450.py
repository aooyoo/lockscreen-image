from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.postgres.fields


def cover_category_name_to_id(apps, scheme_editor):
    ImageForeground = apps.get_model("image", "ImageForeground")
    Category = apps.get_model("image", "ForegroundCategory")

    for image in ImageForeground.objects.all():
        if not image.categories:
            ids = []
        else:
            ids = Category.objects.filter(name__in=image.categories).values_list('id', flat=True)
            ids = list(ids)

        ImageForeground.objects.filter(id=image.id).update(categories_tmp=ids)



class Migration(migrations.Migration):

    dependencies = [
        ('image', '0006_auto_20150120_0829'),
    ]

    operations = [
        migrations.AddField(
            model_name='imageforeground',
            name='categories_tmp',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None, null=True),
        ),

        migrations.RunPython(cover_category_name_to_id),

        migrations.RemoveField(
            model_name='imageforeground',
            name='categories',
        ),

        migrations.RenameField(
            model_name='imageforeground',
            old_name='categories_tmp',
            new_name='categories',
        ),

        migrations.RunSQL("alter table image_foreground alter column categories set not null"),
        migrations.RunSQL("create index img_fore_categories_idx on image_foreground using gin (categories)"),
    ]
