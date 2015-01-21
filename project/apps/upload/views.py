# -*- coding: utf-8 -*-

import json
from django.http import JsonResponse, HttpResponse

from apps.upload.models import UploadForeground, UploadBackground
from apps.image.models import ImageForeground, ImageBackground


# 上传zip处理完毕后的callback
def callback_foreground(request):
    data = json.loads(request.body)
    upload_id = data['id']
    images = data['images']

    upload_obj = UploadForeground.objects.get(id=upload_id)
    categories = upload_obj.get_all_category_ids()

    ImageObjs = []
    for image in images:
        ImageObjs.append(
            ImageForeground(
                categories=categories,
                images=json.dumps(image)
            )
        )

    ImageForeground.objects.bulk_create(ImageObjs)

    UploadForeground.objects.filter(id=upload_id).update(done=True)
    return HttpResponse('ok')


def callback_background(request):
    data = json.loads(request.body)
    upload_id = data['id']
    images = data['images']

    ImageObjs = []
    for image in images:
        ImageObjs.append(
            ImageBackground(
                images=json.dumps(image)
            )
        )

    ImageBackground.objects.bulk_create(ImageObjs)

    UploadBackground.objects.filter(id=upload_id).update(done=True)
    return HttpResponse('ok')


