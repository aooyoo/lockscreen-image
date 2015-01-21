
from django.contrib import admin

from apps.image.models import (
    ForegroundCategory,
    ImageForeground,
    ImageBackground,
    ImagePairForCollect,
    ImagePairForDownload,
)


@admin.register(ForegroundCategory)
class ForegroundCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'icon', 'IconDisplay')

    def IconDisplay(self, obj):
        return '<img src="{0}" width="100px"/>'.format(obj.image_url)
    IconDisplay.allow_tags = True


@admin.register(ImageForeground)
class ImageForegroundAdmin(admin.ModelAdmin):
    list_display = ('id', 'upload_at', 'score', 'images', 'categories')
    ordering = ['-upload_at',]


@admin.register(ImageBackground)
class ImageBackgroundAdmin(admin.ModelAdmin):
    list_display = ('id', 'upload_at', 'score', 'images')
    ordering = ['-upload_at',]



@admin.register(ImagePairForCollect)
class ImagePairForCollectAdmin(admin.ModelAdmin):
    list_display = ('phone_udid', 'foreground_id', 'background_id', 'action_date')

@admin.register(ImagePairForDownload)
class ImagePairForDownloadAdmin(admin.ModelAdmin):
    list_display = ('phone_udid', 'foreground_id', 'background_id', 'action_date')
