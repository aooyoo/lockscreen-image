# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '15-1-20'

import os
import sys


CURRENT_PATH = os.path.dirname(os.path.realpath(__file__))
PARENT_PATH = os.path.normpath(os.path.join(CURRENT_PATH, '../project'))
sys.path.append(PARENT_PATH)

import re
import json
import zipfile

import beanstalkc
import sevencow
import requests

from project import settings


# job = {
#     'zip': zip file path,
#     'callback_url': callback url,         从url来区分是前景还是背景
#     'callback_data': {},                  发来的回调数据
# }
#
# then feebback to callback_url with data:
#     {
#         callback_data from reuqest if provide,
#         'images': [
#             # image 1
#             {
#                 'i4': key,
#                 'i5': key,
#                 ...
#             },
#             # image 2
#             {
#                 'i4': key,
#                 'i5': key,
#                 ...
#             },
#             ...
#         ]
#     }
#


IMAGE_PATTERN = re.compile('.+\.(jpg|JPG|jpeg|JPEG|png|PNG)\s*$')


class ImageUpload(object):
    def __init__(self):
        self.bean = beanstalkc.Connection(
            host=settings.BEAN_HOST,
            port=settings.BEAN_PORT
        )

        self.cow = sevencow.Cow(
            settings.QINIU_ACCESS_KEY,
            settings.QINIU_SECRET_KEY,
        )

        self.bucket = self.cow.get_bucket(settings.QINIU_BUCKET)


    def parse_zip_and_upload(self, zip_file):
        result = []
        z = zipfile.ZipFile(zip_file)
        print z.namelist()

        for name in z.namelist():
            if IMAGE_PATTERN.search(name) is None:
                continue

            data = z.open(name).read()
            res = self.bucket.put(name, data=data)

            phone_types = name.split('/')[-2]
            phone_types = [x for x in phone_types.split('-')]
            phone_types_dict = {tp: res['key'] for tp in phone_types}
            result.append(phone_types_dict)

        return result


    def feedback(self, callback_url, data):
        print "FEEDBACK"
        print data
        requests.post(callback_url, data=json.dumps(data))



    @classmethod
    def run(cls):
        self = cls()
        while True:
            job = self.bean.reserve()
            print "GOT"
            print job.body
            data = json.loads(job.body)
            zip_file = data['zip']
            callback_url = data['callback_url']
            callback_data = data.get('callback_data', {})

            result_data = self.parse_zip_and_upload(zip_file)
            callback_data['images'] = result_data
            self.feedback(callback_url, callback_data)

            job.delete()
            print "FINISH"


if __name__ == '__main__':
    ImageUpload.run()

