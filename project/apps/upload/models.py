#! -*- coding: utf-8 -*-

import json
import uuid

import beanstalkc

from django.conf import settings
from django.db import models
from django.db.models.signals import post_save

from apps.image.models import upload_to


def upload_foreground_zip_to(instance, filename):
    return upload_to(instance, filename, 'foreground_zip')

def upload_background_zip_to(instance, filename):
    return upload_to(instance, filename, 'background_zip')


class Upload(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    upload_at = models.DateTimeField(auto_now_add=True)
    done = models.BooleanField(default=False)

    class Meta:
        abstract = True


class UploadForeground(Upload):
    package = models.FileField("ZIP包", upload_to=upload_foreground_zip_to)
    categories = models.ManyToManyField('image.ForegroundCategory')
    class Meta:
        db_table = 'upload_foreground'
        verbose_name = '上传前景包'
        verbose_name_plural = '上传前景包'

    def get_all_category_names(self):
        return [c.name for c in self.categories.all()]

    def get_all_category_ids(self):
        return [c.id for c in self.categories.all()]


class UploadBackground(Upload):
    package = models.FileField("ZIP包", upload_to=upload_background_zip_to)
    class Meta:
        db_table = 'upload_background'
        verbose_name = '上传背景包'
        verbose_name_plural = '上传背景包'

def package_uploaded(sender, instance, created, **kwargs):
    if not created:
        return

    if sender is UploadForeground:
        callback_url = settings.LISTEN_URL.rstrip('/') + '/callback/foreground-done/'
    else:
        callback_url = settings.LISTEN_URL.rstrip('/') + '/callback/background-done/'

    bean = beanstalkc.Connection(host=settings.BEAN_HOST, port=settings.BEAN_PORT)
    callback_data = {
        'id': str(instance.id),
    }

    data = {
        'zip': instance.package.path,
        'callback_url': callback_url,
        'callback_data': callback_data
    }

    bean.put(json.dumps(data))
    bean.close()


post_save.connect(
    package_uploaded,
    sender=UploadForeground,
    dispatch_uid='foreground_package_upload'
)

post_save.connect(
    package_uploaded,
    sender=UploadBackground,
    dispatch_uid='background_package_upload'
)
