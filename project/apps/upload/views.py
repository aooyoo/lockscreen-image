# -*- coding: utf-8 -*-

import json
from django.http import HttpResponse
from django.db import connection

from apps.upload.models import UploadForeground, UploadBackground
from apps.image.models import ImageForeground, ImageBackground


class CallbackHandler(object):
    def __init__(self, request):
        self.request = request
        data = json.loads(request.body)

        self.upload_id = data['id']
        self.images = data['images']

        if self.request.path.endswith('/background/'):
            self.image_model = ImageBackground
        else:
            self.image_model = ImageForeground


    def process(self):
        images = []
        with connection.cursor() as c:
            for image in self.images:
                sql = "select count(*) from {0} where images = %s".format(self.image_model._meta.db_table)
                params = (json.dumps(image),)
                c.execute(sql, params)
                result = c.fetchone()

                if result[0] > 0:
                    print "==== Warning ===="
                    print "duplicate image, skip"
                    print image
                else:
                    images.append(image)

        if self.image_model is ImageForeground:
            self.process_foreground(images)
        else:
            self.process_background(images)

        return HttpResponse('ok')

    def process_foreground(self, images):
        upload_obj = UploadForeground.objects.get(id=self.upload_id)
        categories = upload_obj.get_all_category_ids()

        ImageObjs = []
        for image in images:
            ImageObjs.append(
                ImageForeground(
                    categories=categories,
                    images=image
                )
            )

        ImageForeground.objects.bulk_create(ImageObjs)
        UploadForeground.objects.filter(id=self.upload_id).update(done=True)


    def process_background(self, images):
        ImageObjs = []
        for image in images:
            ImageObjs.append(
                ImageBackground(
                    images=image
                )
            )

        ImageBackground.objects.bulk_create(ImageObjs)
        UploadBackground.objects.filter(id=self.upload_id).update(done=True)


    @classmethod
    def as_view(cls):
        def wrapper(request):
            self = cls(request)
            return self.process()
        return wrapper
