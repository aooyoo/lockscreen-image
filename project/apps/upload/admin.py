from django.contrib import admin

from apps.upload.models import UploadBackground, UploadForeground

@admin.register(UploadForeground)
class UploadForegroundAdmin(admin.ModelAdmin):
    list_display = ('id', 'Categories', 'upload_at', 'show_at', 'done')

    filter_horizontal = ['categories',]
    exclude = ['done']

    def Categories(self, obj):
        categories = obj.get_all_category_names()
        return ','.join(categories)

@admin.register(UploadBackground)
class UploadBackgroundAdmin(admin.ModelAdmin):
    list_display = ('id', 'upload_at', 'show_at', 'done')
    exclude = ['done']
