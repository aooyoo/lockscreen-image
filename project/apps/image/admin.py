# -*- coding: utf-8 -*-


from django.conf import settings
from django.contrib import admin

from apps.image.models import (
    ForegroundCategory,
    ImageForeground,
    ImageBackground,
    ImagePairForCollect,
    ImagePairForDownload,
)


def _images_hide_action(modeladmin, request, queryset):
    queryset.update(hide=True)
_images_hide_action.short_description = "隐藏图片"

def _images_unhide_action(modeladmin, request, queryset):
    queryset.update(hide=False)
_images_unhide_action.short_description = "显示图片"



@admin.register(ForegroundCategory)
class ForegroundCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_id', 'name', 'name_en', 'IconDisplay')
    exclude = ['key',]

    def IconDisplay(self, obj):
        url = obj.image_url
        return '<a href="{0}" target=_blank><img src="{0}" width="50px" /></a>'.format(
            url
        )
    IconDisplay.allow_tags = True


@admin.register(ImageForeground)
class ImageForegroundAdmin(admin.ModelAdmin):
    list_display = ('id', 'upload_at', 'show_at', 'score', 'images', 'categories', 'ImageShow', 'hide')
    ordering = ['-upload_at',]
    list_filter = ('hide',)
    actions = [_images_hide_action, _images_unhide_action]

    def ImageShow(self, obj):
        url = settings.QINIU_DOMAIN + obj.images.values()[0]
        return '<a href="{0}" target=_blank><img src="{0}" width="50px" /></a>'.format(
            url
        )
    ImageShow.allow_tags = True


@admin.register(ImageBackground)
class ImageBackgroundAdmin(admin.ModelAdmin):
    list_display = ('id', 'upload_at', 'show_at', 'score', 'images', 'ImageShow', 'hide')
    ordering = ['-upload_at',]
    list_filter = ('hide',)
    actions = [_images_hide_action, _images_unhide_action]

    def ImageShow(self, obj):
        url = settings.QINIU_DOMAIN + obj.images.values()[0]
        return '<a href="{0}" target=_blank><img src="{0}" width="50px" /></a>'.format(
            url
        )
    ImageShow.allow_tags = True


@admin.register(ImagePairForCollect)
class ImagePairForCollectAdmin(admin.ModelAdmin):
    list_display = ('phone_udid', 'foreground_id', 'background_id', 'Foreground', 'Background', 'action_date')

    def Foreground(self, obj):
        return '<img src="{0}" width="100px" />'.format(settings.QINIU_DOMAIN + obj.foreground_key)
    Foreground.allow_tags = True

    def Background(self, obj):
        return '<img src="{0}" width="100px" />'.format(settings.QINIU_DOMAIN + obj.background_key)
    Background.allow_tags = True

@admin.register(ImagePairForDownload)
class ImagePairForDownloadAdmin(admin.ModelAdmin):
    list_display = ('phone_udid', 'foreground_id', 'background_id', 'Foreground', 'Background', 'action_date')
    def Foreground(self, obj):
        return '<img src="{0}" width="100px" />'.format(settings.QINIU_DOMAIN + obj.foreground_key)
    Foreground.allow_tags = True

    def Background(self, obj):
        return '<img src="{0}" width="100px" />'.format(settings.QINIU_DOMAIN + obj.background_key)
    Background.allow_tags = True
