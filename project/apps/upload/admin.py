from django.contrib import admin

from apps.upload.models import UploadBackground, UploadForeground

@admin.register(UploadForeground)
class UploadForegroundAdmin(admin.ModelAdmin):
    list_display = ('id', 'package', 'Categories', 'upload_at', 'done')

    filter_horizontal = ['categories',]

    def Categories(self, obj):
        categories = obj.get_all_category_names()
        return ','.join(categories)

@admin.register(UploadBackground)
class UploadBackgroundAdmin(admin.ModelAdmin):
    list_display = ('id', 'package', 'upload_at', 'done')
