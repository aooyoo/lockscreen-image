# -*- coding: utf-8 -*-

from django.conf import settings
from django.http import JsonResponse
from django.db import connection
from apps.image.models import ForegroundCategory, ImageBackground, ImageForeground

from project.exceptions import ProjectException
from project.errorcode import ErrorCode

def get_foregound_category(request):
    # 获取前景分类
    categories = ForegroundCategory.objects.all()
    def _make_data(c):
        return {
            'ID': c.id,
            'name': c.name,
            'icon': c.image_url,
        }

    data = [_make_data(c) for c in categories]
    data = {
        'ret': 0,
        'data': data
    }
    return JsonResponse(data)



class ImageGetter(object):
    BUCKET_SIZE = 45

    def __init__(self, request):
        self.request = request
        self.bucket = int(request.GET.get('bucket', 0))
        self.category = request.GET.get('category', '')
        self.phone = request.session['phone']

        if request.path.endswith('/hot/'):
            self.order_by = 'score desc'
        else:
            self.order_by = 'upload_at desc'

        if self.bucket < 0:
            raise ProjectException(ErrorCode.REQUEST_ERROR)


    def build_sql_for_foreground(self):
        if self.category:
            sql = "select id, images->>%s as image_key from {0} where (images->>%s) is not null and %s = any(categories) order by {1} offset %s limit %s".format(ImageForeground._meta.db_table, self.order_by)
            params = (self.phone, self.phone, self.category, self.bucket*self.BUCKET_SIZE, self.BUCKET_SIZE)
        else:
            sql = "select id, images->>%s as image_key from {0} where (images->>%s) is not null order by {1} offset %s limit %s".format(ImageForeground._meta.db_table, self.order_by)
            params = (self.phone, self.phone, self.bucket*self.BUCKET_SIZE, self.BUCKET_SIZE)

        return sql, params

    def build_sql_for_background(self):
        sql = "select id, images->>%s as image_key from {0} where (images->>%s) is not null order by {1} offset %s limit %s".format(ImageBackground._meta.db_table,  self.order_by)
        params = (self.phone, self.phone, self.bucket*self.BUCKET_SIZE, self.BUCKET_SIZE)
        return sql, params


    def get(self):
        if self.request.path.startswith('/foreground/'):
            sql, parms = self.build_sql_for_foreground()
        else:
            sql, parms = self.build_sql_for_background()

        print sql
        print parms
        with connection.cursor() as c:
            c.execute(sql, parms)
            result = c.fetchall()

        if len(result) == self.BUCKET_SIZE:
            next_bucket = self.bucket + 1
        else:
            next_bucket = None

        def _make_image(record):
            _id = str(record[0])
            _url = settings.QINIU_DOMAIN + record[1]
            return {
                'ID': _id,
                'url': _url,
            }

        images = [_make_image(record) for record in result]
        data = {
            'ret': 0,
            'data': {
                'next_bucket_id': next_bucket,
                'images': images
            }
        }

        return JsonResponse(data)


    @classmethod
    def as_view(cls):
        def wrapper(request):
            self = cls(request)
            return self.get()
        return wrapper

