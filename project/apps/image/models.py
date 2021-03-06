# -*- coding: utf-8 -*-

import os
import time
import uuid
import json
import hashlib

from django.db import models
from django.db.models.signals import post_save
from django.contrib.postgres.fields import ArrayField
from django.conf import settings

from jsonfield import JSONField

def upload_to(instance, filename, subdir):
    _, ext = os.path.splitext(filename)
    new_name = hashlib.md5(filename + str(time.time())).hexdigest()
    return os.path.join(settings.UPLOAD_PATH, subdir, new_name + ext)


def upload_foreground_category_to(instance, filename):
    return upload_to(instance, filename, 'foreground_category_icon')


class ForegroundCategory(models.Model):
    # 前景分类
    # id 1 固定为 全部
    # id 2 固定为 我的收藏
    id = models.IntegerField('ID', primary_key=True)
    order_id = models.IntegerField('排序序号', db_index=True)
    name = models.TextField('中文名字', unique=True)
    name_en = models.TextField('英文名字')
    icon = models.FileField('图标', upload_to=upload_foreground_category_to)
    key = models.TextField(blank=True)

    class Meta:
        db_table = 'category_foreground'
        ordering = ['order_id',]
        verbose_name = '前景分类'
        verbose_name_plural = '前景分类'

    @property
    def image_url(self):
        return settings.QINIU_DOMAIN + self.key

    def __unicode__(self):
        return self.name


class Image(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    upload_at = models.DateTimeField(auto_now_add=True, db_index=True)
    show_at = models.DateTimeField(db_index=True)

    # score 用来打分，每收藏/下载一次+1, 取消收藏-1
    # 最热图片从这里排序获取
    score = models.IntegerField(default=0, db_index=True)

    # {'i4': key, 'i5': key, ...}
    # http://www.postgresql.org/docs/9.4/static/functions-json.html
    images = JSONField(default=json.dumps({}))

    # 是否隐藏
    hide = models.BooleanField(default=False, db_index=True)

    class Meta:
        abstract = True


class ImageForeground(Image):
    categories = ArrayField(models.IntegerField(), default=[])

    class Meta:
        db_table = 'image_foreground'
        verbose_name = '前景图片'
        verbose_name_plural = '前景图片'


class ImageBackground(Image):
    class Meta:
        db_table = 'image_background'
        verbose_name = '背景图片'
        verbose_name_plural = '背景图片'


class ImagePair(models.Model):
    # 收藏/下载记录前景和背景
    phone_udid = models.TextField()
    foreground_id = models.TextField()
    background_id = models.TextField()

    foreground_key = models.TextField()
    background_key = models.TextField()

    action_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        index_together = ['phone_id', 'foreground_id', 'background_id']


class ImagePairForCollect(ImagePair):
    class Meta:
        db_table = 'image_pair_collect'
        verbose_name = '收藏记录'
        verbose_name_plural = '收藏记录'

class ImagePairForDownload(ImagePair):
    class Meta:
        db_table = 'image_pair_download'
        verbose_name = '下载记录'
        verbose_name_plural = '下载记录'


def upload_category_icon(sender, instance, created, **kwargs):
    from sevencow import Cow

    if instance.key:
        with open(instance.icon.path, 'rb') as f:
            data = f.read()

        md5 = hashlib.md5(data).hexdigest()
        key, ext = os.path.splitext(instance.key)
        if md5 == key:
            # icon 没有变化
            return

    c = Cow(settings.QINIU_ACCESS_KEY, settings.QINIU_SECRET_KEY)
    bucket = c.get_bucket(settings.QINIU_BUCKET)
    res = bucket.put(instance.icon.path)

    instance.key = res['key']
    instance.save()


post_save.connect(
    upload_category_icon,
    sender=ForegroundCategory,
    dispatch_uid='foreground_category_upload_icon'
)


